import re
import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert bottom logo
    content = content.replace('class="w-16 h-16 object-contain mix-blend-multiply"', 'class="w-16 h-16 object-contain"')
    
    # Revert top logo
    content = content.replace('class="h-10 md:h-12 w-auto object-contain mix-blend-multiply"', 'class="h-10 md:h-12 w-auto object-contain"')

    # Make the top menu completely transparent to fulfill "remove background"
    # Current navbar: <div class="max-w-7xl mx-auto bg-white/90 backdrop-blur-lg rounded-full shadow-sm border border-gray-100 px-6 py-3 flex justify-between items-center">
    old_nav = 'class="max-w-7xl mx-auto bg-white/90 backdrop-blur-lg rounded-full shadow-sm border border-gray-100 px-6 py-3 flex justify-between items-center"'
    new_nav = 'class="max-w-7xl mx-auto px-6 py-3 flex justify-between items-center"'
    content = content.replace(old_nav, new_nav)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
