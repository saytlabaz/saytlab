import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the UK flag decorative block
uk_flag_block = """                    <div class="absolute top-8 -right-4 bg-white px-4 py-3 rounded-2xl shadow-xl transform rotate-6 animate-float flex items-center gap-3">
                        <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center text-xl overflow-hidden">
                            🇬🇧
                        </div>
                        <div class="flex flex-col text-left">
                            <span class="font-bold text-sm leading-tight text-gray-800">İngilis</span>
                            <span class="font-bold text-sm leading-tight text-gray-800">Dilli Bölmə</span>
                        </div>
                    </div>"""
content = content.replace(uk_flag_block, "")

# Change "Məktəbdə Əla Nəticələr" box in hero section
old_a_plus_box = """                    <div class="absolute bottom-8 left-6 bg-white px-4 py-3 rounded-2xl shadow-xl transform -rotate-6 animate-float flex items-center gap-3" style="animation-delay: 1s;">
                        <div class="w-10 h-10 bg-kidora-yellow rounded-full flex items-center justify-center text-white text-xl font-bold">
                            A+
                        </div>
                        <div class="flex flex-col text-left">
                            <span class="font-bold text-sm leading-tight text-gray-800">Məktəbdə</span>
                            <span class="font-bold text-sm leading-tight text-kidora-green">Əla Nəticələr</span>
                        </div>
                    </div>"""
new_a_plus_box = """                    <div class="absolute bottom-8 left-6 bg-white px-4 py-3 rounded-2xl shadow-xl transform -rotate-6 animate-float flex items-center gap-3" style="animation-delay: 1s;">
                        <div class="w-10 h-10 bg-kidora-yellow rounded-full flex items-center justify-center text-white text-xl font-bold">
                            👶🏻
                        </div>
                        <div class="flex flex-col text-left">
                            <span class="font-bold text-sm leading-tight text-gray-800">1-6 yaş</span>
                            <span class="font-bold text-sm leading-tight text-kidora-green">qəbulu davam edir</span>
                        </div>
                    </div>"""
content = content.replace(old_a_plus_box, new_a_plus_box)

# Remove the erroneous FAQ button from Hero section
erroneous_faq_btn = """            <div class="text-center mt-10" data-reveal="up">
                <a href="suallar.html" class="inline-flex items-center gap-2 bg-kidora-blue text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-blue-600 transition-all shadow-lg hover:-translate-y-1" data-cursor-hot>
                    Suallar bölməsinə keçid <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- About Section -->"""
fixed_hero_end = """        </div>
    </section>

    <!-- About Section -->"""
content = content.replace(erroneous_faq_btn, fixed_hero_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
