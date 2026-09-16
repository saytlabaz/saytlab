import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change 13 to 15
content = content.replace('data-count-to="13"', 'data-count-to="15"')

# 2. Re-center footer slightly (max-w-7xl)
content = content.replace('<div class="w-full px-4 md:px-12 mx-auto" data-reveal="up">', '<div class="max-w-7xl mx-auto" data-reveal="up">')

# 3. Fix Contact alignment
old_contact = """                <div class="flex flex-col text-left md:text-right mt-12 md:mt-0">
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

new_contact = """                <div class="flex flex-col text-left mt-12 md:mt-0 md:ml-auto">
                    <!-- Contact -->
                    <div>
                        <h5 class="font-bold text-xl mb-6 text-kidora-green font-display">Əlaqə</h5>
                        <ul class="space-y-4 text-gray-300 font-bold flex flex-col items-start">
                            <li>
                                <a href="https://maps.app.goo.gl/sPDzZaFzyFPeUnvX7?g_st=ic" target="_blank" class="flex items-center gap-3 hover:text-white group" data-cursor-hot>
                                    <i class="fas fa-map-marker-alt text-kidora-green text-lg group-hover:scale-110 transition-transform w-5 text-center"></i>
                                    <span>Cəfər Xəndan küçəsi 2D Baku, Azerbaijan</span>
                                </a>
                            </li>
                            <li>
                                <a href="https://wa.me/994553776710" target="_blank" class="flex items-center gap-3 hover:text-white group" data-cursor-hot>
                                    <i class="fas fa-phone-alt text-kidora-green text-lg group-hover:scale-110 transition-transform w-5 text-center"></i>
                                    <span>+994553776710</span>
                                </a>
                            </li>
                            <li>
                                <a href="mailto:seferova.ziyafet@mail.ru" class="flex items-center gap-3 hover:text-white group" data-cursor-hot>
                                    <i class="fas fa-envelope text-kidora-green text-lg group-hover:scale-110 transition-transform w-5 text-center"></i>
                                    <span>seferova.ziyafet@mail.ru</span>
                                </a>
                            </li>
                        </ul>
                    </div>
                    
                    <!-- Social (Below Contact) -->
                    <div class="mt-8 flex justify-start">
                        <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-pink-600 transition-colors text-lg shadow-lg" data-cursor-hot title="Instagram">
                            <i class="fab fa-instagram"></i>
                        </a>
                    </div>
                </div>"""
content = content.replace(old_contact, new_contact)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

