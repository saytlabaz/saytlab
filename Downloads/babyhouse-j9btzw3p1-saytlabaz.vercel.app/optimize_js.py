import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_observer = """    var observer = new IntersectionObserver(
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

new_observer = """    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
          } else {
            // Advanced mirror logic to prevent Safari flickering on large elements
            var rect = entry.boundingClientRect;
            // Only remove if it's completely scrolled out of view (either above or below)
            if (rect.top > (window.innerHeight || document.documentElement.clientHeight) || rect.bottom < 0) {
              entry.target.classList.remove('is-revealed');
            }
          }
        });
      },
      { threshold: 0, rootMargin: '0px 0px -10% 0px' }
    );"""
content = content.replace(old_observer, new_observer)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
