(function () {
  "use strict";

  function track(name, details) {
    if (typeof window.gtag !== "function" || !document.querySelector("script[data-ota-analytics]")) return;
    window.gtag("event", name, Object.assign({ page_path: window.location.pathname }, details || {}));
  }

  document.addEventListener("DOMContentLoaded", function () {
    if (document.querySelector("[data-lead-magnet-form]")) {
      track("lead_magnet_view", { lead_magnet: "seag_2026_8_week_plan" });
    }
  });

  document.addEventListener("click", function (event) {
    var open = event.target.closest("[data-lead-magnet-open]");
    if (open) track("lead_magnet_open", { lead_magnet: "seag_2026_8_week_plan", link_url: open.href });

    var download = event.target.closest("[data-lead-magnet-download]");
    if (download) track("lead_magnet_download", { lead_magnet: "seag_2026_8_week_plan", link_url: download.href });
  });
})();
