import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Scroll-reveal to be continuous
reveal_old = """    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.05, rootMargin: '0px 0px 0px 0px' }
    );"""

reveal_new = """    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
          } else {
            // Remove class so it animates again when scrolling back
            entry.target.classList.remove('is-revealed');
          }
        });
      },
      { threshold: 0.05, rootMargin: '0px 0px 0px 0px' }
    );"""
content = content.replace(reveal_old, reveal_new)

# 2. Add Cursor logic
cursor_js = """
  /* --- 8. Custom Cursor --- */
  function initCursor() {
    if (reduceMotion) return;
    var matchMedia = window.matchMedia('(pointer: fine)');
    if (!matchMedia.matches) return;

    var dot = document.querySelector('.cursor-dot');
    var ring = document.querySelector('.cursor-ring');
    if (!dot || !ring) return;

    var root = document.documentElement;
    root.classList.add('cursor-custom');

    var pointer = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
    var cursor = { rx: pointer.x, ry: pointer.y };

    window.addEventListener('mousemove', function(e) {
      pointer.x = e.clientX;
      pointer.y = e.clientY;
      if (e.target.closest('a, button, [data-magnetic], [data-cursor-hot], .ig-card')) {
        root.classList.add('cursor-hot');
      } else {
        root.classList.remove('cursor-hot');
      }
    }, { passive: true });

    window.addEventListener('mouseleave', function() { root.classList.add('cursor-hidden'); }, { passive: true });
    window.addEventListener('mouseenter', function() { root.classList.remove('cursor-hidden'); }, { passive: true });
    window.addEventListener('blur', function() { root.classList.add('cursor-hidden'); });

    function lerp(start, end, amt) {
      return (1 - amt) * start + amt * end;
    }

    function renderCursor() {
      dot.style.transform = `translate3d(${pointer.x}px, ${pointer.y}px, 0)`;
      cursor.rx = lerp(cursor.rx, pointer.x, 0.2);
      cursor.ry = lerp(cursor.ry, pointer.y, 0.2);
      ring.style.transform = `translate3d(${cursor.rx.toFixed(2)}px, ${cursor.ry.toFixed(2)}px, 0)`;
      requestAnimationFrame(renderCursor);
    }
    requestAnimationFrame(renderCursor);
  }
"""

content = content.replace("function init() {", cursor_js + "\n  function init() {")
content = content.replace("initTilt();\n  }", "initTilt();\n    initCursor();\n  }")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

