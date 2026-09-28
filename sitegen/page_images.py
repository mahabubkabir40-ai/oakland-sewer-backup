"""Three in-content photos per indexable page, from images/manifest.json."""

import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "images" / "manifest.json"

# City centers used only when a generic indoor or equipment photo is tagged.
# Outdoor photos and anything with an identifiable place are left without GPS.
GPS = {
    "royal-oak": (42.4895, -83.1446),
    "troy": (42.6064, -83.1498),
    "birmingham": (42.5467, -83.2113),
    "berkley": (42.5031, -83.1835),
    "clawson": (42.5334, -83.1463),
    "oakland-county": (42.5922, -83.3362),
}


@lru_cache(maxsize=1)
def _manifest():
    if not MANIFEST.exists():
        raise SystemExit(f"Missing {MANIFEST}. Image manifest is required to build pages.")
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pages = data["pages"] if isinstance(data, dict) and "pages" in data else data
    return pages


def images_for(page):
    pages = _manifest()
    if page not in pages:
        raise SystemExit(f"Image manifest has no entry for {page!r}")
    rows = pages[page]
    if len(rows) > 3:
        raise SystemExit(f"{page} has {len(rows)} images; expected at most 3")
    images = []
    for row in rows:
        images.append({
            "src": f"/images/{row['file']}",
            "alt": row["alt"],
            "width": int(row["width"]),
            "height": int(row["height"]),
            "eager": bool(row.get("eager")),
        })
    return images
