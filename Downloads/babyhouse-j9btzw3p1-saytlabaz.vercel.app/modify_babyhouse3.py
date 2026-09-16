import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Header WhatsApp Button
content = content.replace(
    '<a href="#elaqe" class="bg-kidora-dark text-white px-7 py-3 data-magnetic rounded-full font-bold hover:bg-gray-800 transition-all transform hover:scale-105 tilt-card shadow-md text-sm uppercase tracking-wide">\n                    Bizimlə Əlaqə\n                </a>',
    '<a href="https://wa.me/994553776710?text=Salam,%20ba%C4%9F%C3%A7a%20il%C9%99%20ba%C4%9Fl%C4%B1%20m%C9%99lumat%20almaq%20ist%C9%99yirdim." target="_blank" class="bg-kidora-dark text-white px-7 py-3 data-magnetic rounded-full font-bold hover:bg-gray-800 transition-all transform hover:scale-105 tilt-card shadow-md text-sm uppercase tracking-wide">\n                    Bizimlə Əlaqə\n                </a>'
)

# 2. Call to Action Banner -> FAQ Section
cta_banner = """    <!-- Call to Action Banner -->
    <section class="py-24 px-6 bg-kidora-blue text-white text-center relative overflow-hidden">
        <div class="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]"></div>
        <div class="max-w-4xl mx-auto relative z-10" data-reveal="zoom">
            <h2 class="text-4xl md:text-6xl font-display font-bold mb-6">Övladınızın gələcəyinə indi sərmayə edin</h2>
            <p class="text-xl md:text-2xl mb-10 text-blue-100 max-w-2xl mx-auto font-medium">
                Səhifəmizi izləyərək və ya birbaşa bizimlə əlaqə saxlayaraq qeydiyyat şərtləri ilə tanış ola bilərsiniz.
            </p>
            <a href="#elaqe" class="inline-flex items-center gap-3 bg-white text-kidora-blue px-10 py-5 rounded-full font-bold text-xl hover:bg-gray-100 transition-all transform hover:scale-105 tilt-card shadow-xl">
                Bizimlə Əlaqə <i class="fas fa-comment-dots"></i>
            </a>
        </div>
    </section>"""

