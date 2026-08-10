(function () {
  "use strict";

  var MEASUREMENT_ID = "G-55Q6YKDDJH";
  var CONSENT_KEY = "ota_analytics_consent_v1";

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  window.gtag("consent", "default", {
    analytics_storage: "denied",
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    wait_for_update: 500
  });

  function loadAnalytics() {
    if (document.querySelector('script[data-ota-analytics]')) return;
    window.gtag("consent", "update", { analytics_storage: "granted" });
    var script = document.createElement("script");
    script.async = true;
    script.dataset.otaAnalytics = "true";
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + MEASUREMENT_ID;
    document.head.appendChild(script);
    window.gtag("js", new Date());
    window.gtag("config", MEASUREMENT_ID, { anonymize_ip: true });
  }

  function removeBanner() {
    var banner = document.querySelector("[data-ota-consent]");
    if (banner) banner.remove();
  }

  function saveChoice(choice) {
    try { localStorage.setItem(CONSENT_KEY, choice); } catch (error) {}
    removeBanner();
    if (choice === "accepted") loadAnalytics();
  }

  function showBanner() {
    removeBanner();
    var style = document.createElement("style");
    style.textContent = ".ota-consent{position:fixed;z-index:2147483000;left:18px;right:18px;bottom:18px;max-width:720px;margin:auto;padding:18px 20px;border:1px solid rgba(20,33,63,.16);border-radius:18px;background:#fff;color:#14213f;box-shadow:0 18px 55px rgba(20,33,63,.22);font:15px/1.55 system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif}.ota-consent strong{display:block;font-size:17px;margin-bottom:4px}.ota-consent p{margin:0}.ota-consent a{color:#14213f;text-decoration:underline}.ota-consent-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}.ota-consent button{border:1px solid #14213f;border-radius:999px;padding:10px 18px;font:inherit;font-weight:700;cursor:pointer}.ota-consent-accept{background:#14213f;color:#fff}.ota-consent-reject{background:#fff;color:#14213f}@media(max-width:520px){.ota-consent{left:10px;right:10px;bottom:10px;padding:16px}.ota-consent-actions button{flex:1}}";
    document.head.appendChild(style);
    var banner = document.createElement("section");
    banner.className = "ota-consent";
    banner.dataset.otaConsent = "true";
    banner.setAttribute("role", "dialog");
    banner.setAttribute("aria-label", "Analytics preferences");
    var privacyUrl = window.location.pathname.indexOf("/blog/") !== -1 ? "../privacy.html" : "privacy.html";
    banner.innerHTML = '<strong>Your privacy choices</strong><p>With your permission, OTA Learning Studio uses Google Analytics to understand visits and improve the website. Analytics stays off if you decline. Read the <a href="' + privacyUrl + '">privacy notice</a>.</p><div class="ota-consent-actions"><button class="ota-consent-accept" type="button" data-ota-accept>Accept analytics</button><button class="ota-consent-reject" type="button" data-ota-reject>Decline</button></div>';
    document.body.appendChild(banner);
    banner.querySelector("[data-ota-accept]").addEventListener("click", function () { saveChoice("accepted"); });
    banner.querySelector("[data-ota-reject]").addEventListener("click", function () { saveChoice("declined"); });
  }

  function eventNameForLink(link) {
    var href = link.getAttribute("href") || "";
    if (href.indexOf("cal.com/") !== -1) return "booking_click";
    if (href.indexOf("wa.me/") !== -1 || href.indexOf("whatsapp.com/") !== -1) return "whatsapp_click";
    if (href.indexOf("mailto:") === 0) return "email_click";
    if (href.indexOf("selar") !== -1) return "product_checkout_click";
    return "";
  }

  document.addEventListener("click", function (event) {
    var settingsButton = event.target.closest("[data-ota-cookie-settings]");
    if (settingsButton) {
      event.preventDefault();
      showBanner();
      return;
    }
    var link = event.target.closest("a[href]");
    if (!link || !document.querySelector('script[data-ota-analytics]')) return;
    var eventName = eventNameForLink(link);
    if (!eventName) return;
    window.gtag("event", eventName, {
      link_url: link.href,
      link_text: (link.textContent || "").trim().slice(0, 100),
      page_path: window.location.pathname
    });
  });

  document.addEventListener("DOMContentLoaded", function () {
    var choice = null;
    try { choice = localStorage.getItem(CONSENT_KEY); } catch (error) {}
    if (choice === "accepted") loadAnalytics();
    else if (choice !== "declined") showBanner();
  });
})();
