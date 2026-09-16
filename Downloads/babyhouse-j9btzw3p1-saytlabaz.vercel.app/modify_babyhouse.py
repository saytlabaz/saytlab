import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fonts and Tailwind Config
content = re.sub(
    r'<!-- Google Fonts: Quicksand for headings \(supports Ə perfectly\), Nunito for body -->.*?<link href="https://fonts.googleapis.com/css2\?family=Nunito:wght@400;600;700;800&family=Quicksand:wght@500;600;700&display=swap" rel="stylesheet">',
    r'<!-- Google Fonts: Poppins for headings, Inter for body -->\n    <link rel="preconnect" href="https://fonts.googleapis.com">\n    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">',
    content,
    flags=re.DOTALL
)

content = re.sub(r"sans: \['Nunito', 'sans-serif'\],", "sans: ['Inter', 'sans-serif'],", content)
content = re.sub(r"display: \['Quicksand', 'sans-serif'\],", "display: ['Poppins', 'sans-serif'],", content)

# 2. Add Cursor Elements to Body and CSS to style
cursor_css = """
        /* --- Custom Cursor --- */
        html.cursor-custom, html.cursor-custom * { cursor: none !important; }
        .cursor-dot, .cursor-ring {
            position: fixed;
            top: 0; left: 0;
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
            opacity: 0;
            transition: opacity .25s ease, width .2s ease, height .2s ease, background-color .2s ease, border-color .2s ease;
            will-change: transform;
        }
        .cursor-custom .cursor-dot, .cursor-custom .cursor-ring { opacity: 1; }
        .cursor-dot {
            width: 7px; height: 7px;
            background: #EF476F;
        }
        .cursor-ring {
            width: 30px; height: 30px;
            border: 1.5px solid rgba(239, 71, 111, 0.5);
            background: rgba(239, 71, 111, 0.04);
        }
        .cursor-custom.cursor-hot .cursor-ring {
            width: 46px; height: 46px;
            border-color: #FFC837;
            background: rgba(255, 200, 55, 0.10);
            box-shadow: 0 0 12px 2px rgba(255, 200, 55, 0.4);
        }
        .cursor-custom.cursor-hot .cursor-dot { background: #FFC837; }
        .cursor-custom.cursor-hidden .cursor-dot,
        .cursor-custom.cursor-hidden .cursor-ring { opacity: 0; }
        @media (prefers-reduced-motion: reduce) {
            html.cursor-custom, html.cursor-custom * { cursor: auto !important; }
            .cursor-dot, .cursor-ring { display: none !important; }
        }
"""
content = content.replace("    </style>", cursor_css + "\n    </style>")
content = content.replace("<body", '<div class="cursor-dot"></div>\n    <div class="cursor-ring"></div>\n\n<body')

# 3. Hero Section Buttons (Qeydiyyata Yazıl & Instagram)
content = content.replace(
    '<a href="#elaqe" class="bg-kidora-pink text-white px-8 py-4 tilt-card rounded-full font-bold text-lg hover:bg-rose-500 transition-all transform hover:-translate-y-1 shadow-[0_8px_0_#be123c] active:translate-y-1 active:shadow-none flex items-center justify-center gap-2">\n                        <span>Qeydiyyata Yazıl</span>\n                        <i class="fas fa-arrow-right"></i>\n                    </a>\n                    <a href="https://www.instagram.com/babyhouse_az?stkn=MTB6b2cxYWJzYTdpYQ%3D%3D&utm_source=qr" target="_blank" class="bg-white text-kidora-dark border-2 border-gray-200 px-8 py-4 rounded-full font-bold text-lg hover:border-pink-500 hover:text-pink-600 transition-all flex items-center justify-center gap-2">\n                        <i class="fab fa-instagram text-xl"></i> Instagram\n                    </a>',
    '<a href="qeydiyyat.html" class="bg-kidora-pink text-white px-8 py-4 tilt-card rounded-full font-bold text-lg hover:bg-rose-500 transition-all transform hover:-translate-y-1 shadow-[0_8px_0_#be123c] active:translate-y-1 active:shadow-none flex items-center justify-center gap-2" data-cursor-hot>\n                        <span>Qeydiyyata Yazıl</span>\n                        <i class="fas fa-arrow-right"></i>\n                    </a>'
)

# 4. Languages Section (Bölmələr)
content = re.sub(r'<div class="w-20 h-20 bg-pink-100 text-kidora-pink rounded-full flex items-center justify-center text-4xl mb-6 group-hover:scale-110 transition-transform">\n\s*🇦🇿\n\s*</div>', '', content)
content = re.sub(r'<div class="w-20 h-20 bg-blue-100 text-kidora-blue rounded-full flex items-center justify-center text-4xl mb-6 group-hover:scale-110 transition-transform">\n\s*🇷🇺\n\s*</div>', '', content)
content = re.sub(r'<div class="w-20 h-20 bg-green-100 text-kidora-green rounded-full flex items-center justify-center text-4xl mb-6 group-hover:scale-110 transition-transform">\n\s*🇬🇧\n\s*</div>', '', content)

