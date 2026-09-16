import glob

bad_css = """    <style>
        html, body {
            -webkit-overflow-scrolling: touch;
            overscroll-behavior-y: none;
            overflow-x: hidden !important;
            width: 100%;
            max-width: 100vw;
            position: relative;
        }"""
        
good_css = """    <style>
        html, body {
            -webkit-overflow-scrolling: touch;
            overscroll-behavior-y: none;
        }"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(bad_css, good_css)
    content = content.replace('<style>html, body { overflow-x: hidden !important; width: 100%; max-width: 100vw; position: relative; }</style></head>', '</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

