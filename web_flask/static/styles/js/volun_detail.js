$(document).ready(() => {
    const apiUrl = "http://127.0.0.2:5001/api/v1/volunteers/"
    const weburl = "http://127.0.0.1:5000/"
    const volun_id = getCookie("volun_id")
    const token = getCookie("X-access-token")

    const myDiv = $('#myDiv');

    myDiv.on('click', '.update-btn', function () {
        window.location.href = weburl + "update-volunteers"
    });

    myDiv.on('click', '.delete-btn', function () {
        $.ajax({
            url: apiUrl + volun_id,
            headers: {
                "Authorization": token
            },
            type: "DELETE",
            success: function(data){
                window.location.href = weburl + "volunteers-list"
            },
            error: function(error){
                clearCookie("message")
                setCookie("message", error.responseJSON.error, 30)
            }
        })
    });

    $.get({
        url: apiUrl,
        headers: {
            "Authorization": token
        },
        success: function(data) {

        },
        error: function(error) {
            $(".Volunter_container").hide()
            clearCookie("message")
            setCookie("message", error.responseJSON.error, 30)
        }
    })

    $.ajax({
        url: apiUrl + volun_id,
        type: "GET",
        headers: {
            'Authorization': token
          },
        success: function(data) {
            if (data.volunteer.image !== null && data.volunteer.image !== undefined){
                $(".image").attr("src", "../static/images" + data.volunteer.image)
            } else {
                $(".image").attr("src", "../static/images/portrait-of-volunteers-pointing-at-t-shirt.jpg")
            }
            $(".full-name").text(`Full Name: ${data.volunteer.first_name} ${data.volunteer.mid_name} ${data.volunteer.last_name}`)
            $(".phone-number").text(`Phone Number: ${data.volunteer.phone_no}`)
            $(".email").text(`Email: ${data.volunteer.email}`)
            $(".gender").text(`Gender: ${data.volunteer.gender}`)
            $(".occupation").text(`Occupation: ${data.volunteer.occupation}`)
            $(".total-hours").text(`Total Hours: ${data.part_time}`)
            var tbody = $('#event_list_vol');
            tbody.empty();
            data.event_list.forEach(function (event_list) {
            var row = $('<tr>');
            row.append($('<td>').text(event_list.title));
            row.append($('<td>').text(event_list.place));
            row.append($('<td>').text(event_list.start_time));
            row.append($('<td>').text(event_list.end_time));
            row.append($('<td>').text(event_list.part_time));

            // Append the row to the table body
            tbody.append(row);
            });
        },
        error: function (error) {
            $(".Volunter_container").hide()
            clearCookie("message")
            setCookie("message", error.responseJSON.error, 30)
        }
    })

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
  
})