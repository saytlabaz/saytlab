import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_nav = 'class="max-w-7xl mx-auto px-6 py-3 flex justify-between items-center"'
new_nav = 'class="max-w-7xl mx-auto bg-white/90 backdrop-blur-lg rounded-full shadow-sm border border-gray-100 px-6 py-3 flex justify-between items-center"'
content = content.replace(old_nav, new_nav)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Do for other html files too
import glob
for filepath in glob.glob('*.html'):
    if filepath == 'index.html': continue
    with open(filepath, 'r', encoding='utf-8') as f:
        file_content = f.read()
    file_content = file_content.replace(old_nav, new_nav)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_content)

