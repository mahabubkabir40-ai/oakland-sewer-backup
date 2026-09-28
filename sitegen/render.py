"""Shared HTML chrome, schema, and page assembly for Oakland Sewer Pros."""

import html
import json
from xml.sax.saxutils import escape as xml_escape

from site_config import (
    AVAILABILITY_DISCLAIMER,
    BRAND,
    DISCLAIMER,
    DOMAIN,
    LASTMOD,
    PHONE_DISPLAY,
    PHONE_E164,
    PHONE_TEL,
)

CITIES = [
    ("royal-oak", "Royal Oak"),
    ("troy", "Troy"),
    ("birmingham", "Birmingham"),
    ("berkley", "Berkley"),
    ("clawson", "Clawson"),
]

# slug suffix -> nav label, image stem, width, height
CITY_SERVICES = [
    ("sewer-cleanup", "Sewer Backup Cleanup", "sewer-cleanup", 600, 600),
    ("sewage-extraction", "Sewage Extraction", "sewage-extraction", 800, 800),
    ("flooded-basement", "Flooded Basement Cleanup", "flooded-basement", 600, 600),
    ("sump-pump-repair", "Sump Pump Repair", "sump-pump-repair", 600, 600),
    ("basement-sanitization", "Basement Sanitization", "basement-sanitization", 600, 600),
    ("water-damage-restoration", "Water Damage Restoration", "flooded-basement", 600, 600),
]

SERVICE_HUBS = [
    ("/services", "All services"),
    ("/water-damage-restoration", "Water Damage Restoration"),
    ("/sewer-backup-cleanup", "Sewer Backup Cleanup"),
    ("/sewage-extraction", "Sewage Extraction"),
    ("/flooded-basement-cleanup", "Flooded Basement Cleanup"),
    ("/sump-pump-repair", "Sump Pump Repair"),
    ("/basement-sanitization", "Basement Sanitization"),
]

# Homeowner resource pages (informational, Article schema). Linked from the home page, footer and hubs.
RESOURCE_LINKS = [
    ("/sewer-backup-claim-guide", "Sewer backup claim guide (45-day notice)"),
    ("/george-w-kuhn-drainage-district", "George W. Kuhn Drainage District"),
    ("/basement-flood-checklist", "Printable basement flood checklist"),
]

PULSE_CSS = """
        .pulse-btn { animation: pulse-danger 2.2s infinite; }
        @keyframes pulse-danger {
            0% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.75); }
            70% { box-shadow: 0 0 0 15px rgba(220, 38, 38, 0); }
            100% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0); }
        }
        details summary::-webkit-details-marker { display: none; }
        summary { list-style: none; }
"""


def esc(value):
    return html.escape(str(value), quote=True)


def a(href, text):
    return (
        f'<a href="{esc(href)}" class="text-red-400 hover:text-red-300 underline font-medium">'
        f"{text}</a>"
    )


def h2(text):
    return f'<h2 class="text-2xl font-outfit font-extrabold text-white">{text}</h2>'


def h3(text):
    return f'<h3 class="text-lg font-outfit font-bold text-white">{text}</h3>'


def p(inner):
    return f'<p class="text-sm text-gray-300 leading-relaxed">{inner}</p>'


def ul(items):
    lis = "".join(f"<li>{item}</li>" for item in items)
    return (
        '<ul class="list-disc list-inside text-sm text-gray-300 space-y-1.5 pl-2">'
        f"{lis}</ul>"
    )


def ol(items):
    lis = "".join(f"<li>{item}</li>" for item in items)
    return (
        '<ol class="list-decimal list-inside text-sm text-gray-200 space-y-2">'
        f"{lis}</ol>"
    )


def callout(title, inner):
    return f"""<div class="bg-red-950/40 border border-red-500/30 p-5 rounded-xl space-y-3">
        <h3 class="text-base font-outfit font-extrabold text-red-300">{title}</h3>
        {inner}
    </div>"""


