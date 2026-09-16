import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def cleanup_class(match):
    cls_str = match.group(1)
    # Split by space
    classes = cls_str.split()
    
    # We want to keep only the highest text- size for base, md:, lg:
    # Actually, the simplest fix is to just strip out the weird ones.
    # Let's filter them
    base_text = None
    md_text = None
    lg_text = None
    
    new_classes = []
    
    for c in classes:
        if c.startswith('text-') and not c.startswith('text-kidora') and not c.startswith('text-gray') and not c.startswith('text-white') and not c.startswith('text-pink') and not c.startswith('text-blue') and not c.startswith('text-center') and not c.startswith('text-left') and not c.startswith('text-right'):
            base_text = c
        elif c.startswith('md:text-') and not c.startswith('md:text-center') and not c.startswith('md:text-left'):
            md_text = c
        elif c.startswith('lg:text-') and not c.startswith('lg:text-center') and not c.startswith('lg:text-left'):
            lg_text = c
        else:
            new_classes.append(c)
            
    if base_text: new_classes.append(base_text)
    if md_text: new_classes.append(md_text)
    if lg_text: new_classes.append(lg_text)
    
    return 'class="' + ' '.join(new_classes) + '"'

content = re.sub(r'class="([^"]*)"', cleanup_class, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Do the same for other html files
import glob
for filepath in glob.glob('*.html'):
    if filepath == 'index.html': continue
    with open(filepath, 'r', encoding='utf-8') as f:
        file_content = f.read()
    file_content = re.sub(r'class="([^"]*)"', cleanup_class, file_content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_content)

