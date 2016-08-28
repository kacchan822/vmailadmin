<!DOCTYPE html>
<html lang='ja'>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Postfix/Dovocot Virtual Mail User Management System</title>
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet">
<link href="/static/css/style.css" rel="stylesheet">
<!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
</head>
<body>
<div class="container">
    <div class="page-header">
    <a href="/"><h1><small>Postfix/Dovocot</small><br>Virtual Mail User Management System</h1></a>
    </div>
    %if error:
        <div class="alert alert-warning" role="alert">{{error}}</div>
    %end
    <div class="jumbotron">
        <form class="form-horizontal" action="login" method="POST">
        	<div class="form-group">
        		<label class="col-sm-2 control-label" for="InputEmail">メールアドレス</label>
        		<div class="col-sm-10">
        			<input type="email" class="form-control" id="InputEmail" placeholder="メールアドレス"  name="email">
        		</div>
        	</div>
        	<div class="form-group">
        		<label class="col-sm-2 control-label" for="InputPassword">パスワード</label>
        		<div class="col-sm-10">
        			<input type="password" class="form-control" id="InputPassword" placeholder="パスワード"  name="password">
        		</div>
        	</div>
        	<div class="form-group">
        		<div class="col-sm-offset-2 col-sm-10">
        			<button type="submit" class="btn btn-primary pull-right">ログイン</button>
        		</div>
        	</div>
        </form>
	</div>
</div><!--container-->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
</body>
</html>
