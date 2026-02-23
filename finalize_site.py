import os
import re

# 1. Update the base index.html content (mainly fixing footer and Tech Stack to emphasize Java & Flutter)
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Update Footer to include proper links for Privacy and Terms
new_footer = """
    <!-- 11. MEGA FOOTER -->
    <footer class="py-24 bg-onyx text-white border-t-8 border-gold px-8">
        <div class="max-w-[1800px] mx-auto grid md:grid-cols-2 lg:grid-cols-4 gap-20">
            <div>
                <span class="text-4xl font-header font-black tracking-tighter uppercase mb-8 block italic">Aurum <span class="text-gold">Legacy.</span></span>
                <p class="text-zinc-500 text-sm leading-relaxed mb-10 font-medium">Protecting the digital empires of tomorrow through rigorous engineering and gold-standard strategy. Est. 2012.</p>
                <div class="h-2 w-20 bg-gold"></div>
            </div>
            
            <div class="space-y-6">
                <h6 class="text-gold uppercase text-[10px] font-black tracking-[0.5em] mb-10">Systems</h6>
                <a href="pages/services.html" class="block text-zinc-400 hover:text-white transition uppercase text-[11px] font-bold">Java Enterprise Core</a>
                <a href="pages/services.html" class="block text-zinc-400 hover:text-white transition uppercase text-[11px] font-bold">Flutter Mobile Apps</a>
                <a href="pages/services.html" class="block text-zinc-400 hover:text-white transition uppercase text-[11px] font-bold">Fintech Gateway Build</a>
                <a href="pages/services.html" class="block text-zinc-400 hover:text-white transition uppercase text-[11px] font-bold">Generative AI LLM-Hub</a>
            </div>

            <div class="space-y-6">
                <h6 class="text-gold uppercase text-[10px] font-black tracking-[0.5em] mb-10">Protocols</h6>
                <a href="pages/privacy.html" class="block text-zinc-400 hover:text-white transition uppercase text-[11px] font-bold">Privacy Policy</a>
                <a href="pages/terms.html" class="block text-zinc-400 hover:text-white transition uppercase text-[11px] font-bold">Terms of Engagement</a>
                <a href="#" class="block text-zinc-400 hover:text-white transition uppercase text-[11px] font-bold">Cyber Resilience Law</a>
                <a href="#" class="block text-zinc-400 hover:text-white transition uppercase text-[11px] font-bold">Ethics in Engineering</a>
            </div>

            <div>
                <h6 class="text-gold uppercase text-[10px] font-black tracking-[0.5em] mb-10">Subscription Relay</h6>
                <p class="text-xs text-zinc-500 mb-6 font-bold italic">Get monthly high-tech engineering insights directly into your terminal.</p>
                <div class="flex">
                    <input type="email" placeholder="TERM: EMAIL_ADDR" class="w-full p-4 bg-zinc-900 border border-zinc-800 outline-none text-[10px] font-black">
                    <button class="bg-gold p-4 text-onyx px-8 font-black">JOIN</button>
                </div>
            </div>
        </div>
        
        <div class="max-w-[1800px] mx-auto mt-32 pt-10 border-t border-zinc-900 text-[9px] uppercase font-black tracking-[0.4em] text-zinc-600 text-center flex flex-col sm:flex-row justify-between items-center gap-4">
            <span>&copy; 2024 Aurum Global Holdings LLC. Built for Immortality. [ST_ACTIVE_RELAY]</span>
            <span class="text-gold tracking-widest leading-loose">FOUNDER & CEO: ABHISHEK KUMAR | +91 9304514787</span>
        </div>
    </footer>
"""
# Replace existing footer
html_content = re.sub(r'<!-- 11\. MEGA FOOTER -->.*</footer>', new_footer.strip(), html_content, flags=re.DOTALL)

