import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_js = """  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement || targetId === '#top') {
        e.preventDefault();
        
        // If it's #top, scroll to 0. Otherwise scroll to element's top position
        const topPos = targetId === '#top' ? 0 : targetElement.getBoundingClientRect().top + window.pageYOffset;
        
        // Scroll exactly over 800ms (0.8 seconds) for a beautifully cinematic scroll
        customSmoothScrollTo(topPos, 1200);"""

new_js = """  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      
      // If it's just # or #top, it means scroll to top
      const isTop = (targetId === '#' || targetId === '#top');
      const targetElement = isTop ? null : document.querySelector(targetId);
      
      if (isTop || targetElement) {
        e.preventDefault();
        
        const topPos = isTop ? 0 : targetElement.getBoundingClientRect().top + window.pageYOffset;
        
        // Slower cinematic scroll (1800ms) as requested by user
        customSmoothScrollTo(topPos, 1800);"""

content = content.replace(old_js, new_js)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
