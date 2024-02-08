// Add this JavaScript to a separate dashboard.js file

$(document).ready(function () {
    const apiUrl = 'http://127.0.0.2:5001/api/v1/dashboard';
    const apiUrl1 = 'http://127.0.0.1:5000/';
    
    var token = getCookie('X-access-token');

    $.ajax({
        url: apiUrl,
        type: 'GET',
        headers: {
          'Authorization': token,
          'Content-Type': 'application/json',
        },
        success: function (data) {
          $(".organization-info h1").text(data.org.name)
          $(".description-section p").text(data.org.description)
          console.log(data)
        },
        error: function (error) {
          $(".dashboard-container ").hide()
            console.error('Error:', error);
            // Handle login error (e.g., display an error message)
        }
    });

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

  
});


document.addEventListener('DOMContentLoaded', function () {
    // Events chart data
    var eventsData = {
      labels: ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
      datasets: [{
        label: 'Events in Each Year',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
        data: [10, 15, 8, 20, 12],
      }]
    };
  
    // Volunteers donut chart data
    var volunteersData = {
      labels: ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
      datasets: [{
        data: [50, 30, 40, 60, 45],
        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4CAF50', '#FF9800'],
        hoverBackgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4CAF50', '#FF9800'],
      }]
    };
  
    // Get chart canvases
    var eventsCanvas = document.getElementById('eventsChart').getContext('2d');
    var volunteersCanvas = document.getElementById('volunteersDonutChart').getContext('2d');
  
    // Create charts
    var eventsChart = new Chart(eventsCanvas, {
      type: 'bar',
      data: eventsData,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [{
            stacked: true,
          }],
          yAxes: [{
            stacked: true,
            ticks: {
              beginAtZero: true,
            },
          }],
        },
      },
    });
  
    var volunteersDonutChart = new Chart(volunteersCanvas, {
      type: 'doughnut',
      data: volunteersData,
      options: {
        responsive: true,
        maintainAspectRatio: false,
      },
    });
  });
  