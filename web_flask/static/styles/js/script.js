// Add this JavaScript to a new script.js file

document.addEventListener('DOMContentLoaded', function() {
    var menuIcon = document.getElementById('menuIcon');
    var mainNav = document.getElementById('mainNav');
  
    menuIcon.addEventListener('click', function() {
      mainNav.classList.toggle('show');
    });
  });
