"""Download + self-host every media asset for luzentucuerpo.com.

Outputs to:
  site/img/        — page images (was whythelight.com hotlinks)
  site/thumbs/     — Vimeo / YouTube poster thumbnails for facades

Each output is WebP (quality 78). Also keeps original-size + a smaller
half-width variant for srcset on big hero images.

Re-runnable: skips files that already exist + match expected size class.
"""
from __future__ import annotations
import json
import shutil
import subprocess
import urllib.request
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).parent
SITE = ROOT / "site"
IMG_DIR = SITE / "img"
THUMB_DIR = SITE / "thumbs"
IMG_DIR.mkdir(parents=True, exist_ok=True)
THUMB_DIR.mkdir(parents=True, exist_ok=True)

# ───── ALL 14 page images (was hotlinked from whythelight.com) ────────────
# Map: short slug → (source URL, target widths for srcset)
PAGE_IMAGES = {
    "aging-battery":       ("https://whythelight.com/wp-content/uploads/2025/11/womanAging-battery-1-1024x981.png", [400, 800, 1024]),
    "video-thumb":         ("https://whythelight.com/wp-content/uploads/2025/11/3-MinuteVideo-thumbnail-2-1.png", [400, 800]),
    "patch-placement":     ("https://whythelight.com/wp-content/uploads/2025/09/SN-Patch-placement-scaled-1-690x1024.jpg", [400, 690]),
    "couple":              ("https://whythelight.com/wp-content/uploads/2025/09/490141872_10162757194347458_245241563246855534_n-1024x1024.jpg", [400, 800, 1024]),
    "kitchen":             ("https://whythelight.com/wp-content/uploads/2025/09/ManWoman-Kitchen-swirl-1024x645.png", [400, 800, 1024]),
    "mountain":            ("https://whythelight.com/wp-content/uploads/2025/11/Man-frontOfMtn-819x1024.png", [400, 819]),
    "patches":             ("https://whythelight.com/wp-content/uploads/2025/09/Phototherapy-LifeWave-patches-clean-1024x1024.jpg", [400, 800, 1024]),
    "tl-days":             ("https://whythelight.com/wp-content/uploads/2025/09/timeline-firstFewDays-2.png", [240, 480]),
    "tl-4w":               ("https://whythelight.com/wp-content/uploads/2025/09/timeline-6weeks-2.png", [240, 480]),
    "tl-6w":               ("https://whythelight.com/wp-content/uploads/2025/09/timeline-3women.png", [240, 480]),
    "tl-3m":               ("https://whythelight.com/wp-content/uploads/2025/09/timeline-3months-2.png", [240, 480]),
    "tl-12m":              ("https://whythelight.com/wp-content/uploads/2025/09/timeline-meditation.png", [240, 480]),
    "holding":             ("https://whythelight.com/wp-content/uploads/2025/11/HoldingPatch-clean-cropped-1024x759.png", [340, 680]),
    "badge":               ("https://whythelight.com/wp-content/uploads/2025/09/90-dayGuarantee.png", [160, 320]),
}

# ───── Vimeo + YouTube IDs for facade thumbnails ──────────────────────────
VIMEO_IDS = [
    "1133694650",  # VIMEO_MAIN
    "1131910398",  # VIMEO_DAVID
    "1118429044", "1118429946", "1118430693", "1118433583", "1118434636",
    "1118418475", "1118426413", "1153060029", "1118418454", "1118427670",
    "1118418407", "1118432346", "1118418371", "1118418429",
]
YOUTUBE_IDS = [
    "oxdeXAW08us",
]


def fetch(url: str, dest: Path) -> Path:
    """Fetch url to dest if not already cached."""
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    print(f"[get] {url} → {dest.name}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; PauliStaticBuilder/1.0)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        dest.write_bytes(resp.read())
    return dest


def convert_to_webp(src: Path, dest: Path, width: int | None = None, quality: int = 78) -> Path:
    """Convert src image to WebP at given width (preserve aspect)."""
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    cmd = ["cwebp", "-quiet", "-q", str(quality), "-mt"]
    if width:
        cmd += ["-resize", str(width), "0"]
    cmd += [str(src), "-o", str(dest)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"cwebp failed for {src}: {res.stderr}")
    return dest


def main():
    # ── PAGE IMAGES ──────────────────────────────────────────────────────
    tmp = SITE / ".tmp-orig"
    tmp.mkdir(exist_ok=True)
    manifest = {}
    for slug, (url, widths) in PAGE_IMAGES.items():
        orig = fetch(url, tmp / f"{slug}{Path(urllib.parse.urlparse(url).path).suffix.lower()}")
        manifest[slug] = {"widths": [], "src": url}
        for w in widths:
            out = IMG_DIR / f"{slug}-{w}.webp"
            convert_to_webp(orig, out, width=w, quality=78)
            manifest[slug]["widths"].append({"w": w, "file": f"/img/{slug}-{w}.webp", "bytes": out.stat().st_size})
        # also a non-resized full WebP for the "natural" intrinsic dimension
        full = IMG_DIR / f"{slug}.webp"
        convert_to_webp(orig, full, width=None, quality=78)
        manifest[slug]["natural"] = {"file": f"/img/{slug}.webp", "bytes": full.stat().st_size}

    # ── VIMEO THUMBNAILS via oEmbed ──────────────────────────────────────
    for vid in VIMEO_IDS:
        target = THUMB_DIR / f"vimeo-{vid}.webp"
        if target.exists() and target.stat().st_size > 0:
            continue
        try:
            req = urllib.request.Request(
                f"https://vimeo.com/api/oembed.json?url=https://vimeo.com/{vid}&width=600",
                headers={"User-Agent": "Mozilla/5.0"},
            )
            with urllib.request.urlopen(req, timeout=15) as r:
                meta = json.load(r)
            thumb_url = meta.get("thumbnail_url")
            if not thumb_url:
                print(f"[skip] vimeo {vid}: no thumbnail_url in oembed")
                continue
            raw = fetch(thumb_url, tmp / f"vimeo-{vid}.raw")
            convert_to_webp(raw, target, width=400, quality=72)
        except Exception as e:
            print(f"[warn] vimeo {vid}: {e}")

    # ── YOUTUBE THUMBNAILS via i.ytimg.com ───────────────────────────────
    for vid in YOUTUBE_IDS:
        target = THUMB_DIR / f"youtube-{vid}.webp"
        if target.exists() and target.stat().st_size > 0:
            continue
        try:
            raw = fetch(f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg", tmp / f"youtube-{vid}.raw")
            convert_to_webp(raw, target, width=800, quality=78)
        except Exception as e:
            print(f"[warn] youtube {vid}: {e}")

    # ── manifest for build_static.py to consume ──────────────────────────
    (SITE / "media-manifest.json").write_text(json.dumps(manifest, indent=2))
    # cleanup originals
    shutil.rmtree(tmp, ignore_errors=True)

    # ── summary ─────────────────────────────────────────────────────────
    img_total = sum(f.stat().st_size for f in IMG_DIR.glob("*.webp"))
    thumb_total = sum(f.stat().st_size for f in THUMB_DIR.glob("*.webp"))
    print(f"\n[done] img/    {len(list(IMG_DIR.glob('*.webp')))} files  {img_total/1024:.0f} KB")
    print(f"[done] thumbs/ {len(list(THUMB_DIR.glob('*.webp')))} files  {thumb_total/1024:.0f} KB")


if __name__ == "__main__":
    main()
