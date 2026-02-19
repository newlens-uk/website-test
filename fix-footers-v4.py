#!/usr/bin/env python3
import os
import glob
import re

# V4 Footer - Removed mt-16 to eliminate the white gap
footer_template = '''<footer class="bg-nl-navy text-white py-12">
        <div class="max-w-7xl mx-auto px-6">
            <div class="grid md:grid-cols-4 gap-12 mb-16">
                <div class="col-span-2 md:col-span-1">
                    <div class="text-2xl font-black text-white mb-6 tracking-tighter">new<span class="text-nl-green">lens</span></div>
                    <p class="text-nl-slate text-sm leading-relaxed mb-4">Enterprise-grade automation and data clarity for UK SMEs. Based in Suffolk.</p>
                    <p class="text-nl-green text-xs font-semibold italic">Your journey from friction to flow.</p>
                    <p class="text-nl-teal text-xs font-bold">Co No. 16945634 | ICO: TBC</p>
                    <p class="text-nl-slate text-xs opacity-60 italic mt-1">Registered in England & Wales</p>
                </div>
                <div>
                    <h4 class="font-black uppercase tracking-widest text-xs mb-6">Platform</h4>
                    <ul class="space-y-4 text-sm">
                        <li><a href="{root}assessment-new.html" class="text-nl-slate hover:text-white transition-colors">AI Readiness Assessment</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-black uppercase tracking-widest text-xs mb-6">Company</h4>
                    <ul class="space-y-4 text-sm">
                        <li><a href="{root}about.html" class="text-nl-slate hover:text-white transition-colors">About</a></li>
                        <li><a href="{root}services.html" class="text-nl-slate hover:text-white transition-colors">Services</a></li>
                        <li><a href="{root}articles/index.html" class="text-nl-slate hover:text-white transition-colors{article_class}">Articles</a></li>
                        <li><a href="{root}qanda.html" class="text-nl-slate hover:text-white transition-colors">Q&A</a></li>
                        <li><a href="{root}contact.html" class="text-nl-slate hover:text-white transition-colors">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-black uppercase tracking-widest text-xs mb-6">Connect</h4>
                    <ul class="space-y-4 text-sm">
                        <li><a href="mailto:info@newlens.uk" class="text-nl-slate hover:text-white transition-colors">info@newlens.uk</a></li>
                        <li><a href="https://www.linkedin.com/company/newlens-uk" target="_blank" class="text-nl-slate hover:text-white transition-colors">LinkedIn</a></li>
                        <li><a href="{root}privacy.html" class="text-nl-slate hover:text-white transition-colors">Privacy Policy</a></li>
                        <li><a href="{root}terms.html" class="text-nl-slate hover:text-white transition-colors">Terms of Service</a></li>
                    </ul>
                </div>
            </div>
            <div class="pt-12 border-t border-white/5 text-center">
                <p class="text-nl-slate/60 text-xs mt-2"><strong>Registered company address:</strong><br>newlens limited, 2 Burghley Way, Littleover, Derby, DE23 4TD</p>
                <p class="text-nl-slate text-[10px] uppercase tracking-widest font-bold mt-4">© 2026 newlens. All Rights Reserved.</p>
            </div>
        </div>
    </footer>
'''

def fix_file(file_path, root_path, article_class=''):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # 1. Remove any existing footer
    content = re.sub(r'<footer.*?</footer>', '', content, flags=re.DOTALL)
    
    # 2. Clean up trailing whitespace and markers
    content = content.replace('FOOTER_START', '').replace('TEST_LINE', '')
    content = re.sub(r'\s+</body>', '\n</body>', content)
    
    # 3. Insert V4 Footer
    footer = footer_template.format(root=root_path, article_class=article_class)
    content = content.replace('</body>', footer + '\n</body>')
    
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Fixed {file_path}")

# Fix Root Files
for f in glob.glob('*.html'):
    if 'FOOTER' not in f:
        fix_file(f, '')

# Fix Articles
for f in glob.glob('articles/*.html'):
    a_class = ' text-nl-green' if 'index.html' in f else ''
    fix_file(f, '../', a_class)
