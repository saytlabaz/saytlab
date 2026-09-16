import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Gallery: Remove Instagram overlays and links
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
            </div>"""

new_gallery = """            <!-- Photo Gallery Grid -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div class="block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100" data-reveal="up" style="transition-delay: 0ms;">
                    <img src="https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Gallery Image 1" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100" data-reveal="up" style="transition-delay: 100ms;">
                    <img src="https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Gallery Image 2" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100" data-reveal="up" style="transition-delay: 200ms;">
                    <img src="https://images.unsplash.com/photo-1544626053-8985dc34ae63?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Gallery Image 3" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="block relative aspect-square group rounded-2xl overflow-hidden bg-gray-100" data-reveal="up" style="transition-delay: 300ms;">
                    <img src="https://images.unsplash.com/photo-1576495199011-eb94736d05d6?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Gallery Image 4" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
            </div>"""
content = content.replace(old_gallery, new_gallery)

# Remove the extra instagram button below it too
extra_ig_btn = """            <div class="mt-8 text-center md:hidden">
                <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="inline-flex items-center gap-2 bg-pink-50 text-pink-600 px-6 py-3 rounded-full font-bold hover:bg-pink-100 transition-colors border border-pink-100">
                    <i class="fab fa-instagram text-xl"></i> Daha çoxu Instagram-da
                </a>
            </div>"""
content = content.replace(extra_ig_btn, "")

# 2. Re-add the "Daha çoxuna bax" button below FAQ
old_faq_end = """                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
new_faq_end = """                        </div>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-10" data-reveal="up">
                <a href="suallar.html" class="inline-flex items-center gap-2 bg-kidora-blue text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-blue-600 transition-all shadow-lg hover:-translate-y-1" data-cursor-hot>
                    Suallar bölməsinə keçid <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </div>
    </section>"""
content = content.replace(old_faq_end, new_faq_end)

# 3. Change Hero badge text
old_hero_badge = """<div class="inline-flex items-center gap-2 bg-kidora-yellow text-kidora-dark px-4 py-2 rounded-full font-bold uppercase tracking-widest text-xs mb-6 shadow-md" data-reveal="zoom">
                    <i class="fas fa-star"></i> Məktəbdə Əla Nəticələr
                </div>"""
new_hero_badge = """<div class="inline-flex items-center gap-2 bg-kidora-yellow text-kidora-dark px-4 py-2 rounded-full font-bold uppercase tracking-widest text-xs mb-6 shadow-md" data-reveal="zoom">
                    <i class="fas fa-child"></i> 1-6 yaş qəbulu davam edir
                </div>"""
content = content.replace(old_hero_badge, new_hero_badge)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

