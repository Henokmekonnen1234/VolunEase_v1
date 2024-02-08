$(document).ready(function(){
    const apiUrl = "http://127.0.0.2:5001/api/v1/"
    const weburl = "http://127.0.0.1:5000/"
    document.getElementById("registration-form").addEventListener('submit', function (event) {
        event.preventDefault();

        // Get form data as a dictionary
        const formData = {};
        const formElements = this.elements;

        // Check if formElements is defined and has a length property
        if (formElements && formElements.length) {
            for (let i = 0; i < formElements.length; i++) {
                const element = formElements[i];
                if (element.type !== 'submit') {
                    formData[element.name] = element.value;
                }
            }

            $.ajax({
                url: apiUrl + "organizations",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify(formData),
                success: function(data){
                    window.location.href = weburl + "log-in"
                },
                error: function (error) {
                    console.error('Error:', error);
                }
            })
        }
    });
});
