import re
import glob

def fix_footer(html):
    # 1. Remove animation from the wrapper
    old_wrapper = '<div class="max-w-7xl mx-auto" data-aos="fade-up">'
    new_wrapper = '<div class="max-w-7xl mx-auto">'
    html = html.replace(old_wrapper, new_wrapper)
    
    # 2. Change fade-up to blur-in inside footer
    # But only inside the footer!
    footer_start = html.find('<footer')
    if footer_start != -1:
        footer_end = html.find('</footer>', footer_start)
        footer_content = html[footer_start:footer_end]
        footer_content = footer_content.replace('data-aos="fade-up"', 'data-aos="blur-in"')
        
        # 3. Remove blur-in from copyright text
        old_copy = '<p data-aos="blur-in">&copy; 2026 BabyHouse. Bütün hüquqlar qorunur.</p>'
        new_copy = '<p>&copy; 2026 BabyHouse. Bütün hüquqlar qorunur.</p>'
        footer_content = footer_content.replace(old_copy, new_copy)
        
        old_lis = '<p data-aos="blur-in" class="mt-2 md:mt-0">Lisenziyalı təhsil müəssisəsi (2011)</p>'
        new_lis = '<p class="mt-2 md:mt-0">Lisenziyalı təhsil müəssisəsi (2011)</p>'
        footer_content = footer_content.replace(old_lis, new_lis)
        
        html = html[:footer_start] + footer_content + html[footer_end:]
        
    # 4. Add custom AOS blur animation CSS to head
    custom_css = """
    <style>
        [data-aos="blur-in"] {
            opacity: 0;
            filter: blur(10px);
            transform: translateY(20px);
            transition-property: transform, opacity, filter;
            will-change: transform, opacity, filter;
        }
        [data-aos="blur-in"].aos-animate {
            opacity: 1;
            filter: blur(0);
            transform: translateY(0);
        }
    </style>
    """
    if '[data-aos="blur-in"]' not in html:
        html = html.replace('</head>', custom_css + '</head>')
        
    return html

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = fix_footer(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
