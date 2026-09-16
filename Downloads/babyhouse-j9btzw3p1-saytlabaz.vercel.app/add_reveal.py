import glob

for filepath in ['qeydiyyat.html', 'suallar.html', 'dernekler.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add data-reveal="up" to logical blocks if missing
    # Let's just do a naive replacement on common block classes like `bg-white rounded-2xl`
    content = content.replace('class="bg-white rounded-2xl p-6', 'data-reveal="up" class="bg-white rounded-2xl p-6')
    content = content.replace('class="text-center mb-16"', 'data-reveal="up" class="text-center mb-16"')
    content = content.replace('class="bg-white rounded-3xl p-8', 'data-reveal="up" class="bg-white rounded-3xl p-8')
    content = content.replace('class="bg-indigo-50 rounded-3xl p-8', 'data-reveal="up" class="bg-indigo-50 rounded-3xl p-8')
    content = content.replace('class="bg-teal-50 rounded-3xl p-8', 'data-reveal="up" class="bg-teal-50 rounded-3xl p-8')
    content = content.replace('class="bg-white rounded-2xl shadow-sm border', 'data-reveal="up" class="bg-white rounded-2xl shadow-sm border')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
