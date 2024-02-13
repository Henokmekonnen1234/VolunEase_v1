$(document).ready(() => {
    const apiUrl = "http://127.0.0.2:5001/api/v1/events/"
    const weburl = "http://127.0.0.1:5000/"
    const events = getCookie("events")
    const myDiv = $('#myDiv');

    myDiv.on('click', '.update-btn', function () {
        window.location.href = weburl + "update-events"
    });

    myDiv.on('click', '.delete-btn', function () {
        $.ajax({
            url: apiUrl + events,
            headers: {
                "Authorization": token
            },
            type: "DELETE",
            success: function(data){
                window.location.href = weburl + "event-list"
            },
            error: function(error){
                console.log("Error ", error)
            }
        })
    });
    $.ajax({
        url: apiUrl + events,
        type: "GET",
        success: function(data) {
            $(".full-name").text(`Event: ${data.event.title}`)
            $(".phone-number").text(`Place: ${data.event.place}`)
            $(".email").text(`Starting Time: ${formatDate(data.event.start_time)}`)
            $(".gender").text(`Ending Time: ${formatDate(data.event.end_time)}`)
            $(".occupation").text(`Description: ${data.event.description}`)
            $(".total-hours").text(`Total Hours: ${data.event.part_time}`)
            var tbody = $('#volunteer-participate');
            tbody.empty();
            data.volun_list.forEach(function (volun_list) {
            var row = $('<tr>');
            row.append($('<td>').text(`${volun_list.first_name} ${volun_list.mid_name} ${volun_list.last_name}`));
            row.append($('<td>').text(volun_list.email));
            row.append($('<td>').text(volun_list.gender));
            row.append($('<td>').text(volun_list.occupation));
            row.append($('<td>').text(volun_list.phone_no));

            tbody.append(row);
            });
        },
        error: function (error) {
            $(".Volunter_container").hide()
            console.log("Error ", error)
        }
    })
    
    function formatDate(value){
        let date = new Date(value);
        return date.toLocaleString();
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
})