import re
import glob

# Tags we want to add AOS to if they don't have it
tags_to_animate = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'li', 'img']

def add_aos(html):
    # First, replace old data-reveal with AOS
    html = html.replace('data-reveal="up"', 'data-aos="fade-up"')
    html = html.replace('data-reveal="left"', 'data-aos="fade-right"')
    html = html.replace('data-reveal="right"', 'data-aos="fade-left"')
    html = html.replace('data-reveal="zoom"', 'data-aos="zoom-in"')
    html = html.replace('data-reveal-delay', 'data-aos-delay')
    
    # Also we want to target almost every text element
    # A naive regex replace to add data-aos="fade-up" to tags
    for tag in tags_to_animate:
        # e.g. <p class="..." -> <p data-aos="fade-up" class="..."
        # only if it doesn't already have data-aos
        pattern = re.compile(rf'<{tag}(\s+[^>]*)?>', re.IGNORECASE)
        
        def replacer(match):
            m = match.group(0)
            if 'data-aos' in m or 'data-src' in m or 'ig-card' in m or 'gallery-item' in m:
                return m
            # Avoid animating internal svg/icons inside buttons or small spans if we are doing tags, but p/h1..h5 is fine
            if tag == 'img' and 'BabyHouse' in m: # skip logo
                return m
            
            # insert data-aos="fade-up"
            if m.startswith(f'<{tag} '):
                return f'<{tag} data-aos="fade-up" ' + m[len(tag)+2:]
            elif m == f'<{tag}>':
                return f'<{tag} data-aos="fade-up">'
            return m
            
        html = pattern.sub(replacer, html)
        
    return html

def minify_mobile(html):
    # Global reductions for mobile
    # text-sm -> text-xs
    # text-base -> text-sm
    # text-lg -> text-base
    # text-xl -> text-lg
    # text-2xl -> text-xl
    # text-3xl -> text-2xl
    # text-4xl -> text-3xl
    # p-6 -> p-4
    # py-16 -> py-10
    # py-24 -> py-16
    
    html = html.replace('text-6xl', 'text-4xl md:text-6xl')
    html = html.replace('text-5xl', 'text-3xl md:text-5xl')
    html = html.replace('text-4xl', 'text-2xl md:text-4xl')
    html = html.replace('text-3xl', 'text-xl md:text-3xl')
    html = html.replace('text-2xl', 'text-lg md:text-2xl')
    
    # Paddings/Gaps
    html = html.replace('py-16 md:py-24', 'py-10 md:py-24')
    html = html.replace('p-8', 'p-5 md:p-8')
    html = html.replace('p-6', 'p-4 md:p-6')
    html = html.replace('gap-12', 'gap-6 md:gap-12')
    html = html.replace('gap-8', 'gap-4 md:gap-8')
    html = html.replace('gap-6', 'gap-3 md:gap-6')
    html = html.replace('mb-16', 'mb-8 md:mb-16')
    html = html.replace('mb-10', 'mb-5 md:mb-10')
    html = html.replace('mb-8', 'mb-4 md:mb-8')
    html = html.replace('mt-16', 'mt-8 md:mt-16')
    
    # Header specific
    html = html.replace('h-16 md:h-20', 'h-14 md:h-20')
    html = html.replace('w-10 h-10 md:w-14 md:h-14', 'w-8 h-8 md:w-14 md:h-14')
    html = html.replace('py-3 md:py-4 px-4 md:px-12', 'py-2 md:py-4 px-3 md:px-12')
    
    return html

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Inject AOS CSS/JS
    if '<link href="https://unpkg.com/aos@2.3.1/dist/aos.css"' not in content:
        content = content.replace('</head>', '    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>')
        
    if '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>' not in content:
        content = content.replace('</body>', '    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n    <script>AOS.init({ once: false, duration: 800, offset: 50, easing: \'ease-out-cubic\' });</script>\n</body>')
        
    content = add_aos(content)
    content = minify_mobile(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
