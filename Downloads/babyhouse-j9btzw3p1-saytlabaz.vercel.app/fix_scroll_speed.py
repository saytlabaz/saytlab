import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace 1800ms with 800ms for normal speed
content = content.replace('customSmoothScrollTo(topPos, 1800);', 'customSmoothScrollTo(topPos, 800);')

# Also, if there are any other occurrences, let's fix them just in case
content = content.replace('customSmoothScrollTo(topPos, 1200);', 'customSmoothScrollTo(topPos, 800);')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
