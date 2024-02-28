
$(document).ready(function () {
    let apiUrl = "http://127.0.0.2:5001/api/v1/";
    let weburl = "http://127.0.0.1:5000/";
    const token = getCookie('X-access-token');
    const events = getCookie("events")
    let methods = ""
    $.get({
        url: apiUrl + "volunteers",
        headers: {
            "Authorization": token
        },
        success: function(data) {
            let select = $("#volunteers")
            select.empty()
            data.forEach((value) => {
                select.append($("<option>").attr("value", value.id).text(`${value.first_name} ${value.mid_name} ${value.last_name}`))
            })
            console.log("Success form ",data)
        },
        error: function(error){
            clearCookie("message")
            setCookie("message", error, 30)
        }
    })

    $.get({
        url: apiUrl + "volunteers",
        headers: {
            "Authorization": token
        },
        success: function(data) {

        },
        error: function(error) {
            $(".event_container").hide()
            setCookie("message", error, 30)
        }
    })

    if ($(".create-event-form").attr("id") == "update_event") {
        apiUrl = apiUrl + "events/" + events
        methods = "PUT"
        $.get({
            url: apiUrl,
            success: function(data) {
                $("#title").val(`${data.event.title}`)
                $("#place").val(`${data.event.place}`)
                $("#start_time").val(`${data.event.start_time.substring(0, 19)}`)
                $("#end_time").val(`${data.event.end_time.substring(0, 19)}`)
                $("#description").text(`Description: ${data.event.description}`)
                console.log(data)
            },
            error: function(error) {
                setCookie("message", error, 30)
            }
        })
    } else if ($(".create-event-form").attr("id") == "create_event") {
        apiUrl = apiUrl + "events"
        methods = "POST"
    }

    $('.create-event-form').submit(function (event) {
      event.preventDefault();
        console.log("button pressed")
      // Get form data as a dictionary
      const selectElement = document.getElementById('volunteers');
      const selectedOptions = Array.from(selectElement.selectedOptions).map(option => option.value);

      const formData = new FormData(this);
      const image = document.getElementById("image")
      //const formElements = this.elements;

      // Check if formElements is defined and has a length property
    //   if (formElements && formElements.length) {
    //     for (let i = 0; i < formElements.length; i++) {
    //       const element = formElements[i];
    //       if (element.type !== 'submit' || element.type !== "") {
    //         formData[element.name] = element.value;
    //       }
    //     }
        if( image.files.length > 0) {
            formData.append("image", image.files[0])
        }

        formData.set("volunteers", selectedOptions);

        console.log("all files" , formData)
        $.ajax({
            url: apiUrl,
            type: methods,
            headers: {
                "Authorization": token
            },
            data: formData,
            contentType: false,
            processData: false,
            success: function(data){
                if ($(".create-event-form").attr("id") == "create_event") {
                    clearCookie("events")
                    setCookie("events", data.events.id, 30)
                }
                clearCookie("message")
                setCookie("message", data.message, 30)
                window.location.href = weburl + "events"
                console.log(data)
            },
            error: function(error){
                clearCookie("message")
                setCookie("message", error, 30)
            }
        })

      }

    );

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

  });
