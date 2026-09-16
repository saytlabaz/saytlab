import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Gallery Update
old_gallery = """            <!-- Instagram Grid (Simulated Posts) -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <!-- Post 1 -->
                <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100 ig-card" data-reveal="up" style="transition-delay: 0ms;">
                    <img src="https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Instagram Post 1" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="ig-overlay absolute inset-0 bg-black/50 flex items-center justify-center gap-6 text-white font-bold text-lg">
                        <span class="flex items-center gap-2"><i class="fas fa-heart"></i> 124</span>
                        <span class="flex items-center gap-2"><i class="fas fa-comment"></i> 12</span>
                    </div>
                </a>
                <!-- Post 2 -->
                <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100 ig-card" data-reveal="up" style="transition-delay: 100ms;">
                    <img src="https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Instagram Post 2" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="ig-overlay absolute inset-0 bg-black/50 flex items-center justify-center gap-6 text-white font-bold text-lg">
                        <span class="flex items-center gap-2"><i class="fas fa-heart"></i> 98</span>
                        <span class="flex items-center gap-2"><i class="fas fa-comment"></i> 5</span>
                    </div>
                </a>
                <!-- Post 3 -->
                <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100 ig-card" data-reveal="up" style="transition-delay: 200ms;">
                    <img src="https://images.unsplash.com/photo-1544626053-8985dc34ae63?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Instagram Post 3" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="ig-overlay absolute inset-0 bg-black/50 flex items-center justify-center gap-6 text-white font-bold text-lg">
                        <span class="flex items-center gap-2"><i class="fas fa-heart"></i> 156</span>
                        <span class="flex items-center gap-2"><i class="fas fa-comment"></i> 24</span>
                    </div>
                </a>
                <!-- Post 4 -->
                <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100 ig-card" data-reveal="up" style="transition-delay: 300ms;">
                    <img src="https://images.unsplash.com/photo-1576495199011-eb94736d05d6?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Instagram Post 4" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="ig-overlay absolute inset-0 bg-black/50 flex items-center justify-center gap-6 text-white font-bold text-lg">
                        <span class="flex items-center gap-2"><i class="fas fa-heart"></i> 210</span>
                        <span class="flex items-center gap-2"><i class="fas fa-comment"></i> 18</span>
                    </div>
                </a>
            </div>
            <div class="mt-8 text-center md:hidden">
                <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="inline-flex items-center gap-2 bg-pink-50 text-pink-600 px-6 py-3 rounded-full font-bold hover:bg-pink-100 transition-colors border border-pink-100">
                    <i class="fab fa-instagram text-xl"></i> Daha çoxu Instagram-da
                </a>
            </div>"""

new_gallery = """            <!-- Photo Gallery Grid -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4" id="gallery-grid">
                <div class="cursor-pointer block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100 gallery-item" data-src="https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" data-reveal="up" style="transition-delay: 0ms;" data-cursor-hot>
                    <img src="https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Gallery Image 1" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 pointer-events-none">
                </div>
                <div class="cursor-pointer block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100 gallery-item" data-src="https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" data-reveal="up" style="transition-delay: 100ms;" data-cursor-hot>
                    <img src="https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Gallery Image 2" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 pointer-events-none">
                </div>
                <div class="cursor-pointer block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100 gallery-item" data-src="https://images.unsplash.com/photo-1544626053-8985dc34ae63?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" data-reveal="up" style="transition-delay: 200ms;" data-cursor-hot>
                    <img src="https://images.unsplash.com/photo-1544626053-8985dc34ae63?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Gallery Image 3" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 pointer-events-none">
                </div>
                <div class="cursor-pointer block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100 gallery-item" data-src="https://images.unsplash.com/photo-1576495199011-eb94736d05d6?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" data-reveal="up" style="transition-delay: 300ms;" data-cursor-hot>
                    <img src="https://images.unsplash.com/photo-1576495199011-eb94736d05d6?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Gallery Image 4" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 pointer-events-none">
                </div>
            </div>"""
content = content.replace(old_gallery, new_gallery)

# Add Lightbox modal at the end before </footer>
content = content.replace(
    '<!-- Footer -->',
    """<!-- Lightbox Modal -->
    <div id="lightbox" class="fixed inset-0 z-[100] bg-black/90 hidden flex items-center justify-center opacity-0 transition-opacity duration-300 backdrop-blur-sm">
        <button id="lightbox-close" class="absolute top-6 right-6 text-white text-5xl hover:text-kidora-pink transition-colors focus:outline-none" data-cursor-hot>&times;</button>
        <img id="lightbox-img" src="" alt="Böyüdülmüş şəkil" class="max-w-[90%] max-h-[90vh] object-contain rounded-xl shadow-2xl scale-95 transition-transform duration-300">
    </div>

    <!-- Footer -->"""
)

# 2. Add FAQs and view all button
old_faq_end = """                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
new_faq_end = """                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden" data-reveal="up" style="transition-delay: 300ms;">
                    <button class="faq-btn w-full px-6 py-5 text-left flex justify-between items-center font-bold text-xl text-kidora-dark focus:outline-none" data-cursor-hot>
                        <span>Uşaqların təhlükəsizliyi necə təmin edilir?</span>
                        <i class="fas fa-chevron-down text-kidora-green transition-transform duration-300"></i>
                    </button>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out">
                        <div class="px-6 pb-5 text-gray-600 font-medium">
                            Bağçamızda 24/7 rejimdə işləyən yüksək keyfiyyətli (Hikvision) kamera müşahidə sistemi mövcuddur. Hər zaman uşaqlar nəzarətdədir və kənar şəxslərin daxil olması qəti qadağandır.
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden" data-reveal="up" style="transition-delay: 400ms;">
                    <button class="faq-btn w-full px-6 py-5 text-left flex justify-between items-center font-bold text-xl text-kidora-dark focus:outline-none" data-cursor-hot>
                        <span>Xarici dillər tədris olunurmu?</span>
                        <i class="fas fa-chevron-down text-kidora-purple transition-transform duration-300"></i>
                    </button>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out">
                        <div class="px-6 pb-5 text-gray-600 font-medium">
                            Bəli, Azərbaycan bölməsi ilə yanaşı Rus və İngilis dilli qruplarımız fəaliyyət göstərir. Eyni zamanda digər bölmələrdə də mütəmadi olaraq xarici dil məşğələləri keçirilir.
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-10" data-reveal="up">
                <a href="suallar.html" class="inline-flex items-center gap-2 bg-kidora-blue text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-blue-600 transition-all shadow-lg hover:-translate-y-1" data-cursor-hot>
                    Daha çoxuna bax <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </div>
    </section>"""
content = content.replace(old_faq_end, new_faq_end)

# 3. Add text to Hero
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
content = content.replace(old_hero_text, new_hero_text)

# 4. Add text to Azerbaijan section
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
content = content.replace(old_az_section, new_az_section)

# 5. Add Qrant Qalibi to About
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
content = content.replace(old_about, new_about)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

