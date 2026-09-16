import re
import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Navbar Logo
    content = content.replace('<a href="#" class="flex items-center gap-3">', '<a href="#top" class="flex items-center gap-3">')
    # Navbar Ana Səhifə
    content = content.replace('<a href="#" class="hover:text-kidora-pink', '<a href="#top" class="hover:text-kidora-pink')
    # Mobile menu Ana Səhifə
    content = content.replace('<a href="#" class="text-kidora-dark hover:text-kidora-pink', '<a href="#top" class="text-kidora-dark hover:text-kidora-pink')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