# Update Tech stack icons in index.html to emphasize Java and Flutter
html_content = html_content.replace('<i class="fab fa-rust text-5xl text-gold group-hover:text-onyx"></i>\n                    <span class="font-bold uppercase text-[10px] tracking-widest">Rust Speed</span>', '<i class="fab fa-java text-5xl text-gold group-hover:text-onyx"></i>\n                    <span class="font-bold uppercase text-[10px] tracking-widest">Java SpringBoot</span>')
html_content = html_content.replace('<i class="fab fa-swift text-5xl text-gold group-hover:text-onyx"></i>\n                    <span class="font-bold uppercase text-[10px] tracking-widest">Swift & Apple</span>', '<i class="fas fa-mobile-alt text-5xl text-gold group-hover:text-onyx"></i>\n                    <span class="font-bold uppercase text-[10px] tracking-widest">Flutter Dart</span>')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Re-create subpages using the updated index.html as a template
subpages = ['pages/about.html', 'pages/services.html', 'pages/portfolio.html', 'pages/contact.html', 'pages/careers.html', 'pages/privacy.html', 'pages/terms.html']
for page in subpages:
    # Get index html
    page_content = html_content
    # Fix internal links on subpages
    page_content = page_content.replace('href="pages/', 'href="')
    page_content = page_content.replace('href="#', 'href="../index.html#')
    page_content = page_content.replace('<a href="index.html" class="flex items-center space-x-4 cursor-pointer">', '<a href="../index.html" class="flex items-center space-x-4 cursor-pointer">')
    
    # Save base temp page
    with open(page, 'w', encoding='utf-8') as f:
        f.write(page_content)

