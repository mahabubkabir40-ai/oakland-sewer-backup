"""Validate generated HTML, schema, links, compliance, and city-page uniqueness."""

import json
import re
from difflib import SequenceMatcher
from pathlib import Path

from bs4 import BeautifulSoup
from html5lib.html5parser import parse as html5_parse

from site_config import AVAILABILITY_DISCLAIMER, DISCLAIMER, PHONE_DISPLAY

ROOT = Path(__file__).resolve().parent
CITIES = ["royal-oak", "troy", "birmingham", "berkley", "clawson"]
THIN = ["sewage-extraction", "flooded-basement", "basement-sanitization"]

errors = []


def err(msg):
    errors.append(msg)


def visible_text(html, exclude_nav=True):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["script", "style", "header", "footer"]):
        tag.decompose()
    if exclude_nav:
        for tag in soup.find_all("nav"):
            tag.decompose()
    return " ".join(soup.get_text(" ", strip=True).split())


def normalize_cities(text):
    for city in ["Royal Oak", "Troy", "Birmingham", "Berkley", "Clawson", "royal-oak", "birmingham", "berkley", "clawson"]:
        text = re.sub(re.escape(city), "CITY", text, flags=re.I)
    # troy as a word is risky; do it after longer names
    text = re.sub(r"\bTroy\b", "CITY", text)
    return text


def grams(text, n=5):
    words = re.findall(r"[a-z0-9']+", text.lower())
    return [" ".join(words[i : i + n]) for i in range(len(words) - n + 1)]


pages = sorted(ROOT.glob("*.html"))
hrefs = {}
for path in pages:
    raw = path.read_text(encoding="utf-8")
    try:
        html5_parse(raw)
    except Exception as exc:  # noqa: BLE001
        err(f"{path.name}: html5 parse {exc}")
    soup = BeautifulSoup(raw, "html.parser")
    if soup.html.get("lang") != "en":
        err(f"{path.name}: missing lang")
    h1s = soup.find_all("h1")
    if len(h1s) != 1:
        err(f"{path.name}: h1 count {len(h1s)}")
    # heading order
    last = 0
    for tag in soup.find_all(re.compile(r"^h[1-6]$")):
        level = int(tag.name[1])
        if last and level > last + 1:
            err(f"{path.name}: heading skip h{last} to h{level} ({tag.get_text(' ', strip=True)[:60]})")
            break
        last = level
    desc = soup.find("meta", attrs={"name": "description"})
    if not desc or not desc.get("content"):
        err(f"{path.name}: missing meta description")
    else:
        n = len(desc["content"])
        if not 140 <= n <= 155:
            err(f"{path.name}: meta {n}")
        if "...." in desc["content"]:
            err(f"{path.name}: truncated meta")
    canon = soup.find("link", rel="canonical")
    if path.name == "404.html":
        if canon:
            err(f"{path.name}: 404 should not have a canonical")
    elif not canon:
        err(f"{path.name}: no canonical")
    else:
        href = canon["href"]
        slug = "" if path.name == "index.html" else path.stem
        expected = "https://oaklandsewerpros.com/" if slug == "" else f"https://oaklandsewerpros.com/{slug}"
        if href != expected:
            err(f"{path.name}: canonical {href} != {expected}")
    if DISCLAIMER not in raw:
        err(f"{path.name}: missing disclaimer")
    if AVAILABILITY_DISCLAIMER not in raw:
        err(f"{path.name}: missing availability disclaimer")
    if "LocalBusiness" in raw or "streetAddress" in raw or "Dispatch Hub" in raw:
        err(f"{path.name}: fake local business schema")
    if re.search(r"\b(IICRC|45-minute|45 minute|45-min|premium|elite|cheapest)\b", raw, re.I):
        err(f"{path.name}: banned claim")
    if re.search(r"\$\d", raw):
        err(f"{path.name}: price")
    if "Emergency Pros" in raw or "Emergency Hub" in raw:
        err(f"{path.name}: old brand")
    robots = soup.find("meta", attrs={"name": "robots"})
    if path.name in ("thank-you.html", "404.html"):
        if not robots or "noindex" not in robots.get("content", ""):
            err(f"{path.name}: should be noindex")
    for form in soup.find_all("form"):
        if form.get("method", "").lower() != "post":
            err(f"{path.name}: form not POST")
        if "thank-you" not in (form.get("action") or ""):
            err(f"{path.name}: form action")
    for img in soup.find_all("img"):
        if not img.get("width") or not img.get("height"):
            err(f"{path.name}: img missing dimensions {img.get('src')}")
        if not img.get("alt"):
            err(f"{path.name}: img missing alt")
        parent = img.find_parent("picture")
        if parent is None or not parent.find("source"):
            err(f"{path.name}: img without webp picture {img.get('src')}")
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        try:
            data = json.loads(script.string)
        except Exception as exc:  # noqa: BLE001
            err(f"{path.name}: bad json-ld {exc}")
            continue
        blob = json.dumps(data)
        if "LocalBusiness" in blob or "streetAddress" in blob:
            err(f"{path.name}: address schema")
    hrefs[path.name] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/") and not href.startswith("//"):
            hrefs[path.name].append(href.split("#")[0])

