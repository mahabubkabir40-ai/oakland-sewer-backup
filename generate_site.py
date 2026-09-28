"""Generate every HTML page and sitemap.xml from site_config and sitegen copy.

Run this, or run build.py, after changing the phone number in site_config.py.
"""

import re
import subprocess
from pathlib import Path

from site_config import BRAND, LASTMOD, PHONE_DISPLAY, PHONE_TEL
from sitegen.copy_core import (
    ABOUT_FAQS,
    CONTACT_FAQS,
    NOT_FOUND_LINKS_INTRO,
    PRIVACY_FAQS,
    TERMS_FAQS,
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
    CITY_FAQS,
    CITY_H1,
    CITY_HERO,
    HUB_FAQS,
    flood_hub,
    sanit_hub,
    services_article,
    sewage_hub,
    sewer_hub,
    sump_hub,
    water_hub,
)
from sitegen.copy_resources import RESOURCE_FAQS, RESOURCE_PAGES
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
from sitegen.page_images import images_for
from sitegen.render import (
    CITIES,
    CITY_SERVICES,
    RESOURCE_LINKS,
    SERVICE_HUBS,
    call_button,
    city_name,
    content_figure,
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
    spread_article,
    trust_row,
    ul,
    write_sitemap,
)

ROOT = Path(__file__).resolve().parent
META_ERRORS = []
SITEMAP = []


def fill(text):
    return text.format(PHONE_DISPLAY=PHONE_DISPLAY)


