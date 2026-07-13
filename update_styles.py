import os, re

path = r'c:\Users\Malolan T\Desktop\Github-repo\texts\styles.css'
with open(path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update typography
css = css.replace("'EB Garamond', Georgia, serif", "'EB Garamond', serif")
css = css.replace("'Inter', system-ui, sans-serif", "'Outfit', 'Inter', system-ui, sans-serif")

# 2. Add glassmorphism to topbars/navs
css = re.sub(
    r'(\.topbar \{[^}]+)background: var\(--night\);',
    r'\1background: rgba(18, 14, 4, 0.85); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);',
    css
)

css = re.sub(
    r'(#nav \{[^}]+)background: var\(--surface\);',
    r'\1background: rgba(255, 252, 242, 0.85); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);',
    css
)

css = re.sub(
    r'(nav \{[^}]+)background: rgba\(253,246,227,0\.92\);',
    r'\1background: rgba(253, 248, 236, 0.85);',
    css
)

# 3. Enhance colors
replacements = {
    '--parchment: #fdf8ec;': '--parchment: #faf4e1;',
    '--parchment-dim: #f5edcf;': '--parchment-dim: #f0e6c8;',
    '--night: #1c160a;': '--night: #120e04;',
    '--saffron: #d4960e;': '--saffron: #e6a817;',
    
    '--bg: #fdf8ec;': '--bg: #faf4e1;',
    '--surface: #fffcf2;': '--surface: #fcf9f2;',
    '--border: #e8d88a;': '--border: #e0cc70;',
    '--border-strong: #c9a84c;': '--border-strong: #d4af37;',
    '--accent: #b07c10;': '--accent: #d4af37;',
    '--accent-bright: #d4960e;': '--accent-bright: #f1c40f;',
    
    # Dark mode enhancements
    '--bg: #120e04;': '--bg: #0d0a03;',
    '--surface: #1c1608;': '--surface: #151106;',
    '--border: #3a2e0e;': '--border: #4d3d12;',
    '--accent: #d4960e;': '--accent: #f1c40f;',
    
    # Micro animations (add transition to interactive elements)
    '.project-card {': '.project-card { transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s ease;',
    '.project-card:hover { border-color: var(--saffron); }': '.project-card:hover { border-color: var(--saffron); transform: translateY(-4px); box-shadow: 0 12px 24px rgba(230, 168, 23, 0.15); }',
    
    '.result-card {': '.result-card { transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;',
    '.result-card:hover { border-color: var(--saffron); }': '.result-card:hover { border-color: var(--saffron); transform: translateY(-2px); box-shadow: 0 8px 16px rgba(230, 168, 23, 0.1); }',
    
    '.file-card:hover { border-color: var(--border-strong); background: var(--accent-dim); transform: translateY(-1px); box-shadow: 0 3px 10px rgba(176,124,16,0.12); }': '.file-card:hover { border-color: var(--border-strong); background: var(--accent-dim); transform: translateY(-3px) scale(1.01); box-shadow: 0 12px 24px rgba(212, 175, 55, 0.15); }',
}

for old, new in replacements.items():
    css = css.replace(old, new)

# Import Outfit font
font_import = "@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');\n"
if "@import" not in css:
    css = font_import + css

with open(path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated styles.css with beautiful aesthetics!")
