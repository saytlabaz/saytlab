/* =========================================================================
   SAYTLAB — wa.js  (BÜTÜN səhifələrdə yüklənir, defer)

   1) WhatsApp nömrəsi — TƏK MƏNBƏ. script.js ("Sifariş et" düymələri) və
      domain-search.js window.SAYTLAB_WA_NUMBER-dən oxuyur, nömrə başqa yerdə
      kodda təkrar yazılmır (HTML-dəki href-lər yalnız JS-siz fallback-dır).
   2) [data-wa="mesaj"] linkləri — href əvvəlcədən doldurulmuş WhatsApp
      mesajına çevrilir (e-poçt sifarişi və s.).
   3) Əlaqə formu (#contactForm) — heç bir serverə göndərilmir: sahələr
      yığılıb WhatsApp-da hazır mətn kimi açılır.
   CSP: inline script yoxdur — bu fayl <script defer> ilə qoşulur.
   ========================================================================= */
(function () {
  'use strict';

  var WA_NUMBER = '994103136941';
  window.SAYTLAB_WA_NUMBER = WA_NUMBER;

  function waUrl(text) {
    return 'https://wa.me/' + WA_NUMBER + (text ? '?text=' + encodeURIComponent(text) : '');
  }
  window.saytlabWaUrl = waUrl;

  function init() {
    /* ---------- [data-wa] linkləri ---------- */
    var links = document.querySelectorAll('a[data-wa]');
    for (var i = 0; i < links.length; i++) {
      links[i].href = waUrl(links[i].getAttribute('data-wa'));
    }

    /* ---------- Əlaqə formu → WhatsApp ---------- */
    var form = document.getElementById('contactForm');
    if (!form) return;
    var errorEl = document.getElementById('contactError');

    function showError(msg, field) {
      if (errorEl) { errorEl.textContent = msg; errorEl.hidden = false; }
      if (field) { field.setAttribute('aria-invalid', 'true'); field.focus(); }
    }
    function clearError() {
      if (errorEl) { errorEl.textContent = ''; errorEl.hidden = true; }
      var bad = form.querySelectorAll('[aria-invalid="true"]');
      for (var j = 0; j < bad.length; j++) bad[j].removeAttribute('aria-invalid');
    }
    form.addEventListener('input', function (e) {
      if (e.target.getAttribute('aria-invalid') === 'true') clearError();
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      clearError();
      var name = form.elements.name.value.trim();
      var phone = form.elements.phone.value.trim();
      var service = form.elements.service.value;
      var message = form.elements.message.value.trim();

      if (name.length < 2) { showError('Zəhmət olmasa adınızı yazın.', form.elements.name); return; }
      if (message.length < 3) { showError('Zəhmət olmasa mesajınızı yazın.', form.elements.message); return; }

      var lines = [
        'Salam, SaytLab!',
        'Ad: ' + name,
      ];
      if (phone) lines.push('Telefon: ' + phone);
      lines.push('Xidmət: ' + service, '', message);

      var url = waUrl(lines.join('\n'));
      /* Yeni tabda aç; brauzer popup-u bloklasa eyni tabda keç. */
      var win = window.open(url, '_blank');
      if (win) { try { win.opener = null; } catch (_) { /* cross-origin */ } }
      else window.location.href = url;
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
