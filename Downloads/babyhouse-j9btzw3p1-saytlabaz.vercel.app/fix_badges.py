import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the English flag badge
old_uk_badge = """                    <!-- Overlay Decor -->
                    <div class="absolute top-6 right-6 bg-white px-4 py-3 rounded-2xl shadow-xl transform rotate-6 animate-float flex items-center gap-3">
                        <span class="text-4xl">🇬🇧</span>
                        <div class="flex flex-col text-left">
                            <span class="font-bold text-sm leading-tight text-gray-800">İngilis</span>
                            <span class="font-bold text-sm leading-tight text-gray-800">Dilli Bölmə</span>
                        </div>
                    </div>"""
content = content.replace(old_uk_badge, "")

# 2. Change "Bədii Gimnastika" to "Musiqi Dərnəyi"
old_gymnastics = """                <!-- Gimnastika -->
                <div class="relative group rounded-3xl overflow-hidden card-shadow mt-0 lg:mt-12" data-reveal="up">
                    <img src="https://images.unsplash.com/photo-1515523110800-9415d13b84a8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Gimnastika" class="w-full h-80 object-cover group-hover:scale-105 tilt-card transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-kidora-dark/90 via-kidora-dark/40 to-transparent flex flex-col justify-end p-8 text-white">
                        <div class="w-12 h-12 bg-white text-kidora-pink rounded-full flex items-center justify-center text-xl mb-4">
                            <i class="fas fa-running"></i>
                        </div>
                        <h4 class="text-3xl font-display font-bold mb-2">Bədii Gimnastika</h4>
                        <p class="text-gray-200 font-medium">Fiziki inkişaf, çeviklik, sağlam duruş və koordinasiyanı təmin edən idman məşğələləri.</p>
                    </div>
                </div>"""

new_music = """                <!-- Musiqi -->
                <div class="relative group rounded-3xl overflow-hidden card-shadow mt-0 lg:mt-12" data-reveal="up">
                    <img src="https://images.unsplash.com/photo-1514119412350-e170420d9e26?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Musiqi" class="w-full h-80 object-cover group-hover:scale-105 tilt-card transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-kidora-dark/90 via-kidora-dark/40 to-transparent flex flex-col justify-end p-8 text-white">
                        <div class="w-12 h-12 bg-white text-kidora-pink rounded-full flex items-center justify-center text-xl mb-4">
                            <i class="fas fa-music"></i>
                        </div>
                        <h4 class="text-3xl font-display font-bold mb-2">Musiqi Dərnəyi</h4>
                        <p class="text-gray-200 font-medium">Ritmi hiss etmək, musiqi duyumunu artırmaq və enerjini düzgün yönləndirmək üçün əyləncəli dərslər.</p>
                    </div>
                </div>"""
content = content.replace(old_gymnastics, new_music)

# Ensure "Rəsm" is "İncəsənət Dərnəyi"
old_art = """                <!-- Rəsm -->
                <div class="relative group rounded-3xl overflow-hidden card-shadow" data-reveal="right">
                    <img src="https://images.unsplash.com/photo-1513364776144-60967b0f800f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Rəsm" class="w-full h-80 object-cover group-hover:scale-105 tilt-card transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-kidora-dark/90 via-kidora-dark/40 to-transparent flex flex-col justify-end p-8 text-white">
                        <div class="w-12 h-12 bg-white text-kidora-yellow rounded-full flex items-center justify-center text-xl mb-4">
                            <i class="fas fa-palette"></i>
                        </div>
                        <h4 class="text-3xl font-display font-bold mb-2">Rəsm & İncəsənət</h4>
                        <p class="text-gray-200 font-medium">Uşaqların daxili dünyasını kəşf etmələri və yaradıcılıq qabiliyyətini göstərmələri üçün azad mühit.</p>
                    </div>
                </div>"""
new_art = """                <!-- İncəsənət -->
                <div class="relative group rounded-3xl overflow-hidden card-shadow" data-reveal="right">
                    <img src="https://images.unsplash.com/photo-1513364776144-60967b0f800f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="İncəsənət" class="w-full h-80 object-cover group-hover:scale-105 tilt-card transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-kidora-dark/90 via-kidora-dark/40 to-transparent flex flex-col justify-end p-8 text-white">
                        <div class="w-12 h-12 bg-white text-kidora-yellow rounded-full flex items-center justify-center text-xl mb-4">
                            <i class="fas fa-palette"></i>
                        </div>
                        <h4 class="text-3xl font-display font-bold mb-2">İncəsənət Dərnəyi</h4>
                        <p class="text-gray-200 font-medium">Uşaqların daxili dünyasını kəşf etmələri və yaradıcılıq qabiliyyətini göstərmələri üçün azad mühit.</p>
                    </div>
                </div>"""
content = content.replace(old_art, new_art)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

