$(document).ready(function(){
  let message = " " + getCookie("message")
  const closeMessage = $("#messageBox")
  console.log("" + message)
  console.log(typeof message === "string")
  console.log(typeof message === "object")
  if (message !== null && message !== undefined && Object.prototype.toString.call(message) === "[object String]"){
    document.getElementById('messageBox').style.display = 'flex';
    $("#messageBox p").text(message)
    clearCookie("message")
    setTimeout(() => {
      document.getElementById('messageBox').style.display = 'none';
      clearCookie("message")
    }, 5000);
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