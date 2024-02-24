$(document).ready(function(){
    const searchInput = $('#searchInput');
    let apiUrl = "http://127.0.0.2:5001/api/v1/"
    let weburl = "http://127.0.0.1:5000/"
    const token = getCookie("X-access-token")

    if ($(".event-listing").attr("id") === "event_list"){
        apiUrl = apiUrl + "events"
        weburl = weburl + "event-list"
    } else if ($(".event-listing").attr("id") === "volun_list"){
        apiUrl = apiUrl + "volunteers"
        weburl = weburl + "volunteers-list"
    }
    searchInput.on('input', function (event) {
        event.preventDefault()
        const search_p = $(this).val();

        if (search_p.trim() !== '') {
          // Make an AJAX request to your server
          $.ajax({
            url: apiUrl,
            type: 'GET',
            headers: {
                "Authorization": token
            },
            data: {"search": search_p},
            success: function (data) {
                console.log(data)
                let eventList = $(".event-listing")
                eventList.empty()
                data.forEach((values) => {
                if ($(".event-listing").attr("id") === "event_list"){
                        let eventItem = $("<div class=\"event-item\">")
                        if (values.image !== null && values.image !== undefined){
                            eventItem.append($("<img>").attr("src", "../static/images" + values.image).attr("id",values.id))
                        }else {
                            eventItem.append($("<img>").attr("src", "../static/images/portrait-of-volunteers-pointing-at-t-shirt.jpg").attr("id",values.id))
                        }
                        eventItem.append($("<h3>").text(values.title))
                        eventItem.append($("<p class=\"place\">").text(`Place: ${values.place}`))
                        eventItem.append($("<p class=\"time\">").text(`Starting time: ${formatDate(values.start_time)}`))
                        eventItem.append($("<p class=\"time\">").text(`Ending time: ${formatDate(values.end_time)}`))
                        eventList.append(eventItem)

                } else if ($(".event-listing").attr("id") === "volun_list"){
                        let eventItem = $("<div class=\"event-item\">")
                        eventItem.empty()
                        if (values.image !== null && values.image !== undefined){
                            eventItem.append($("<img>").attr("src", "../static/images" + values.image).attr("id",values.id))
                        }else {
                            eventItem.append($("<img>").attr("src", "../static/images/portrait-of-volunteers-pointing-at-t-shirt.jpg").attr("id",values.id))
                        }
                        eventItem.append($("<h3>").text(`Full Name: ${values.first_name} ${values.mid_name} ${values.last_name}`))
                        eventItem.append($("<p class=\"place\">").text(values.gender))
                        eventItem.append($("<p class=\"time\">").text(values.email))
                        eventList.append(eventItem)
                }
            })
            },
            error: function (error) {
                clearCookie("message")
                setCookie("message", error.responseJSON.error, 30)
                window.location.href = weburl
            }
          });
        } else {
            window.location.href = weburl
        }
      });

      function formatDate(value){
        let date = new Date(value);
        return date.toLocaleString();
    }

    function setCookie(name, value, days) {
        const expires = new Date();
        expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
        document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
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

    function clearCookie(name) {
        document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`;
    }
})