import re

def update_page_content(filepath, new_content):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace everything from <!-- 2. HERO SECTION 4.0 --> to just before <!-- 11. MEGA FOOTER -->
    pattern = re.compile(r'(<!-- 2\. HERO SECTION 4\.0 -->).*?(<!-- 11\. MEGA FOOTER -->)', re.DOTALL)
    
    new_html = r'\1\n' + new_content + r'\n    \2'
    
    content = pattern.sub(new_html, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

about_content = """
    <section class="py-32 bg-white dark:bg-onyx flex-grow min-h-screen pt-40">
        <div class="max-w-7xl mx-auto px-8 lg:px-16 text-center">
            <h1 class="text-6xl md:text-8xl font-header font-black leading-tight mb-8">
                About <span class="text-gold italic">Aurum Legacy</span>
            </h1>
            <p class="text-xl text-zinc-500 max-w-3xl mx-auto mb-16 leading-relaxed">
                Founded by Abhishek, a visionary in the Indian IT space, Aurum Legacy is built to bring world-class engineering, digital strategy, and enterprise AI transformation directly to high-growth organizations.
            </p>
            <div class="grid md:grid-cols-2 gap-10 text-left mt-20">
                <div class="p-10 border border-gold/20 bg-softGrey dark:bg-slateDark shadow-lg">
                    <h3 class="text-3xl font-black uppercase mb-4 text-gold">The Founder's Vision</h3>
                    <p class="text-zinc-500 leading-relaxed mb-6">
                        Under the leadership of Abhishek, we aim to bridge the gap between traditional IT infrastructure and modern AI-driven cloud ecosystems. We are fundamentally transforming how Indian and Global businesses scale, securely and efficiently.
                    </p>
                </div>
                <div class="p-10 border border-gold/20 bg-softGrey dark:bg-slateDark shadow-lg">
                    <h3 class="text-3xl font-black uppercase mb-4 text-gold">Our Ethos</h3>
                    <p class="text-zinc-500 leading-relaxed mb-6">
                        We don't settle for "good enough". Whether it is cloud migration, hybrid mobile applications, or next-generation generative AI labs, we treat every project as a piece of digital craftsmanship.
                    </p>
                </div>
            </div>
            <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=1200" class="w-full h-[500px] object-cover mt-20 border-2 border-gold mx-auto grayscale hover:grayscale-0 transition-all duration-1000">
        </div>
    </section>
"""


services_content = """
    <section class="py-32 bg-softGrey dark:bg-onyx flex-grow min-h-screen pt-40">
        <div class="max-w-[1400px] mx-auto px-8 lg:px-16 text-center">
            <span class="text-gold font-bold uppercase tracking-[0.6em] text-[10px] mb-4 block">Our Offerings</span>
            <h1 class="text-6xl md:text-8xl font-header font-black leading-tight mb-20 uppercase">Core <span class="text-gold italic">Services</span></h1>
            
            <div class="grid md:grid-cols-3 gap-8 text-left">
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift">
                    <i class="fas fa-microchip text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">Enterprise Architecture</h4>
                    <p class="text-zinc-500">End-to-end custom software development designed for high traffic and maximum security.</p>
                </div>
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift">
                    <i class="fas fa-mobile-screen text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">Mobile & Hybrid Dev</h4>
                    <p class="text-zinc-500">Premium applications available on iOS & Android crafted with Flutter, React Native, and Swift.</p>
                </div>
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift">
                    <i class="fas fa-server text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">Cloud & DevOps</h4>
                    <p class="text-zinc-500">AWS, Azure, and Google Cloud infrastructure setups optimized for scale and zero downtime.</p>
                </div>
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift">
                    <i class="fas fa-robot text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">AI Integration Labs</h4>
                    <p class="text-zinc-500">Automate your business processes using Fine-Tuned LLMs, Machine Learning, and NLP models.</p>
                </div>
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift">
                    <i class="fas fa-vault text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">FinTech Core Solutions</h4>
                    <p class="text-zinc-500">Building compliant, encrypted payment gateways, trading platforms, and banking ledger systems.</p>
                </div>
                <div class="bg-white dark:bg-slateDark p-12 border border-gold/10 hover-lift">
                    <i class="fas fa-magnifying-glass-chart text-4xl text-gold mb-6"></i>
                    <h4 class="text-2xl font-black uppercase mb-4">Data Analytics</h4>
                    <p class="text-zinc-500">Uncover deep market insights through structured data lakes and realtime pipeline analytics.</p>
                </div>
            </div>
        </div>
    </section>
"""

portfolio_content = """
    <section class="py-32 bg-white dark:bg-onyx flex-grow min-h-screen pt-40">
        <div class="max-w-[1400px] mx-auto px-8 lg:px-16">
            <div class="text-center mb-20">
                <span class="text-gold font-bold uppercase tracking-[0.6em] text-[10px] mb-4 block">Proven Deployments</span>
                <h1 class="text-6xl md:text-8xl font-header font-black leading-tight mb-8 uppercase">Project <span class="text-gold italic">Portfolio</span></h1>
                <p class="text-xl text-zinc-500 max-w-2xl mx-auto">From Indian government tech portals to high-frequency private financial networks, view our global footprint.</p>
            </div>
            
            <div class="grid md:grid-cols-2 gap-12">
                <div class="group cursor-pointer">
                    <div class="overflow-hidden border border-gold/20 relative">
                        <img src="https://images.unsplash.com/photo-1563986768494-4dee2763ff0f?auto=format&fit=crop&q=80&w=800" class="w-full h-80 object-cover grayscale group-hover:grayscale-0 transition duration-700">
                    </div>
                    <div class="pt-6">
                        <span class="text-gold text-xs font-bold uppercase tracking-widest">Fintech / Indian Market</span>
                        <h3 class="text-3xl font-black uppercase mt-2">PayNet India Gateway</h3>
                        <p class="text-zinc-500 mt-4 leading-relaxed">A high-scale UPI integrated system capable of processing 1M daily transactions with zero failed states.</p>
                    </div>
                </div>
                <div class="group cursor-pointer">
                    <div class="overflow-hidden border border-gold/20 relative">
                        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=800" class="w-full h-80 object-cover grayscale group-hover:grayscale-0 transition duration-700">
                    </div>
                    <div class="pt-6">
                        <span class="text-gold text-xs font-bold uppercase tracking-widest">E-Commerce / SAAS</span>
                        <h3 class="text-3xl font-black uppercase mt-2">Bharat Mart Enterprise</h3>
                        <p class="text-zinc-500 mt-4 leading-relaxed">Built from scratch custom multi-vendor B2B platform with integrated ERP logistics and automated inventory tracking.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

careers_content = """
    <section class="py-32 bg-softGrey dark:bg-slateDark flex-grow min-h-screen pt-40">
        <div class="max-w-4xl mx-auto px-8 lg:px-16 text-center">
            <span class="text-gold font-bold uppercase tracking-[0.6em] text-[10px] mb-4 block">Join The Guild</span>
            <h1 class="text-6xl md:text-8xl font-header font-black leading-tight mb-8 uppercase">Our <span class="text-gold italic">Careers</span></h1>
            <p class="text-xl text-zinc-500 mx-auto mb-20 leading-relaxed">
                We are constantly looking for talented Indian engineers, innovators, and cloud architects who love solving hard systemic challenges.
            </p>
            
            <div class="space-y-6 text-left">
                <div class="p-10 bg-white dark:bg-onyx border border-gold/10 hover-lift cursor-pointer flex justify-between items-center group">
                    <div>
                        <span class="text-gold uppercase text-[10px] font-bold tracking-widest">Engineering - Remote</span>
                        <h3 class="text-2xl font-black mt-2 uppercase">Full Stack Developer (MERN)</h3>
                    </div>
                    <button class="bg-onyx text-white group-hover:bg-gold group-hover:text-onyx px-8 py-4 uppercase font-bold text-xs transition">Apply Now</button>
                </div>
                
                <div class="p-10 bg-white dark:bg-onyx border border-gold/10 hover-lift cursor-pointer flex justify-between items-center group">
                    <div>
                        <span class="text-gold uppercase text-[10px] font-bold tracking-widest">Cloud - Gurugram HQ</span>
                        <h3 class="text-2xl font-black mt-2 uppercase">Senior AWS Solutions Architect</h3>
                    </div>
                    <button class="bg-onyx text-white group-hover:bg-gold group-hover:text-onyx px-8 py-4 uppercase font-bold text-xs transition">Apply Now</button>
                </div>
                
                <div class="p-10 bg-white dark:bg-onyx border border-gold/10 hover-lift cursor-pointer flex justify-between items-center group">
                    <div>
                        <span class="text-gold uppercase text-[10px] font-bold tracking-widest">AI & Data - Hybrid</span>
                        <h3 class="text-2xl font-black mt-2 uppercase">Generative AI Engineer (Python/PyTorch)</h3>
                    </div>
                    <button class="bg-onyx text-white group-hover:bg-gold group-hover:text-onyx px-8 py-4 uppercase font-bold text-xs transition">Apply Now</button>
                </div>
            </div>
            <div class="mt-20 p-10 border-2 border-gold/30">
                <h4 class="font-header text-3xl font-black mb-4">Don't see a fit?</h4>
                <p class="text-zinc-500 mb-6 font-ui">Send your GitHub profile and resume directly to the founder.</p>
                <a href="mailto:abhishek@auramlegacy.com" class="text-gold font-bold uppercase tracking-widest border-b-2 border-gold pb-1 hover:text-white transition">Pitch Us Here</a>
            </div>
        </div>
    </section>
"""

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
                            <label class="block text-[10px] uppercase font-bold tracking-widest text-gold mb-2">Transmission Message</label>
                            <textarea rows="4" placeholder="How can we help you scale?" class="w-full p-4 bg-transparent border-b-2 border-zinc-300 dark:border-zinc-800 focus:border-gold outline-none text-lg"></textarea>
                        </div>
                        <button type="button" class="w-full py-6 bg-onyx text-white hover:bg-gold hover:text-onyx uppercase font-black tracking-widest transition">Initialize Contact</button>
                    </form>
                </div>
                
                <div class="space-y-16 py-10">
                    <div>
                        <h4 class="text-xl font-bold uppercase tracking-widest text-gold mb-4">India Hub (HQ)</h4>
                        <p class="text-3xl font-header font-black">Cyber Hub, Level 4<br>Gurugram, Haryana</p>
                        <p class="text-zinc-500 mt-4 font-ui uppercase tracking-widest text-sm">+91 98765 43210</p>
                    </div>
                    <div>
                        <h4 class="text-xl font-bold uppercase tracking-widest text-gold mb-4">Founder Direct Relay</h4>
                        <p class="text-3xl font-header font-black">Abhishek</p>
                        <p class="text-zinc-500 mt-4 font-ui uppercase tracking-widest text-sm">abhishek@auramlegacy.com</p>
                    </div>
                    
                    <div class="flex space-x-8 text-3xl text-gold pt-10 border-t border-zinc-200 dark:border-zinc-800">
                        <a href="#" class="hover:scale-125 transition"><i class="fab fa-linkedin"></i></a>
                        <a href="#" class="hover:scale-125 transition"><i class="fab fa-twitter"></i></a>
                        <a href="#" class="hover:scale-125 transition"><i class="fab fa-github"></i></a>
                        <a href="#" class="hover:scale-125 transition"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

update_page_content('pages/about.html', about_content)
update_page_content('pages/services.html', services_content)
update_page_content('pages/portfolio.html', portfolio_content)
update_page_content('pages/careers.html', careers_content)
update_page_content('pages/contact.html', contact_content)

print("All Subpages unique content updated successfully.")
