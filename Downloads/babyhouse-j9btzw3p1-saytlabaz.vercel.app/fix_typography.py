import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix h1
old_h1 = '<h1 data-aos="fade-up" data-aos-delay="100" class="text-xl md:text-3xl md:text-5xl md:text-lg md:text-2xl md:text-4xl md:text-6xl lg:text-7xl font-display font-bold text-kidora-dark leading-[1.1] mb-6">'
new_h1 = '<h1 data-aos="fade-up" data-aos-delay="100" class="text-3xl md:text-5xl lg:text-6xl font-display font-bold text-kidora-dark leading-[1.1] mb-6">'
content = content.replace(old_h1, new_h1)

# Fix p
old_p = '<p data-aos="fade-up" data-aos-delay="150" class="text-xl md:text-lg md:text-2xl text-gray-600 mb-5 md:mb-10 max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed">'
new_p = '<p data-aos="fade-up" data-aos-delay="150" class="text-[15px] md:text-lg text-gray-600 mb-5 md:mb-10 max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed">'
content = content.replace(old_p, new_p)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

