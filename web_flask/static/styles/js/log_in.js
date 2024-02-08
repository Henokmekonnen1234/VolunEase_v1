
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
                // Store the token in the local storage
                localStorage.setItem('X-access-token', data.token);

                // Redirect to the dashboard page
                window.location.href = apiUrl1 + 'dashboard';
                console.log("token ",data.token)
                console.log(data.orgs)
            },
            error: function (error) {
                console.error('Error:', error);
                // Handle login error (e.g., display an error message)
            }
        });
    });
});


document.getElementById('logoutButton').addEventListener('click', function () {
    // Clear the token from local storage
    localStorage.removeItem('token');

    // Redirect to the login page
    window.location.href = '/login';
});
