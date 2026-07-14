---
name: ai-seo
description: Perform strategic local and search engine optimization using Google Search Console data, striking-distance keywords, and CTR analysis.
---

# AI SEO Skill

This skill outlines how to leverage Google Search Console (GSC) API performance data to identify rank-climbing opportunities and execute local optimizations.

## Strategic Workflow

1. **Find Striking-Distance Keywords:**
   - Run [fetch_gsc.py](file:///c:/Users/USER/Desktop/oakland-sewer-backup/fetch_gsc.py) to look for queries with high impressions but average position between 11 and 25 (Page 2).
   - These represent low-hanging fruit where minor optimizations (internal links, headings) can push the page to Page 1.

2. **Optimize CTR (Click-Through Rate):**
   - Target queries with low CTR despite decent average position.
   - Refine the page title to lead with the exact query.
   - Add numbers (e.g. `24/7 Response`) or trust indicators (`Licensed & Insured`, `Direct Insurance Billing`) to the title and meta description.

3. **GSC Query Filtering:**
   - Keep the Search Console API query filtered by country (`usa` ISO code) to remove international noise and get precise local rankings.

4. **Off-Page Local Signals:**
   - Build NAP (Name, Address, Phone) citation authority on local directories like Yelp, Foursquare, and local directories listed in `directories.csv`.
