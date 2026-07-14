---
name: site-architecture
description: Plan, audit, and structure URL sitemaps and parent-child silo link networks for local lead generation sites.
---

# Site Architecture Skill

This skill provides instructions for designing, auditing, and optimizing the website structure, URL paths, and internal linking to maximize search engine crawlability and PageRank distribution for Oakland Sewer Pros.

## 1. Logical Hierarchy (Hub-and-Spoke Model)
To pass SEO authority effectively, the site follows a flat silo structure:
* **The Hub (Homepage)**: `https://oaklandsewerpros.com/` (represents the main brand and entry point).
* **The Spokes (City Landing Pages)**: `/suburb-service-intent` (e.g. `/royal-oak-sewer-cleanup`, `/troy-sump-pump-repair`). Keep all pages flat (no page > 2 clicks from the homepage).

## 2. URL Naming Standards
* Use lowercase letters only.
* Use hyphens `-` instead of underscores `_` or spaces.
* Pattern: `https://oaklandsewerpros.com/[suburb]-[service-intent]`
* Keep URLs short, descriptive, and keyword-focused.

## 3. Internal Linking Strategy
* **Contextual Body Links**: Link back to the Homepage using the anchor text `Oakland Sewer Pros`.
* **Neighboring Silo Links**: Interlink subpages to geographically adjacent neighbor cities to pass authority (e.g., Troy pages link to Royal Oak and Clawson pages).
* **Footer Navigation**: Provide clean HTML footer links to all core pages and location landing pages.
* **Sitemaps**: Every new URL must be registered in [sitemap.xml](file:///c:/Users/USER/Desktop/oakland-sewer-backup/sitemap.xml) with appropriate priority (`0.8` for spokes, `1.0` for homepage).
