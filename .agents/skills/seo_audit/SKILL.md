---
name: seo-audit
description: Analyze local HTML files for SEO optimization, schema correctness, speed issues, and internal link structure.
---

# SEO Audit Skill

This skill provides steps and checks to audit HTML pages on the website for on-page SEO issues, technical compliance, and metadata health.

## Audit Checklist

1. **Title & Meta Tags:**
   - `<title>` is under 60 characters and leads with target local keywords. Pattern: `[Suburb] [Service] | Oakland Sewer Pros`.
   - `<meta name="description">` is between 120-160 characters, includes a CTA, and contains your tracking phone number `(248) 825-8312`.
   - Canonical tag is present and points to the correct domain: `<link rel="canonical" href="https://oaklandsewerpros.com/[page-name]">` (no typos like `oaklandseweremergency.com`).
   - OpenGraph and Twitter card titles/descriptions match page-specific content.

2. **Heading Hierarchy:**
   - Exactly one `<h1>` tag per page containing the primary local service phrase (e.g., `24/7 Emergency Sewer Backup Cleanup in Troy, MI`).
   - Proper nesting: `<h2>` for major sections, `<h3>` for subsections.

3. **Images & Media:**
   - Every `<img>` tag must have a descriptive, localized `alt` attribute.
   - Core above-the-fold hero images should use `rel="preload"` to prevent Largest Contentful Paint (LCP) delays.
   - Images should be compressed WebP formats.

4. **Structured Data:**
   - JSON-LD script block is present and contains valid syntax.
   - Run the local validator script or API check to audit GSC indexation using [check_indexing.py](file:///c:/Users/USER/Desktop/oakland-sewer-backup/check_indexing.py).
