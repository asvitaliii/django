$(document).ready(function(){
    $('#check').click(function(){
        let login_val=$('#login_field').val()
        $.ajax({
            url: '/ajax_log',
            data: 'login_field=' + login_val,
            success: function(result){
                if (result.res==='OK'){
                    $('#check_state').text('')
                    $('.form').attr('onsubmit', 'return true')
                }else{
                $('#check_state').text('Пользователя не существует!')
                }
            }
        })
    })
})