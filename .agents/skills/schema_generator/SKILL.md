---
name: schema-generator
description: Generate validated JSON-LD structured data schema markup for LocalBusiness, FAQPage, and BreadcrumbList.
---

# Schema Structured Data Skill

This skill outlines best practices for generating and validating JSON-LD structured data schemas for Oakland Sewer Pros suburbs.

## Core Rules

1. **Syntax Escaping (CRITICAL):**
   - When placing HTML links or tags inside JSON-LD properties (like a FAQ answer's `text` property), you **MUST** escape all double quotes inside the string.
   - **Incorrect:** `"text": "Check <a href="https://site.com">link</a>"`
   - **Correct:** `"text": "Check <a href=\"https://site.com\">link</a>"`

2. **Common Schema Types for Local SEO:**
   - **LocalBusiness / WaterDamageRestoration**: Define on the homepage and location pages with NAP (Name, Address, Phone) details, geo-coordinates, and logo.
   - **FAQPage**: Generate questions and answers targeting common local emergency queries.
   - **BreadcrumbList**: Define breadcrumbs to show clean paths in search results.

3. **Oakland County Suburb Coordinates Reference:**
   * **Troy**: Lat: `42.5796`, Lon: `-83.1199`
   * **Royal Oak**: Lat: `42.4895`, Lon: `-83.1446`
   * **Berkley**: Lat: `42.5020`, Lon: `-83.1827`
   * **Birmingham**: Lat: `42.5467`, Lon: `-83.2155`
   * **Clawson**: Lat: `42.5273`, Lon: `-83.1463`
   * **Farmington Hills**: Lat: `42.4990`, Lon: `-83.3677`
   * **Rochester Hills**: Lat: `42.6584`, Lon: `-83.1499`
   * **Southfield**: Lat: `42.4734`, Lon: `-83.2219`
   * **Novi**: Lat: `42.4806`, Lon: `-83.4755`
   * **Pontiac**: Lat: `42.6389`, Lon: `-83.2910`
