import re
import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add scroll-smooth to HTML
    if '<html lang="az"' in content and 'scroll-smooth' not in content:
        content = content.replace('<html lang="az"', '<html lang="az" class="scroll-smooth"')
        content = content.replace('<html lang="az" >', '<html lang="az" class="scroll-smooth">')

    # Also make sure the footer BabyHouse link explicitly goes to top
    if filepath == 'index.html':
        old_footer_link = '<a href="#" class="flex items-center gap-3 mb-6">'
        new_footer_link = '<a href="#top" class="flex items-center gap-3 mb-6">'
        content = content.replace(old_footer_link, new_footer_link)
        
        # Add id="top" to the body tag just in case
        if '<body class=' in content and 'id="top"' not in content:
            content = content.replace('<body class="', '<body id="top" class="')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

