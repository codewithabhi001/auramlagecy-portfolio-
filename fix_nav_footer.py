import re
import os

# Define the HTML template pieces
desktop_nav_index = """
                <a href="pages/about.html" class="hover:text-gold transition text-onyx dark:text-white">Our Mission</a>
                <a href="pages/services.html" class="hover:text-gold transition text-onyx dark:text-white">Ecosystem & Services</a>
                <a href="index.html#tech" class="hover:text-gold transition text-onyx dark:text-white">Technology</a>
                <a href="index.html#blueprint" class="hover:text-gold transition text-onyx dark:text-white">Process</a>
                <a href="pages/portfolio.html" class="hover:text-gold transition text-onyx dark:text-white">Cases & Portfolio</a>
                <a href="pages/careers.html" class="hover:text-gold transition text-onyx dark:text-white">Join Guild</a>
"""

mobile_nav_index = """
            <a href="pages/about.html" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Our Mission</a>
            <a href="pages/services.html" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Ecosystem & Services</a>
            <a href="index.html#tech" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Technology</a>
            <a href="index.html#blueprint" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Process</a>
            <a href="pages/portfolio.html" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Cases & Portfolio</a>
            <a href="pages/careers.html" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Join Guild</a>
"""

contact_link_index = "pages/contact.html"


desktop_nav_sub = """
                <a href="about.html" class="hover:text-gold transition text-onyx dark:text-white">Our Mission</a>
                <a href="services.html" class="hover:text-gold transition text-onyx dark:text-white">Ecosystem & Services</a>
                <a href="../index.html#tech" class="hover:text-gold transition text-onyx dark:text-white">Technology</a>
                <a href="../index.html#blueprint" class="hover:text-gold transition text-onyx dark:text-white">Process</a>
                <a href="portfolio.html" class="hover:text-gold transition text-onyx dark:text-white">Cases & Portfolio</a>
                <a href="careers.html" class="hover:text-gold transition text-onyx dark:text-white">Join Guild</a>
"""

mobile_nav_sub = """
            <a href="about.html" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Our Mission</a>
            <a href="services.html" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Ecosystem & Services</a>
            <a href="../index.html#tech" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Technology</a>
            <a href="../index.html#blueprint" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Process</a>
            <a href="portfolio.html" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Cases & Portfolio</a>
            <a href="careers.html" class="hover:text-gold transition w-full block py-2 text-onyx dark:text-white">Join Guild</a>
"""

contact_link_sub = "contact.html"


nav_template = """<nav class="fixed w-full z-[999] bg-white/95 dark:bg-onyx/95 border-b-2 border-gold/20 backdrop-blur-xl">
        <div class="max-w-[1800px] mx-auto px-6 lg:px-16 flex justify-between items-center h-24 relative">
            <a href="{home_link}" class="flex items-center space-x-4 cursor-pointer">
                <div class="w-14 h-14 bg-gold flex items-center justify-center font-black text-2xl text-onyx italic">AL</div>
                <div class="hidden sm:block">
                    <span class="block text-2xl font-black uppercase tracking-tighter leading-none font-header text-onyx dark:text-white">Aurum <span class="text-gold">Legacy</span></span>
                    <span class="text-[9px] tracking-[0.4em] font-ui uppercase opacity-60 text-onyx dark:text-white">Engineering Excellence</span>
                </div>
            </a>

            <!-- Desktop Nav -->
            <div class="hidden xl:flex items-center space-x-12 font-ui font-bold text-[11px] uppercase tracking-[0.2em]">
                {desktop_links}
                <button onclick="document.documentElement.classList.toggle('dark')" class="w-10 h-10 border border-gold/30 rounded-none flex items-center justify-center">
                    <i class="fas fa-moon dark:hidden text-gold"></i>
                    <i class="fas fa-sun hidden dark:block text-gold"></i>
                </button>
                <a href="{contact_link}" class="px-10 py-5 bg-onyx text-white dark:bg-gold dark:text-onyx border-2 border-onyx hover:bg-transparent hover:text-onyx dark:hover:text-white dark:hover:border-white transition-all text-center">Capital Inquiry</a>
            </div>

            <!-- Mobile Toggle -->
            <div class="xl:hidden flex items-center space-x-6">
                <button onclick="document.documentElement.classList.toggle('dark')" class="w-10 h-10 border border-gold/30 rounded-none flex items-center justify-center">
                    <i class="fas fa-moon dark:hidden text-gold"></i>
                    <i class="fas fa-sun hidden dark:block text-gold"></i>
                </button>
                <button id="mobile-menu-btn" class="text-3xl text-gold focus:outline-none hover:text-onyx dark:hover:text-white transition">
                    <i class="fas fa-bars"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Nav Overlay -->
        <div id="mobile-menu" class="hidden absolute top-24 left-0 w-full bg-white dark:bg-onyx border-b-2 border-gold/20 shadow-2xl flex-col items-center py-10 space-y-6 font-ui font-bold text-sm uppercase tracking-widest text-center">
            {mobile_links}
            <a href="{contact_link}" class="px-10 py-5 mt-4 bg-onyx text-white dark:bg-gold dark:text-onyx border-2 border-onyx hover:bg-transparent dark:hover:text-white dark:hover:border-white transition-all w-3/4 max-w-xs">Capital Inquiry</a>
        </div>
    </nav>"""


