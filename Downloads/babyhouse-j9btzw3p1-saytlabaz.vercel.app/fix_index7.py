import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

erroneous_faq_btn = """            <div class="text-center mt-10" data-reveal="up">
                <a href="suallar.html" class="inline-flex items-center gap-2 bg-kidora-blue text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-blue-600 transition-all shadow-lg hover:-translate-y-1" data-cursor-hot>
                    Suallar bölməsinə keçid <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </div>
    </section>

    

    <!-- About Section / Tarixçə -->"""

fixed_hero_end = """        </div>
    </section>

    <!-- About Section / Tarixçə -->"""

content = content.replace(erroneous_faq_btn, fixed_hero_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
