"""Generate the og:image at site/img/og.png — 1200×630, dark + gold brand."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os

ROOT = Path(__file__).parent
OUT = ROOT / "site" / "img" / "og.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

W, H = 1200, 630
img = Image.new("RGB", (W, H), "#000000")
d = ImageDraw.Draw(img)

# Decorative gold dot pattern in the background
import random
random.seed(42)
for _ in range(80):
    x = random.randint(0, W)
    y = random.randint(0, H)
    r = random.randint(1, 3)
    op = random.randint(50, 150)
    d.ellipse([x-r, y-r, x+r, y+r], fill=(212, 169, 74, op))

# Find a system font
def find_font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Geneva.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    if bold:
        candidates = [
            "/System/Library/Fonts/SFNSDisplay-Bold.otf",
            "/System/Library/Fonts/HelveticaBold.ttc",
        ] + candidates
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

f_big = find_font(78, bold=True)
f_med = find_font(40)
f_small = find_font(28)

# Title
title = "Luz en tu cuerpo"
sub = "Pauli Wellness · Fototerapia LifeWave X39"
tagline = "Dos décadas de ciencia · +200 patentes globales"

# Center vertically
y = H // 2 - 150
d.text((W // 2, y), title, fill="#ffffff", font=f_big, anchor="mm")
# Gold accent under title
d.rectangle([W // 2 - 80, y + 60, W // 2 + 80, y + 64], fill="#d4a94a")
y += 130
d.text((W // 2, y), sub, fill="#d4a94a", font=f_med, anchor="mm")
y += 80
d.text((W // 2, y), tagline, fill="#bdbdbd", font=f_small, anchor="mm")

# Bottom domain
d.text((W // 2, H - 60), "luzentucuerpo.com", fill="#777777", font=f_small, anchor="mm")

img.save(OUT, optimize=True)
print(f"Wrote {OUT}  ({OUT.stat().st_size:,} bytes)")