def git_lastmod(path):
    """Date the built HTML last changed in git, or LASTMOD when this build rewrote it.

    Unchanged pages keep the commit date of their HTML file instead of the build date.
    Every current page was last committed on 2026-09-28, so a no-op rebuild stays on that day.
    """
    filename = "index.html" if path in ("", "/") else f"{path}.html"
    current = (ROOT / filename).read_bytes()
    try:
        head = subprocess.check_output(
            ["git", "show", f"HEAD:{filename}"],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return LASTMOD
    if current != head:
        return LASTMOD
    try:
        logged = subprocess.check_output(
            ["git", "log", "-1", "--format=%cs", "--", filename],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return LASTMOD
    return logged or LASTMOD


# Extra clauses used only to land unique descriptions in the 140–155 character window.
_META_TAILS = [
    " Keep people and pets out of the water.",
    " Get the scope and price in writing.",
    " Ask the crew for license and insurance.",
    " Say where the water came from.",
    " Photograph the water before cleanup.",
    " Stop using water and call.",
    " A local crew handles the cleanup.",
]

_BANNED_META_SENTENCES = {
    "the form is not stored",
    "a number",
}


def _meta_sentences(text):
    # Keep initials such as "George W. Kuhn"; still split after "MI." and "URL."
    chunks = re.split(r"(?<!\b[A-Z])\.\s+", text.strip())
    return [chunk.strip().rstrip(".") for chunk in chunks if chunk.strip()]


def _tail_body(tail):
    return tail.strip().rstrip(".").lower()


def _tail_already_in(tail, base):
    return _tail_body(tail) in base.lower()


def _pair_ok(first, second):
    first_l = first.lower()
    second_l = second.lower()
    if "crew" in first_l and "crew" in second_l:
        return False
    if "price" in first_l and "price" in second_l:
        return False
    return True


def _has_dup_sentences(text):
    parts = [part.lower() for part in _meta_sentences(text)]
    return len(parts) != len(set(parts))


def _clean_meta_base(text):
    kept = []
    for sentence in _meta_sentences(text):
        lowered = sentence.lower()
        if lowered in _BANNED_META_SENTENCES:
            continue
        if lowered.startswith("we refer") or lowered.startswith("connect with"):
            continue
        if lowered in [item.lower() for item in kept]:
            continue
        kept.append(sentence)
    if not kept:
        return text
    return ". ".join(kept) + "."


# Clause text is taken from _META_TAILS. A second clause is used only when one
# clause cannot land the description in the 140–155 window.
_META_CLAUSES = [
    ("keep people and pets out of the water", ""),
    ("get the scope and price in writing", "price"),
    ("ask the crew for license and insurance", "crew"),
    ("say where the water came from", ""),
    ("photograph the water before cleanup", ""),
    ("stop using water", ""),
]

USED_METAS = set()


def _clause_ok(clause, tag, base):
    lowered = base.lower()
    if clause in lowered:
        return False
    if tag and tag in lowered:
        return False
    return True


def _michigan(sentence):
    return sentence.replace(", MI", ", Michigan").replace(" MI", " Michigan")


def _valid_pair(item, source_had_phone):
    parts = _meta_sentences(item)
    lowered = item.lower()
    if not (140 <= len(item) <= 155 and len(parts) == 2):
        return False
    if _has_dup_sentences(item):
        return False
    if "we refer" in lowered or "connect with" in lowered or "the form is not stored" in lowered:
        return False
    if source_had_phone and "825-8312" not in item:
        return False
    if item in USED_METAS:
        return False
    return True


def _call_sentences(base, doubles):
    singles = []
    paired = []
    usable = [(clause, tag) for clause, tag in _META_CLAUSES if _clause_ok(clause, tag, base)]
    for clause, _tag in usable:
        singles.append(f"Call (248) 825-8312 and {clause}.")
    if doubles:
        for index, (first, first_tag) in enumerate(usable):
            for second, second_tag in usable[index + 1 :]:
                if first_tag and second_tag and first_tag == second_tag:
                    continue
                paired.append(f"Call (248) 825-8312, {first}, and {second}.")
    return singles, paired


def _topic_variants(parts):
    topic = parts[0]
    variants = [topic]
    expanded = _michigan(topic)
    if expanded != topic:
        variants.append(expanded)
    clarifiers = []
    for part in parts[1:]:
        lowered = part.lower()
        if "825-8312" in part:
            continue
        if lowered.startswith("not "):
            clarifiers.append("not " + part[4:])
        elif "means michigan" in lowered:
            clarifiers.append(part)
    widened = []
    for base in variants:
        for clarifier in clarifiers:
            if clarifier[:1].isupper():
                widened.append(f"{base}, and {clarifier}")
            else:
                widened.append(f"{base}, {clarifier}")
    return variants + widened


def _extend_phone_sentence(phone_sentence):
    base = _michigan(phone_sentence).rstrip(".")
    extended = []
    for clause, tag in _META_CLAUSES:
        if _clause_ok(clause, tag, base):
            extended.append(f"{base} and {clause}.")
    usable = [(clause, tag) for clause, tag in _META_CLAUSES if _clause_ok(clause, tag, base)]
    for index, (first, first_tag) in enumerate(usable):
        for second, second_tag in usable[index + 1 :]:
            if first_tag and second_tag and first_tag == second_tag:
                continue
            extended.append(f"{base}, {first}, and {second}.")
    return extended


def _content_extras(parts):
    clause_text = {clause for clause, _tag in _META_CLAUSES}
    extras = []
    for part in parts[1:]:
        lowered = part.lower()
        if "825-8312" in part or lowered.startswith("not ") or "means michigan" in lowered:
            continue
        if lowered in clause_text or any(lowered.startswith(clause) for clause in clause_text):
            continue
        if len(part.split()) < 4:
            continue
        first = part.split()[0].strip(",")
        if first in {"Royal", "Troy", "Birmingham", "Berkley", "Clawson", "Oakland", "Michigan", "George"}:
            piece = part
        else:
            piece = part[0].lower() + part[1:]
        extras.append(piece)
    return extras


def _openings(parts):
    bases = _topic_variants(parts)
    openings = list(bases)
    for base in bases:
        if ", not " in base or "means Michigan" in base:
            continue
        for extra in _content_extras(parts):
            openings.append(f"{base}, and {extra}")
    return openings


def _pair_score(item, source):
    parts = _meta_sentences(item)
    second = parts[1].lower() if len(parts) > 1 else ""
    source_l = source.lower()
    item_l = item.lower()
    dropped = 0
    for marker in ("not alabama", "extraction page", "means michigan", "form was not saved", "find a city", "keep people and pets out of the water"):
        if marker in source_l and marker not in item_l:
            dropped += 1
    stacked = 1 if "keep people and pets out of the water" in item_l and "stop using water" in item_l else 0
    return (dropped, stacked, second.count(","), len(item))


def fit_meta(text):
    return fill(text).strip()

def remember(path, title, description, body, crumbs, faqs=None, service=None, robots="index, follow", priority="0.8", index=True, article=None, extra_css=""):
    description = fit_meta(description)
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
        article=article,
        extra_css=extra_css,
    )
    filename = "index.html" if path in ("", "/") else f"{path}.html"
    (ROOT / filename).write_text(html_out, encoding="utf-8")
    if index:
        SITEMAP.append((path, priority))


def emit_city_service(city_slug, service_slug, title, h1, description, hero, article_html, faqs, alt, priority):
    city = city_name(city_slug)
    del alt  # per-photo alt text lives in the image manifest
    label = next(label for slug, label, *_rest in CITY_SERVICES if slug == service_slug)
    body = service_body(
        city_slug,
        service_slug,
        h1,
        esc(hero),
        article_html,
        images_for(f"{city_slug}-{service_slug}"),
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
            "name": f"{label} in {city}, Michigan",
            "description": f"A local crew handles {label.lower()} in {city}, Michigan.",
            "area": city,
        },
        priority=priority,
    )


