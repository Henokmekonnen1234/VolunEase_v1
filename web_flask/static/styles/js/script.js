// Add this JavaScript to a new script.js file

document.addEventListener('DOMContentLoaded', function() {
    var menuIcon = document.getElementById('menuIcon');
    var mainNav = document.getElementById('mainNav');
  
    menuIcon.addEventListener('click', function() {
      mainNav.classList.toggle('show');
    });

    document.getElementById('logout').addEventListener('click', function () {
      // Clear the token from local storage
      clearCookie('X-access-token');
  
      // Redirect to the login page
      window.location.href = apiUrl1 ;
  });
  
    function clearCookie(name) {
      document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`;
  }
  
  });
