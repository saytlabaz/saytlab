import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_az_section = """                    <h4 class="text-2xl font-display font-bold text-kidora-dark mb-4">Azərbaycan Bölməsi</h4>
                    <p class="text-gray-600 leading-relaxed">Ana dilində mükəmməl nitq inkişafı, məktəbəqədər hazırlıq və milli dəyərlərin öyrədilməsi əsasında qurulmuş proqram.</p>
                    <a href="qeydiyyat.html" class="inline-block mt-6 bg-kidora-pink text-white px-6 py-2 rounded-full font-bold shadow-md hover:bg-rose-500 transition-colors" data-cursor-hot>Qeydiyyat</a>"""

new_az_section = """                    <h4 class="text-2xl font-display font-bold text-kidora-dark mb-4">Azərbaycan Bölməsi</h4>
                    <p class="text-gray-600 leading-relaxed">Ana dilində mükəmməl nitq inkişafı, məktəbəqədər hazırlıq və milli dəyərlərin öyrədilməsi əsasında qurulmuş proqram.</p>
                    <div class="mt-5 p-4 bg-pink-50 rounded-xl border border-pink-100 text-left relative overflow-hidden">
                        <div class="absolute top-0 right-0 w-16 h-16 bg-pink-100 rounded-bl-full opacity-50"></div>
                        <p class="text-[13px] text-kidora-dark font-bold mb-2 relative z-10"><i class="fas fa-bullhorn text-kidora-pink mr-1"></i> Dövlət dəstəyi ilə qəbul davam edir!</p>
                        <p class="text-[14px] text-kidora-pink font-extrabold mb-1 leading-tight relative z-10">Aylıq ödəniş <del class="text-gray-400">500 AZN</del> əvəzinə cəmi 150 AZN!</p>
                        <p class="text-xs text-gray-600 font-medium relative z-10">2026–2027-ci tədris ili üçün myGov üzərindən müraciət edə bilərsiniz.</p>
                    </div>
                    <a href="qeydiyyat.html" class="inline-block mt-6 bg-kidora-pink text-white px-6 py-2 rounded-full font-bold shadow-md hover:bg-rose-500 transition-colors" data-cursor-hot>Qeydiyyat</a>"""

content = content.replace(old_az_section, new_az_section)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
