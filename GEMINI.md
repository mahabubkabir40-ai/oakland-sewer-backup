# Oakland Sewer Pros – Workspace Agent Directives & Project Rules

> **CRITICAL INSTRUCTION FOR ALL AGENTS & SESSIONS:**
> This project (`oaklandsewerpros.com`) is an active, production lead-generation asset.
> You MUST read and strictly adhere to these directives on EVERY turn. For complete historical logs, keyword mappings, and roadmap, consult `PROJECT_STATUS_AND_ROADMAP.md`.

---

## 1. Business Model & Monetization
- **Primary Goal:** Generate qualified emergency water/sewer disaster calls in Oakland County, MI to hit $200–$400/month in early stages, scaling with storm seasons.
- **Affiliate Partner:** Marketcall (Offer 8915, Campaign 356406).
- **Payout:** $64 to $1,280 per qualified inbound call (>60–90s connected).
- **Sole Phone Number:** `(248) 825-8312` (`tel:2488258312`).
- **Required Footer Disclaimer:** Marketcall Offer 8915 mandatory legal text MUST remain in the footer across all 50 indexable pages.

---

## 2. Cardinal Operating Directives (Non-Negotiable)

### Directive 1: Zero Phone Leakage
- **NEVER** re-introduce any municipal, police, or city department phone numbers (e.g., Troy Water Division, Troy Police, Royal Oak DPS, Berkley DPW, Clawson DPW) into money pages or hubs.
- Every phone number on the page that is not `(248) 825-8312` leaks revenue and loses leads.
- `<meta name="format-detection" content="telephone=no">` must stay in `<head>` on all pages to prevent mobile browsers from auto-linking plain digits.

### Directive 2: Title & Meta Description Discipline
- Every money page meta description **MUST** frontload the phone number: `Call (248) 825-8312 for 24/7...`
- Length Constraint: **Strictly between 140 and 155 characters**. `build.py` enforces assertions.
- Titles must feature high-intent, 24/7 emergency phrasing (e.g., `24/7 Water Damage Restoration Troy MI | Water Damage Repair`).

### Directive 3: Build & Deployment Workflow
- The site is built with a custom Python static site generator (`generate_site.py` & `sitegen/*.py`).
- **Always build before deploying:** Run `python build.py` to regenerate all HTML files in root and `public/`.
- **Always push to live:** Cloudflare Pages only updates upon `git push origin main`. A change is NOT live until it is pushed to `origin/main`.

### Directive 4: Linking Structure
- Internal links: maintain the 63–70 link silo mesh on every page (service drop-downs, nearby cities, hubs).
- External citations: ALL external URLs must use `target="_blank" rel="noopener noreferrer"`.
- Resource guides must prominently display emergency extraction callouts pointing to money pages.

---

## 3. Current Project Status (Updated Nov 15, 2026)
- **All 36 Money Pages:** 100% optimized with GSC keywords, 24/7 titles, frontloaded meta descriptions, and zero phone leakage.
- **Sitemap:** `sitemap.xml` updated with `<lastmod>2026-11-14</lastmod>` for all 50 URLs.
- **GSC Indexing Submissions:** 11 priority money pages manually submitted to Google Search Console (Batch 1: 5 URLs, Batch 2: 6 URLs - daily quota hit).
- **Current Milestone:** Monitor GSC crawl timestamp updates and keyword ranking movement (positions 10–30 into top 3).
