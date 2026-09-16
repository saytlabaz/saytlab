import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Favicon and Title
content = re.sub(
    r'<title>BabyHouse - 2011-ci ildən Lisenziyalı Uşaq Bağçası</title>',
    r'<title>BabyHouse</title>\n    <link rel="icon" type="image/png" href="BabyHouse.png">',
    content
)

# 3. Marquee removal
content = re.sub(
    r'<!-- Marquee Section -->\s*<div class="bg-kidora-dark text-white py-5 overflow-hidden border-y-4 border-kidora-yellow relative flex">.*?</div>\s*</div>',
    '',
    content,
    flags=re.DOTALL
)

# 4. Gallery instagram link removal
content = re.sub(
    r'<a href="https://www.instagram.com/babyhouse_az\?stkn=[^"]*" target="_blank" class="hidden md:inline-flex items-center gap-2 bg-pink-50 text-pink-600 px-6 py-3 rounded-full font-bold hover:bg-pink-100 transition-colors border border-pink-100">\s*<i class="fab fa-instagram text-xl"></i> @babyhouse_az\s*</a>',
    '',
    content
)

# 6. Navbar Instagram icon removal
content = re.sub(
    r'<a href="https://www.instagram.com/babyhouse_az\?stkn=[^"]*" target="_blank" class="text-pink-500 hover:text-pink-600 text-3xl transition-transform hover:scale-110" aria-label="Instagram">\s*<i class="fab fa-instagram"></i>\s*</a>',
    '',
    content
)

# 7. Navbar Lisenziyalı Bağça text removal
content = re.sub(
    r'<span class="text-\[10px\] uppercase font-bold tracking-widest text-kidora-blue mt-1">Lisenziyalı Bağça</span>',
    '',
    content,
    count=1
)

# 5. Footer Layout Change
footer_start = '<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">'
footer_replacement = '<div class="flex flex-col md:flex-row justify-between gap-12 md:gap-24 mb-16 w-full">'
content = content.replace(footer_start, footer_replacement)

content = content.replace(
    '<!-- Brand -->\n                <div>',
    '<!-- Brand -->\n                <div class="md:max-w-sm">'
)

content = content.replace(
    '<!-- Contact -->\n                <div>\n                    <h5 class="font-bold text-xl mb-6 text-kidora-green font-display">Əlaqə</h5>',
    '<div class="flex flex-col md:flex-row gap-12 lg:gap-24 md:ml-auto">\n                <!-- Contact -->\n                <div>\n                    <h5 class="font-bold text-xl mb-6 text-kidora-green font-display">Əlaqə</h5>'
)

content = content.replace(
    'Ən son yeniliklər üçün bizi instagramdan izləməyi unutmayın.</p>\n                </div>\n            </div>',
    'Ən son yeniliklər üçün bizi instagramdan izləməyi unutmayın.</p>\n                </div>\n                </div>\n            </div>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

