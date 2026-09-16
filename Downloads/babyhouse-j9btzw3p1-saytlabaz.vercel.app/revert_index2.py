import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert Gallery
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
content = content.replace(new_gallery, old_gallery)

# Remove Lightbox Modal HTML
lightbox_modal = """<!-- Lightbox Modal -->
    <div id="lightbox" class="fixed inset-0 z-[100] bg-black/90 hidden flex items-center justify-center opacity-0 transition-opacity duration-300 backdrop-blur-sm">
        <button id="lightbox-close" class="absolute top-6 right-6 text-white text-5xl hover:text-kidora-pink transition-colors focus:outline-none" data-cursor-hot>&times;</button>
        <img id="lightbox-img" src="" alt="Böyüdülmüş şəkil" class="max-w-[90%] max-h-[90vh] object-contain rounded-xl shadow-2xl scale-95 transition-transform duration-300">
    </div>

    <!-- Footer -->"""
content = content.replace(lightbox_modal, '<!-- Footer -->')

# 2. Revert FAQ length
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
old_faq_end = """                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
content = content.replace(new_faq_end, old_faq_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
