import os, re

base_dir = r'c:\Users\Malolan T\Desktop\Github-repo\texts'
files = ['index.html', r'Agama\index.html', r'sAmam\index.html', r'srivaishnavam\index.html']
all_styles = []

for f in files:
    path = os.path.join(base_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if match:
        style_content = match.group(1)
        all_styles.append(f'/* --- Styles from {f} --- */\n' + style_content)
        
        link_path = 'styles.css' if f == 'index.html' else '../styles.css'
        new_content = content[:match.start()] + f'<link rel=\"stylesheet\" href=\"{link_path}\">' + content[match.end():]
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Processed {f}')

styles_path = os.path.join(base_dir, 'styles.css')
with open(styles_path, 'w', encoding='utf-8') as file:
    file.write('\n\n'.join(all_styles))
print('Created styles.css')
