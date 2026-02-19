# 🚀 PRE-LAUNCH CHECKLIST - newlens.uk

**DO NOT LAUNCH WITHOUT COMPLETING THIS LIST**

Created: 2026-02-19
Status: PENDING

---

## 🔴 CRITICAL - MUST DO BEFORE GO-LIVE

### 1. ✅ Legal Compliance
- [x] Cookie consent banner (live)
- [x] Terms of Service (live)
- [x] Privacy Policy (exists)
- [x] Registered company address (all pages)
- [ ] **ICO Registration Number** - Awaiting (applied, "ICO: TBC" placeholder on all pages)

### 2. 🔍 SEO REVIEW & SETUP
- [ ] **FULL SEO REVIEW** - Meta descriptions, titles, keywords across all 13 pages
- [ ] Confirm production domain (newlens.uk? www.newlens.uk?)
- [ ] Generate complete sitemap.xml (all 13 pages + articles)
- [ ] Update all hardcoded URLs (replace Vercel URLs with production domain)
- [ ] Verify schema markup (homepage, articles, business info)
- [ ] Submit sitemap to Google Search Console
- [ ] Verify robots.txt (test site blocked, prod site open)
- [ ] Check internal links (all relative links working)
- [ ] Verify canonical URLs
- [ ] Test social media preview cards (Open Graph tags)

### 3. 🧪 Assessment Backend
- [ ] n8n workflow imported and configured
- [ ] API keys configured (OpenRouter, HubSpot, SMTP)
- [ ] LLM testing (Kimi K2.5 report generation)
- [ ] Email templates tested (Email 0 + Email 1)
- [ ] PDF generation tested
- [ ] End-to-end testing (6 UAT scenarios)
- [ ] Escalation logic tested
- [ ] Alpha Partner form webhook fixed

### 4. ✅ Forms Testing
- [x] Contact form (functional)
- [x] Assessment form frontend (functional)
- [ ] Assessment form backend (blocked - needs n8n)
- [x] Alpha Partner form frontend (functional)
- [ ] Alpha Partner form backend (webhook broken)

### 5. 📅 Integrations
- [ ] Calendly setup (Mat to configure, 14-day Pro trial)
- [ ] Calendly booking link added to site (4 locations: nav, hero, footer, contact page)
- [ ] HubSpot connected (for assessment lead capture)

### 6. 🎨 Content Review
- [x] No fictitious testimonials
- [x] No fake case studies
- [x] No unsourced statistics
- [ ] Blog Article 1 reviewed by Mat
- [ ] Blog Article 2 reviewed by Mat
- [ ] All copy proofread
- [ ] Images optimized

---

## 🟡 HIGH PRIORITY - RECOMMENDED BEFORE LAUNCH

### 7. 📱 Cross-Browser/Device Testing
- [ ] Chrome (desktop + mobile)
- [ ] Safari (desktop + mobile)
- [ ] Firefox (desktop)
- [ ] Edge (desktop)
- [ ] Mobile responsiveness verified
- [ ] Navigation/mobile menu tested

### 8. 🔗 Link Verification
- [ ] All internal links working
- [ ] All external links working (Portal, LinkedIn, etc.)
- [ ] Email links working (info@newlens.uk, mailto: links)
- [ ] Footer links consistent across all pages
- [ ] No broken links (run link checker)

### 9. 🎯 Analytics & Tracking
- [ ] Decide on Google Analytics (yes/no)
- [ ] If yes: Configure GA4
- [ ] If yes: Update cookie consent banner with GA toggle
- [ ] Test cookie consent accept/reject flow

---

## 🟢 NICE TO HAVE - POST-LAUNCH ACCEPTABLE

### 10. 📊 Performance
- [ ] Run Lighthouse audit
- [ ] Optimize images if needed
- [ ] Check page load times
- [ ] Verify favicon on all pages

### 11. 🏆 Social Proof
- [ ] JGTA testimonial (awaiting response)
- [ ] Insite M&A testimonial (awaiting response)
- [ ] First Alpha partner testimonial (after onboarding)

### 12. 🎓 MBCS Credential
- [x] Added to About page
- [ ] Mat to add to LinkedIn
- [ ] Mat to add to email signature

---

## 📋 LAUNCH DAY CHECKLIST

When you say "GO LIVE":

1. [ ] Replace test URLs with production domain (global find/replace)
2. [ ] Update sitemap.xml with production URLs
3. [ ] Verify DNS pointing to correct host
4. [ ] Update robots.txt sitemap line with production URL
5. [ ] Submit sitemap to Google Search Console
6. [ ] Test all forms on live domain
7. [ ] Verify SSL certificate
8. [ ] Test cookie banner on live domain
9. [ ] Send test contact form submission
10. [ ] Post launch announcement (LinkedIn?)

---

## 🚫 BLOCKERS

**Cannot Launch Until:**
1. ICO registration number received (or accept "ICO: TBC" placeholder)
2. **SEO REVIEW COMPLETE** ⚠️
3. Assessment backend complete OR decision to launch with frontend only (no promotion)
4. Production domain confirmed

---

## 📝 NOTES

- Test site (website-test) is blocked from indexing ✅
- Prod site (website-prod) ready but awaiting domain finalization
- All legacy pages deleted (assessment, calculator, case-studies, solutions) ✅
- Zero fictitious content (testimonials, case studies, statistics) ✅

---

**REMINDER:** Mat specifically requested SEO review not be forgotten! ⚠️

Last updated: 2026-02-19 09:40 AM
