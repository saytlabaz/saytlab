import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("window.addEventListener('mouseleave', function() { root.classList.add('cursor-hidden'); }, { passive: true });", "// mouseleave removed")
content = content.replace("window.addEventListener('mouseenter', function() { root.classList.remove('cursor-hidden'); }, { passive: true });", "// mouseenter removed")
content = content.replace("window.addEventListener('blur', function() { root.classList.add('cursor-hidden'); });", "// blur removed")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

