"""Generate every HTML page and sitemap.xml from site_config and sitegen copy.

Run this, or run build.py, after changing the phone number in site_config.py.
"""

from pathlib import Path

from site_config import BRAND, LASTMOD, PHONE_DISPLAY, PHONE_TEL
from sitegen.copy_core import (
    NOT_FOUND_LINKS_INTRO,
    THANK_YOU,
    about_article,
    contact_article,
    privacy_article,
    terms_article,
)
from sitegen.copy_flood import ALT as FLOOD_ALT
from sitegen.copy_flood import ARTICLES as FLOOD_ARTICLES
from sitegen.copy_flood import DESCRIPTIONS as FLOOD_DESC
from sitegen.copy_flood import FAQS as FLOOD_FAQS
from sitegen.copy_flood import HERO as FLOOD_HERO
from sitegen.copy_hubs import (
    CITY_ARTICLES,
    CITY_DESC,
    CITY_HERO,
    flood_hub,
    sanit_hub,
    services_article,
    sewage_hub,
    sewer_hub,
    sump_hub,
    water_hub,
)
from sitegen.copy_sanit import ALT as SANIT_ALT
from sitegen.copy_sanit import ARTICLES as SANIT_ARTICLES
from sitegen.copy_sanit import DESCRIPTIONS as SANIT_DESC
from sitegen.copy_sanit import FAQS as SANIT_FAQS
from sitegen.copy_sanit import HERO as SANIT_HERO
from sitegen.copy_sewage import ALT as SEWAGE_ALT
from sitegen.copy_sewage import ARTICLES as SEWAGE_ARTICLES
from sitegen.copy_sewage import DESCRIPTIONS as SEWAGE_DESC
from sitegen.copy_sewage import FAQS as SEWAGE_FAQS
from sitegen.copy_sewage import HERO as SEWAGE_HERO
from sitegen.copy_sewer import ALT as SEWER_ALT
from sitegen.copy_sewer import DESCRIPTIONS as SEWER_DESC
from sitegen.copy_sewer import FAQS as SEWER_FAQS
from sitegen.copy_sewer import HERO as SEWER_HERO
from sitegen.copy_sewer import article as sewer_article
from sitegen.copy_sump import ALT as SUMP_ALT
from sitegen.copy_sump import ARTICLES as SUMP_ARTICLES
from sitegen.copy_sump import DESCRIPTIONS as SUMP_DESC
from sitegen.copy_sump import FAQS as SUMP_FAQS
from sitegen.copy_sump import HERO as SUMP_HERO
from sitegen.copy_water import ALT as WATER_ALT
from sitegen.copy_water import ARTICLES as WATER_ARTICLES
from sitegen.copy_water import DESCRIPTIONS as WATER_DESC
from sitegen.copy_water import FAQS as WATER_FAQS
from sitegen.copy_water import HERO as WATER_HERO
from sitegen.render import (
    CITIES,
    CITY_SERVICES,
    SERVICE_HUBS,
    call_button,
    city_name,
    esc,
    faq_html,
    form_fields,
    h2,
    h3,
    p,
    picture,
    render_document,
    require_meta,
    service_body,
    trust_row,
    ul,
    write_sitemap,
)

ROOT = Path(__file__).resolve().parent
META_ERRORS = []
SITEMAP = []


def fill(text):
    return text.format(PHONE_DISPLAY=PHONE_DISPLAY)


# Extra clauses used only to land unique descriptions in the 140–155 character window.
_META_TAILS = [
    " You confirm the provider's license and insurance.",
    " Ask the company for license and insurance.",
    " Verify license and insurance before hiring.",
    " You check license and insurance yourself.",
    " The provider sets the price, not this site.",
    " This site does not perform the cleanup.",
    " Availability depends on the provider.",
    " No arrival time is promised.",
    " We do not quote a price.",
    " Call is the way to reach a provider.",
    " The form on this site is not stored.",
    " Independent companies do the work.",
    " We are not the restoration contractor.",
    " You hire the provider directly.",
    " Scope and price come from the provider.",
    " No office address is listed, on purpose.",
]


