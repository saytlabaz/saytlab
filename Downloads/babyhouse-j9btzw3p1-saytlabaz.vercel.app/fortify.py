import re
import glob

def fortify_html(content):
    # Add preconnects and theme-color to head
    head_additions = """
    <meta name="theme-color" content="#F8FAFC">
    <link rel="preconnect" href="https://images.unsplash.com">
    <link rel="dns-prefetch" href="https://images.unsplash.com">
    """
    if '<meta name="theme-color"' not in content:
        content = content.replace('<title>', head_additions + '<title>')
        
    # Make all images lazy loaded EXCEPT the first one (hero image)
    # The first image already has loading="eager" from the previous script
    # Let's add lazy to others
    img_pattern = re.compile(r'<img\s+([^>]*?)>')
    def lazy_img(match):
        m = match.group(0)
        if 'loading="eager"' in m:
            return m
        if 'loading="lazy"' not in m:
            if m.endswith('/>'):
                return m[:-2] + ' loading="lazy" decoding="async" />'
            else:
                return m[:-1] + ' loading="lazy" decoding="async">'
        return m
    
    content = img_pattern.sub(lazy_img, content)
    
    # Add global CSS reset for iOS Safari scroll bounce/flicker
    safari_fix = """
    <style>
        html, body {
            -webkit-overflow-scrolling: touch;
            overscroll-behavior-y: none;
        }
        img {
            -webkit-user-drag: none;
        }
    </style>
    """
    if 'overscroll-behavior-y' not in content:
        content = content.replace('</head>', safari_fix + '</head>')
        
    return content

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = fortify_html(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

