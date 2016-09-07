# -*- coding: utf-8 -*-

## python3 standerd modules
from crypt import crypt, mksalt, METHOD_MD5, METHOD_SHA256, METHOD_SHA512
from hmac import compare_digest
import smtplib
from email.mime.text import MIMEText
import json

## bottle modules
import bottle
from plugins import bottle_sqlite
from collection_json import Collections

## bottle settings
app = application = bottle.Bottle()
sqlite_plugin = bottle_sqlite.SQLitePlugin(dbfile='mailadmin.db', autocommit=True)
app.install(sqlite_plugin)


## common functions
def csrf():
    csrf_key = 'WW5CRSlFSDZDWklbXmMxRDs6amFlMXIpUS46dz17'
    return csrf_key


def gen_crypt_password(password):
    crypt_password = crypt(password, mksalt(METHOD_SHA512))
    return crypt_password


def check_password(plainpass, hashpass):
    return compare_digest(crypt(plainpass, hashpass), hashpass)


def loggedin():
    return bottle.request.get_cookie('loggedin', secret=csrf())


def json_response(data, response_code):
    res = bottle.HTTPResponse(status=response_code, body=data)
    # res.set_header('Content-Type', 'application/json; charset=utf-8')
    res.set_header('Content-Type', 'application/vnd.collection+json; charset=utf-8')
    return res


## Routings
@app.route('/')
def home():
    return bottle.redirect('/lists')

@app.route('/lists')
def lists():
    return bottle.template('lists', error=False)


@app.route('/login', method='POST')
def do_login(db):
    username = bottle.request.forms.get('email')
    password = bottle.request.forms.get('password')
    c = db.execute("SELECT password FROM users WHERE email = ?", (username,))
    row = c.fetchone()
    if row:
        hashpass = row['password']
        if check_password(password, hashpass):
            bottle.response.set_cookie('loggedin', username, max_age='3600', secret=csrf())
            return bottle.redirect('/genpass')
        else:
            return bottle.template('index', error='パスワードが正しくありません。')
    else:
        return bottle.template('index', error=username+'というユーザーは存在しません')


@app.route('/json/<table>.json')
def get_tabledata(db, table):
    # if loggedin():
    if table in Collections().formats_dict.keys():
        res = Collections().get_format(table)
        sql = "SELECT * FROM " + table
        c = db.execute(sql)
        rows = c.fetchall()
        for row in rows:
            d = {}
            if table == 'domain':
                # d['href'] = '/json/domain/' + row['domain'] + '/domain.json'
                d['href'] = '/json/domain/' + row['domain'] + '/' + str(row['id']) + '.json'
            elif table == 'alias':
                # d['href'] = '/json/alias/' + row['email'].split('@')[1] + '/' + row['email'].replace('@','_') + '.json'
                d['href'] = '/json/alias/' + row['email'].split('@')[1] + '/' + str(row['id']) + '.json'
            elif table == 'mailbox':
                # d['href'] = '/json/mailbox/' + row['domain_part'] + '/' + row['local_part'] + '.json'
                d['href'] = '/json/mailbox/' + row['domain_part'] + '/' + str(row['id']) + '.json'
            d['data'] = []
            datas = Collections().get_template(table)
            for data in datas:
                data['value'] = row[data['name']]
                d['data'].append(data)
            res['collection']['items'].append(d)
        error_obj = res['collection']['error']
        error_obj['title'] = 'Found items'
        error_obj['code'] = '200'
        error_obj['message'] = 'Mach the requested table.'

        return json_response(json.dumps(res, indent=4), 200)
    else:
        res = Collections().error_data
        error_obj = res['collection']['error']
        error_obj['title'] = 'Not Found'
        error_obj['code'] = '404'
        error_obj['message'] = 'There is not the requested table.'
        return json_response(json.dumps(res, indent=4), 404)


@app.route('/json/<table>/<domain>/<data>.json')
def get_jsondata(db, table, domain, data):
    pass


@app.route('/json/<table>/<domain>/<id>.json', method='POST')
def post_jsondata(db, table, domain, id):
    json_data = bottle.request.json
    keys = []
    values = []
    q = []
    for x in json_data:
        if x['value']:
            if x['name'] == 'password':
                x['value'] = gen_crypt_password(x['value'])
            keys.append(x['name'])
            values.append(x['value'])
            q.append('?')
    sql = 'REPLACE INTO {0} ({1}) VALUES ({2});'.format(table, ','.join(keys), ','.join(q))
    db.execute(sql,tuple(values))
    return json_response({'status': 'success', 'uri': '/json/'+table+'.json' }, 200)


@app.route('/del/json/<table>/<domain>/<id>.json', method='POST')
def delete_data(db, table, domain, id):
    json_data = bottle.request.json
    data_dict = {x['name']:x['value'] for x in json_data}

    if data_dict['id'] == id:
        sql = 'SELECT id FROM {0} WHERE id = ?;'.format(table)
        c = db.execute(sql, data_dict['id']).fetchone()
        if c:
            sql = 'DELETE FROM {0} WHERE id = ?;'.format(table)
            db.execute(sql, data_dict['id'])
    return json_response({'status': 'success', 'uri': '/json/'+table+'.json' }, 200)


## for development ###########################################################
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='./static')

if __name__ == '__main__':
    bottle.run(
        app,
        host='127.0.0.1',
        port=8080,
        debug=True,
        reloader=True
    )
##############################################################################