def note(inner):
    return (
        '<p class="text-sm text-gray-300 leading-relaxed italic border-l-2 border-red-600 pl-3 '
        f'bg-slate-950/20 py-2">{inner}</p>'
    )


def picture(src, alt, width, height, eager=False, css="w-full h-auto max-h-[350px] object-cover rounded-xl border border-slate-800 shadow-lg"):
    webp = src.rsplit(".", 1)[0] + ".webp"
    loading = "eager" if eager else "lazy"
    priority = ' fetchpriority="high"' if eager else ""
    return f"""<picture>
        <source srcset="{esc(webp)}" type="image/webp">
        <img src="{esc(src)}" alt="{esc(alt)}" width="{width}" height="{height}" class="{css}" loading="{loading}" decoding="async"{priority}>
    </picture>"""


def phone_link(label=None, css="text-red-400 font-bold underline"):
    text = label or PHONE_DISPLAY
    return f'<a href="tel:{PHONE_TEL}" class="{css}">{esc(text)}</a>'


def city_name(slug):
    for s, name in CITIES:
        if s == slug:
            return name
    raise KeyError(slug)


def city_service_href(city_slug, service_slug):
    return f"/{city_slug}-{service_slug}"


def nearby_links(service_slug, label, current_city):
    parts = []
    for slug, name in CITIES:
        if slug == current_city:
            continue
        href = city_service_href(slug, service_slug)
        parts.append(a(href, f"{label} in {name}"))
    return ", ".join(parts[:-1]) + (", and " if len(parts) > 1 else "") + parts[-1]


def breadcrumbs(crumbs):
    """crumbs: list of (label, href or None for current)."""
    if not crumbs:
        return "", None
    items_html = []
    schema_items = []
    for i, (label, href) in enumerate(crumbs, start=1):
        if href:
            items_html.append(
                f'<li><a href="{esc(href)}" class="text-red-400 hover:text-red-300 underline">{esc(label)}</a></li>'
            )
            schema_items.append({
                "@type": "ListItem",
                "position": i,
                "name": label,
                "item": DOMAIN + href if href.startswith("/") else href,
            })
        else:
            items_html.append(f'<li aria-current="page" class="text-gray-200">{esc(label)}</li>')
            schema_items.append({
                "@type": "ListItem",
                "position": i,
                "name": label,
            })
        if i != len(crumbs):
            items_html.append('<li aria-hidden="true" class="text-gray-500">/</li>')
    html_nav = (
        '<nav aria-label="Breadcrumb" class="mb-6">'
        '<ol class="flex flex-wrap items-center gap-2 text-xs text-gray-300">'
        + "".join(items_html)
        + "</ol></nav>"
    )
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": schema_items,
    }
    return html_nav, schema


def organization_graph():
    return [
        {
            "@type": "Organization",
            "@id": f"{DOMAIN}/#organization",
            "name": BRAND,
            "url": f"{DOMAIN}/",
            "telephone": PHONE_E164,
            "description": (
                f"{BRAND} is a referral service that connects Oakland County, Michigan homeowners "
                "with independent local providers for sewer backup cleanup, sewage extraction, flooded "
                "basement cleanup, water damage restoration, sump pump repair, and basement sanitization "
                "after a flood or sewage backup."
            ),
            "areaServed": {
                "@type": "AdministrativeArea",
                "name": "Oakland County, Michigan",
            },
        },
        {
            "@type": "WebSite",
            "@id": f"{DOMAIN}/#website",
            "url": f"{DOMAIN}/",
            "name": BRAND,
            "publisher": {"@id": f"{DOMAIN}/#organization"},
        },
    ]


def json_ld(obj):
    payload = json.dumps(obj, ensure_ascii=False, indent=2)
    if "</" in payload:
        payload = payload.replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{payload}\n</script>'


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": answer},
            }
            for question, answer in faqs
        ],
    }


