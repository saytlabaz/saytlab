import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the clubs in "Xüsusi Dərnəklərimiz" section
old_clubs = """            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 relative z-10" id="dernekler-grid">
                
                <div class="bg-white rounded-3xl p-8 card-shadow tilt-card border border-gray-100 group" data-reveal="up" data-magnetic>
                    <div class="w-16 h-16 bg-kidora-yellow text-white rounded-2xl flex items-center justify-center text-2xl mb-6 shadow-lg shadow-kidora-yellow/30 group-hover:scale-110 transition-transform">
                        <i class="fas fa-palette"></i>
                    </div>
                    <h3 class="text-2xl font-display font-bold text-kidora-dark mb-4">İncəsənət & Rəsm</h3>
                    <p class="text-gray-600 font-medium">Uşaqların yaradıcılıq qabiliyyətini və incə motorikasını inkişaf etdirən rəngarəng məşğələlər.</p>
                </div>

                <div class="bg-white rounded-3xl p-8 card-shadow tilt-card border border-gray-100 group" data-reveal="up" data-reveal-delay="100" data-magnetic>
                    <div class="w-16 h-16 bg-kidora-pink text-white rounded-2xl flex items-center justify-center text-2xl mb-6 shadow-lg shadow-kidora-pink/30 group-hover:scale-110 transition-transform">
                        <i class="fas fa-music"></i>
                    </div>
                    <h3 class="text-2xl font-display font-bold text-kidora-dark mb-4">Musiqi & Rəqs</h3>
                    <p class="text-gray-600 font-medium">Ritmi hiss etmək, musiqi duyumunu artırmaq və enerjini düzgün yönləndirmək üçün əyləncəli dərslər.</p>
                </div>

                <div class="bg-white rounded-3xl p-8 card-shadow tilt-card border border-gray-100 group" data-reveal="up" data-reveal-delay="200" data-magnetic>
                    <div class="w-16 h-16 bg-kidora-blue text-white rounded-2xl flex items-center justify-center text-2xl mb-6 shadow-lg shadow-kidora-blue/30 group-hover:scale-110 transition-transform">
                        <i class="fas fa-robot"></i>
                    </div>
                    <h3 class="text-2xl font-display font-bold text-kidora-dark mb-4">Robotexnika</h3>
                    <p class="text-gray-600 font-medium">Məntiqi təfəkkürü, problem həll etmə bacarığını və texnologiyaya marağı oyadan müasir dərnək.</p>
                </div>"""

new_clubs = """            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 relative z-10" id="dernekler-grid">
                
                <div class="bg-white rounded-3xl p-8 card-shadow tilt-card border border-gray-100 group" data-reveal="up" data-magnetic>
                    <div class="w-16 h-16 bg-kidora-blue text-white rounded-2xl flex items-center justify-center text-2xl mb-6 shadow-lg shadow-kidora-blue/30 group-hover:scale-110 transition-transform">
                        <i class="fas fa-chess"></i>
                    </div>
                    <h3 class="text-2xl font-display font-bold text-kidora-dark mb-4">Şahmat Dərnəyi</h3>
                    <p class="text-gray-600 font-medium">Məntiqi təfəkkürü, diqqəti və strateji düşünmə bacarığını oyadan intellektual oyun məşğələləri.</p>
                </div>

                <div class="bg-white rounded-3xl p-8 card-shadow tilt-card border border-gray-100 group" data-reveal="up" data-reveal-delay="100" data-magnetic>
                    <div class="w-16 h-16 bg-kidora-pink text-white rounded-2xl flex items-center justify-center text-2xl mb-6 shadow-lg shadow-kidora-pink/30 group-hover:scale-110 transition-transform">
                        <i class="fas fa-music"></i>
                    </div>
                    <h3 class="text-2xl font-display font-bold text-kidora-dark mb-4">Musiqi Dərnəyi</h3>
                    <p class="text-gray-600 font-medium">Ritmi hiss etmək, musiqi duyumunu artırmaq və enerjini düzgün yönləndirmək üçün əyləncəli dərslər.</p>
                </div>

                <div class="bg-white rounded-3xl p-8 card-shadow tilt-card border border-gray-100 group" data-reveal="up" data-reveal-delay="200" data-magnetic>
                    <div class="w-16 h-16 bg-kidora-yellow text-white rounded-2xl flex items-center justify-center text-2xl mb-6 shadow-lg shadow-kidora-yellow/30 group-hover:scale-110 transition-transform">
                        <i class="fas fa-palette"></i>
                    </div>
                    <h3 class="text-2xl font-display font-bold text-kidora-dark mb-4">İncəsənət Dərnəyi</h3>
                    <p class="text-gray-600 font-medium">Uşaqların yaradıcılıq qabiliyyətini və incə motorikasını inkişaf etdirən rəngarəng rəsm məşğələləri.</p>
                </div>"""
