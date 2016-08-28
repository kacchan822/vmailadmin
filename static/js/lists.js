//omajinai
(function() {
'use strict';

//code
function dataget(data_uri){
    $.getJSON( data_uri, function(data){
        var itemsTemplate = data.collection.template.data;

        for ( var i in itemsTemplate ) {
            $('.modal-body').append( $('<div class="form-group"></div>')
                .append(
                    $('<label></label>')
                        .attr('for', itemsTemplate[i].name)
                        .html(itemsTemplate[i].name)
                    )
                .append(
                    $('<input>')
                        .attr('type', 'text')
                        .attr('class', 'form-control')
                        .attr('id', itemsTemplate[i].name)
                        .attr('name', itemsTemplate[i].name)
                    )
                )
        };

        for ( var i in itemsTemplate ) {
            $('#t_head').append('<th>' + itemsTemplate[i].name + '</th>');
        };
        $('#t_head').append('<th>Action</th>');

    	var itemsArray = data.collection.items;
        for ( var i in itemsArray ) {
            $('#t_body').append(
                $('<tr></tr>').attr('id', 'items_row_no_' + i )
            );
            for (var j in itemsArray[i].data ) {
                if ( itemsArray[i].data[j].name == 'id' ) {
                    $('#items_row_no_' + i).append(
                        $('<td></td>').append(
                            $('<a></a>')
                                .attr('href', itemsArray[i].href)
                                .html(itemsArray[i].data[j].value)
                        ).attr('class', 'items_data_name_' + itemsArray[i].data[j].name)
                    );
                } else {
                    $('#items_row_no_' + i).append(
                        $('<td></td>')
                            .html(itemsArray[i].data[j].value)
                            .attr('class', 'items_data_name_' + itemsArray[i].data[j].name)
                    );
                }
            }
            $('#items_row_no_' + i).append(
                $('<td></td>').append(
                    $('<a></a>')
                        .attr('href', '#')
                        .attr('class', 'btn btn-default')
                        .attr('data-toggle', 'modal')
                        .attr('data-target', '#editData')
                        .attr('data-rowno', i)
                        .text('Edit')
                )
            );
        };
    });
};


// Event handlers
$('#editData').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var rowno = button.data('rowno');
    var row_data = $('#items_row_no_' + rowno).find('.items_data_name_id').text();
    var row_uri = $('#items_row_no_' + rowno).find('a').attr('href');
    var modal = $(this);

    modal.find('.modal-title').text('Edit data for ' + 'id' + ':' + row_data);

    if ( row_uri ) {
        modal.find('#editData_submit').attr('data-uri', row_uri);
    } else {
        var now_table = $('li.active').find('a').text()
        row_uri = '/json/' + now_table + '/add/add.json'
        modal.find('#editData_submit').attr('data-uri', row_uri);
    }

    var inputdata = $('#items_row_no_' + rowno );

    $("input").each(function(i) {
        var v = inputdata.find('td.items_data_name_' + $(this).attr('name'));
        $(this).attr('value', v.text());
        switch ($(this).attr('name')) {
            case 'id':
            case 'local_part':
            case 'domain_part':
                $(this).attr('readonly', 'readonly');
                break;
            case 'password':
                $(this).attr('type', 'password');
        };
    });

    $('input#username').change(function(e) {
        var username = $(this).val();
        var reg_mail = /([\w.-]+)@([\w.-]+)/;

        $('input#local_part').attr('value', username.match(reg_mail)[1]);
        $('input#domain_part').attr('value', username.match(reg_mail)[2]);
    });
});


$('#editData').on('hidden.bs.modal', function (event) {
    $(this).find('form')[0].reset();
});


$('#editData_submit').on('click', function(event) {
    var row_uri = $(this).attr('data-uri');
    var data = [];
    var data_row = {};

    // create JSON data
    $("input").each(function(i) {
        data_row = { name: $(this).attr('name'), value: $(this).val() };
        data.push(data_row);
    });


    // ajax POST
    $.ajax({
        url: row_uri,
        method: 'post',
        dataType: 'json',
        data: JSON.stringify(data),
        cache: false,
        contentType: 'application/json'
    }).done(function( res ) {
        alert('success');
        $('#t_head').empty();
        $('#t_body').empty();
        $('.modal-body').empty();
        dataget(res['uri']);
    }).fail(function( jqXHR, textStatus, errorThrown ) {
        alert('failed')
    });
});


$('#addData_submit').on('click', function(event) {
    var data = [];
    var data_row = {};

    // create JSON data
    $("input").each(function(i) {
        data_row = { name: $(this).attr('name'), value: $(this).val() };
        data.push(data_row);
    });

    // ajax POST
    $.ajax({
        url: '/json/'+ $('li.active').text() +'/new/new.json',
        method: 'post',
        dataType: 'json',
        data: JSON.stringify(data),
        cache: false,
        contentType: 'application/json'
    }).done(function( res ) {
        alert('success');
        $('#t_head').empty();
        $('#t_body').empty();
        $('.modal-body').empty();
        dataget(res['uri']);
    }).fail(function( jqXHR, textStatus, errorThrown ) {
        alert('failed')
    });
});


$('a[data-toggle="tab"]').on('shown.bs.tab', function (event) {
  $('#t_head').empty();
  $('#t_body').empty();
  $('.modal-body').empty();
  if ( $(event.target).text() != 'list index' ){
      dataget('/json/' + $(event.target).text() + '.json');
  };
});

//end code
// omajinai
})();