def fit_meta(text):
    text = fill(text).strip()
    if 140 <= len(text) <= 155:
        return text
    base = text[:-1] if text.endswith(".") else text
    candidates = []
    for tail in _META_TAILS:
        candidates.append(base + "." + tail)
    for first in _META_TAILS:
        for second in _META_TAILS:
            if first == second:
                continue
            candidates.append(base + "." + first + second)
    hits = [item for item in candidates if 140 <= len(item) <= 155]
    if not hits:
        return text
    # Prefer the shortest addition that fits so the original sentence stays intact.
    hits.sort(key=len)
    return hits[0]


def remember(path, title, description, body, crumbs, faqs=None, service=None, robots="index, follow", priority="0.8", index=True):
    description = fit_meta(description) if "{PHONE_DISPLAY}" in description or len(description) < 140 or len(description) > 155 else description
    length = len(description)
    if length < 140 or length > 155 or "...." in description:
        META_ERRORS.append((path or "/", length, description))
    html_out = render_document(
        path,
        title,
        description,
        body,
        crumbs,
        faqs=faqs,
        service=service,
        robots=robots,
    )
    filename = "index.html" if path in ("", "/") else f"{path}.html"
    (ROOT / filename).write_text(html_out, encoding="utf-8")
    if index:
        SITEMAP.append((path, priority))


def image_for(city_slug, service_slug):
    for slug, _label, stem, width, height in CITY_SERVICES:
        if slug == service_slug:
            return f"/images/{city_slug}-{stem}.jpg", width, height
    raise KeyError(service_slug)


def emit_city_service(city_slug, service_slug, title, h1, description, hero, article_html, faqs, alt, priority):
    city = city_name(city_slug)
    src, width, height = image_for(city_slug, service_slug)
    label = next(label for slug, label, *_rest in CITY_SERVICES if slug == service_slug)
    body = service_body(
        city_slug,
        service_slug,
        h1,
        esc(hero),
        article_html,
        src,
        alt,
        width,
        height,
        f"{city} questions",
        faqs,
    )
    remember(
        f"{city_slug}-{service_slug}",
        title,
        fill(description),
        body,
        [("Home", "/"), (city, f"/{city_slug}"), (label, None)],
        faqs=faqs,
        service={
            "name": f"Referrals for {label.lower()} in {city}, Michigan",
            "description": (
                f"{BRAND} connects {city}, Michigan homeowners with independent providers for {label.lower()}. "
                f"{BRAND} does not perform the work."
            ),
            "area": city,
        },
        priority=priority,
    )


def prose_body(h1, lead, article, faqs=None, faq_heading="Questions", image=None, alt="", width=800, height=800):
    img = ""
    if image:
        img = f'<div class="my-6">{picture(image, alt, width, height)}</div>'
    faq = faq_html(faqs, faq_heading) if faqs else ""
    return f"""<section class="bg-slate-950/40 py-12 md:py-16 px-4 border-b border-slate-800">
        <div class="max-w-4xl mx-auto">
            <h1 class="text-3xl md:text-5xl font-outfit font-extrabold text-white leading-tight">{h1}</h1>
            <div class="text-base md:text-lg text-gray-300 mt-6 leading-relaxed space-y-4">{lead}</div>
            <div class="mt-8">{call_button()}</div>
        </div>
    </section>
    <section class="py-12 px-4">
        <div class="max-w-4xl mx-auto space-y-6">{img}{article}</div>
    </section>
    {trust_row()}
    {faq}
    """