footer_template = """<footer class="py-24 bg-onyx text-white border-t-8 border-gold px-8 relative z-50">
        <div class="max-w-[1800px] mx-auto grid md:grid-cols-2 lg:grid-cols-4 gap-20">
            <div>
                <span class="text-4xl font-header font-black tracking-tighter uppercase mb-8 block italic">Aurum <span class="text-gold">Legacy.</span></span>
                <p class="text-zinc-500 text-sm leading-relaxed mb-10 font-medium">Protecting the digital empires of tomorrow through rigorous engineering and gold-standard strategy. Est. 2012.</p>
                <div class="h-2 w-20 bg-gold"></div>
            </div>
            
            <div class="space-y-6">
                <h6 class="text-gold uppercase text-[10px] font-black tracking-[0.5em] mb-10">Systems & Services</h6>
                <a href="{services_link}#java" class="block text-zinc-400 hover:text-white hover:text-gold transition uppercase text-[11px] font-bold">Java Enterprise Core</a>
                <a href="{services_link}#flutter" class="block text-zinc-400 hover:text-white hover:text-gold transition uppercase text-[11px] font-bold">Flutter Mobile Apps</a>
                <a href="{services_link}#fintech" class="block text-zinc-400 hover:text-white hover:text-gold transition uppercase text-[11px] font-bold">Fintech Gateway Build</a>
                <a href="{services_link}#ai" class="block text-zinc-400 hover:text-white hover:text-gold transition uppercase text-[11px] font-bold">Generative AI LLM-Hub</a>
            </div>

            <div class="space-y-6">
                <h6 class="text-gold uppercase text-[10px] font-black tracking-[0.5em] mb-10">Protocols & Policies</h6>
                <a href="{privacy_link}" class="block text-zinc-400 hover:text-white hover:text-gold transition uppercase text-[11px] font-bold">Privacy Policy</a>
                <a href="{terms_link}" class="block text-zinc-400 hover:text-white hover:text-gold transition uppercase text-[11px] font-bold">Terms of Engagement</a>
                <a href="{contact_link}" class="block text-zinc-400 hover:text-white hover:text-gold transition uppercase text-[11px] font-bold">Capital Inquiry</a>
                <a href="{about_link}" class="block text-zinc-400 hover:text-white hover:text-gold transition uppercase text-[11px] font-bold">Our Mission</a>
            </div>

            <div>
                <h6 class="text-gold uppercase text-[10px] font-black tracking-[0.5em] mb-10">Direct Contact Relay</h6>
                <p class="text-xs text-zinc-500 mb-6 font-bold italic">Speak directly with Founder & CEO</p>
                <ul class="text-zinc-400 space-y-4 font-bold text-[11px] uppercase tracking-widest">
                    <li><i class="fas fa-phone text-gold mr-3"></i> +91 9304514787</li>
                    <li><i class="fas fa-envelope text-gold mr-3"></i> abhishek@auramlegacy.com</li>
                    <li><i class="fab fa-whatsapp text-gold mr-3"></i> +91 9304514787</li>
                    <li><i class="fas fa-building text-gold mr-3"></i> Gurugram HQ, India</li>
                </ul>
            </div>
        </div>
        
        <div class="max-w-[1800px] mx-auto mt-32 pt-10 border-t border-zinc-900 text-[9px] uppercase font-black tracking-[0.4em] text-zinc-600 text-center flex flex-col sm:flex-row justify-between items-center gap-6">
            <span>&copy; 2026 Aurum Global Holdings LLC. Built for Immortality.</span>
            <span class="text-gold tracking-widest leading-loose bg-onyx px-4 py-2 border border-gold/20 shadow-lg">FOUNDER & CEO: ABHISHEK KUMAR | +91 9304514787</span>
        </div>
    </footer>"""

js_injection = """
    <script>
        // Mobile Menu Toggle Logic
        document.addEventListener('DOMContentLoaded', () => {
            const btn = document.getElementById('mobile-menu-btn');
            const menu = document.getElementById('mobile-menu');
            if (btn && menu) {
                btn.addEventListener('click', () => {
                    menu.classList.toggle('hidden');
                    menu.classList.toggle('flex');
                    
                    const icon = btn.querySelector('i');
                    if (menu.classList.contains('flex')) {
                        icon.classList.remove('fa-bars');
                        icon.classList.add('fa-times');
                    } else {
                        icon.classList.remove('fa-times');
                        icon.classList.add('fa-bars');
                    }
                });
            }
        });
    </script>
"""

def process_file(filepath, is_index):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Nav
        nav = nav_template.format(
            home_link="index.html" if is_index else "../index.html",
            desktop_links=desktop_nav_index if is_index else desktop_nav_sub,
            mobile_links=mobile_nav_index if is_index else mobile_nav_sub,
            contact_link=contact_link_index if is_index else contact_link_sub
        )
        content = re.sub(r'<nav.*?</nav>', nav, content, flags=re.DOTALL)

        # Update Footer
        footer = footer_template.format(
            services_link="pages/services.html" if is_index else "services.html",
            privacy_link="pages/privacy.html" if is_index else "privacy.html",
            terms_link="pages/terms.html" if is_index else "terms.html",
            contact_link="pages/contact.html" if is_index else "contact.html",
            about_link="pages/about.html" if is_index else "about.html"
        )
        content = re.sub(r'<footer.*?</footer>', footer, content, flags=re.DOTALL)
        
        # Inject JS if not already injected
        if 'Mobile Menu Toggle Logic' not in content:
            content = content.replace('</body>', js_injection + '\n</body>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        print(f"Error on {filepath}: {e}")

# Process index
process_file('index.html', True)

# Process subpages
subpages = ['pages/about.html', 'pages/services.html', 'pages/portfolio.html', 'pages/contact.html', 'pages/careers.html', 'pages/privacy.html', 'pages/terms.html']
for p in subpages:
    process_file(p, False)

print("Nav and Footer massively overhauled for mobile responsiveness and robust links.")