content = content.replace(old_clubs, new_clubs)

# 2. Hero Section badages: Remove "İngilis bölməsi", Change "Məktəbdə Əla Nəticələr" to "1-6 yaş qəbulu davam edir"
# Looking at the original hero code
old_hero_badges = """            <div class="w-full lg:w-1/2 relative mt-16 lg:mt-0" data-reveal="left">
                <div class="relative w-full aspect-square max-w-[500px] mx-auto">
                    <!-- Decorative background elements -->
                    <div class="absolute inset-0 bg-kidora-pink rounded-[40px] rotate-3 opacity-20 scale-105"></div>
                    <div class="absolute inset-0 bg-kidora-yellow rounded-[40px] -rotate-3 opacity-20 scale-105"></div>
                    
                    <img src="https://images.unsplash.com/photo-1516627145497-ae6968895b74?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Xoşbəxt uşaqlar" class="relative w-full h-full object-cover rounded-[40px] shadow-2xl z-10">
                    
                    <!-- Floating Badge 1 -->
                    <div class="absolute -left-8 top-1/4 bg-white p-4 rounded-2xl shadow-xl z-20 animate-float" data-magnetic>
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-xl overflow-hidden">
                                🇬🇧
                            </div>
                            <div>
                                <p class="text-xs text-gray-500 font-bold">Xarici Dil</p>
                                <p class="text-sm font-bold text-kidora-dark">İngilis Bölməsi</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Floating Badge 2 -->
                    <div class="absolute -right-8 bottom-1/4 bg-white p-4 rounded-2xl shadow-xl z-20 animate-float" style="animation-delay: 2s;" data-magnetic>
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-yellow-100 flex items-center justify-center text-kidora-yellow text-xl">
                                <i class="fas fa-star"></i>
                            </div>
                            <div>
                                <p class="text-xs text-gray-500 font-bold">Təhsilin Keyfiyyəti</p>
                                <p class="text-sm font-bold text-kidora-dark">Məktəbdə Əla Nəticələr</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""

new_hero_badges = """            <div class="w-full lg:w-1/2 relative mt-16 lg:mt-0" data-reveal="left">
                <div class="relative w-full aspect-square max-w-[500px] mx-auto">
                    <!-- Decorative background elements -->
                    <div class="absolute inset-0 bg-kidora-pink rounded-[40px] rotate-3 opacity-20 scale-105"></div>
                    <div class="absolute inset-0 bg-kidora-yellow rounded-[40px] -rotate-3 opacity-20 scale-105"></div>
                    
                    <img src="https://images.unsplash.com/photo-1516627145497-ae6968895b74?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Xoşbəxt uşaqlar" class="relative w-full h-full object-cover rounded-[40px] shadow-2xl z-10">
                    
                    <!-- Floating Badge 2 (Now the only one) -->
                    <div class="absolute -right-8 bottom-1/4 bg-white p-4 rounded-2xl shadow-xl z-20 animate-float" style="animation-delay: 2s;" data-magnetic>
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-yellow-100 flex items-center justify-center text-kidora-yellow text-xl">
                                👶🏻
                            </div>
                            <div>
                                <p class="text-xs text-gray-500 font-bold">Qeydiyyat</p>
                                <p class="text-sm font-bold text-kidora-dark">1-6 yaş qəbulu davam edir</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""
content = content.replace(old_hero_badges, new_hero_badges)

# Wait, they also said: "Ana səhifədə ilk görünən şəkil üstündəki qutucuqdakı "Məktəbdə Əla Nəticələr" - Bu cümlələrin yerinə bunu yaz - "1-6 yaş qəbulu davam edir""
# There was another "Məktəbdə Əla Nəticələr" in the main text area (I changed it earlier to 1-6 yaş qəbulu davam edir, then reverted).
# But now they specifically say "ilk görünən şəkil üstündəki qutucuqdakı", so they mean the Floating Badge 2 over the image! Which is what I just replaced above. Let's make sure.

# They also said "Yuxarıda suallar bölməsinə keçidi ləğv et ancaq aşağıda olsun ana səhifəsi geniş olsun"
# Ah! In the navigation header menu, did I have a link to "Suallar"?
# Let's check the header of index.html.
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
