$(document).ready(function(){
    const message = getCookie("message")
  const closeMessage = $("#messageBox")
  console.log(typeof message)
  if (message !== null && message !== undefined && typeof message === "string"){
    document.getElementById('messageBox').style.display = 'flex';
    $("#messageBox p").text(message)
    console.log(message)

    setTimeout(() => {
      document.getElementById('messageBox').style.display = 'none';
      clearCookie("message")
    }, 10000);
  }

  closeMessage.on("click", ".close-button", function(){
      document.getElementById('messageBox').style.display = 'none';
      clearCookie("message")
  })

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