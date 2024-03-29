
// login.js
$(document).ready(function () {
    $('.login-form').submit(function (event) {
        event.preventDefault();

        const apiUrl = 'http://127.0.0.2:5001/api/v1/';
        const apiUrl1 = "http://127.0.0.1:5000/"
        const username = $('#email').val();
        const password = $('#password').val();

        $.ajax({
            url: apiUrl + 'login',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                email: username,
                password: password,
            }),
            success: function (data) {
                clearCookie('X-access-token');
                setCookie('X-access-token', data.token, 30);
                window.location.href = apiUrl1 + 'dashboard';
                console.log(data.orgs)
            },
            error: function (error) {
                clearCookie("message")
                setCookie("message", error.responseJSON.error, 30)
               window.location.href = apiUrl1 + "log-in"
            // console.log(error.responseJSON.message)
            }
        });
    });

    function setCookie(name, value, days) {
        const expires = new Date();
        expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
        document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
    }

    function clearCookie(name) {
        document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`;
    }

});