def prose_body(h1, lead, article, faqs=None, faq_heading="Questions", images=None):
    near = ""
    if images:
        article, near_fig = spread_article(article, images)
        if near_fig:
            near = f'<div class="max-w-3xl mx-auto px-4 pt-4">{near_fig}</div>'
    faq = faq_html(faqs, faq_heading) if faqs else ""
    return f"""<section class="bg-slate-950/40 py-12 md:py-16 px-4 border-b border-slate-800">
        <div class="max-w-4xl mx-auto">
            <h1 class="text-3xl md:text-5xl font-outfit font-extrabold text-white leading-tight">{h1}</h1>
            <div class="text-base md:text-lg text-gray-300 mt-6 leading-relaxed space-y-4">{lead}</div>
            <div class="mt-8">{call_button()}</div>
        </div>
    </section>
    <section class="py-12 px-4">
        <div class="max-w-4xl mx-auto space-y-6">{article}</div>
    </section>
    {trust_row()}
    {near}
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
    photos = images_for("index")
    home_faqs = [
        (
            "What should I do before a crew arrives?",
            "Stop using water. Keep people and pets out of the flooded area. Do not snake a sewage backup with a household tool, and do not wade in if the water has reached outlets, the panel, or the furnace. Then call (248) 825-8312 and say your city and whether a drain backed up.",
        ),
        (
            "Which Oakland County cities have their own sewer pages?",
            "Royal Oak, Troy, Birmingham, Berkley, and Clawson. Berkley's sewer is a combined gravity pipe. Troy discharges through three districts. Birmingham's system is gravity and the city owns no pump stations. Open the city where the house stands.",
        ),
        (
            "What is the George W. Kuhn district?",
            "It is the regional drainage district, formerly Twelve Towns, upstream of the Red Run Drain. It serves all or part of 14 communities, including those five cities, about 24,500 acres. Dry-weather flow goes to the Detroit plant. Wet-weather flow is typically more than 93 percent stormwater. It does not name the pipe in front of one house.",
        ),
        (
            "How long do I have to notify a city after a sewer backup?",
            "Michigan law requires written notice within 45 days of discovering the damage before compensation for a sewage disposal event is possible. The notice needs your name, address, and phone, the property address, the discovery date, and a brief description. Each city has its own contact. That letter is not your insurance claim.",
        ),
        (
            "Will homeowners insurance pay for an Oakland County sewer backup?",
            "Not automatically. Sewer backup is often excluded unless the policy has an endorsement, and groundwater is often limited. Ask your insurer. Photograph the water before anything is thrown away.",
        ),
    ]
    services = f"""<section id="services" class="py-16 bg-gray-50 text-slate-900 px-4">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-3xl font-outfit font-extrabold text-center mb-10">Cleanup help you can call for</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <a href="/water-damage-restoration" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Water damage restoration</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Extraction, drying, and water damage repair decisions after a flood or backup. Get the scope in writing before work starts.</p>
                </a>
                <a href="/sewer-backup-cleanup" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Sewer backup cleanup</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Sewage that came up through a floor drain or basement fixture. Open your city for the local steps, then call.</p>
                </a>
                <a href="/sewage-extraction" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Sewage extraction</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Removing contaminated water with pumps and protective gear built for sewage. A household vac only spreads it.</p>
                </a>
                <a href="/flooded-basement-cleanup" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Flooded basement cleanup</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Basement water removal after storms, window wells, or a sump overflow. If a drain backed up, treat the water as sewage.</p>
                </a>
                <a href="/sump-pump-repair" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Sump pump repair</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">A stuck, dead, or overflowing pump. If the floor is already wet, you need the water removed as well as the repair.</p>
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
                    <p class="text-sm text-gray-300 leading-relaxed">Call the number above and say your city and whether the water came from a drain, a sump, or a storm.</p>
                </div>
                <div class="bg-slate-950 border border-slate-800 p-6 rounded-2xl">
                    <h3 class="text-white font-bold font-outfit mb-2">2. A local crew takes the job</h3>
                    <p class="text-sm text-gray-300 leading-relaxed">They look at the water, tell you what has to come out, and say when they can be there.</p>
                </div>
                <div class="bg-slate-950 border border-slate-800 p-6 rounded-2xl">
                    <h3 class="text-white font-outfit font-bold mb-2">3. Get it in writing</h3>
                    <p class="text-sm text-gray-300 leading-relaxed">Before anyone starts, ask for a written scope, the price, and proof of license and insurance.</p>
                </div>
            </div>
        </div>
    </section>"""
    cities = f"""<section class="py-16 bg-slate-950 px-4 border-t border-slate-800">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-3xl font-outfit font-extrabold text-white text-center mb-4">Oakland County cities</h2>
            <p class="text-sm text-gray-300 text-center max-w-3xl mx-auto mb-10">Royal Oak, Troy, Birmingham, Berkley, and Clawson each have pages for sewer backup, sewage extraction, flooded basement cleanup, water damage restoration, sump pump repair, and basement sanitization.</p>
            {city_directory()}
            <h2 class="text-2xl font-outfit font-extrabold text-white text-center mt-14 mb-4">Find your city and the job</h2>
            <p class="text-sm text-gray-300 text-center max-w-3xl mx-auto mb-6">If sewage came up a drain, use that city's sewer backup link. Extraction is only the pumping step.</p>
            <ul class="max-w-3xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-2 text-sm text-gray-300">
                <li><a class="text-red-400 underline" href="/troy-sewer-cleanup">Sewage cleanup in Troy, MI</a></li>
                <li><a class="text-red-400 underline" href="/royal-oak-sewer-cleanup">Sewage cleanup in Royal Oak, MI</a></li>
                <li><a class="text-red-400 underline" href="/birmingham-sewer-cleanup">Sewage cleanup in Birmingham, MI</a></li>
                <li><a class="text-red-400 underline" href="/berkley-sewer-cleanup">Sewage cleanup in Berkley, MI</a></li>
                <li><a class="text-red-400 underline" href="/clawson-sewer-cleanup">Sewage cleanup in Clawson, MI</a></li>
                <li><a class="text-red-400 underline" href="/clawson-flooded-basement">Flooded basement cleanup in Clawson, MI</a></li>
                <li><a class="text-red-400 underline" href="/berkley-sewage-extraction">Sewage extraction in Berkley, MI</a></li>
                <li><a class="text-red-400 underline" href="/berkley-basement-sanitization">Basement sanitization in Berkley, MI</a></li>
                <li><a class="text-red-400 underline" href="/clawson-sewage-extraction">Sewage extraction in Clawson</a></li>
                <li><a class="text-red-400 underline" href="/clawson-basement-sanitization">Basement sanitization in Clawson</a></li>
                <li><a class="text-red-400 underline" href="/royal-oak-sewage-extraction">Sewage extraction in Royal Oak</a></li>
                <li><a class="text-red-400 underline" href="/royal-oak-flooded-basement">Flooded basement cleanup in Royal Oak</a></li>
                <li><a class="text-red-400 underline" href="/troy-flooded-basement">Flooded basement cleanup in Troy</a></li>
                <li><a class="text-red-400 underline" href="/troy-basement-sanitization">Basement sanitization in Troy</a></li>
                <li><a class="text-red-400 underline" href="/birmingham-sewage-extraction">Sewage extraction in Birmingham</a></li>
                <li><a class="text-red-400 underline" href="/birmingham-basement-sanitization">Basement sanitization in Birmingham</a></li>
                <li><a class="text-red-400 underline" href="/contact">Contact</a></li>
                <li><a class="text-red-400 underline" href="/terms">Terms of service</a></li>
            </ul>
        </div>
    </section>"""
    resources = """<section id="resources" class="py-16 bg-gray-50 text-slate-900 px-4">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-3xl font-outfit font-extrabold text-center mb-4">Homeowner resources</h2>
            <p class="text-sm text-gray-700 text-center max-w-3xl mx-auto mb-10">Plain-language guides with links to the official city, county and state sources. Information only, not legal advice.</p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <a href="/sewer-backup-claim-guide" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Sewer backup claim guide</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Michigan's 45-day written notice rule, what to document, and the claim contact for Royal Oak, Troy, Birmingham, Berkley and Clawson.</p>
                </a>
                <a href="/george-w-kuhn-drainage-district" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">George W. Kuhn Drainage District</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">The regional combined sewer district behind many southeast Oakland County basements, and why heavy rain backs it up.</p>
                </a>
                <a href="/basement-flood-checklist" class="bg-white border border-gray-200 p-6 rounded-2xl block hover:border-gray-300">
                    <h3 class="text-lg font-outfit font-extrabold mb-3">Printable basement flood checklist</h3>
                    <p class="text-sm text-gray-700 leading-relaxed">Before, during and after a storm, with city sewer numbers, DTE outage reporting and the claim notice step.</p>
                </a>
            </div>
        </div>
    </section>"""
    form = f"""<section id="contact" class="py-16 bg-slate-900 px-4">
        <div class="max-w-xl mx-auto bg-slate-950 border border-slate-800 p-8 rounded-2xl">
            <h2 class="text-2xl font-outfit font-bold text-white mb-2">Call first</h2>
            <p class="text-sm text-gray-300 mb-6">Calling {esc(PHONE_DISPLAY)} is how you reach a crew. This form only opens a confirmation screen.</p>
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
                    <p class="text-base md:text-lg text-gray-300 mt-6 leading-relaxed">Sewage or floodwater in an Oakland County basement needs a cleanup company now. A local crew handles the cleanup for sewer backup, sewage cleanup, basement flood cleanup, and water damage restoration. They'll tell you when they can be there.</p>
                    <p class="text-sm text-gray-300 mt-4 leading-relaxed">County pages: <a class="text-red-400 underline" href="/sewer-backup-cleanup">sewage cleanup and sewer backup in Oakland County</a>, <a class="text-red-400 underline" href="/flooded-basement-cleanup">basement flood cleanup in Oakland County</a>, and <a class="text-red-400 underline" href="/water-damage-restoration">water damage restoration</a>. If a drain backed up, that is sewage, not a rain flood.</p>
                    <div class="mt-8">{call_button()}</div>
                </div>
                <div class="lg:col-span-5">
                    {picture(photos[0]["src"], photos[0]["alt"], photos[0]["width"], photos[0]["height"], eager=True, css="w-full h-64 md:h-80 object-cover rounded-2xl border border-slate-800")}
                </div>
            </div>
        </div>
    </section>"""
    mid = ""
    if len(photos) > 1:
        mid = f'<div class="bg-slate-900 px-4 pb-8"><div class="max-w-3xl mx-auto">{content_figure(photos[1])}</div></div>'
    near_faq = ""
    if len(photos) > 2:
        near_faq = f'<div class="max-w-3xl mx-auto px-4 pt-12">{content_figure(photos[2])}</div>'
    return intro + services + steps + mid + resources + cities + form + near_faq + faq_html(home_faqs, "Questions about a sewer backup"), home_faqs


def main():
    META_ERRORS.clear()
    SITEMAP.clear()
    USED_METAS.clear()

    home_html, home_faqs = home_body()
    remember(
        "",
        "Sewage Cleanup & Sewer Backup in Oakland County, MI",
        "Sewage cleanup, sewer backup and basement flood cleanup in Oakland County, MI. A local crew pumps, cleans and dries your basement. Call (248) 825-8312 now.",
        home_html,
        [],
        faqs=home_faqs,
        priority="1.0",
    )

    # City services
    packs = [
        ("sewer-cleanup", "Sewer Backup Cleanup {city} MI | Sewage Cleanup", "Sewer Backup Cleanup {city} MI", SEWER_HERO, SEWER_DESC, SEWER_FAQS, SEWER_ALT, "0.9", None),
        ("sewage-extraction", "Sewage Extraction {city} MI | Oakland Sewer Pros", "Sewage Extraction in {city}, MI", SEWAGE_HERO, SEWAGE_DESC, SEWAGE_FAQS, SEWAGE_ALT, "0.8", SEWAGE_ARTICLES),
        ("flooded-basement", "Flooded Basement Water Removal {city} MI | Oakland Sewer Pros", "Flooded Basement Cleanup & Water Removal in {city}, MI", FLOOD_HERO, FLOOD_DESC, FLOOD_FAQS, FLOOD_ALT, "0.8", FLOOD_ARTICLES),
        ("sump-pump-repair", "Sump Pump Repair in {city}, Michigan", "Sump Pump Repair in {city}, Michigan", SUMP_HERO, SUMP_DESC, SUMP_FAQS, SUMP_ALT, "0.8", SUMP_ARTICLES),
        ("basement-sanitization", "Basement Sanitization {city} MI | Oakland Sewer Pros", "Basement Sanitization after Sewage or Flood in {city}, MI", SANIT_HERO, SANIT_DESC, SANIT_FAQS, SANIT_ALT, "0.8", SANIT_ARTICLES),
        ("water-damage-restoration", "Water Damage Restoration {city}, MI | Oakland Sewer Pros", "Water Damage Restoration in {city}, MI", WATER_HERO, WATER_DESC, WATER_FAQS, WATER_ALT, "0.9", WATER_ARTICLES),
    ]
    for city_slug, city in CITIES:
        for service_slug, title_t, h1_t, heroes, descriptions, faqs, alts, priority, articles in packs:
            if service_slug == "sewer-cleanup":
                article_html = sewer_article(city_slug, city)
            else:
                article_html = articles[city_slug]()
            title = title_t.format(city=city)
            h1 = h1_t.format(city=city)
            if city_slug == "clawson" and service_slug == "flooded-basement":
                title = "Flooded Basement Cleanup Clawson, MI | Water Removal"
            if city_slug == "royal-oak" and service_slug == "flooded-basement":
                title = "Royal Oak Flooded Basement Cleanup | Oakland Sewer Pros"
            if city_slug == "birmingham" and service_slug == "flooded-basement":
                title = "Birmingham Flooded Basement Cleanup | Oakland Sewer Pros"
            if city_slug == "berkley" and service_slug == "flooded-basement":
                title = "Berkley Flooded Basement Cleanup | Oakland Sewer Pros"
            if city_slug == "berkley" and service_slug == "sewage-extraction":
                title = "Sewage Extraction in Berkley, MI | Bungalow Basements"
            if city_slug == "berkley" and service_slug == "basement-sanitization":
                title = "Basement Sanitization Berkley, MI | After Sewage"
            emit_city_service(
                city_slug,
                service_slug,
                title,
                h1,
                descriptions[city_slug],
                heroes[city_slug],
                article_html,
                faqs[city_slug],
                alts[city_slug],
                priority,
            )

    for city_slug, city in CITIES:
        faqs = CITY_FAQS[city_slug]
        body = prose_body(
            esc(CITY_H1[city_slug]),
            f"<p>{esc(CITY_HERO[city_slug])}</p>",
            CITY_ARTICLES[city_slug](),
            faqs=faqs,
            faq_heading=f"{city} questions",
            images=images_for(city_slug),
        )
        remember(
            city_slug,
            f"{city} Sewer & Water Damage Help | Oakland Sewer Pros",
            fill(CITY_DESC[city_slug]),
            body,
            [("Home", "/"), (city, None)],
            faqs=faqs,
            service={
                "name": f"Sewer and water help in {city}, Michigan",
                "description": f"A local crew handles sewer and water damage in {city}.",
                "area": city,
            },
            priority="0.8",
        )

    hub_pages = [
        ("services", "Oakland County Sewer & Water Services | Oakland Sewer Pros", "Sewer backup, sewage extraction, flooded basement, water damage and sump pump services in Oakland County, MI. Find your city or call (248) 825-8312.", "Services for Oakland County homeowners", "If sewage or floodwater is in the basement, match the job to the water, then open your city. A local cleanup crew handles the visit, and they'll tell you when they can be there.", services_article(), "0.8"),
        ("water-damage-restoration", "Water Damage Restoration Oakland County | Oakland Sewer Pros", "Water damage restoration in Oakland County, MI. A local crew removes water, dries your basement and handles sewage-soaked materials. Call (248) 825-8312.", "Water damage restoration in Oakland County, MI", "The basement is wet, and sewage makes water damage restoration in Oakland County a stricter cleanup than a clean leak. A local cleanup crew handles the visit, and they'll tell you when they can be there.", water_hub(), "0.9"),
        ("sewer-backup-cleanup", "Sewage Cleanup & Sewer Backup in Oakland County", "Sewer backup cleanup in Oakland County, MI. A local crew pumps out sewage, removes ruined materials and disinfects your basement. Call (248) 825-8312.", "Sewage cleanup and sewer backup in Oakland County, MI", "Sewage is in the basement and it needs to come out. A local cleanup crew handles the visit, and they'll tell you when they can be there. Open your city's page for the local steps.", sewer_hub(), "0.8"),
        ("sewage-extraction", "Sewage Extraction Oakland County MI | Oakland Sewer Pros", "Sewage extraction in Oakland County, MI. A local crew pumps sewage out of your basement and hauls away soaked materials safely. Call (248) 825-8312.", "Sewage extraction in Oakland County, MI", "Contaminated water is in the basement and it has to be pumped out. A local cleanup crew handles the visit, and they'll tell you when they can be there.", sewage_hub(), "0.8"),
        ("flooded-basement-cleanup", "Basement Flood Cleanup in Oakland County, MI", "Basement flood cleanup in Oakland County, MI. A local crew pumps out storm or sump water and dries the walls and floors. Call (248) 825-8312 now.", "Basement flood cleanup in Oakland County, MI", "Standing water from a storm or a sump is in the basement. A local cleanup crew handles the visit, and they'll tell you when they can be there. If a drain backed up, tell them it is sewage.", flood_hub(), "0.8"),
        ("sump-pump-repair", "Sump Pump Repair in Oakland County, Michigan", "Sump pump repair in Oakland County, MI. A local crew fixes stuck, dead or overflowing pumps and removes the water if the floor is wet. Call (248) 825-8312.", "Sump pump repair in Oakland County, Michigan", "A stuck or dead pump has left the basement wet. A local crew handles the visit, and they'll tell you when they can be there. Birmingham here means Birmingham, Michigan.", sump_hub(), "0.8"),
        ("basement-sanitization", "Basement Sanitization Oakland County | Oakland Sewer Pros", "Basement sanitization in Oakland County, MI after sewage or a flood. A local crew removes ruined materials and disinfects the rest. Call (248) 825-8312.", "Basement sanitization after sewage or flooding", "The water is out and the basement still needs cleaning after sewage or a flood. A local cleanup crew handles the visit, and they'll tell you when they can be there. Extraction comes first if the water is still there.", sanit_hub(), "0.8"),
    ]
    for path, title, description, h1, lead, article, priority in hub_pages:
        faqs = HUB_FAQS[path]
        article_html = article() if callable(article) else article
        body = prose_body(esc(h1), f"<p>{esc(lead)}</p>", article_html, faqs=faqs, faq_heading="Questions", images=images_for(path))
        service = None
        if path != "services":
            service = {
                "name": h1,
                "description": f"A local crew handles this work in Oakland County.",
                "area": "Oakland County, Michigan",
            }
        crumbs = [("Home", "/"), ("Services", "/services"), (h1, None)] if path != "services" else [("Home", "/"), ("Services", None)]
        remember(path, title, fill(description), body, crumbs, faqs=faqs, service=service, priority=priority)

    for slug, title, h1, description, lead, article_fn, css, label in RESOURCE_PAGES:
        faqs = RESOURCE_FAQS[slug]
        body = prose_body(esc(h1), lead, article_fn(), faqs=faqs, images=images_for(slug))
        remember(
            slug,
            title,
            fill(description),
            body,
            [("Home", "/"), (label, None)],
            faqs=faqs,
            priority="0.7",
            article={"headline": h1, "published": "2026-09-28", "modified": LASTMOD},
            extra_css=css,
        )

    remember(
        "about",
        "About Oakland Sewer Pros | Oakland County Sewage Cleanup",
        "About Oakland Sewer Pros: one number for sewage and flooded basement cleanup in Oakland County, MI, handled by a local crew. Call (248) 825-8312.",
        prose_body("About Oakland Sewer Pros", f"<p>Who handles the cleanup when you call {esc(PHONE_DISPLAY)}, and what to check first.</p>", about_article(), faqs=ABOUT_FAQS, images=images_for("about")),
        [("Home", "/"), ("About", None)],
        faqs=ABOUT_FAQS,
        priority="0.5",
    )
    remember(
        "contact",
        "Contact Oakland Sewer Pros | Oakland County MI",
        "Contact Oakland Sewer Pros for sewage and flooded basement cleanup in Oakland County, MI. Call (248) 825-8312 to reach a local crew; the form is not saved.",
        prose_body(
            "Contact Oakland Sewer Pros",
            f"<p>Phone is the real contact. The form does not save what you type.</p>",
            contact_article() + form_fields(include_email=True, include_priority=True, id_prefix="contact"),
            faqs=CONTACT_FAQS,
            images=images_for("contact"),
        ),
        [("Home", "/"), ("Contact", None)],
        faqs=CONTACT_FAQS,
        priority="0.6",
    )
    remember(
        "privacy",
        "Privacy Policy | Oakland Sewer Pros",
        "Privacy policy for Oakland Sewer Pros in Oakland County, MI. Website forms do not store your details. For sewage cleanup help, call (248) 825-8312.",
        prose_body("Privacy", "<p>What this static site does with the details you might type or the number you call.</p>", privacy_article(), faqs=PRIVACY_FAQS, images=images_for("privacy")),
        [("Home", "/"), ("Privacy", None)],
        faqs=PRIVACY_FAQS,
        priority="0.4",
    )
    remember(
        "terms",
        "Terms of Service | Oakland Sewer Pros",
        "Terms of service for Oakland Sewer Pros in Oakland County, MI. Check the crew's license and insurance and get the scope in writing. Call (248) 825-8312.",
        prose_body("Terms of Service", "<p>Last updated September 27, 2026.</p>", terms_article(), faqs=TERMS_FAQS, images=images_for("terms")),
        [("Home", "/"), ("Terms", None)],
        faqs=TERMS_FAQS,
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
        "Your form was not saved. For a sewer backup or flooded basement in Oakland County, MI, call (248) 825-8312 now to reach a local cleanup crew.",
        thank_body,
        [("Home", "/"), ("Confirmation", None)],
        robots="noindex, nofollow",
        index=False,
    )

    missing_links = ul(
        [f'<a class="text-red-400 underline" href="{href}">{esc(label)}</a>' for href, label in SERVICE_HUBS]
        + [f'<a class="text-red-400 underline" href="{href}">{esc(label)}</a>' for href, label in RESOURCE_LINKS]
        + [f'<a class="text-red-400 underline" href="/{slug}">{esc(name)}</a>' for slug, name in CITIES]
    )
    remember(
        "404",
        "Page not found | Oakland Sewer Pros",
        "Page not found. Find sewage cleanup and flooded basement help for your Oakland County, MI city, or call (248) 825-8312 to reach a local crew.",
        prose_body(
            "Page not found",
            f"<p>{esc(NOT_FOUND_LINKS_INTRO)}</p>",
            h2("Services and cities") + missing_links,
        ),
        [("Home", "/"), ("Page not found", None)],
        robots="noindex, nofollow",
        index=False,
    )

    lastmods = {path: git_lastmod(path) for path, _priority in SITEMAP}
    (ROOT / "sitemap.xml").write_text(write_sitemap(SITEMAP, lastmods), encoding="utf-8")
    if META_ERRORS:
        print("META LENGTH ERRORS:")
        for path, length, text in META_ERRORS:
            print(f"  {length:3} {path}: {text}")
        raise SystemExit(1)
    image_errors = []
    for path, _priority in SITEMAP:
        filename = "index.html" if path in ("", "/") else f"{path}.html"
        count = (ROOT / filename).read_text(encoding="utf-8").count("<img ")
        if count > 3:
            image_errors.append(f"{filename}: {count} img tags")
    for filename in ("thank-you.html", "404.html"):
        count = (ROOT / filename).read_text(encoding="utf-8").count("<img ")
        if count:
            image_errors.append(f"{filename}: unexpected {count} img tags")
    if image_errors:
        print("IMAGE COUNT ERRORS:")
        for item in image_errors:
            print(" ", item)
        raise SystemExit(1)
    print(f"Generated {len(SITEMAP)} indexable URLs plus noindex pages. lastmod {LASTMOD}.")


if __name__ == "__main__":
    main()
