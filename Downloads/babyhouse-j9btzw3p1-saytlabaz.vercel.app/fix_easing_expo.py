with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_ease = "      const ease = 1 - Math.pow(1 - progress, 4);"
new_ease = "      const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);"

content = content.replace(old_ease, new_ease)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
