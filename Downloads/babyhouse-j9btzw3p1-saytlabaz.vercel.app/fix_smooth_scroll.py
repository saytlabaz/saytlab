import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

smooth_scroll_js = """
  /* --- Smooth Scroll Intercept (Fix for Safari) --- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement || targetId === '#top') {
        e.preventDefault();
        
        // If it's #top, scroll to absolute top
        const topPos = targetId === '#top' ? 0 : targetElement.getBoundingClientRect().top + window.scrollY;
        
        window.scrollTo({
          top: topPos,
          behavior: 'smooth'
        });
        
        // Close mobile menu if open
        const mobileMenu = document.getElementById('mobileMenu');
        const mobileMenuToggle = document.getElementById('mobileMenuToggle');
        if (mobileMenu && mobileMenu.classList.contains('is-open')) {
            mobileMenu.classList.remove('is-open');
            if (mobileMenuToggle) mobileMenuToggle.setAttribute('aria-expanded', 'false');
        }
      }
    });
  });
"""

if "Smooth Scroll Intercept" not in content:
    content += "\n" + smooth_scroll_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

