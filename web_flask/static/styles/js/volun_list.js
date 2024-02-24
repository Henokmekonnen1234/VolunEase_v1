$(document).ready(function (){
    const apiUrl = "http://127.0.0.2:5001/api/v1/volunteers"
    const weburl = "http://127.0.0.1:5000/volunteers"
    const token = getCookie("X-access-token")
    $.get({
        url: apiUrl,
        headers: {
            "Authorization": token
        },
        success: function(data) {

        },
        error: function(error) {
            $(".registration-container").hide()
        }
    })
    $.ajax({
        url:apiUrl,
        type: "GET",
        headers: {
            'Authorization': token,
          },
        success: function(datas){
            let eventList = $(".event-listing")
            eventList.empty()
            datas.forEach((data) => {
                let eventItem = $("<div class=\"event-item\">")
                eventItem.empty()
                if(data.image !== null && data.image !== undefined){
                    eventItem.append($("<img>").attr("src", "../static/images" + data.image).attr("id", data.id))
                } else {
                    eventItem.append($("<img>").attr("src", "../static/images/portrait-of-volunteers-pointing-at-t-shirt.jpg").attr("id", data.id))
                }
                eventItem.append($("<h3>").text(`Full Name: ${data.first_name} ${data.mid_name} ${data.last_name}`))
                eventItem.append($("<p class=\"place\">").text(data.gender))
                eventItem.append($("<p class=\"time\">").text(data.email))
                
                eventList.append(eventItem)
            });
        },
        error: function(error){
            console.log("Event ", error)
        }
    })

    $(".event-listing").on("click", "img", function () {
        const volun_id = $(this).attr("id")
        clearCookie("volun_id")
        setCookie("volun_id", volun_id, 30)
        window.location.href = weburl
    })

    function setCookie(name, value, days) {
        const expires = new Date();
        expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
        document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
    }

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
})