# Add Register buttons under languages
content = re.sub(
    r'(<p class="text-gray-600 leading-relaxed">Ana dilində mükəmməl nitq inkişafı, məktəbəqədər hazırlıq və milli dəyərlərin öyrədilməsi əsasında qurulmuş proqram.</p>)',
    r'\1\n                    <a href="qeydiyyat.html" class="inline-block mt-6 bg-kidora-pink text-white px-6 py-2 rounded-full font-bold shadow-md hover:bg-rose-500 transition-colors" data-cursor-hot>Qeydiyyat</a>',
    content
)
content = re.sub(
    r'(<p class="text-gray-600 leading-relaxed">Rus dilində təməl anlayışlar, sərbəst danışıq mühiti və rus dilli məktəblərə tam zəmanətli hazırlıq.</p>)',
    r'\1\n                    <a href="qeydiyyat.html" class="inline-block mt-6 bg-kidora-blue text-white px-6 py-2 rounded-full font-bold shadow-md hover:bg-blue-600 transition-colors" data-cursor-hot>Qeydiyyat</a>',
    content
)
content = re.sub(
    r'(<p class="text-gray-600 leading-relaxed">Uşaqlar üçün xüsusi seçilmiş beynəlxalq metodikalarla erkən yaşdan ingilis dili mühitinə inteqrasiya və tədris.</p>)',
    r'\1\n                    <a href="qeydiyyat.html" class="inline-block mt-6 bg-kidora-green text-white px-6 py-2 rounded-full font-bold shadow-md hover:bg-green-600 transition-colors" data-cursor-hot>Qeydiyyat</a>',
    content
)


# 5. Dərnəklər Hamsına bax
content = content.replace(
    '</section>\n\n    <!-- Why Us (Üstünlüklər & Counter Animation) -->',
    '        <div class="text-center mt-12" data-reveal="up">\n                <a href="dernekler.html" class="inline-flex items-center gap-2 bg-kidora-green text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-green-600 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-1" data-cursor-hot>\n                    Hamsına bax <i class="fas fa-arrow-right"></i>\n                </a>\n            </div>\n        </div>\n    </section>\n\n    <!-- Why Us (Üstünlüklər & Counter Animation) -->'
)

# 6. Qalereya
content = content.replace('Instagram Qalereyası', 'Qalereya')
content = content.replace(
    '</section>\n\n    <!-- Call to Action Banner -->',
    '        <div class="text-center mt-12" data-reveal="up">\n                <a href="qalereya.html" class="inline-flex items-center gap-2 bg-pink-500 text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-pink-600 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-1" data-cursor-hot>\n                    Hamsına bax <i class="fas fa-arrow-right"></i>\n                </a>\n            </div>\n        </div>\n    </section>\n\n    <!-- Call to Action Banner -->'
)

# 7. Footer - Contact, Address, Logo, Remove Quick Links
content = content.replace('<span>Bakı şəhəri, Azərbaycan</span>', '<span>Cəfər Xəndan küçəsi 2D Baku, Azerbaijan</span>')
content = content.replace('<span>+994 (__) ___ __ __<br><span class="text-sm text-gray-500 font-medium">(Nömrənizi buraya əlavə edəcəyik)</span></span>', '<span>+994553776710</span>\n                        </li>\n                        <li class="flex items-start gap-3">\n                            <i class="fas fa-envelope text-kidora-green mt-1 text-lg"></i>\n                            <span>seferova.ziyafet@mail.ru</span>')
content = content.replace(
    '<div class="w-12 h-12 bg-kidora-pink rounded-full flex items-center justify-center text-white font-display font-bold text-2xl blob-shape shadow-md">\n                            B\n                        </div>',
    '<img src="BabyHouse.png" alt="BabyHouse" class="w-16 h-16 object-contain">'
)

content = re.sub(
    r'<!-- Links -->\s*<div>\s*<h5 class="font-bold text-xl mb-6 text-kidora-yellow font-display">Sürətli Keçidlər</h5>\s*<ul class="space-y-3 text-gray-300 font-bold">.*?</ul>\s*</div>',
    '',
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'<a href="#" class="w-12 h-12 bg-white/5 rounded-full flex items-center justify-center hover:bg-blue-600 transition-colors text-xl shadow-lg opacity-50 cursor-not-allowed" title="Tezliklə">\s*<i class="fab fa-facebook-f"></i>\s*</a>\s*<a href="#" class="w-12 h-12 bg-white/5 rounded-full flex items-center justify-center hover:bg-green-500 transition-colors text-xl shadow-lg opacity-50 cursor-not-allowed" title="Tezliklə">\s*<i class="fab fa-whatsapp"></i>\s*</a>',
    '',
    content
)

# Add data-reveal="up" to sections/tags that might be missing it for more "animations everywhere" feel
# Since we can't easily parse HTML with regex safely for every tag, we'll just leave the existing data-reveal tags 
# which already cover most elements.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