def service_schema(name, description, url_path, area_name):
    area = {"@type": "AdministrativeArea", "name": area_name}
    if area_name != "Oakland County, Michigan":
        area = {
            "@type": "City",
            "name": area_name,
            "containedInPlace": {"@type": "State", "name": "Michigan"},
        }
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "description": description,
        "url": f"{DOMAIN}{url_path}",
        "provider": {"@id": f"{DOMAIN}/#organization"},
        "areaServed": area,
        "serviceType": name,
    }


def article_schema(headline, description, url_path, date_published, date_modified):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": description,
        "url": f"{DOMAIN}{url_path}",
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{DOMAIN}{url_path}"},
        "datePublished": date_published,
        "dateModified": date_modified,
        "inLanguage": "en-US",
        "author": {"@type": "Organization", "@id": f"{DOMAIN}/#organization", "name": BRAND, "url": f"{DOMAIN}/"},
        "publisher": {"@type": "Organization", "@id": f"{DOMAIN}/#organization", "name": BRAND, "url": f"{DOMAIN}/"},
    }


def faq_html(faqs, heading):
    blocks = []
    for question, answer in faqs:
        blocks.append(f"""<details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
            <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors">
                <span>{esc(question)}</span>
                <span class="transition group-open:rotate-180 text-red-400 font-bold shrink-0 ml-4" aria-hidden="true">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </span>
            </summary>
            <div class="p-5 border-t border-slate-800/60 text-sm text-gray-300 leading-relaxed bg-slate-950/20">{esc(answer)}</div>
        </details>""")
    return f"""<section id="faq" class="py-16 bg-slate-900 px-4">
        <div class="max-w-3xl mx-auto">
            <h2 class="text-2xl font-outfit font-extrabold text-white text-center mb-10">{esc(heading)}</h2>
            <div class="space-y-4">{''.join(blocks)}</div>
        </div>
    </section>"""


def trust_row():
    cells = [
        ("Referral line", "We connect you with independent local providers. The company you hire does the work."),
        ("You check credentials", "Ask the provider for the license and insurance the job requires."),
        ("Price from the company", "The provider you hire sets the scope and the price."),
    ]
    inner = []
    for title, text in cells:
        inner.append(f"""<div class="flex items-start gap-3">
            <div>
                <span class="block text-white font-bold">{esc(title)}</span>
                <span class="text-xs text-gray-300">{esc(text)}</span>
            </div>
        </div>""")
    return f"""<section class="py-12 bg-slate-950 px-4 border-t border-b border-slate-800">
        <div class="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">{''.join(inner)}</div>
    </section>"""


def sidebar(city_slug, active_slug):
    name = city_name(city_slug)
    links = []
    for slug, label, _stem, _w, _h in CITY_SERVICES:
        href = city_service_href(city_slug, slug)
        current = slug == active_slug
        if current:
            links.append(
                f'<a href="{href}" aria-current="page" class="px-4 py-2.5 rounded-lg border text-sm text-left font-semibold bg-emergency-600/10 border-emergency-600/30 text-red-400">{esc(label)} in {esc(name)}</a>'
            )
        else:
            links.append(
                f'<a href="{href}" class="px-4 py-2.5 rounded-lg border text-sm text-left font-semibold bg-slate-900 border-slate-800 text-gray-300 hover:border-red-500/30 hover:text-white">{esc(label)} in {esc(name)}</a>'
            )
    return f"""<nav aria-label="Services in {esc(name)}" class="lg:col-span-4 bg-slate-950/80 border border-slate-800 p-6 rounded-2xl space-y-4">
        <p class="text-lg font-outfit font-extrabold text-white border-b border-slate-800 pb-3">Services in {esc(name)}</p>
        <div class="flex flex-col gap-2">{''.join(links)}</div>
        <a href="/{city_slug}" class="block text-sm text-red-400 hover:text-red-300 underline">{esc(name)} service area</a>
    </nav>"""


