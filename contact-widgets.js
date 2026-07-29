(function () {
  "use strict";

  var whatsappNumber = "2348079675840";
  var message = "Hello OTA Learning Studio, I would like to make an enquiry.";

  function addWhatsAppButton() {
    if (document.querySelector(".ota-whatsapp-button")) return;

    var link = document.createElement("a");
    link.className = "ota-whatsapp-button";
    link.href =
      "https://wa.me/" +
      whatsappNumber +
      "?text=" +
      encodeURIComponent(message);
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.setAttribute("aria-label", "Chat with OTA Learning Studio on WhatsApp");
    link.innerHTML =
      '<span class="ota-whatsapp-label">Chat on WhatsApp</span>' +
      '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M19.11 17.21c-.26-.13-1.53-.75-1.77-.84-.24-.09-.41-.13-.59.13-.17.26-.67.84-.82 1.01-.15.17-.3.2-.56.07-.26-.13-1.09-.4-2.08-1.29-.77-.68-1.29-1.53-1.44-1.79-.15-.26-.02-.4.11-.53.12-.12.26-.3.39-.45.13-.15.17-.26.26-.43.09-.17.04-.32-.02-.45-.07-.13-.59-1.42-.8-1.94-.21-.51-.43-.44-.59-.45h-.5c-.17 0-.45.07-.69.32-.24.26-.91.89-.91 2.17 0 1.27.93 2.5 1.06 2.67.13.17 1.83 2.79 4.43 3.91.62.27 1.1.43 1.48.55.62.2 1.18.17 1.63.1.5-.07 1.53-.63 1.75-1.23.22-.6.22-1.12.15-1.23-.06-.11-.24-.17-.5-.3zM16.04 5.33a10.49 10.49 0 0 0-8.9 16.06L5.65 26.8l5.54-1.45a10.49 10.49 0 1 0 4.85-20.02zm0 19.1a8.6 8.6 0 0 1-4.39-1.2l-.31-.19-3.29.86.88-3.2-.2-.33a8.6 8.6 0 1 1 7.31 4.06z"/></svg>';
    document.body.appendChild(link);
  }

  function loadTawk() {
    if (document.querySelector('script[src*="embed.tawk.to/6a6a6487e2808e1d43ea2a34"]')) {
      return;
    }

    window.Tawk_API = window.Tawk_API || {};
    window.Tawk_LoadStart = new Date();

    var script = document.createElement("script");
    var firstScript = document.getElementsByTagName("script")[0];
    script.async = true;
    script.src = "https://embed.tawk.to/6a6a6487e2808e1d43ea2a34/1junphcod";
    script.charset = "UTF-8";
    script.setAttribute("crossorigin", "*");

    if (firstScript && firstScript.parentNode) {
      firstScript.parentNode.insertBefore(script, firstScript);
    } else {
      document.head.appendChild(script);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", addWhatsAppButton);
  } else {
    addWhatsAppButton();
  }

  loadTawk();
})();

