import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the previous block with a bulletproof custom smooth scroll
bulletproof_scroll = """
  /* --- Bulletproof Smooth Scroll (Works on ALL Safari versions) --- */
  function customSmoothScrollTo(targetPosition, duration) {
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    let startTime = null;

    function animation(currentTime) {
      if (startTime === null) startTime = currentTime;
      const timeElapsed = currentTime - startTime;
      const progress = Math.min(timeElapsed / duration, 1);
      
      // Easing function (easeInOutCubic)
      const ease = progress < 0.5 
        ? 4 * progress * progress * progress 
        : 1 - Math.pow(-2 * progress + 2, 3) / 2;
        
      window.scrollTo(0, startPosition + distance * ease);
      
      if (timeElapsed < duration) {
        requestAnimationFrame(animation);
      }
    }
    
    requestAnimationFrame(animation);
  }

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement || targetId === '#top') {
        e.preventDefault();
        
        // If it's #top, scroll to 0. Otherwise scroll to element's top position
        const topPos = targetId === '#top' ? 0 : targetElement.getBoundingClientRect().top + window.pageYOffset;
        
        // Scroll exactly over 800ms (0.8 seconds) for a beautifully cinematic scroll
        customSmoothScrollTo(topPos, 1200);
        
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

# Remove old intercept
import re
content = re.sub(r'/\* --- Smooth Scroll Intercept.*', '', content, flags=re.DOTALL)
content += bulletproof_scroll

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

