
document.addEventListener('DOMContentLoaded', function() {
  var menuIcon = document.getElementById('menuIcon');
  var mainNav = document.getElementById('mainNav');

  menuIcon.addEventListener('click', function() {
    mainNav.classList.toggle('show');
  });
});

$(document).ready(function(){
  let apiUrl = "http://127.0.0.2:5001/api/v1/"
  const weburl = "http://127.0.0.1:5000/"

    $("#logout").on('click', function () {
      // Clear the token from local storage
      clearCookie('X-access-token');

      // Redirect to the login page
      window.location.href = weburl;
  });
  token = getCookie("X-access-token")

  $.get({
    url: apiUrl + "volunteers",
    headers: {
      "Authorization": token
    },
    success: function(data){
      $("#unsigned").hide()
      $("#unsigned_dashboard").hide()
    },
    error: function(error){
      clearCookie("X-access-token")
      setCookie("message", error, 30)
      $("#dashboard").hide()
      $("#volunteers_data").hide()
      $("#event_create").hide()
      $("#signed").hide()
      $("#myDiv").hide()
    }
  })

  $("#delete").on('click', function () {
    // Clear the token from local storage

    $.ajax({
      url: apiUrl + "organizations",
      type: "DELETE",
      headers: {
        "Authorization": token
      },
      success: function(data){
        clearCookie('X-access-token');
        clearCookie("message")
        setCookie("message", error.responseJSON.error, 30)
        window.location.href = weburl;
      },
      error: function(error){
        clearCookie("X-access-token")
        clearCookie("message")
            setCookie("message", error.responseJSON.error, 30)
      }
    })
});

  function clearCookie(name) {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`;
}

function getCookie(name) {
  const cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + '=')) {
          return cookie.substring(name.length + 1);
      }
  }
  return null;
}

function setCookie(name, value, days) {
  const expires = new Date();
  expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
  document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
}

  });