def city_directory():
    cards = []
    for slug, name in CITIES:
        links = [f'<li><a class="text-red-400 hover:text-red-300 underline" href="/{slug}">{esc(name)} overview</a></li>']
        for service_slug, label, _stem, _w, _h in CITY_SERVICES:
            links.append(
                f'<li><a class="text-red-400 hover:text-red-300 underline" href="/{slug}-{service_slug}">{esc(label)}</a></li>'
            )
        cards.append(
            f"""<div class="bg-slate-950 border border-red-500/20 p-5 rounded-xl text-left">
                <h3 class="text-lg font-outfit font-bold text-white mb-3">{esc(name)}</h3>
                <ul class="space-y-2 text-sm">{''.join(links)}</ul>
            </div>"""
        )
    return f'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">{"".join(cards)}</div>'


def home_body():
    home_faqs = [
        (
            "Is Oakland Sewer Pros the company that cleans up the basement?",
            "No. Oakland Sewer Pros is a referral service. Independent providers do the work. We do not own trucks, employ technicians, or guarantee the job. You verify license and insurance with the company you hire.",
        ),
        (
            "Do you guarantee a 24/7 arrival in Oakland County?",
            "No. The phone line can be used at any hour, but a visit happens only when a participating provider is available for your location. Availability is not guaranteed.",
        ),
        (
            "Which Oakland County cities have pages?",
            "Royal Oak, Troy, Birmingham, Berkley, and Clawson. Each city has its own pages for sewer backup cleanup, sewage extraction, flooded basements, water damage restoration, sump pumps, and sanitizing after a backup.",
        ),
        (
            "Will homeowners insurance pay for a sewer backup or water damage?",
            "Not automatically. Sewer backup is often excluded unless the policy has an endorsement, and groundwater is often limited. Ask your insurer. Oakland Sewer Pros does not file claims or bill insurance companies.",
        ),
    ]
    lead = f"""<p>If sewage or floodwater is in a basement in Oakland County, call {esc(PHONE_DISPLAY)}. This is a free referral line to independent local providers. We do not pump, dry, or repair the house ourselves.</p>"""
    services = f"""<section id="services" class="py-16 bg-gray-50 text-slate-900 px-4">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-3xl font-outfit font-extrabold text-center mb-10">Services we can connect you with</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <a href="/water-damage-restoration" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Water damage restoration</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Extraction, drying, and water damage repair decisions after a flood or backup. The provider you hire sets the scope.</p>
                </a>
                <a href="/sewer-backup-cleanup" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Sewer backup cleanup</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Sewage that came up through a floor drain or basement fixture. City pages keep their existing addresses.</p>
                </a>
                <a href="/sewage-extraction" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Sewage extraction</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Removing contaminated water. A household vac spreads it. An outside company should do this work.</p>
                </a>
                <a href="/flooded-basement-cleanup" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Flooded basement cleanup</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Basement water removal after storms, window wells, or a sump overflow. Drain backups are a different page.</p>
                </a>
                <a href="/sump-pump-repair" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Sump pump repair</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">A stuck, dead, or overflowing pump. This site does not quote parts or labor.</p>
                </a>
                <a href="/basement-sanitization" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Basement sanitization</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Cleaning after sewage or a contaminated flood. Not a routine house-cleaning visit.</p>
                </a>
            </div>
        </div>
    </section>"""
    steps = """<section class="py-16 bg-slate-900 px-4 border-t border-slate-800">
        <div class="max-w-5xl mx-auto">
            <h2 class="text-3xl font-outfit font-extrabold text-white text-center mb-10">How a call works</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-slate-950 border border-slate-800 p-6 rounded-2xl">
                    <h3 class="text-white font-outfit font-bold mb-2">1. You call</h3>
                    <p class="text-sm text-gray-300 leading-relaxed">Use the number on this page and say your city and whether the water came from a drain, a sump, or a storm.</p>
                </div>
                <div class="bg-slate-950 border border-slate-800 p-6 rounded-2xl">
                    <h3 class="text-white font-bold font-outfit mb-2">2. A provider may take it</h3>
                    <p class="text-sm text-gray-300 leading-relaxed">If a participating independent company is available, the call can be connected. If not, there is no visit. We do not promise a response time.</p>
                </div>
                <div class="bg-slate-950 border border-slate-800 p-6 rounded-2xl">
                    <h3 class="text-white font-outfit font-bold mb-2">3. You hire them, or you don't</h3>
                    <p class="text-sm text-gray-300 leading-relaxed">Ask for a written scope, the price, and proof of license and insurance. They do the work. We do not.</p>
                </div>
            </div>
        </div>
    </section>"""
    cities = f"""<section class="py-16 bg-slate-950 px-4 border-t border-slate-800">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-3xl font-outfit font-extrabold text-white text-center mb-4">Oakland County cities</h2>
            <p class="text-sm text-gray-300 text-center max-w-3xl mx-auto mb-10">Every city page is linked here, including sewer backup, sewage extraction, flooded basement cleanup, water damage restoration, sump pump repair, and basement sanitization.</p>
            {city_directory()}
        </div>
    </section>"""
    form = f"""<section id="contact" class="py-16 bg-slate-900 px-4">
        <div class="max-w-xl mx-auto bg-slate-950 border border-slate-800 p-8 rounded-2xl">
            <h2 class="text-2xl font-outfit font-bold text-white mb-2">Call first</h2>
            <p class="text-sm text-gray-300 mb-6">The form does not dispatch anyone. Calling {esc(PHONE_DISPLAY)} is how you reach a provider.</p>
            {form_fields(id_prefix="home")}
        </div>
    </section>"""
    intro = f"""<section class="relative bg-slate-900 py-12 md:py-20 px-4 border-b border-slate-800">
        <div class="max-w-6xl mx-auto">
            <div class="mb-8 bg-red-950/70 border border-red-500/30 rounded-xl p-4 text-center">
                <p class="text-sm text-red-300 leading-relaxed">Sewage in a basement is contaminated water. Keep people and pets out. Do not wade in if it has reached outlets or the furnace.</p>
            </div>
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                <div class="lg:col-span-7">
                    <h1 class="text-3xl md:text-5xl font-outfit font-extrabold text-white leading-tight">24/7 Emergency Sewer Backup Cleanup &amp; Sewage Extraction in Oakland County, MI</h1>
                    <p class="text-base md:text-lg text-gray-300 mt-6 leading-relaxed">Oakland Sewer Pros connects Oakland County homeowners with independent local providers for sewer backups, sewage extraction, flooded basements, and water damage restoration. Arrival depends on the provider. We do not guarantee a response time.</p>
                    <p class="text-sm text-gray-300 mt-4 leading-relaxed">Start with <a class="text-red-400 underline" href="/royal-oak-sewer-cleanup">sewer backup cleanup in Royal Oak</a>, <a class="text-red-400 underline" href="/troy-sewage-extraction">sewage extraction in Troy</a>, <a class="text-red-400 underline" href="/birmingham-water-damage-restoration">water damage restoration in Birmingham</a>, <a class="text-red-400 underline" href="/berkley-flooded-basement">flooded basement cleanup in Berkley</a>, or <a class="text-red-400 underline" href="/clawson-basement-sanitization">basement sanitization in Clawson</a>.</p>
                    <div class="mt-8">{call_button()}</div>
                </div>
                <div class="lg:col-span-5">
                    {picture("/images/homepage_hero.jpg", "Wet basement floor after a sewer backup or flood, the kind of Oakland County loss this referral line is for", 800, 800, eager=True, css="w-full h-64 md:h-80 object-cover rounded-2xl border border-slate-800")}
                </div>
            </div>
        </div>
    </section>"""
    return intro + services + steps + cities + form + faq_html(home_faqs, "Questions about this referral line"), home_faqs