def nearby_section(service_slug, label, current_city):
    name = city_name(current_city)
    return f"""<div class="border-t border-slate-800/60 pt-6 mt-6">
        <h2 class="text-lg font-outfit font-bold text-white mb-3">{esc(label)} in nearby cities</h2>
        <p class="text-sm text-gray-300 leading-relaxed">If the house is in a neighboring city, the same phone line covers {nearby_links(service_slug, label, current_city)}. Open the city where the house stands. The details there match that place, not {esc(name)}.</p>
    </div>"""


def _menu_links():
    service_links = "".join(
        f'<a href="{href}" class="block px-4 py-2 text-sm text-gray-300 hover:text-white hover:bg-slate-900" role="menuitem">{esc(label)}</a>'
        for href, label in SERVICE_HUBS
    )
    city_links = "".join(
        f'<a href="/{slug}" class="block px-4 py-2.5 text-sm text-gray-300 hover:text-white hover:bg-slate-900">{esc(name)}</a>'
        for slug, name in CITIES
    )
    mobile_services = "".join(
        f'<a href="{href}" class="block px-4 py-2 text-sm text-gray-300 hover:text-white hover:bg-slate-900">{esc(label)}</a>'
        for href, label in SERVICE_HUBS
    )
    mobile_cities = "".join(
        f'<a href="/{slug}" class="block px-4 py-2 text-sm text-gray-300 hover:text-white hover:bg-slate-900">{esc(name)}</a>'
        for slug, name in CITIES
    )
    desktop = f"""<nav class="hidden md:flex items-center gap-6 text-sm font-medium" aria-label="Primary">
        <div class="relative group py-2">
            <button type="button" class="text-gray-300 group-hover:text-white transition-colors flex items-center gap-1" aria-haspopup="true">
                <span>Services</span>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
            </button>
            <div class="absolute left-0 mt-2 w-64 bg-slate-950 border border-slate-800 rounded-xl py-2 shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50" role="menu">
                {service_links}
            </div>
        </div>
        <div class="relative group py-2">
            <button type="button" class="text-gray-300 group-hover:text-white transition-colors flex items-center gap-1" aria-haspopup="true">
                <span>Service Areas</span>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
            </button>
            <div class="absolute left-0 mt-2 w-48 bg-slate-950 border border-slate-800 rounded-xl py-2 shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                {city_links}
            </div>
        </div>
        <a href="/about" class="text-gray-300 hover:text-white transition-colors">About</a>
        <a href="/contact" class="text-gray-300 hover:text-white transition-colors">Contact</a>
    </nav>"""
    mobile = f"""<details class="md:hidden relative">
        <summary class="cursor-pointer px-3 py-2 text-sm font-semibold text-white border border-slate-800 rounded-lg">Menu</summary>
        <div class="absolute right-0 mt-2 w-64 max-h-96 overflow-y-auto bg-slate-950 border border-slate-800 rounded-xl py-2 shadow-2xl z-50">
            <p class="px-4 pt-2 pb-1 text-xs font-bold uppercase tracking-wider text-gray-400">Services</p>
            {mobile_services}
            <p class="px-4 pt-3 pb-1 text-xs font-bold uppercase tracking-wider text-gray-400">Service areas</p>
            {mobile_cities}
            <a href="/about" class="block px-4 py-2 text-sm text-gray-300 hover:text-white hover:bg-slate-900">About</a>
            <a href="/contact" class="block px-4 py-2 text-sm text-gray-300 hover:text-white hover:bg-slate-900">Contact</a>
            <a href="/privacy" class="block px-4 py-2 text-sm text-gray-300 hover:text-white hover:bg-slate-900">Privacy</a>
        </div>
    </details>"""
    return desktop, mobile


