import re
import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove mix-blend-multiply and filter blur-3xl from the decorative blobs
    # These are massive performance killers on mobile Safari when repainting
    content = content.replace('mix-blend-multiply filter blur-3xl', 'opacity-50')
    content = content.replace('shadow-2xl', 'shadow-xl') # Slightly cheaper shadow
    
    # 2. Add loading="eager" to hero image to prevent decoding delays
    content = content.replace('alt="Xoşbəxt uşaqlar"', 'alt="Xoşbəxt uşaqlar" loading="eager" decoding="async"')
    
    # 3. Add explicit hardware acceleration to the hero image container
    content = content.replace('class="relative w-full aspect-square', 'class="relative w-full aspect-square transform-gpu"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

