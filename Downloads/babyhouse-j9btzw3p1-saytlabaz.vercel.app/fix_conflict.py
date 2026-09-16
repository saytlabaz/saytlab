import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove scroll-smooth class from html
    content = content.replace('class="scroll-smooth"', '')
    content = content.replace('class=" scroll-smooth"', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

