$(document).ready(function(){
    let login_valid = false;
    let email_valid = false;
    let password_valid = false;
    let password_conf_valid = false;

    let login_exp = /^[a-zA-Z0-9]{5,15}$/;
    let regExp_email = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;

    $('#login_field').change(function(){
        let login_val = $(this).val()
        if (!login_exp.test(login_val)){
            $('#login_err').text('Некорректный логин!');
            login_valid = false
        }else{
            $.ajax({
                url: '/ajax_reg',
                data: 'login_field=' + login_val,
                success: function(result){
                    if (result.message_login==='Логин занят!'){
                        $('#login_err').text(result.message_login);
                        login_valid = false
                    }else{
                        $('#login_err').text('');
                        login_valid = true
                    }
                }
            })
        }
    })

    $('#login_field').focus(function(){
        $('#login_err').text('');
    })

    $('#email_field').blur(function(){
        let email_val=$(this).val()
        if (regExp_email.test(email_val)){
            $('#email_err').text('');
            email_valid = true;
        }else{
            $('#email_err').text('email некорректный!');
            email_valid = false;
        }
    })

    $('#email_field').focus(function(){
        $('#email_err').text('');
    })


    $('#password_field').blur(function(){
        let password_val=$(this).val()
        if (password_val.length>7 && password_val.length<16){
            $('#password_err').text('');
            password_valid = true;
        }else{
            $('#password_err').text('Пароль должен быть от 8 до 15 символов!');
            password_valid = false;
        }
    })

    $('#password_field').focus(function(){
        $('#password_err').text('');
    })

    $('#password_confirmation_field').blur(function(){
        let password_confirm_val=$(this).val()
        let password_val=$('#password_field').val()
        if (password_val === password_confirm_val){
            $('#password_confirmation_err').text('');
            password_confirm_valid = true;
        }else{
            $('#password_confirmation_err').text('Пароли должны совпадать!');
            password_confirm_valid = false;
        }
    })

    $('#password_confirmation_field').focus(function(){
        $('#password_confirmation_err').text('');
    })

    $('#submit').click(function(){
        if (login_valid===true && email_valid===true && password_valid===true && password_confirm_valid===true){
            $('.form').attr('onsubmit', 'return true');
        }
    })
})

