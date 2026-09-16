import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the call to initReveal()
content = content.replace('initReveal();', '// initReveal(); removed in favor of AOS')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
