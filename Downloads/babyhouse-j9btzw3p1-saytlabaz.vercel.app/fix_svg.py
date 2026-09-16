import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_svg_block = """                    Övladınızın <span class="text-kidora-pink relative">
                        uğurlu gələcəyi
                        <svg class="absolute w-full h-4 -bottom-1 left-0 text-kidora-yellow opacity-70" viewBox="0 0 100 10" preserveAspectRatio="none"><path d="M0 5 Q 50 10 100 5" stroke="currentColor" stroke-width="8" fill="none"/></svg>
                    </span><br>buradan başlayır"""

new_svg_block = """                    Övladınızın <span class="text-kidora-pink">uğurlu gələcəyi</span><br>buradan başlayır"""

content = content.replace(old_svg_block, new_svg_block)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
