$(document).ready(function () {
    const apiUrl = 'http://127.0.0.2:5001/api/v1/dashboard';

    const token = getCookie('X-access-token');
    let dataValue;


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
          $(".organization-image img").attr("src", "../static/images" + data.org.image)
          dataValue = data.events_year

          //chart data
          let keys = Object.keys(dataValue)
    let values = Object.values(dataValue)
    var eventsData = {
      labels: keys, //['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
      datasets: [{
        label: 'Events in Each Year',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
        data: values, // [10, 15, 8, 20, 12]
      }]
    };

    // Volunteers donut chart data
    var volunteersData = {
      labels: Object.keys(data.volun_year), //['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
      datasets: [{
        data: Object.values(data.volun_year), //[50, 30, 40, 60, 45]
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


        },
        error: function (error) {
          $(".dashboard-container ").hide()
          clearCookie("message")
          setCookie("message", error, 30)
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

  function setCookie(name, value, days) {
    const expires = new Date();
    expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
    document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
  }

  function clearCookie(name) {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`;
}

  });
