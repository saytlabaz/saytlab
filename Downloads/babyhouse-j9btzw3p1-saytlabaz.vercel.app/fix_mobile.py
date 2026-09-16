import re
import glob

def fix_css(content):
    # 1. Fix Safari stutter by removing blur filter
    old_css_reveal = """        .js-reveal [data-reveal] {
            opacity: 0;
            filter: blur(12px);
            transform: translateY(50px);
            transition: opacity 1s cubic-bezier(0.22, 1, 0.36, 1), 
                        transform 1s cubic-bezier(0.22, 1, 0.36, 1),
                        filter 1s cubic-bezier(0.22, 1, 0.36, 1);
            will-change: opacity, transform, filter;
        }"""
    new_css_reveal = """        .js-reveal [data-reveal] {
            opacity: 0;
            transform: translateY(40px);
            transition: opacity 0.8s cubic-bezier(0.22, 1, 0.36, 1), 
                        transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
            will-change: opacity, transform;
        }"""
    content = content.replace(old_css_reveal, new_css_reveal)
    
    old_css_revealed = """        .js-reveal [data-reveal].is-revealed {
            opacity: 1;
            filter: blur(0);
            transform: translate(0) scale(1);
        }"""
    new_css_revealed = """        .js-reveal [data-reveal].is-revealed {
            opacity: 1;
            transform: translate(0) scale(1);
        }"""
    content = content.replace(old_css_revealed, new_css_revealed)
    
    # 2. Fix Mobile menu animation
    old_mobile_menu_css = """        #mobileMenu {
            display: none;
            opacity: 0;
            transform: translateY(-10px);
            transition: opacity 0.4s ease, transform 0.4s ease;
        }
        #mobileMenu.is-open {
            display: flex;
            opacity: 1;
            transform: translateY(0);
        }"""
    new_mobile_menu_css = """        #mobileMenu {
            visibility: hidden;
            opacity: 0;
            transform: translateY(-20px) scale(0.95);
            transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.3s;
            pointer-events: none;
            display: flex; /* keep it flex so children layout correctly before appearing */
        }
        #mobileMenu.is-open {
            visibility: visible;
            opacity: 1;
            transform: translateY(0) scale(1);
            pointer-events: auto;
        }"""
    content = content.replace(old_mobile_menu_css, new_mobile_menu_css)
    
    # Also fix it for other pages that had the injected CSS (though they don't have mobileMenu)
    return content

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = fix_css(content)
    
    # 3. Typography and Spacing Tweaks on Mobile
    if filepath == 'index.html':
        # Hero text size
        content = content.replace('text-6xl lg:text-[5.5rem]', 'text-4xl md:text-5xl lg:text-[5rem]')
        content = content.replace('text-4xl md:text-5xl lg:text-6xl', 'text-3xl md:text-4xl lg:text-5xl')
        content = content.replace('text-3xl font-display font-bold', 'text-2xl md:text-3xl font-display font-bold')
        content = content.replace('text-5xl font-display font-bold', 'text-3xl md:text-5xl font-display font-bold')
        content = content.replace('text-4xl md:text-5xl font-display font-bold', 'text-3xl md:text-4xl lg:text-5xl font-display font-bold')
        
        # Padding tweaks
        content = content.replace('pt-36 pb-20 md:pt-48 md:pb-32', 'pt-28 pb-16 md:pt-40 md:pb-28')
        content = content.replace('py-24 px-6', 'py-16 md:py-24 px-5 md:px-6')
        
        # Menu text size
        content = content.replace('text-2xl tracking-tight text-kidora-dark', 'text-xl md:text-2xl tracking-tight text-kidora-dark')
        content = content.replace('h-12 w-auto', 'h-10 md:h-12 w-auto')
        content = content.replace('py-4 px-6 md:px-12', 'py-3 md:py-4 px-4 md:px-12')
        content = content.replace('text-lg z-50', 'text-base z-50')
        
    else:
        # Inner pages header sizes
        content = content.replace('h-24 flex items-center justify-between', 'h-16 md:h-20 flex items-center justify-between')
        content = content.replace('w-14 h-14', 'w-10 h-10 md:w-14 md:h-14')
        content = content.replace('text-3xl tracking-tight', 'text-xl md:text-2xl tracking-tight')
        content = content.replace('font-bold text-kidora-dark hover:text-kidora-blue', 'text-sm md:text-base font-bold text-kidora-dark hover:text-kidora-blue')
        content = content.replace('pt-32 pb-24 px-6', 'pt-24 pb-16 px-5 md:px-6')
        content = content.replace('text-5xl md:text-6xl font-display font-bold', 'text-3xl md:text-5xl font-display font-bold')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
