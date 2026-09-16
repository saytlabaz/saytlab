import re
import glob

def fix_html(content, is_index):
    # Fix Instagram button
    old_ig = """                    <!-- Social (Below Contact) -->
                    <div class="mt-8 flex justify-start">
                        <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-pink-600 transition-colors shadow-lg text-lg" data-cursor-hot title="Instagram">
                            <i class="fab fa-instagram"></i>
                        </a>
                    </div>"""
    
    new_ig = """                    <!-- Social (Below Contact) -->
                    <div class="mt-8 flex justify-start" data-aos="blur-in">
                        <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="flex items-center gap-3 bg-white/10 px-5 py-2 rounded-full hover:bg-pink-600 transition-colors shadow-lg text-lg group text-white" data-cursor-hot title="Instagram">
                            <i class="fab fa-instagram group-hover:scale-110 transition-transform text-xl"></i>
                            <span class="font-bold text-sm tracking-wide">Bizi İzləyin</span>
                        </a>
                    </div>"""
    content = content.replace(old_ig, new_ig)

    # Global CSS fix for horizontal scroll
    # We already have a style block added by fortify.py:
    # <style>
    #     html, body {
    #         -webkit-overflow-scrolling: touch;
    #         overscroll-behavior-y: none;
    #     }
    old_style = """    <style>
        html, body {
            -webkit-overflow-scrolling: touch;
            overscroll-behavior-y: none;
        }"""
    
    new_style = """    <style>
        html, body {
            -webkit-overflow-scrolling: touch;
            overscroll-behavior-y: none;
            overflow-x: hidden !important;
            width: 100%;
            max-width: 100vw;
            position: relative;
        }"""
        
    content = content.replace(old_style, new_style)
    
    # Just in case fortify.py's style isn't caught, inject a global guarantee
    if 'overflow-x: hidden !important;' not in content:
        guarantee = """<style>html, body { overflow-x: hidden !important; width: 100%; max-width: 100vw; position: relative; }</style></head>"""
        content = content.replace('</head>', guarantee)

    return content

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = fix_html(content, filepath == 'index.html')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

