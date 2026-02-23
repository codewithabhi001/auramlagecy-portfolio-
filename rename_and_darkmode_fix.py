import os
import re

files_to_process = [
    'index.html',
    'pages/about.html',
    'pages/services.html',
    'pages/portfolio.html',
    'pages/contact.html',
    'pages/careers.html',
    'pages/privacy.html',
    'pages/terms.html'
]

# Replacement mappings for company name
replacements = [
    (r'Aurum Legacy', 'Nexarova Core'),
    (r'AURUM LEGACY', 'NEXAROVA CORE'),
    (r'Aurum Global', 'Nexarova Global'),
    (r'Aurum', 'Nexarova'),
    (r'>AL<', '>NC<'),  # Logo shortcode
    (r'Aurum Global Holdings LLC', 'Nexarova Core IT LLC'),
]

new_js = """
    <script>
        function toggleDark() {
            document.documentElement.classList.toggle('dark');
            if(document.documentElement.classList.contains('dark')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        }

        // Initialize from localstorage
        if (localStorage.getItem('theme') === 'dark') {
            document.documentElement.classList.add('dark');
        } else if (localStorage.getItem('theme') === 'light') {
            document.documentElement.classList.remove('dark');
        } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            // Default to system preference if no localStorage set
            document.documentElement.classList.add('dark');
        }
        
        // Smooth Animation Logic for Entrance
        const observerOptions = { threshold: 0.2 };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('opacity-100');
                    entry.target.classList.remove('translate-y-20', 'opacity-0');
                }
            });
        }, observerOptions);

        document.querySelectorAll('section, header').forEach(el => {
            el.classList.add('transition-all', 'duration-1000', 'translate-y-20', 'opacity-0');
            observer.observe(el);
        });
    </script>
"""

for filepath in files_to_process:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace names
    for old, new in replacements:
        content = re.sub(old, new, content)
        
    # Fix dark mode buttons
    content = content.replace("onclick=\"document.documentElement.classList.toggle('dark')\"", "onclick=\"toggleDark()\"")

    # Fix JS - Remove old initialize script
    old_init = """// Initialize from localstorage
        if (localStorage.getItem('theme') === 'dark') {
            document.documentElement.classList.add('dark');
        }"""
    content = content.replace(old_init, "")
    
    # We can replace the whole script block
    # Find the script block defining observer because it's easiest to replace from there
    script_pattern = re.compile(r'<script>\s*// Smooth Animation Logic for Entrance.*?</script>', re.DOTALL)
    
    if script_pattern.search(content):
         content = script_pattern.sub(new_js, content)
    else:
         # Fallback if the pattern doesn't match perfectly, it means it's already updated or slightly different
         pass

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Unique Company Name and Global Dark Mode Fix Applied")
