import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_box = """                    <div class="absolute -bottom-10 -left-10 bg-kidora-yellow text-kidora-dark p-5 md:p-8 rounded-3xl shadow-xl w-64 rotate-3">
                        <h4 data-aos="fade-up" class="font-display font-bold mb-2 text-xl md:text-5xl"><span data-count-to="15">0</span>+</h4>
                        <p data-aos="fade-up" class="font-bold leading-tight text-lg">İllik qüsursuz təcrübə və fəaliyyət</p>
                    </div>"""

new_box = """                    <div class="absolute -bottom-6 left-4 md:-bottom-10 md:-left-10 bg-kidora-yellow text-kidora-dark p-4 md:p-8 rounded-2xl md:rounded-3xl shadow-xl w-48 md:w-64 rotate-3 z-20">
                        <h4 data-aos="fade-up" class="font-display font-bold mb-1 md:mb-2 text-3xl md:text-5xl"><span data-count-to="15">0</span>+</h4>
                        <p data-aos="fade-up" class="font-bold leading-tight text-xs md:text-lg">İllik qüsursuz təcrübə və fəaliyyət</p>
                    </div>"""

content = content.replace(old_box, new_box)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

