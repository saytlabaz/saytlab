import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert Hero Text
old_hero_text = """                <p class="text-xl md:text-2xl text-gray-600 mb-10 max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed">
                    3 dildə (Azərbaycan, Rus, İngilis) mükəmməl tədris, illərin qüsursuz təcrübəsi və güvənli mühit. Bizimlə böyüyən uşaqlar məktəbdə həmişə seçilir!
                </p>"""
new_hero_text = """                <p class="text-xl md:text-2xl text-gray-600 mb-6 max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed">
                    3 dildə (Azərbaycan, Rus, İngilis) mükəmməl tədris, illərin qüsursuz təcrübəsi və güvənli mühit. Bizimlə böyüyən uşaqlar məktəbdə həmişə seçilir!
                </p>
                <div class="bg-white/60 backdrop-blur-md rounded-2xl p-5 mb-8 border border-white shadow-sm inline-block text-left relative z-10" data-reveal="up">
                    <p class="text-kidora-dark font-bold text-base md:text-lg leading-snug">
                        Balacalar üçün təhlükəsiz və qayğı dolu mühit.<br>
                        Gündəlik inkişaf və nəzarət sistemi.<br>
                        <span class="text-kidora-pink">AZ</span> | <span class="text-kidora-blue">RU</span> | <span class="text-kidora-green">ENG</span> bölmələri.<br>
                        <span class="text-kidora-purple">1-6 yaş qəbulu davam edir!</span>
                    </p>
                </div>"""
content = content.replace(new_hero_text, old_hero_text)

# 2. Revert Az section
old_az_section = """                    <h4 class="text-2xl font-display font-bold text-kidora-dark mb-4">Azərbaycan Bölməsi</h4>
                    <p class="text-gray-600 leading-relaxed">Ana dilində mükəmməl nitq inkişafı, məktəbəqədər hazırlıq və milli dəyərlərin öyrədilməsi əsasında qurulmuş proqram.</p>
                    <a href="qeydiyyat.html" class="inline-block mt-6 bg-kidora-pink text-white px-6 py-2 rounded-full font-bold shadow-md hover:bg-rose-500 transition-colors" data-cursor-hot>Qeydiyyat</a>"""
new_az_section = """                    <h4 class="text-2xl font-display font-bold text-kidora-dark mb-4">Azərbaycan Bölməsi</h4>
                    <p class="text-gray-600 leading-relaxed">Ana dilində mükəmməl nitq inkişafı, məktəbəqədər hazırlıq və milli dəyərlərin öyrədilməsi əsasında qurulmuş proqram.</p>
                    <div class="mt-5 p-4 bg-pink-50 rounded-xl border border-pink-100 text-left">
                        <p class="text-sm text-gray-800 font-bold mb-2">2026–2027-ci tədris ili üçün uşaqların dövlət dəstəyi ilə bağçaya qəbulu davam edir.</p>
                        <p class="text-[15px] text-kidora-pink font-extrabold mb-2 leading-tight">Bağçanın aylıq ödənişi <del class="text-gray-400">500 AZN</del> olduğu halda, dövlət dəstəyi ilə valideynin ödədiyi məbləğ cəmi 150 AZN təşkil edir!</p>
                        <p class="text-xs text-gray-600 font-medium">Övladınızın sevgi, qayğı və diqqətlə əhatə olunduğu, eyni zamanda inkişafını dəstəkləyən zəngin mühitdə böyüməsi üçün doğru seçim edin.</p>
                    </div>
                    <a href="qeydiyyat.html" class="inline-block mt-6 bg-kidora-pink text-white px-6 py-2 rounded-full font-bold shadow-md hover:bg-rose-500 transition-colors" data-cursor-hot>Qeydiyyat</a>"""
content = content.replace(new_az_section, old_az_section)

# 3. Revert About Section
old_about = """                    <div class="grid grid-cols-2 gap-6">
                        <div class="flex items-center gap-4">
                            <div class="w-12 h-12 bg-green-100 text-kidora-green rounded-xl flex items-center justify-center text-xl">
                                <i class="fas fa-shield-alt"></i>
                            </div>
                            <span class="font-bold text-gray-800">100% Təhlükəsizlik</span>
                        </div>
                        <div class="flex items-center gap-4">
                            <div class="w-12 h-12 bg-blue-100 text-kidora-blue rounded-xl flex items-center justify-center text-xl">
                                <i class="fas fa-graduation-cap"></i>
                            </div>
                            <span class="font-bold text-gray-800">Mükəmməl Nəticələr</span>
                        </div>
                    </div>"""
new_about = """                    <div class="grid grid-cols-2 gap-6">
                        <div class="flex items-center gap-4">
                            <div class="w-12 h-12 bg-green-100 text-kidora-green rounded-xl flex items-center justify-center text-xl shrink-0">
                                <i class="fas fa-shield-alt"></i>
                            </div>
                            <span class="font-bold text-gray-800 text-sm md:text-base leading-tight">100% Təhlükəsizlik</span>
                        </div>
                        <div class="flex items-center gap-4">
                            <div class="w-12 h-12 bg-yellow-100 text-kidora-yellow rounded-xl flex items-center justify-center text-xl shrink-0">
                                <i class="fas fa-trophy"></i>
                            </div>
                            <span class="font-bold text-gray-800 text-sm md:text-base leading-tight">Qrant Müsabiqə Qalibi</span>
                        </div>
                    </div>
                    <div class="mt-6 inline-flex items-center gap-3 bg-blue-50 px-5 py-3 rounded-xl border border-blue-100 shadow-sm">
                        <i class="fas fa-file-contract text-kidora-blue text-xl"></i>
                        <span class="text-sm text-gray-700 font-bold">Qeydiyyat zamanı rəsmi lisenziya adı:<br><span class="text-kidora-blue text-lg">Beybi Hauz</span></span>
                    </div>"""
content = content.replace(new_about, old_about)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
