import re
import glob

def fix_aos(html):
    # We want to change 'fade-up', 'fade-right', 'fade-left' to 'blur-in' 
    # for most text-based elements, or maybe just globally.
    html = html.replace('data-aos="fade-up"', 'data-aos="blur-in"')
    html = html.replace('data-aos="fade-right"', 'data-aos="blur-in"')
    html = html.replace('data-aos="fade-left"', 'data-aos="blur-in"')
    html = html.replace('data-aos="zoom-in"', 'data-aos="blur-in"')
    
    # Also adjust AOS initialization to ensure smooth triggering
    # Increase offset slightly so it triggers a bit later, making the animation more visible
    old_aos_init = "AOS.init({ once: false, duration: 800, offset: 50, easing: 'ease-out-cubic' });"
    new_aos_init = "AOS.init({ once: false, duration: 1000, offset: 120, easing: 'ease-out-cubic', mirror: true });"
    html = html.replace(old_aos_init, new_aos_init)
    
    return html

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = fix_aos(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

