import os
import re

files = ['pages/about.html', 'pages/services.html', 'pages/portfolio.html', 'pages/contact.html', 'pages/careers.html', 'pages/privacy.html', 'pages/terms.html']

new_nav = '''<div
                class="hidden xl:flex items-center space-x-12 font-ui font-bold text-[11px] uppercase tracking-[0.2em]">
                <a href="about.html" class="hover:text-gold transition">Our Mission</a>
                <a href="services.html" class="hover:text-gold transition">Ecosystem & Services</a>
                <a href="../index.html#tech" class="hover:text-gold transition">Technology</a>
                <a href="../index.html#blueprint" class="hover:text-gold transition">Process</a>
                <a href="portfolio.html" class="hover:text-gold transition">Cases & Portfolio</a>
                <a href="careers.html" class="hover:text-gold transition">Join Guild</a>
                <button onclick="document.documentElement.classList.toggle('dark')"
                    class="w-10 h-10 border border-gold/30 rounded-none flex items-center justify-center">
                    <i class="fas fa-moon dark:hidden text-gold"></i>
                    <i class="fas fa-sun hidden dark:block text-gold"></i>
                </button>
                <a href="contact.html"
                    class="px-10 py-5 bg-onyx text-white dark:bg-gold dark:text-onyx border-2 border-onyx hover:bg-transparent hover:text-onyx dark:hover:text-white dark:hover:border-white transition-all">Capital
                    Inquiry</a>
            </div>'''

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace logo container with a link
    content = content.replace('<div class="flex items-center space-x-4 cursor-pointer" onclick="window.scrollTo(0,0)">', '<a href="../index.html" class="flex items-center space-x-4 cursor-pointer">')
    # Use robust regex to fix closing tag of logo
    content = re.sub(r'Worldwide</span>\s*</div>\s*</div>', r'Worldwide</span>\n                </div>\n            </a>', content)
            
    # Modify the nav
    nav_pattern = re.compile(r'<div\s+class="hidden xl:flex items-center space-x-12 font-ui font-bold text-\[11px\] uppercase tracking-\[0\.2em\]">.*?</div>', re.DOTALL)
    content = nav_pattern.sub(new_nav, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Nav updated in all subpages")
