import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_ease = """      // Easing function (easeInOutCubic)
      const ease = progress < 0.5 
        ? 4 * progress * progress * progress 
        : 1 - Math.pow(-2 * progress + 2, 3) / 2;"""

new_ease = """      // Easing function (easeOutQuart - starts fast instantly, slows down at the end)
      const ease = 1 - Math.pow(1 - progress, 4);"""

content = content.replace(old_ease, new_ease)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
