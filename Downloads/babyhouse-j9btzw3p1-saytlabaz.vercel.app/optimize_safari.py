import re
import glob

def fix_css(content):
    old_css_reveal = """        .js-reveal [data-reveal] {
            opacity: 0;
            transform: translateY(40px);
            transition: opacity 0.8s cubic-bezier(0.22, 1, 0.36, 1), 
                        transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
            will-change: opacity, transform;
        }"""
    # Using 3D transforms forces the GPU to render the element, avoiding layout trashing
    new_css_reveal = """        .js-reveal [data-reveal] {
            opacity: 0;
            transform: translate3d(0, 40px, 0);
            transition: opacity 0.7s cubic-bezier(0.215, 0.610, 0.355, 1.000), 
                        transform 0.7s cubic-bezier(0.215, 0.610, 0.355, 1.000);
            will-change: opacity, transform;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            -webkit-transform-style: preserve-3d;
            transform-style: preserve-3d;
        }"""
    content = content.replace(old_css_reveal, new_css_reveal)
    
    old_css_revealed = """        .js-reveal [data-reveal].is-revealed {
            opacity: 1;
            transform: translate(0) scale(1);
        }"""
    new_css_revealed = """        .js-reveal [data-reveal].is-revealed {
            opacity: 1;
            transform: translate3d(0, 0, 0) scale(1);
        }"""
    content = content.replace(old_css_revealed, new_css_revealed)
    
    # Also adjust left/right animations to 3D
    content = content.replace('transform: translateX(-50px);', 'transform: translate3d(-50px, 0, 0);')
    content = content.replace('transform: translateX(50px);', 'transform: translate3d(50px, 0, 0);')
    content = content.replace('transform: scale(0.9) translateY(20px);', 'transform: translate3d(0, 20px, 0) scale3d(0.95, 0.95, 1);')
    
    return content

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = fix_css(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
