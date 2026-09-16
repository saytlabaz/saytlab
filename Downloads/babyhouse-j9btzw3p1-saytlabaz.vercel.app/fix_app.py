import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the incorrectly appended part
content = content.split('})();')[0]

# Add initFAQ inside the IIFE
faq_js = """
  /* --- 9. FAQ Accordion --- */
  function initFAQ() {
    const faqBtns = document.querySelectorAll('.faq-btn');
    faqBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const content = btn.nextElementSibling;
        const icon = btn.querySelector('i');
        
        // Close all other accordions
        faqBtns.forEach(otherBtn => {
            if(otherBtn !== btn) {
                otherBtn.nextElementSibling.style.maxHeight = null;
                otherBtn.querySelector('i').style.transform = 'rotate(0deg)';
            }
        });

        if (content.style.maxHeight) {
          content.style.maxHeight = null;
          icon.style.transform = 'rotate(0deg)';
        } else {
          content.style.maxHeight = content.scrollHeight + 'px';
          icon.style.transform = 'rotate(180deg)';
        }
      });
    });
  }
"""

content = content.replace('function init() {', faq_js + '\n  function init() {')
content = content.replace('initCursor();\n  }', 'initCursor();\n    initFAQ();\n  }')

content += "\n})();\n"

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

