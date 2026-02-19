#!/usr/bin/env python3
import os
import glob

footer_template = '''<footer class="bg-nl-navy text-white py-12 mt-16">
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

# Process root HTML files
for file in glob.glob('*.html'):
    if file in ['FOOTER_MASTER_TEMPLATE.html', 'FOOTER_V3.html', 'FOOTER_INDEX_OLD.html']:
        continue
    
    with open(file, 'r') as f:
        content = f.read()
    
    # Remove existing footer if present
    if '<footer' in content:
        start = content.find('<footer')
        end = content.find('</footer>') + len('</footer>')
        content = content[:start] + content[end:]
    
    # Remove marker lines if present
    content = content.replace('FOOTER_START\n', '')
    content = content.replace('TEST_LINE\n', '')
    content = content.replace('FOOTER_START', '')
    content = content.replace('TEST_LINE', '')
    
    # Remove large gaps before the footer (common in some pages)
    # Using more aggressive regex-style cleaning for any amount of whitespace between tags
    import re
    content = re.sub(r'</section>\s+<footer', '</section><footer', content)
    content = re.sub(r'</div>\s+<footer', '</div><footer', content)
    content = re.sub(r'</main>\s+<footer', '</main><footer', content)
    
    # Insert footer before </body>
    footer = footer_template.format(root='', article_class='')
    content = content.replace('</body>', footer + '\n</body>')
    
    with open(file, 'w') as f:
        f.write(content)
    
    print(f'✓ Fixed {file}')

# Process articles
for file in glob.glob('articles/*.html'):
    with open(file, 'r') as f:
        content = f.read()
    
    # Remove existing footer if present
    if '<footer' in content:
        start = content.find('<footer')
        end = content.find('</footer>') + len('</footer>')
        content = content[:start] + content[end:]
    
    # Determine if this is the articles index
    article_class = ' text-nl-green' if 'articles/index.html' in file else ''
    
    # Insert footer before </body>
    footer = footer_template.format(root='../', article_class=article_class)
    content = content.replace('</body>', footer + '\n</body>')
    
    with open(file, 'w') as f:
        f.write(content)
    
    print(f'✓ Fixed {file}')

print('\n✅ All footers fixed!')