def header():
    desktop, mobile = _menu_links()
    return f"""<a href="tel:{PHONE_TEL}" class="fixed bottom-0 left-0 right-0 z-50 bg-emergency-600 hover:bg-emergency-700 text-white py-3 px-4 text-center font-outfit font-extrabold text-xs sm:text-sm uppercase tracking-wider shadow-xl border-t border-red-500 md:hidden block pulse-btn" aria-label="Call {BRAND} 24/7 at {PHONE_DISPLAY}">
        <span class="flex items-center justify-center gap-2">Call 24/7: {PHONE_DISPLAY}</span>
    </a>
    <header class="bg-slate-950/80 backdrop-blur-md border-b border-slate-800 sticky top-0 z-40">
        <div class="max-w-6xl mx-auto px-4 h-20 flex items-center justify-between gap-3">
            <a href="/" class="flex items-center gap-2 shrink-0" aria-label="{BRAND} home">
                <div class="p-2 bg-emergency-600 rounded-lg text-white font-bold text-lg font-outfit">OS</div>
                <div class="leading-tight">
                    <span class="block text-white font-extrabold text-base sm:text-lg tracking-tight font-outfit">OAKLAND SEWER</span>
                    <span class="block text-xs font-semibold tracking-wider text-red-500 uppercase">PROS</span>
                </div>
            </a>
            {desktop}
            <div class="flex items-center gap-2">
                {mobile}
                <a href="tel:{PHONE_TEL}" aria-label="Call {PHONE_DISPLAY}" class="flex items-center justify-center gap-2 p-2.5 sm:px-4 sm:py-2 bg-emergency-600 hover:bg-emergency-700 text-white font-extrabold text-sm rounded-lg transition-colors shadow-lg">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.94.725l.548 2.2a1 1 0 01-.321.988l-1.305.98a10.582 10.582 0 004.872 4.872l.98-1.305a1 1 0 01.988-.321l2.2.548a1 1 0 01.725.94V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                    <span class="hidden sm:inline">{PHONE_DISPLAY}</span>
                </a>
            </div>
        </div>
    </header>"""


def footer():
    services = "".join(
        f'<li><a href="{href}" class="hover:text-white transition-colors">{esc(label)}</a></li>'
        for href, label in SERVICE_HUBS
    )
    cities = "".join(
        f'<li><a href="/{slug}" class="hover:text-white transition-colors">{esc(name)}</a></li>'
        for slug, name in CITIES
    )
    resources = "".join(
        f'<li><a href="{href}" class="hover:text-white transition-colors">{esc(label)}</a></li>'
        for href, label in RESOURCE_LINKS
    )
    return f"""<footer class="bg-slate-950 text-gray-300 py-10 text-xs border-t border-slate-800">
        <div class="max-w-6xl mx-auto px-4 text-left">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-sm">
                <nav aria-label="Footer services">
                    <p class="text-white font-bold mb-3">Services</p>
                    <ul class="space-y-2 text-gray-300">{services}</ul>
                </nav>
                <nav aria-label="Footer service areas">
                    <p class="text-white font-bold mb-3">Service areas</p>
                    <ul class="space-y-2 text-gray-300">{cities}</ul>
                </nav>
                <div>
                <nav aria-label="Footer homeowner resources" class="mb-6">
                    <p class="text-white font-bold mb-3">Homeowner resources</p>
                    <ul class="space-y-2 text-gray-300">{resources}</ul>
                </nav>
                <nav aria-label="Footer company">
                    <p class="text-white font-bold mb-3">Company</p>
                    <ul class="space-y-2 text-gray-300">
                        <li><a href="/about" class="hover:text-white transition-colors">About</a></li>
                        <li><a href="/contact" class="hover:text-white transition-colors">Contact</a></li>
                        <li><a href="/privacy" class="hover:text-white transition-colors">Privacy</a></li>
                        <li><a href="/terms" class="hover:text-white transition-colors">Terms of Service</a></li>
                        <li><a href="tel:{PHONE_TEL}" class="hover:text-white transition-colors">Call {PHONE_DISPLAY}</a></li>
                    </ul>
                </nav>
                </div>
            </div>
            <div class="mt-8 border-t border-slate-800 pt-6 space-y-3 leading-relaxed text-gray-300">
                <p>{esc(DISCLAIMER)}</p>
                <p>{esc(AVAILABILITY_DISCLAIMER)}</p>
                <p>&copy; 2026 {esc(BRAND)}. All rights reserved.</p>
            </div>
        </div>
    </footer>"""


