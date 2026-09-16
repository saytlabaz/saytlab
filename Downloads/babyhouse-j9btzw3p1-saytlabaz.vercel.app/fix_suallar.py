import re

with open('suallar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the inline script block
content = re.sub(r'<script>.*?const faqBtns.*?faqBtns\.forEach\(btn.*?\}\);\n        \}\);\n    </script>\n', '', content, flags=re.DOTALL)

with open('suallar.html', 'w', encoding='utf-8') as f:
    f.write(content)

