
$(document).ready(function () {
    let apiUrl = "http://127.0.0.2:5001/api/v1/";
    let weburl = "http://127.0.0.1:5000/";
    const register = "http://127.0.0.1:5000/register"

    let token = getCookie('X-access-token');
    let volun_id = getCookie("volun_id")

    if ($('.registration-form').attr("id") === "org_registration") {
        apiUrl = apiUrl + "organizations"
        weburl = weburl + "log-in"
        methods = "POST"
    } else if ($('.registration-form').attr("id") === "volun_registeer"){
        apiUrl = apiUrl + "volunteers"
        weburl = weburl + "volunteers"
        methods = "POST"
        $.get({
            url: apiUrl,
            headers: {
                "Authorization": token
            },
            success: function(data) {

            },
            error: function(error) {
                $(".registration-container").hide()
                clearCookie("message")
                setCookie("message", error.responseJSON.error, 30)
            }
        })
    } else if($('.registration-form').attr("id") === "update_org") {
      apiUrl = apiUrl + "organizations"
        weburl = weburl + "dashboard"
        methods = "PUT"
        $.get({
          url: apiUrl,
          headers: {
              "Authorization": token
          },
          success: function(data) {
            $("#name").val(data.name)
            $("#email").val(data.email)
            $("#password").val(data.password)
            $("#phone_no").val(data.phone_no)
            $("#website").val(data.website)
            $("#address").val(data.address)
            $("#description").text(data.description)

          },
          error: function(error) {
            clearCookie("message")
            setCookie("message", error.responseJSON.error, 30)
              window.location.href = register
          }
    })
  } else if($('.registration-form').attr("id") === "update_volun") {
    apiUrl = apiUrl + "volunteers/" + volun_id
      weburl = weburl + "volunteers"
      methods = "PUT"
      $.get({
        url: apiUrl,
        headers: {
            "Authorization": token
        },
        success: function(data) {
          $("#first_name").val(data.volunteer.first_name)
          $("#mid_name").val(data.volunteer.mid_name)
          $("#last_name").val(data.volunteer.last_name)
          $("#phone_no").val(data.volunteer.phone_no)
          $("#gender").val(data.volunteer.gender)
          $("#email").val(data.volunteer.email)
          $("#occupation").val(data.volunteer.occupation)
          console.log(data)
        },
        error: function(error) {
            clearCookie("message")
            setCookie("message", error.responseJSON.error, 30)
            window.location.href = register
        }
  })
}

    $('.registration-form').submit(function (event) {
      event.preventDefault();


      const formData = new FormData(this);
      if (document.getElementById('image').files.length > 0 ){
      formData.append('image', document.getElementById('image').files[0]);
      if ($('.registration-form').attr("id") === "org_registration") {
        formData.append('legal_document', document.getElementById('legal_document').files[0]);
      }
    }

        $.ajax({
          url: apiUrl,
          type: methods,
          headers: {
            "Authorization": token,
          },
          data: formData,
          contentType: false,  // Important: prevent jQuery from setting contentType
          processData: false,
          success: function (data) {
            if ($(".registration-form").attr("id") === "volun_registeer"){
                clearCookie("volun_id")
                setCookie("volun_id", data.id)
            }
            window.location.href = weburl

          },
          error: function (error) {
            clearCookie("message")
            setCookie("message", error.responseJSON.error, 30)
            window.location.href = register
          }
        });

      //}


  });


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




      // // Get form data as a dictionary
      // const formData = {};
      // const formElements = this.elements;

      // // Check if formElements is defined and has a length property
      // if (formElements && formElements.length) {
      //   for (let i = 0; i < formElements.length; i++) {
      //     const element = formElements[i];
      //     if (element.type !== 'submit') {
      //       formData[element.name] = element.value;
      //     }
      //   }
