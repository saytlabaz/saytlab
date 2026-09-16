import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Separate out the newly appended part
parts = content.split('})();')
main_content = parts[0]
appended_js = parts[1]

# Inject it before the init function
main_content = main_content.replace('function init() {', appended_js + '\n  function init() {')

# Hook it inside init
main_content = main_content.replace('initFAQ();\n  }', 'initFAQ();\n    initLightbox();\n  }')

final_content = main_content + '\n})();\n'

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(final_content)

