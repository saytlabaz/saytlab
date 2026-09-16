import re
import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add mix-blend-multiply to any BabyHouse.png to remove white background
    content = content.replace('src="BabyHouse.png" alt="BabyHouse Logo" class="h-10 md:h-12 w-auto object-contain"', 'src="BabyHouse.png" alt="BabyHouse Logo" class="h-10 md:h-12 w-auto object-contain mix-blend-multiply"')
    content = content.replace('src="BabyHouse.png" alt="BabyHouse" class="w-16 h-16 object-contain"', 'src="BabyHouse.png" alt="BabyHouse" class="w-16 h-16 object-contain mix-blend-multiply"')

    # Also maybe they mean the navbar container background? 
    # Usually "logonun arxa planin sil" means the logo's white box. I'll stick to that.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
