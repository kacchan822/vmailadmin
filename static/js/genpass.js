(function() {
    'use strict';

    var length = document.getElementById('length');
    var length_value = document.getElementById('length_value');
    var btn = document.getElementById('generate_password');
    var InputPassword = document.getElementById('InputPassword');
    var numbers = document.getElementById('numbers');
    var symbols = document.getElementById('symbols');
    var available_password = document.getElementById('available_password');
    var addAccount_close = document.getElementById('addAccount_close');


    function getpassword() {
        var alphabet_seeds = 'abcdefghijklmnopqrstuvwxyz';
        var numbers_seeds = '0123456789';
        var symbols_seeds = '+=@#%?<>/&';

        var len = length.value;
        var pass = '';

        var seeds = alphabet_seeds + alphabet_seeds.toUpperCase();

        if (numbers.checked === true) {
            seeds += numbers_seeds;
        }

        if (symbols.checked === true) {
            seeds += symbols_seeds;
        }


        for (var i = 0; i < len; i++) {
            pass += seeds[Math.floor(Math.random() * seeds.length)];
        }
        InputPassword.value = pass;
    }

    length.addEventListener('change', function() {
        length_value.innerHTML = this.value;
    });

    btn.addEventListener('click', function() {
        getpassword();
        InputPassword.type = 'text';
        available_password.checked  = true;
    });

    available_password.addEventListener('change', function() {
        if ( available_password.checked  === true ) {
            InputPassword.type = 'text';
        } else {
            InputPassword.type = 'password';
        }
    });

    InputPassword.addEventListener('click', function() {
        this.select();
    });

    addAccount_close.addEventListener('click', function() {
        InputPassword.value = '';
        InputPassword.type = 'password';
        available_password.checked  = false;
    });


})();
