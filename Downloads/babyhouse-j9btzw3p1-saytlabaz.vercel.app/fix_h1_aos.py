import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove data-aos from the parent container
old_parent = '<div class="flex-1 text-center lg:text-left z-10" data-aos="fade-right">'
new_parent = '<div class="flex-1 text-center lg:text-left z-10">'
content = content.replace(old_parent, new_parent)

# Also ensure the button container has AOS
old_btn = '<div class="flex flex-col sm:flex-row gap-5 justify-center lg:justify-start">'
new_btn = '<div class="flex flex-col sm:flex-row gap-5 justify-center lg:justify-start" data-aos="fade-up" data-aos-delay="200">'
content = content.replace(old_btn, new_btn)

# Ensure the small badge also has AOS
old_badge_div = """                <div class="inline-block bg-white px-5 py-2 rounded-full text-kidora-blue font-bold text-sm mb-6 border border-kidora-blue/20 shadow-sm uppercase tracking-wider animate-float">"""
new_badge_div = """                <div data-aos="fade-down" class="inline-block bg-white px-5 py-2 rounded-full text-kidora-blue font-bold text-sm mb-6 border border-kidora-blue/20 shadow-sm uppercase tracking-wider animate-float">"""
content = content.replace(old_badge_div, new_badge_div)

# Adjust the h1 delay so it falls in sequence
old_h1 = '<h1 data-aos="fade-up" class="'
new_h1 = '<h1 data-aos="fade-up" data-aos-delay="100" class="'
content = content.replace(old_h1, new_h1)

# Adjust the p delay
old_p = '<p data-aos="fade-up" class="text-xl md:text-lg md:text-2xl text-gray-600 mb-5 md:mb-10 max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed">'
new_p = '<p data-aos="fade-up" data-aos-delay="150" class="text-xl md:text-lg md:text-2xl text-gray-600 mb-5 md:mb-10 max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed">'
content = content.replace(old_p, new_p)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
