"""480w and 800w WebP variants for content photos. Original files are not rewritten."""

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "images"
WIDTHS = (480, 800)
# Article column is about 640px after the 12-column layout and padding.
# Below 768px the image is essentially the viewport width.
SIZES = "(max-width: 768px) 100vw, 640px"

_widths = {}


def ensure_variants():
    """Write smaller WebP files next to each content image that is wider than the target."""
    _widths.clear()
    for src in sorted(IMAGES.glob("*.webp")):
        if src.stem.endswith("-480") or src.stem.endswith("-800"):
            continue
        with Image.open(src) as im:
            width = im.width
            _widths[src.name] = width
            for target in WIDTHS:
                if width <= target:
                    continue
                dest = src.with_name(f"{src.stem}-{target}.webp")
                if dest.exists() and dest.stat().st_mtime >= src.stat().st_mtime:
                    continue
                height = max(1, round(im.height * target / width))
                resized = im.resize((target, height), Image.Resampling.LANCZOS)
                resized.save(dest, "WEBP", quality=80, method=6)


def srcset_for(webp_url):
    """Return a srcset for a /images/*.webp URL, including the original width."""
    name = Path(webp_url).name
    width = _widths.get(name)
    original = IMAGES / name
    if width is None and original.exists():
        with Image.open(original) as im:
            width = im.width
            _widths[name] = width
    if not width:
        return webp_url
    stem = Path(name).stem
    parts = []
    for target in WIDTHS:
        variant = IMAGES / f"{stem}-{target}.webp"
        if width > target and variant.exists():
            parts.append(f"/images/{stem}-{target}.webp {target}w")
    parts.append(f"{webp_url} {width}w")
    return ", ".join(parts)