def call_button(extra_class=""):
    return (
        f'<a href="tel:{PHONE_TEL}" class="flex items-center justify-center gap-2 px-6 py-3.5 bg-emergency-600 hover:bg-emergency-700 text-white font-extrabold text-base rounded-xl shadow-xl w-full sm:w-auto pulse-btn {extra_class}">'
        f"Call {PHONE_DISPLAY}</a>"
    )


def form_fields(include_email=False, include_priority=False, id_prefix="lead"):
    email = ""
    if include_email:
        email = f"""<div>
            <label for="{id_prefix}-email" class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-2">Email</label>
            <input type="email" id="{id_prefix}-email" name="email" autocomplete="email" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-white text-sm">
        </div>"""
    priority = ""
    if include_priority:
        priority = f"""<fieldset>
            <legend class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-2">How urgent is it?</legend>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-sm">
                <label class="flex items-center gap-2 p-3 bg-red-950/40 border border-red-500/30 rounded-lg"><input type="radio" name="priority" value="Emergency"> <span>Active backup</span></label>
                <label class="flex items-center gap-2 p-3 bg-slate-950 border border-slate-800 rounded-lg"><input type="radio" name="priority" value="Urgent"> <span>Needs a visit soon</span></label>
                <label class="flex items-center gap-2 p-3 bg-slate-950 border border-slate-800 rounded-lg"><input type="radio" name="priority" value="Standard"> <span>Question</span></label>
            </div>
        </fieldset>"""
    options = "".join(
        f'<option value="{esc(name)}">{esc(name)}</option>' for _slug, name in CITIES
    )
    return f"""<form method="post" action="/thank-you" class="space-y-4" onsubmit="event.preventDefault(); window.location.assign('/thank-you');">
        <div>
            <label for="{id_prefix}-name" class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-2">Name</label>
            <input type="text" id="{id_prefix}-name" name="name" autocomplete="name" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-white text-sm">
        </div>
        <div>
            <label for="{id_prefix}-phone" class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-2">Phone</label>
            <input type="tel" id="{id_prefix}-phone" name="phone" autocomplete="tel" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-white text-sm">
        </div>
        {email}
        <div>
            <label for="{id_prefix}-location" class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-2">City</label>
            <select id="{id_prefix}-location" name="location" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-white text-sm">
                <option value="">Select a city</option>
                {options}
                <option value="Other Oakland County">Other Oakland County</option>
            </select>
        </div>
        {priority}
        <div>
            <label for="{id_prefix}-message" class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-2">What is happening?</label>
            <textarea id="{id_prefix}-message" name="message" rows="4" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-white text-sm"></textarea>
        </div>
        <button type="submit" class="w-full py-3.5 bg-emergency-600 hover:bg-emergency-700 text-white font-bold rounded-lg text-sm">Show confirmation page</button>
        <p class="text-xs text-gray-300 leading-relaxed">This form does not save or email your details. For a live connection, call {phone_link()}. Submitting only opens the confirmation page, and your name, phone, and email are not added to the page address.</p>
    </form>"""