# internal links
existing = {p.stem for p in pages}
existing.add("")  # home via /
for name, links in hrefs.items():
    for href in links:
        if href.startswith("/images") or href.startswith("/css") or href.startswith("/fonts"):
            continue
        slug = href.strip("/")
        if slug.endswith(".html"):
            slug = slug[:-5]
        if slug not in existing and href not in ("/",):
            err(f"{name}: broken link {href}")

# sitemap
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
if "<lastmod>" not in sm:
    err("sitemap missing lastmod")
if "thank-you" in sm or "/404" in sm:
    err("sitemap includes noindex page")
for stem in existing:
    if stem in ("thank-you", "404"):
        continue
    loc = "https://oaklandsewerpros.com/" if stem == "index" else f"https://oaklandsewerpros.com/{stem}"
    if loc not in sm and stem != "index":
        err(f"sitemap missing {loc}")
if "https://oaklandsewerpros.com/" not in sm:
    err("sitemap missing home")

# uniqueness for thin pages
print("SIMILARITY (city-normalized, exclude header/footer/nav)")
for service in THIN + ["sump-pump-repair", "water-damage-restoration", "sewer-cleanup"]:
    texts = {}
    for city in CITIES:
        raw = (ROOT / f"{city}-{service}.html").read_text(encoding="utf-8")
        texts[city] = normalize_cities(visible_text(raw))
    ratios = []
    cities = list(texts)
    for i, a in enumerate(cities):
        for b in cities[i + 1 :]:
            ratios.append(SequenceMatcher(None, texts[a].split(), texts[b].split()).ratio())
    # unique 5-gram share vs other cities
    shares = []
    all_grams = {city: grams(texts[city]) for city in cities}
    for city in cities:
        mine = all_grams[city]
        others = set()
        for other in cities:
            if other != city:
                others.update(all_grams[other])
        if not mine:
            shares.append(0)
            continue
        unique = sum(1 for g in mine if g not in others)
        shares.append(unique / len(mine))
    print(
        f"  {service}: seq min {min(ratios):.2f} avg {sum(ratios)/len(ratios):.2f} "
        f"unique-5gram min {min(shares):.2f} avg {sum(shares)/len(shares):.2f}"
    )

# word counts for water + thin main text
print("WORDS (exclude header/footer/nav)")
for service in THIN + ["water-damage-restoration"]:
    for city in CITIES:
        raw = (ROOT / f"{city}-{service}.html").read_text(encoding="utf-8")
        words = visible_text(raw).split()
        if city == "royal-oak":
            print(f"  {city}-{service}: {len(words)} (sample)")
        elif len(words) < 500:
            err(f"{city}-{service}: only {len(words)} words")

descs = []
for path in pages:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    descs.append(soup.find("meta", attrs={"name": "description"})["content"])
if len(descs) != len(set(descs)):
    err("duplicate meta descriptions")

if PHONE_DISPLAY not in (ROOT / "index.html").read_text(encoding="utf-8"):
    err("home missing phone")

print(f"ERRORS {len(errors)}")
for item in errors:
    print(" -", item)
raise SystemExit(1 if errors else 0)
