(function () {
  "use strict";

  function track(name, details) {
    if (typeof window.gtag !== "function" || !document.querySelector("script[data-ota-analytics]")) return;
    window.gtag("event", name, Object.assign({ page_path: window.location.pathname }, details || {}));
  }

  var viewed = false;
  function trackView() {
    if (viewed || !document.querySelector('[data-lead-magnet-form]') || !document.querySelector('script[data-ota-analytics]')) return;
    viewed = true;
    track('lead_magnet_view', { lead_magnet: 'seag_2026_8_week_plan' });
  }
  document.addEventListener('DOMContentLoaded', trackView);

  document.addEventListener("click", function (event) {
    if (event.target.closest("[data-ota-accept]")) trackView();
    var open = event.target.closest("[data-lead-magnet-open]");
    if (open) track("lead_magnet_open", { lead_magnet: "seag_2026_8_week_plan", link_url: open.href });

    var download = event.target.closest("[data-lead-magnet-download]");
    if (download) track("lead_magnet_download", { lead_magnet: "seag_2026_8_week_plan", link_url: download.href });
  });
})();