def update_page_injection(filepath, new_content):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'(<!-- 2\. HERO SECTION 4\.0 -->).*?(<!-- 11\. MEGA FOOTER -->)', re.DOTALL)
    new_html = r'\1\n' + new_content + r'\n    \2'
    content = pattern.sub(new_html, content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# --- ABOUT PAGE CONTENT (CEO ABHISHEK KUMAR) ---
about_content = """
    <section class="py-32 bg-white dark:bg-onyx flex-grow min-h-screen pt-40">
        <div class="max-w-7xl mx-auto px-8 lg:px-16">
            <div class="text-center mb-20">
                <span class="text-gold font-bold uppercase tracking-[0.6em] text-[10px] mb-4 block">The Visionary</span>
                <h1 class="text-6xl md:text-8xl font-header font-black leading-tight mb-8">
                    Abhishek <span class="text-gold italic">Kumar</span>
                </h1>
                <p class="text-xl text-zinc-500 max-w-3xl mx-auto font-ui uppercase tracking-widest">
                    Founder & CEO | Architecting the Next Gen Indian IT Enterprise
                </p>
                <div class="mt-8 flex justify-center space-x-6">
                    <span class="px-6 py-2 border border-gold/30 text-gold text-sm font-bold tracking-widest uppercase">Java Enterprise Specialist</span>
                    <span class="px-6 py-2 border border-gold/30 text-gold text-sm font-bold tracking-widest uppercase">Flutter Innovator</span>
                </div>
            </div>

            <div class="grid lg:grid-cols-2 gap-20 items-center">
                <div class="relative">
                    <div class="absolute inset-0 bg-gold translate-x-4 translate-y-4 shadow-2xl z-[-1]"></div>
                    <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&q=80&w=800" alt="Tech Founder" class="w-full h-[600px] object-cover grayscale hover:grayscale-0 transition-all duration-700">
                    <div class="absolute bottom-6 left-6 bg-onyx text-white p-6 border-l-4 border-gold">
                        <p class="font-bold text-xs uppercase tracking-widest opacity-70">Direct Relay</p>
                        <p class="text-2xl font-black mt-2">+91 9304514787</p>
                    </div>
                </div>
                
                <div class="space-y-8">
                    <h3 class="text-4xl font-black uppercase text-onyx dark:text-white">Redefining Tech Ecosystems</h3>
                    <p class="text-zinc-500 dark:text-zinc-400 leading-relaxed text-lg">
                        Our journey began with a simple but profound ethos: to deliver "Engineering Craftsmanship" to the global market right from the heart of India. Under the leadership of Abhishek Kumar, Aurum Legacy has grown into a formidable force in custom software development.
                    </p>
                    <p class="text-zinc-500 dark:text-zinc-400 leading-relaxed text-lg">
                        Unlike traditional "body-shopping" IT firms, we operate as elite digital commandos. We specialize in high-transaction Java backend systems, heavily encrypted financial pipelines, and pixel-perfect Flutter hybrid applications that scale dynamically to millions of active users.
                    </p>
                    
                    <div class="grid grid-cols-2 gap-8 pt-8 border-t border-gold/20">
                        <div>
                            <span class="text-4xl font-header font-black text-gold block mb-2">1M+</span>
                            <span class="text-xs font-bold uppercase tracking-widest opacity-60">Lines of Code Deployed</span>
                        </div>
                        <div>
                            <span class="text-4xl font-header font-black text-gold block mb-2">99.9%</span>
                            <span class="text-xs font-bold uppercase tracking-widest opacity-60">Uptime on Core Systems</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="mt-32 p-16 bg-softGrey dark:bg-slateDark border border-gold/10 text-center shadow-xl">
                <i class="fas fa-quote-left text-4xl text-gold mb-6 opacity-50"></i>
                <h4 class="text-3xl font-header font-black italic max-w-4xl mx-auto leading-relaxed">
                    "We do not just write code or deliver generic products. We engineer digital sovereignty. When a business partners with us, they do not get a vendor—they get a vanguard protecting their digital future."
                </h4>
                <p class="mt-8 font-bold uppercase tracking-widest text-gold text-xs">— Abhishek Kumar, CEO</p>
            </div>
        </div>
    </section>
"""

# --- SERVICES CONTENT (Emphasize Java and Flutter) ---
services_content = """
    <section class="py-32 bg-softGrey dark:bg-onyx flex-grow min-h-screen pt-40">
        <div class="max-w-[1400px] mx-auto px-8 lg:px-16 text-center">
            <span class="text-gold font-bold uppercase tracking-[0.6em] text-[10px] mb-4 block">Our Offerings</span>
            <h1 class="text-6xl md:text-8xl font-header font-black leading-tight mb-20 uppercase">Core <span class="text-gold italic">Expertise</span></h1>
            
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 text-left">
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift relative overflow-hidden group">
                    <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-100 transition duration-500 text-6xl text-gold"><i class="fab fa-java"></i></div>
                    <i class="fas fa-microchip text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">Java Enterprise Engineering</h4>
                    <p class="text-zinc-500">Massively scalable Spring Boot microservices, high-throughput JVM architectures, and bulletproof security for banking & retail logistics.</p>
                </div>
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift relative overflow-hidden group">
                    <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-100 transition duration-500 text-6xl text-gold">FL</div>
                    <i class="fas fa-mobile-screen text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">Flutter Hybrid Apps</h4>
                    <p class="text-zinc-500">Premium interfaces deployed natively on iOS & Android using the Flutter framework and Dart. Guaranteed 60FPS with custom gesture integrations.</p>
                </div>
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift">
                    <i class="fas fa-server text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">Cloud & DevOps</h4>
                    <p class="text-zinc-500">AWS, Azure, and Google Cloud infrastructure setups optimized for scale, CI/CD pipelines, Docker, Kubernetes, and zero downtime.</p>
                </div>
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift">
                    <i class="fas fa-robot text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">AI Integration Labs</h4>
                    <p class="text-zinc-500">Automate your business processes using Fine-Tuned LLMs, Machine Learning, and NLP models deployed via fast Python APIs.</p>
                </div>
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift">
                    <i class="fas fa-vault text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">FinTech Core Solutions</h4>
                    <p class="text-zinc-500">Building compliant, encrypted payment gateways, trading platforms, and banking ledger systems using the strongest cryptographic standards.</p>
                </div>
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift">
                    <i class="fas fa-magnifying-glass-chart text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">Data Analytics</h4>
                    <p class="text-zinc-500">Uncover deep market insights through structured data lakes, realtime pipeline analytics, and intuitive dashboard visualization.</p>
                </div>
            </div>
        </div>
    </section>
"""

# --- CONTACT CONTENT (Update Phone Number & Name) ---
contact_content = """
    <section class="py-32 bg-white dark:bg-onyx flex-grow min-h-screen pt-40">
        <div class="max-w-7xl mx-auto px-8 lg:px-16 text-center">
            <span class="text-gold font-bold uppercase tracking-[0.6em] text-[10px] mb-4 block">Initialization</span>
            <h1 class="text-6xl md:text-8xl font-header font-black leading-tight mb-20">Contact <span class="text-gold italic">Command</span></h1>
            
            <div class="grid lg:grid-cols-2 gap-20 text-left">
                <div class="p-12 border-4 border-gold bg-softGrey dark:bg-slateDark relative shadow-2xl">
                    <h3 class="text-4xl font-black uppercase mb-10">Send a Project Dossier</h3>
                    <form class="space-y-8">
                        <div>
                            <label class="block text-[10px] uppercase font-bold tracking-widest text-gold mb-2">Your Name</label>
                            <input type="text" placeholder="John Doe" class="w-full p-4 bg-transparent border-b-2 border-zinc-300 dark:border-zinc-800 focus:border-gold outline-none text-lg">
                        </div>
                        <div>
                            <label class="block text-[10px] uppercase font-bold tracking-widest text-gold mb-2">Company Email</label>
                            <input type="email" placeholder="john@enterprise.com" class="w-full p-4 bg-transparent border-b-2 border-zinc-300 dark:border-zinc-800 focus:border-gold outline-none text-lg">
                        </div>
                        <div>
                            <label class="block text-[10px] uppercase font-bold tracking-widest text-gold mb-2">Transmission Message (Budget, Deadline, Java/Flutter Req)</label>
                            <textarea rows="4" placeholder="How can we help you scale your digital infrastructure?" class="w-full p-4 bg-transparent border-b-2 border-zinc-300 dark:border-zinc-800 focus:border-gold outline-none text-lg"></textarea>
                        </div>
                        <button type="button" class="w-full py-6 bg-onyx text-white hover:bg-gold hover:text-onyx uppercase font-black tracking-widest transition">Initialize Contact</button>
                    </form>
                </div>
                
                <div class="space-y-16 py-10">
                    <div>
                        <h4 class="text-xl font-bold uppercase tracking-widest text-gold mb-4">India Hub (HQ)</h4>
                        <p class="text-3xl font-header font-black">Cyber Hub, Level 4<br>Gurugram, Haryana</p>
                        <p class="text-zinc-500 mt-4 font-ui uppercase tracking-widest text-sm">+91 9304514787</p>
                    </div>
                    <div>
                        <h4 class="text-xl font-bold uppercase tracking-widest text-gold mb-4">Founder Direct Relay</h4>
                        <p class="text-3xl font-header font-black">Abhishek Kumar</p>
                        <p class="text-zinc-500 mt-4 font-ui uppercase tracking-widest text-sm text-gold">CEO & Lead Java/Flutter Architect</p>
                        <p class="text-zinc-500 mt-4 font-ui uppercase tracking-widest text-sm">+91 9304514787 (WhatsApp/Call)</p>
                        <p class="text-zinc-500 mt-2 font-ui uppercase tracking-widest text-sm">abhishek@auramlegacy.com</p>
                    </div>
                    
                    <div class="flex space-x-8 text-3xl text-gold pt-10 border-t border-zinc-200 dark:border-zinc-800">
                        <a href="https://linkedin.com/in/" target="_blank" class="hover:scale-125 transition"><i class="fab fa-linkedin"></i></a>
                        <a href="https://github.com/codewithabhi001" target="_blank" class="hover:scale-125 transition"><i class="fab fa-github"></i></a>
                        <a href="#" class="hover:scale-125 transition"><i class="fab fa-twitter"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

privacy_content = """
    <section class="py-32 bg-white dark:bg-onyx flex-grow min-h-screen pt-40">
        <div class="max-w-4xl mx-auto px-8 lg:px-16 text-left">
            <h1 class="text-6xl font-header font-black leading-tight mb-8">Privacy <span class="text-gold italic">Policy</span></h1>
            <div class="text-lg text-zinc-500 dark:text-zinc-400 space-y-6 leading-relaxed">
                <p>Welcome to Aurum Legacy's Privacy Policy. Authored under the supervision of Abhishek Kumar (CEO).</p>
                <h3 class="text-2xl font-bold text-onyx dark:text-white mt-12 mb-4">1. Information Collection</h3>
                <p>We collect essential corporate information when you initiate contact regarding Java, Flutter, or Enterprise architecture projects. This includes company name, email address, phone numbers (e.g. +91 9304514787 communications), and project briefs.</p>
                <h3 class="text-2xl font-bold text-onyx dark:text-white mt-12 mb-4">2. Non-Disclosure Clause</h3>
                <p>We operate as a high-security tactical IT unit. Any code, architecture blueprints, or competitive information shared with Aurum Legacy is strictly protected under Indian NDA and International IP laws.</p>
                <h3 class="text-2xl font-bold text-onyx dark:text-white mt-12 mb-4">3. Cookie Data Analytics</h3>
                <p>Our web terminal captures anonymous interaction analytics to optimize the UI/UX performance, reflecting the exact standards we code into our client's applications.</p>
                <p class="mt-20 border-t border-gold/20 pt-8 text-xs uppercase tracking-widest">Last Updated: 2026 | Governing Body: India HQ</p>
            </div>
        </div>
    </section>
"""

terms_content = """
    <section class="py-32 bg-white dark:bg-onyx flex-grow min-h-screen pt-40">
        <div class="max-w-4xl mx-auto px-8 lg:px-16 text-left">
            <h1 class="text-6xl font-header font-black leading-tight mb-8">Terms of <span class="text-gold italic">Engagement</span></h1>
            <div class="text-lg text-zinc-500 dark:text-zinc-400 space-y-6 leading-relaxed">
                <p>By engaging with Aurum Legacy, you agree to our rigorous terms of engineering deployment.</p>
                <h3 class="text-2xl font-bold text-onyx dark:text-white mt-12 mb-4">Service Acceptance & Sprints</h3>
                <p>We execute projects primarily utilizing Java backend systems, scalable cloud infrastructure, and cross-platform native-feeling applications built in Flutter. We maintain full intellectual property rights over underlying library structures unless specifically contractually relinquished via full acquisition.</p>
                <h3 class="text-2xl font-bold text-onyx dark:text-white mt-12 mb-4">Communication Vectors</h3>
                <p>All official correspondences are to be validated through the primary relay node overseen by our Founder, Abhishek Kumar. Urgent operations can be directed to +91 9304514787.</p>
                <h3 class="text-2xl font-bold text-onyx dark:text-white mt-12 mb-4">Liability Caps</h3>
                <p>Aurum Legacy executes robust unit and integration testing; however, liability for critical systems failure post-deployment handover is limited according to mutually signed SLA and Indian jurisdictional law.</p>
            </div>
        </div>
    </section>
"""

# Portfolio needs to remain as is or just read from the previous content
# Careers needs to remain as is or just read from the previous content
# I'll just write an empty replacement for Portfolio and Careers so they stay intact? No, wait, if I use the injection, I am REPLACING it. So I need to retain them or hardcode them here.
with open('pages/portfolio.html', 'r', encoding='utf-8') as f:
    pt_cont = f.read()
    portfolio_injection = re.search(r'(<section.*?)</section>\s*<!-- 11', pt_cont, re.DOTALL)
    if portfolio_injection:
        portfolio_content = portfolio_injection.group(1) + '</section>'
    else:
        portfolio_content = ''

with open('pages/careers.html', 'r', encoding='utf-8') as f:
    c_cont = f.read()
    careers_injection = re.search(r'(<section.*?)</section>\s*<!-- 11', c_cont, re.DOTALL)
    if careers_injection:
        careers_content = careers_injection.group(1) + '</section>'
    else:
        careers_content = ''


update_page_injection('pages/about.html', about_content)
update_page_injection('pages/services.html', services_content)
update_page_injection('pages/contact.html', contact_content)
update_page_injection('pages/privacy.html', privacy_content)
update_page_injection('pages/terms.html', terms_content)

if portfolio_content:
    update_page_injection('pages/portfolio.html', portfolio_content)
if careers_content:
    update_page_injection('pages/careers.html', careers_content)

print("Final structural updates applied.")