faq_section = """    <!-- FAQ Section (Suallar) -->
    <section id="suallar" class="py-24 px-6 bg-kidora-bg relative overflow-hidden">
        <div class="max-w-4xl mx-auto relative z-10">
            <div class="text-center mb-16" data-reveal="up">
                <h2 class="text-kidora-blue font-bold tracking-widest uppercase mb-3 text-sm md:text-base">Tez-tez Verilən Suallar</h2>
                <h3 class="text-4xl md:text-5xl font-display font-bold text-kidora-dark">Bizi Daha Yaxından Tanıyın</h3>
            </div>
            
            <div class="space-y-4">
                <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden" data-reveal="up">
                    <button class="faq-btn w-full px-6 py-5 text-left flex justify-between items-center font-bold text-xl text-kidora-dark focus:outline-none" data-cursor-hot>
                        <span>Bağçanızın iş saatları necədir?</span>
                        <i class="fas fa-chevron-down text-kidora-blue transition-transform duration-300"></i>
                    </button>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out">
                        <div class="px-6 pb-5 text-gray-600 font-medium">
                            Bağçamız həftə içi 5 gün, səhər saat 08:00-dan axşam 18:30-dək fəaliyyət göstərir. İstirahət və bayram günləri qeyri-iş günləridir.
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden" data-reveal="up" style="transition-delay: 100ms;">
                    <button class="faq-btn w-full px-6 py-5 text-left flex justify-between items-center font-bold text-xl text-kidora-dark focus:outline-none" data-cursor-hot>
                        <span>Qidalanma necə təşkil olunur?</span>
                        <i class="fas fa-chevron-down text-kidora-pink transition-transform duration-300"></i>
                    </button>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out">
                        <div class="px-6 pb-5 text-gray-600 font-medium">
                            Uşaqlar gündə 4 dəfə (səhər, nahar, ikindi, axşam) təbii və sağlam məhsullardan ibarət xüsusi pediatr təsdiqli menyu ilə qidalanırlar.
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden" data-reveal="up" style="transition-delay: 200ms;">
                    <button class="faq-btn w-full px-6 py-5 text-left flex justify-between items-center font-bold text-xl text-kidora-dark focus:outline-none" data-cursor-hot>
                        <span>Hansı dərnəklər fəaliyyət göstərir?</span>
                        <i class="fas fa-chevron-down text-kidora-yellow transition-transform duration-300"></i>
                    </button>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out">
                        <div class="px-6 pb-5 text-gray-600 font-medium">
                            Şahmat, rəsm, bədii gimnastika və məntiq dərnəklərimiz var. Hər biri peşəkar müəllimlər tərəfindən uşaqların fiziki və zehni inkişafı nəzərə alınaraq tədris olunur.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
content = content.replace(cta_banner, faq_section)

# 3. Footer Modifications
# Change <div class="max-w-7xl mx-auto" data-reveal="up"> to <div class="w-full px-4 md:px-12 mx-auto" data-reveal="up">
content = content.replace('<div class="max-w-7xl mx-auto" data-reveal="up">', '<div class="w-full px-4 md:px-12 mx-auto" data-reveal="up">')

# Extract and replace the whole wrapper for Contact & Social
old_contact_social = """<div class="flex flex-col md:flex-row gap-12 lg:gap-24 md:ml-auto">
                <!-- Contact -->
                <div>
                    <h5 class="font-bold text-xl mb-6 text-kidora-green font-display">Əlaqə</h5>
                    <ul class="space-y-4 text-gray-300 font-bold">
                        <li class="flex items-start gap-3">
                            <i class="fas fa-map-marker-alt text-kidora-green mt-1 text-lg"></i>
                            <span>Cəfər Xəndan küçəsi 2D Baku, Azerbaijan</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fas fa-phone-alt text-kidora-green mt-1 text-lg"></i>
                            <span>+994553776710</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fas fa-envelope text-kidora-green mt-1 text-lg"></i>
                            <span>seferova.ziyafet@mail.ru</span>
                        </li>
                    </ul>
                </div>
                
                <!-- Social -->
                <div>
                    <h5 class="font-bold text-xl mb-6 text-kidora-pink font-display">Sosial Şəbəkələr</h5>
                    <div class="flex gap-4">
                        <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center hover:bg-pink-600 transition-colors text-xl shadow-lg">
                            <i class="fab fa-instagram"></i>
                        </a>
                        
                    </div>
                    <p class="text-gray-400 text-sm mt-6 font-medium">Ən son yeniliklər üçün bizi instagramdan izləməyi unutmayın.</p>
                </div>
                </div>"""

new_contact_social = """<div class="flex flex-col text-left md:text-right mt-12 md:mt-0">
                    <!-- Contact -->
                    <div>
                        <h5 class="font-bold text-xl mb-6 text-kidora-green font-display md:text-right">Əlaqə</h5>
                        <ul class="space-y-4 text-gray-300 font-bold flex flex-col items-start md:items-end">
                            <li>
                                <a href="https://maps.app.goo.gl/sPDzZaFzyFPeUnvX7?g_st=ic" target="_blank" class="flex items-center gap-3 hover:text-white group" data-cursor-hot>
                                    <span class="order-2 md:order-1">Cəfər Xəndan küçəsi 2D Baku, Azerbaijan</span>
                                    <i class="fas fa-map-marker-alt text-kidora-green text-lg order-1 md:order-2 group-hover:scale-110 transition-transform"></i>
                                </a>
                            </li>
                            <li>
                                <a href="https://wa.me/994553776710" target="_blank" class="flex items-center gap-3 hover:text-white group" data-cursor-hot>
                                    <span class="order-2 md:order-1">+994553776710</span>
                                    <i class="fas fa-phone-alt text-kidora-green text-lg order-1 md:order-2 group-hover:scale-110 transition-transform"></i>
                                </a>
                            </li>
                            <li>
                                <a href="mailto:seferova.ziyafet@mail.ru" class="flex items-center gap-3 hover:text-white group" data-cursor-hot>
                                    <span class="order-2 md:order-1">seferova.ziyafet@mail.ru</span>
                                    <i class="fas fa-envelope text-kidora-green text-lg order-1 md:order-2 group-hover:scale-110 transition-transform"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                    
                    <!-- Social (Below Contact) -->
                    <div class="mt-8 flex justify-start md:justify-end">
                        <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-pink-600 transition-colors text-lg shadow-lg" data-cursor-hot title="Instagram">
                            <i class="fab fa-instagram"></i>
                        </a>
                    </div>
                </div>"""
content = content.replace(old_contact_social, new_contact_social)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

