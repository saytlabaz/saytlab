import re
import glob

animation_css = """
    <style>
        /* --- Heavy/Slow Cinematic Reveal Animations (Blur to Clear) --- */
        .js-reveal [data-reveal] {
            opacity: 0;
            filter: blur(12px);
            transform: translateY(50px);
            transition: opacity 1s cubic-bezier(0.22, 1, 0.36, 1), 
                        transform 1s cubic-bezier(0.22, 1, 0.36, 1),
                        filter 1s cubic-bezier(0.22, 1, 0.36, 1);
            will-change: opacity, transform, filter;
        }
        .js-reveal [data-reveal="left"] {
            transform: translateX(-50px);
        }
        .js-reveal [data-reveal="right"] {
            transform: translateX(50px);
        }
        .js-reveal [data-reveal="zoom"] {
            transform: scale(0.9) translateY(20px);
        }
        .js-reveal [data-reveal].is-revealed {
            opacity: 1;
            filter: blur(0);
            transform: translate(0) scale(1);
        }

        /* --- Magnetic & Tilt Utilities --- */
        [data-magnetic] {
            display: inline-block;
            transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1);
        }
        .tilt-card {
            transition: transform 0.1s ease-out;
            transform-style: preserve-3d;
            will-change: transform;
        }
    </style>
"""

# HTML files to fix
files_to_fix = ['qeydiyyat.html', 'suallar.html', 'dernekler.html', 'qalereya.html']

for filepath in files_to_fix:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '.js-reveal [data-reveal]' not in content:
            content = content.replace('</head>', animation_css + '</head>')
            
            # Make sure body has js-reveal if it's missing (it usually gets added by app.js, but let's check if there are data-reveal elements)
            # wait, app.js adds `.js-reveal` to `document.documentElement` (html element). Let's let app.js do it.
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