def render_document(path, title, description, body, crumbs, faqs=None, service=None, robots="index, follow", article=None, extra_css=""):
    canonical = f"{DOMAIN}/" if path in ("", "/") else f"{DOMAIN}/{path.strip('/')}"
    url_path = "/" if path in ("", "/") else f"/{path.strip('/')}"
    crumb_html, crumb_schema = breadcrumbs(crumbs)
    if crumb_html:
        crumb_html = f'<div class="max-w-6xl mx-auto px-4 pt-6">{crumb_html}</div>'
    scripts = [json_ld({"@context": "https://schema.org", "@graph": organization_graph()})]
    if crumb_schema:
        scripts.append(json_ld(crumb_schema))
    if faqs:
        scripts.append(json_ld(faq_schema(faqs)))
    if service:
        scripts.append(json_ld(service_schema(
            service["name"],
            service["description"],
            url_path,
            service["area"],
        )))
    if article:
        scripts.append(json_ld(article_schema(
            article["headline"],
            description,
            url_path,
            article["published"],
            article["modified"],
        )))
    og_type = "article" if article else "website"
    robots_tag = f'<meta name="robots" content="{esc(robots)}">'
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(description)}">
    {robots_tag}
    <link rel="canonical" href="{esc(canonical)}">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(description)}">
    <meta property="og:url" content="{esc(canonical)}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:site_name" content="{esc(BRAND)}">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(description)}">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="preload" href="/fonts/outfit-800.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="/css/fonts.css">
    <link rel="stylesheet" href="/css/main.css">
    <style>{PULSE_CSS}{extra_css}</style>
    {''.join(scripts)}
</head>
<body class="font-sans text-gray-200 bg-slate-900 min-h-screen flex flex-col justify-between pb-16 md:pb-0">
    {header()}
    <main class="flex-grow">
        {crumb_html}
        {body}
    </main>
    {footer()}
</body>
</html>
"""


def service_body(city_slug, service_slug, h1, hero_lead, article_html, image_src, alt, width, height, faq_heading, faqs):
    name = city_name(city_slug)
    crumb_slot = ""  # crumbs are rendered above body; hero follows
    return f"""<section class="relative bg-slate-950/40 py-12 md:py-20 px-4 border-b border-slate-800">
        <div class="max-w-4xl mx-auto text-center">
            <p class="inline-flex items-center gap-1.5 px-3.5 py-1.5 bg-red-950/60 border border-red-500/30 text-red-300 rounded-full text-xs font-extrabold uppercase tracking-widest mb-6">{esc(name)}, Michigan</p>
            <h1 class="text-3xl md:text-5xl font-outfit font-extrabold text-white leading-tight tracking-tight">{esc(h1)}</h1>
            <p class="text-base md:text-lg text-gray-300 mt-6 leading-relaxed max-w-2xl mx-auto">{hero_lead}</p>
            <div class="mt-8 flex justify-center">{call_button()}</div>
        </div>
    </section>
    <section class="py-16 bg-slate-900 px-4">
        <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <article class="lg:col-span-8 space-y-6 bg-slate-950/40 border border-slate-800/80 p-6 md:p-8 rounded-2xl">
                <div class="my-2">{picture(image_src, alt, width, height)}</div>
                {article_html}
            </article>
            {sidebar(city_slug, service_slug)}
        </div>
    </section>
    {trust_row()}
    {faq_html(faqs, faq_heading)}
    """


def write_sitemap(paths_with_priority, lastmods=None):
    """paths_with_priority: list of (path, priority) where path is '' for home.

    lastmods maps path -> YYYY-MM-DD. Missing keys fall back to the build date.
    """
    urls = []
    for path, priority in paths_with_priority:
        loc = f"{DOMAIN}/" if path in ("", "/") else f"{DOMAIN}/{path}"
        lastmod = LASTMOD if not lastmods else lastmods.get(path, LASTMOD)
        urls.append(
            "  <url>\n"
            f"    <loc>{xml_escape(loc)}</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            f"    <priority>{priority}</priority>\n"
            "  </url>"
        )
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    return body


def require_meta(description, label):
    length = len(description)
    if length < 140 or length > 155:
        raise SystemExit(f"Meta description for {label} is {length} characters: {description}")
    if "...." in description or description.endswith("..."):
        raise SystemExit(f"Truncated meta on {label}")
    return description
