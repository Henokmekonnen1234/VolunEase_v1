$(document).ready(function (){
    const apiUrl = "http://127.0.0.2:5001/api/v1/events"
    const weburl = "http://127.0.0.1:5000/events"
    let events;

    $.ajax({
        url: apiUrl,
        type: "GET",
        success: function(data){
            let eventList = $(".event-listing")
            eventList.empty()

            data.forEach((values) => {
                let eventItem = $("<div class=\"event-item\">")

                eventItem.append($("<img>").attr("src", "../static/images/portrait-of-volunteers-pointing-at-t-shirt.jpg").attr("id",values.id))
                eventItem.append($("<h3>").text(values.title))
                eventItem.append($("<p class=\"place\">").text(`Place: ${values.place}`))
                eventItem.append($("<p class=\"time\">").text(`Starting time: ${formatDate(values.start_time)}`))
                eventItem.append($("<p class=\"time\">").text(`Ending time: ${formatDate(values.end_time)}`))
                eventList.append(eventItem)
            })
        }
    });

    $(".event-listing").on("click", "img", function (event){
        event.preventDefault()
        events = $(this).attr("id")
        clearCookie("events")
        setCookie("events", events, 30)
        window.location.href = weburl
    })

    function formatDate(value){
        let date = new Date(value);
        return date.toLocaleString();
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