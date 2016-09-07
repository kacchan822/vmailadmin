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

    <div><!-- tab -->
        <!-- Nav tabs -->
        <ul class="nav nav-tabs" role="tablist">
            <li role="presentation" class="active"><a href="#listindex" aria-controls="listindex" role="tab" data-toggle="tab">list index</a></li>
            <li role="presentation"><a href="#domain" aria-controls="domain" role="tab" data-toggle="tab">domain</a></li>
            <li role="presentation"><a href="#alias" aria-controls="alias" role="tab" data-toggle="tab">alias</a></li>
            <li role="presentation"><a href="#mailbox" aria-controls="mailbox" role="tab" data-toggle="tab">mailbox</a></li>
        </ul>
        <!-- Tab panes -->
        <div class="tab-content">
            <div role="tabpanel" class="tab-pane active" id="listindex">
                <h2>list index</h2>
                <p>Choose tab which you want to manage.</p>
            </div>
            <div role="tabpanel" class="tab-pane" id="domain">
                <h2>domain
                <a href="#" class="text-success btn btn-default" data-toggle="modal" data-target="#editData">Add</a></h2>
            </div>
            <div role="tabpanel" class="tab-pane" id="alias">
                <h2>alias
                <a href="#" class="text-success btn btn-default" data-toggle="modal" data-target="#editData">Add</a></h2>
            </div>
            <div role="tabpanel" class="tab-pane" id="mailbox">
                <h2>mailbox
                <a href="#" class="text-success btn btn-default" data-toggle="modal" data-target="#editData">Add</a></h2>
            </div>
        </div>
    </div><!-- tab -->
    <table class="table table-hover">
        <thead>
            <tr id="t_head"></tr>
        </thead>
        <tbody id="t_body">
        </tbody>
    </table>
</div><!--container-->


<div class="modal fade" id="editData" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <form>
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Edit data for </h4>
            </div>
            <div class="modal-body">
            </div>
            <div class="modal-footer">
            <button type="button" class="btn btn-danger pull-left" data-dismiss="modal" id="deleteData_submit">Delete</button>
            <button type="button" class="btn btn-default" data-dismiss="modal" id="editData_close">Close</button>
            <button type="button" class="btn btn-primary" data-dismiss="modal" id="editData_submit">Submit</button>
            </div>
            </form>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
<script src="/static/js/lists.js"></script>
<script>
</script>
</body>
</html>
