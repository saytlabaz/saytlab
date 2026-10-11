/* Meta (Facebook) Pixel — bütün səhifələrdə PageView izləməsi.
   Meta-nın standart snippet-i; CSP-ni sərt saxlamaq üçün (script-src 'unsafe-inline'
   OLMASIN) ayrıca fayldadır. Pixel ID: 4331233943803470

   FƏRQ (performans): fbevents.js ~406 KB-dır və özündən sonra daha ~320 KB config
   çəkir. Əvvəl bu, səhifə ilə eyni anda yüklənirdi və ilk render üçün lazım olan
   şəbəkə/CPU-nu yeyirdi (xüsusilə Safari-də, JS parse/exec daha bahalıdır).
   İndi fbq() dərhal təyin olunur və çağırışlar növbəyə (n.queue) yığılır — heç bir
   hadisə itmir — kitabxananın özü isə yalnız `load`-dan sonra, boş vaxtda (və ya
   istifadəçi ilk dəfə toxunanda/klikləyəndə, hansı əvvəl olsa) yüklənir. Kitabxana
   qalxan kimi növbədəki init + PageView avtomatik göndərilir. */
!function (f, b, e, v) {
  if (f.fbq) return;
  var n = f.fbq = function () {
    n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
  };
  if (!f._fbq) f._fbq = n;
  n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];

  var injected = false;
  function inject() {
    if (injected) return;
    injected = true;
    var t = b.createElement(e); t.async = !0; t.src = v;
    var s = b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t, s);
  }

  /* DONMA DÜZƏLİŞİ (2026-10): əvvəl kitabxana `load`-dan dərhal sonra (idle, ~0.7–1s)
     yüklənirdi — bu, məhz preloader-in "şüşə qırılması" və hero giriş animasiyasının
     oynadığı ana düşürdü. fbevents.js-in parse/exec-i uzun bloklayıcı tapşırıqdır və
     animasiyanı bir anlıq dondururdu. İndi: load + 3.5s gözlə, sonra boş vaxtda yüklə.
     İlk toxunuş/klikdə də artıq yüklənmir (o an yüklənsə həmin klik "donmuş" hiss
     olunurdu). Hadisələr itmir: fbq() növbəsi saxlanılır, istifadəçi səhifəni tərk
     edəndə (gizlənəndə) isə dərhal yüklənir. */
  var START_DELAY = 3500;
  function schedule() {
    setTimeout(function () {
      if (f.requestIdleCallback) f.requestIdleCallback(inject, { timeout: 2000 });
      else inject();
    }, START_DELAY);
  }

  if (b.readyState === 'complete') schedule();
  else f.addEventListener('load', schedule, { once: true });

  /* Tab gizlənəndə / səhifə tərk ediləndə gözləmə — PageView itməsin. */
  b.addEventListener('visibilitychange', function () {
    if (b.visibilityState === 'hidden') inject();
  });
  f.addEventListener('pagehide', inject, { once: true });
}(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');

fbq('init', '4331233943803470');
fbq('track', 'PageView');
