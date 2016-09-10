# -*- coding: utf-8 -*-

## python3 standerd modules
from crypt import crypt, mksalt, METHOD_MD5, METHOD_SHA256, METHOD_SHA512
from hmac import compare_digest
import smtplib
from email.mime.text import MIMEText
import json
import re

## bottle modules
import bottle
from plugins import bottle_sqlite
from collection_json import Collections

## bottle settings
app = application = bottle.Bottle()
sqlite_plugin = bottle_sqlite.SQLitePlugin(dbfile='mailadmin.db', autocommit=True)
app.install(sqlite_plugin)


## common functions
def gen_crypt_password(password):
    crypt_password = crypt(password, mksalt(METHOD_SHA512))
    return crypt_password


def check_password_crypted(password):
    r = re.compile('^\$(1|5|6)\$[a-zA-Z0-9./]{,16}\$[a-zA-Z0-9./]+')
    if r.search(password):
        return password
    else:
        return gen_crypt_password(password)


def check_password(plainpass, hashpass):
    return compare_digest(crypt(plainpass, hashpass), hashpass)


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


@app.route('/json/<table:re:(domain|alias|mailbox)>.json')
def get_tabledata(db, table):
    res = Collections().get_format(table)
    sql = "SELECT * FROM {0}".format(table)
    c = db.execute(sql)
    for row in c.fetchall():
        d = {}
        if table == 'domain':
            domain_name = row['domain']
        elif table == 'alias':
            domain_name = row['email'].split('@')[1]
        elif table == 'mailbox':
            domain_name = row['domain_part']
        d['href'] = '/json/{0}/{1}/{2}.json'.format(table, domain_name, row['id'])
        d['data'] = []
        datas = Collections().get_template(table)
        for data in datas:
            data['value'] = row[data['name']]
            d['data'].append(data)
        res['collection']['items'].append(d)
    return json_response(json.dumps(res, indent=4), 200)


@app.route('/json/<table:re:(domain|alias|mailbox)>/<domain>/<data>.json')
def get_jsondata(db, table, domain, data):
    pass


@app.route('/json/<table:re:(domain|alias|mailbox)>/<domain>/<id>.json', method='POST')
def post_jsondata(db, table, domain, id):
    json_data = bottle.request.json
    keys = []
    values = []
    q = []
    for x in json_data:
        if x['value']:
            if x['name'] == 'password':
                x['value'] = check_password_crypted(x['value'])
            keys.append(x['name'])
            values.append(x['value'])
            q.append('?')
    sql = 'REPLACE INTO {0} ({1}) VALUES ({2});'.format(table, ','.join(keys), ','.join(q))
    db.execute(sql,tuple(values))
    return json_response({'status': 'success', 'uri': '/json/'+table+'.json' }, 200)


@app.route('/del/json/<table:re:(domain|alias|mailbox)>/<domain>/<id>.json', method='POST')
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
