# Oakland Sewer Pros – Project State, Master Context & Next Steps Roadmap

> **Document Purpose:** This file serves as the single source of truth (SSOT) and persistent project memory for any AI agent or engineer continuing work on this lead generation asset across any session, account, or tool.

---

## 1. Project Identity & Business Model
- **Domain:** `https://oaklandsewerpros.com`
- **Hosting / Deployment:** Cloudflare Pages (connected via GitHub `main` branch to `https://github.com/mahabubkabir40-ai/oakland-sewer-backup.git`).
- **Niche:** Emergency Sewer Backup Cleanup, Flooded Basement Water Removal, Sewage Extraction, Sump Pump Repair, Basement Sanitization, and Water Damage Restoration.
- **Service Area:** Oakland County, Michigan (Focus on 5 Core Cities: Royal Oak, Troy, Birmingham, Berkley, Clawson).
- **Affiliate Monetization:** 
  - **Network:** Marketcall Pay-Per-Call
  - **Offer:** Offer 8915 (Campaign 356406)
  - **Payout:** $64 to $1,280 per qualified inbound call (based on duration, emergency scope, and service type).
  - **Revenue Target:** $200 – $400/month in early stages, scaling with storm seasons.
  - **Call Tracking Number:** `(248) 825-8312` (`tel:2488258312`).
  - **Legal Compliance:** Mandatory Marketcall Offer 8915 disclaimer in footer on all 50 indexable pages (independent contractors, actor depictions, no warranty).

---

## 2. GSC Performance Baseline (Audited Nov 2026)
- **Total Impressions (28-day):** 3,035 (+169% month-over-month growth).
- **Total Clicks:** 7 (Kuhn Drainage District: 3, Claim Guide: 3, Sump Pump: 1).
- **Average Position:** 36.1.
- **Top Striking-Distance Keywords (Positions 10.1 – 30.0):**
  - `troy mi water damage restoration` / `water damage restoration troy mi`
  - `royal oak sump pump repair` (Position 8.7)
  - `flooded basement cleanup troy mi` / `royal oak flooded basement`
  - `sewer backup cleanup near me` / `sewer backup cleanup troy mi`
  - `sewage extraction royal oak mi`

---

## 3. What Was Recently Completed & Deployed Live (Nov 14–15, 2026)
All 50 URLs (36 money/hub pages + 14 informational/city/utility pages) have been fully audited, rebuilt with `python build.py`, committed, pushed to `origin/main`, and deployed live on Cloudflare Pages:

1. **Zero Phone Leakage (100% Secured Conversion Channel):**
   - **Problem Solved:** Homeowners previously saw municipal phone numbers (Troy Water Division, Troy Police, Royal Oak DPS, Berkley DPW) and called city hall instead of our affiliate line.
   - **Fix:** ALL municipal telephone numbers were removed from the body copy and FAQs of all 36 money pages. The ONLY telephone number visible or clickable is `(248) 825-8312`.
   - **Mobile Protection:** `<meta name="format-detection" content="telephone=no">` was injected into the `<head>` of all 50 pages to prevent mobile Safari/Chrome regex auto-linking.
2. **Title Tag & Meta Description Optimization (36/36 Money Pages):**
   - **Titles:** High-CTR, 24/7 emergency phrasing (e.g., `24/7 Water Damage Restoration Troy MI | Water Damage Repair`).
   - **Descriptions:** Every money page meta description strictly frontloads the phone number (`Call (248) 825-8312 for 24/7...`) and stays strictly within 140–155 characters for flawless SERP rendering.
3. **On-Page Content & H1/H2 Optimization:**
   - Single distinct H1 on every page incorporating target city + primary GSC query.
   - High-converting hero introductory paragraph highlighting 30–45 minute local dispatch, emergency truck-mounted extraction, and direct insurance billing.
   - Added structured H2 headings matching GSC user search queries across all 6 service verticals.
4. **Internal & External Linking:**
   - Internal linking mesh active: each page has 63 to 70 internal links connecting city silos, sibling services, and parent hubs.
   - 3 Resource Guides (`/sewer-backup-claim-guide`, `/basement-flood-checklist`, `/george-w-kuhn-drainage-district`) now feature prominent emergency callout boxes directly linking to money pages.
   - All external citation links (Michigan Act 222, municipal portals, CDC, FEMA) use `target="_blank" rel="noopener noreferrer"`.
5. **Sitemap & Technical Verification:**
   - `sitemap.xml` updated with `<lastmod>2026-11-14</lastmod>` for all 50 URLs.
   - 100% of pages return HTTP `200 OK` from Cloudflare Edge.

---

## 4. Google Search Console (GSC) Re-Indexing Status
- **Sitemap Status:** `sitemap.xml` submitted and verified as `Success` with 50 discovered pages.
- **Manual "Request Indexing" Submissions:**
  - **Batch 1 (Nov 14):** 5 priority URLs submitted:
    1. `/troy-water-damage-restoration`
    2. `/royal-oak-water-damage-restoration`
    3. `/troy-flooded-basement`
    4. `/royal-oak-flooded-basement`
    5. `/sewer-backup-claim-guide`
  - **Batch 2 (Nov 15):** 6 priority URLs submitted:
    6. `/royal-oak-sump-pump-repair`
    7. `/royal-oak-sewer-cleanup`
    8. `/troy-sewer-cleanup`
    9. `/birmingham-water-damage-restoration`
    10. `/berkley-water-damage-restoration`
    11. `/royal-oak-sewage-extraction`
  - *(Quota reached for Nov 15; remaining pages will be indexed via sitemap and internal link graph).*

---

## 5. Next Steps Roadmap (What Any Agent/Engineer Should Do Next)

### Stage 1: SERP & Crawl Monitoring (Next 3–5 Days)
1. Inspect GSC URL Inspection data on the 11 submitted URLs to verify "Last crawl" timestamp updates to post-Nov 14.
2. Monitor GSC Performance report for striking-distance keyword movement (queries jumping from pos 15–25 into pos 1–5).
3. Check mobile SERP snippet appearance on Google to verify frontloaded phone number display in snippets.

### Stage 2: Off-Page Local Authority & Citations (Week 2)
1. Build / audit consistent local directory citations (Name, Address, Phone, Website - NAP) across top free trade directories (Yelp, YellowPages, Angi, BBB, MerchantCircle).
2. Ensure phone number `(248) 825-8312` is consistently cited with target city service locations.

### Stage 3: Conversion Rate Optimization & Call Quality (Ongoing)
1. Log in to Marketcall dashboard and verify call routing status on Offer 8915 (Campaign 356406).
2. Monitor call duration and ensure callers meet the qualification threshold (>60–90 seconds connected with active service dispatch) to lock in $64–$1,280 payouts.
3. If specific city pages receive high impressions but low calls, test visual call button contrasts or sticky bottom mobile call banners.

---
*Created on 2026-11-15. Auto-maintained by Antigravity.*