def main():
    META_ERRORS.clear()
    SITEMAP.clear()

    home_html, home_faqs = home_body()
    remember(
        "",
        "Oakland County Sewer Backup Cleanup | Oakland Sewer Pros",
        fill("Sewer backup and water damage restoration referrals in Oakland County, MI. Call {PHONE_DISPLAY}."),
        home_html,
        [],
        faqs=home_faqs,
        priority="1.0",
    )

    # City services
    packs = [
        ("sewer-cleanup", "Sewer Backup Cleanup {city} MI | Oakland Sewer Pros", "Sewer Backup Cleanup {city} MI", SEWER_HERO, SEWER_DESC, SEWER_FAQS, SEWER_ALT, "0.9", None),
        ("sewage-extraction", "Sewage Extraction {city} MI | Oakland Sewer Pros", "Sewage Extraction in {city}, MI", SEWAGE_HERO, SEWAGE_DESC, SEWAGE_FAQS, SEWAGE_ALT, "0.8", SEWAGE_ARTICLES),
        ("flooded-basement", "Flooded Basement Water Removal {city} MI | Oakland Sewer Pros", "Flooded Basement Cleanup & Water Removal in {city}, MI", FLOOD_HERO, FLOOD_DESC, FLOOD_FAQS, FLOOD_ALT, "0.8", FLOOD_ARTICLES),
        ("sump-pump-repair", "Sump Pump Repair {city} MI | Oakland Sewer Pros", "Sump Pump Repair {city} MI", SUMP_HERO, SUMP_DESC, SUMP_FAQS, SUMP_ALT, "0.8", SUMP_ARTICLES),
        ("basement-sanitization", "Basement Sanitization {city} MI | Oakland Sewer Pros", "Basement Sanitization after Sewage or Flood in {city}, MI", SANIT_HERO, SANIT_DESC, SANIT_FAQS, SANIT_ALT, "0.8", SANIT_ARTICLES),
        ("water-damage-restoration", "Water Damage Restoration {city}, MI | Oakland Sewer Pros", "Water Damage Restoration in {city}, MI", WATER_HERO, WATER_DESC, WATER_FAQS, WATER_ALT, "0.9", WATER_ARTICLES),
    ]
    for city_slug, city in CITIES:
        for service_slug, title_t, h1_t, heroes, descriptions, faqs, alts, priority, articles in packs:
            if service_slug == "sewer-cleanup":
                article_html = sewer_article(city_slug, city)
            else:
                article_html = articles[city_slug]()
            emit_city_service(
                city_slug,
                service_slug,
                title_t.format(city=city),
                h1_t.format(city=city),
                descriptions[city_slug],
                heroes[city_slug],
                article_html,
                faqs[city_slug],
                alts[city_slug],
                priority,
            )

    for city_slug, city in CITIES:
        faqs = [
            (
                f"Does {BRAND} have an office in {city}?",
                f"No. There is no {city} office, dispatch hub, or crew stationed in the city. The phone line refers you to independent providers when one is available.",
            ),
            (
                f"Which {city} page should I open first?",
                "If sewage came from a drain, open sewer backup cleanup. If the basement is wet from a storm or a sump and the drains stayed quiet, open flooded basement cleanup. If materials are already soaked, open water damage restoration.",
            ),
        ]
        body = prose_body(
            esc(f"{city}, MI sewer and water damage referrals"),
            f"<p>{esc(CITY_HERO[city_slug])}</p>",
            CITY_ARTICLES[city_slug](),
            faqs=faqs,
            faq_heading=f"{city} questions",
        )
        remember(
            city_slug,
            f"{city} Sewer & Water Damage Help | Oakland Sewer Pros",
            fill(CITY_DESC[city_slug]),
            body,
            [("Home", "/"), (city, None)],
            faqs=faqs,
            service={
                "name": f"Home service referrals in {city}, Michigan",
                "description": f"{BRAND} refers {city} homeowners to independent providers for sewer and water damage. {BRAND} does not perform the work.",
                "area": city,
            },
            priority="0.8",
        )

    hub_pages = [
        ("services", "Sewer & Water Damage Services | Oakland Sewer Pros", "Service referrals for sewer backups, water damage, flooded basements, and sump pumps in Oakland County, MI. Call {PHONE_DISPLAY}.", "Services for Oakland County homeowners", "Pick the job that matches the water, then the city. Calling is how you reach an independent provider.", services_article(), "0.8", None),
        ("water-damage-restoration", "Water Damage Restoration Oakland County | Oakland Sewer Pros", "Water damage restoration referrals in Oakland County, MI, including five city pages. Call {PHONE_DISPLAY} to connect.", "Water damage restoration in Oakland County, MI", "County page for extraction, drying, and sewage water damage. Each city page is separate.", water_hub(), "0.9", [
            ("What does water damage restoration mean here?", "Removing standing water, discarding materials that cannot be saved, and drying what remains. An independent provider does it. Oakland Sewer Pros does not."),
            ("Do you cover every Oakland County city?", "The pages are Royal Oak, Troy, Birmingham, Berkley, and Clawson. A provider may or may not accept a different ZIP. They decide."),
        ]),
        ("sewer-backup-cleanup", "Sewer Backup Cleanup Oakland County | Oakland Sewer Pros", "Sewer backup cleanup referrals for five Oakland County, MI cities. Independent providers. Call {PHONE_DISPLAY}.", "Sewer backup cleanup in Oakland County, MI", "Use the city page that matches the house. The provider, not this site, does the cleanup.", sewer_hub(), "0.8", None),
        ("sewage-extraction", "Sewage Extraction Oakland County MI | Oakland Sewer Pros", "Sewage extraction referrals in Oakland County, MI. We connect you with independent providers. Call {PHONE_DISPLAY}.", "Sewage extraction in Oakland County, MI", "Contaminated water has to be removed by a company equipped for it. We only make the introduction.", sewage_hub(), "0.8", None),
        ("flooded-basement-cleanup", "Flooded Basement Cleanup Oakland County | Oakland Sewer Pros", "Flooded basement cleanup and basement water removal referrals in Oakland County, MI. Call {PHONE_DISPLAY}.", "Flooded basement cleanup in Oakland County, MI", "Basement water removal for storms and sump overflows. Drain backups belong on the sewage pages.", flood_hub(), "0.8", None),
        ("sump-pump-repair", "Sump Pump Repair Oakland County MI | Oakland Sewer Pros", "Sump pump repair referrals in Oakland County, MI. No price list. Independent providers. Call {PHONE_DISPLAY}.", "Sump pump repair in Oakland County, MI", "A stuck or dead pump is a repair. Water on the floor is a separate cleanup. We quote neither.", sump_hub(), "0.8", None),
        ("basement-sanitization", "Basement Sanitization Oakland County | Oakland Sewer Pros", "Basement sanitizing after sewage or a flood in Oakland County, MI. Independent providers. Call {PHONE_DISPLAY}.", "Basement sanitization after sewage or flooding", "This is post-backup cleaning, not a maid service. Extraction comes first.", sanit_hub(), "0.8", None),
    ]
    for path, title, description, h1, lead, article, priority, faqs in hub_pages:
        article_html = article() if callable(article) else article
        body = prose_body(esc(h1), f"<p>{esc(lead)}</p>", article_html, faqs=faqs, faq_heading="Questions")
        service = None
        if path != "services":
            service = {
                "name": h1,
                "description": f"{BRAND} refers Oakland County homeowners to independent providers. {BRAND} does not perform this work.",
                "area": "Oakland County, Michigan",
            }
        crumbs = [("Home", "/"), ("Services", "/services"), (h1, None)] if path != "services" else [("Home", "/"), ("Services", None)]
        remember(path, title, fill(description), body, crumbs, faqs=faqs, service=service, priority=priority)

    about_faqs = [
        (
            "Are you a contractor?",
            "No. Oakland Sewer Pros is a referral service. Independent companies do the work. We do not guarantee their prices, licenses, insurance, or results.",
        ),
    ]
    remember(
        "about",
        "About Oakland Sewer Pros | Referral Service",
        fill("Oakland Sewer Pros is a referral line to independent sewer and water damage providers in Oakland County, MI. Call {PHONE_DISPLAY}."),
        prose_body("About Oakland Sewer Pros", f"<p>Honest description of what {esc(BRAND)} is, and what it is not.</p>", about_article(), faqs=about_faqs),
        [("Home", "/"), ("About", None)],
        faqs=about_faqs,
        priority="0.5",
    )
    remember(
        "contact",
        "Contact Oakland Sewer Pros | Oakland County MI",
        fill("Call Oakland Sewer Pros at {PHONE_DISPLAY} for a sewer or water damage referral in Oakland County, MI. The form is not stored."),
        prose_body(
            "Contact Oakland Sewer Pros",
            f"<p>Phone is the real contact. The form does not save what you type.</p>",
            contact_article() + form_fields(include_email=True, include_priority=True, id_prefix="contact"),
        ),
        [("Home", "/"), ("Contact", None)],
        priority="0.6",
    )
    remember(
        "privacy",
        "Privacy Policy | Oakland Sewer Pros",
        fill("How Oakland Sewer Pros handles calls and website forms. Form entries are not stored or put in the URL. Call {PHONE_DISPLAY}."),
        prose_body("Privacy", "<p>What this static site does with the details you might type or the number you call.</p>", privacy_article()),
        [("Home", "/"), ("Privacy", None)],
        priority="0.4",
    )
    remember(
        "terms",
        "Terms of Service | Oakland Sewer Pros",
        fill("Terms for the Oakland Sewer Pros referral site in Oakland County, MI. We do not guarantee contractor work. Call {PHONE_DISPLAY}."),
        prose_body("Terms of Service", "<p>Last updated September 27, 2026.</p>", terms_article()),
        [("Home", "/"), ("Terms", None)],
        priority="0.4",
    )

    thank_body = prose_body(
        "Call if water is in the house",
        f"<p>{esc(THANK_YOU[0][1])}</p><p>{esc(THANK_YOU[1][1])}</p>",
        p(f"Return to the <a class=\"text-red-400 underline\" href=\"/\">home page</a> or open <a class=\"text-red-400 underline\" href=\"/services\">services</a>."),
    )
    remember(
        "thank-you",
        "Call for help | Oakland Sewer Pros",
        fill("The form was not saved. If you have a sewer backup or flood in Oakland County, MI, call {PHONE_DISPLAY}."),
        thank_body,
        [("Home", "/"), ("Confirmation", None)],
        robots="noindex, nofollow",
        index=False,
    )

    missing_links = ul(
        [f'<a class="text-red-400 underline" href="{href}">{esc(label)}</a>' for href, label in SERVICE_HUBS]
        + [f'<a class="text-red-400 underline" href="/{slug}">{esc(name)}</a>' for slug, name in CITIES]
    )
    remember(
        "404",
        "Page not found | Oakland Sewer Pros",
        fill("That page is not on Oakland Sewer Pros. Find a city or service, or call {PHONE_DISPLAY} for a referral."),
        prose_body(
            "Page not found",
            f"<p>{esc(NOT_FOUND_LINKS_INTRO)}</p>",
            h2("Services and cities") + missing_links,
        ),
        [("Home", "/"), ("Page not found", None)],
        robots="noindex, nofollow",
        index=False,
    )

    (ROOT / "sitemap.xml").write_text(write_sitemap(SITEMAP), encoding="utf-8")
    if META_ERRORS:
        print("META LENGTH ERRORS:")
        for path, length, text in META_ERRORS:
            print(f"  {length:3} {path}: {text}")
        raise SystemExit(1)
    print(f"Generated {len(SITEMAP)} indexable URLs plus noindex pages. lastmod {LASTMOD}.")


if __name__ == "__main__":
    main()
