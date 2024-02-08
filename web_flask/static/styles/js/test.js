$(document).ready(() => {
    const apiUrl = 'http://127.0.0.1:5000';
    const messageDiv = $('#message');

    // Function to handle AJAX requests
    const sendRequest = (url, method, data, callback) => {
        $.ajax({
            url: apiUrl + url,
            type: method,
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: callback,
            error: (xhr, status, error) => {
                console.error(`Error: ${status} - ${error}`);
            }
        });
    };

    // Login Button Click Event
    $('#loginButton').click(() => {
        const username = prompt('Enter username:');
        const password = prompt('Enter password:');
        
        sendRequest('/login', 'POST', { username, password }, (response) => {
            if (response.token) {
                // Store the token securely (e.g., in a cookie or local storage)
                document.cookie = `token=${response.token}`;
                messageDiv.text('Login successful!');
            } else {
                messageDiv.text(response.message);
            }
        });
    });

    // Dashboard Button Click Event
    $('#dashboardButton').click(() => {
        const token = getCookie('token');
        if (token) {
            sendRequest('/dashboard', 'GET', { token }, (response) => {
                messageDiv.text(response.message);
            });
        } else {
            messageDiv.text('Please log in first.');
        }
    });

    // Logout Button Click Event
    $('#logoutButton').click(() => {
        // Remove the token (e.g., clear the cookie or local storage)
        document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
        messageDiv.text('Logout successful!');
    });

    // Function to get a cookie by name
    const getCookie = (name) => {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [cookieName, cookieValue] = cookie.trim().split('=');
            if (cookieName === name) {
                return cookieValue;
            }
        }
        return null;
    };
});
