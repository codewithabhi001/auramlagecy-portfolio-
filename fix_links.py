import re
import os

files = ['pages/about.html', 'pages/services.html', 'pages/portfolio.html', 'pages/contact.html', 'pages/careers.html']
content = open('index.html', encoding='utf-8').read()

# Replace links targeting IDs on the same page with links pointing back to index.html
content = re.sub(r'href="#(\w+)"', r'href="../index.html#\1"', content)

for f in files:
    open(f, 'w', encoding='utf-8').write(content)

print("Links updated successfully.")
