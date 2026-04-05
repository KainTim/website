#!/usr/bin/env python3
"""
Logo & Favicon Generator
Extracted from CSS color scheme:
  Background:   #161b22 (dark navy)
  Border:       #30363d (dark grey)
  Primary text: #e6edf3 (near-white)
  Secondary:    #c9d1d9 (light grey)
  Muted:        #8b949e (medium grey)
  Accent:       #2f81f7 (vivid blue)

Outputs:
  logo.png      — 600 × 180 px  (wide wordmark)
  logo@2x.png   — 1200 × 360 px (retina)
  favicon.ico   — 16×16, 32×32, 48×48 multi-size ICO
  favicon-32.png
  favicon-16.png
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os
import struct
import io

# ── Palette ────────────────────────────────────────────────────────────────────
BG        = (22,  27,  34,  255)   # #161b22
BORDER    = (48,  54,  61,  255)   # #30363d
TEXT_PRI  = (230, 237, 243, 255)   # #e6edf3
TEXT_SEC  = (201, 209, 217, 255)   # #c9d1d9
TEXT_MUTE = (139, 148, 158, 255)   # #8b949e
ACCENT    = (47,  129, 247, 255)   # #2f81f7
ACCENT_DIM= (47,  129, 247,  36)   # translucent blue fill

# ── Helpers ────────────────────────────────────────────────────────────────────

def lerp_color(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(4))


def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill,
                            outline=outline, width=width)


def add_glow(img, center, radius, color, intensity=0.55):
    """Soft radial glow overlay using additive blending."""
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(glow)
    cx, cy = center
    steps = 18
    for i in range(steps, 0, -1):
        t = i / steps
        r = int(radius * t)
        alpha = int(intensity * (1 - t) ** 0.6 * 255)
        c = (*color[:3], alpha)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    return Image.alpha_composite(img, glow)


def make_font(size):
    """Try to load a system sans-serif; fall back to PIL default."""
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                pass

    # Ask fontconfig for whatever sans-serif is available
    try:
        import subprocess
        result = subprocess.run(
              ["fc-match", "--format=%{file}", "sans-serif:bold"],
              capture_output=True, text=True
        )
        path = result.stdout.strip()
        if path:
              return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default(size)


def make_font_regular(size):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
        "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                pass
    # Ask fontconfig for whatever sans-serif is available
    try:
      import subprocess
      result = subprocess.run(
        ["fc-match", "--format=%{file}", "sans-serif"],
        capture_output=True, text=True
      )
      path = result.stdout.strip()
      if path:
        return ImageFont.truetype(path, size)
    except Exception:
      pass
    return ImageFont.load_default(size)

# ── Icon mark (the "gem" shape) ────────────────────────────────────────────────

def draw_icon_mark(draw, img, cx, cy, size):
    """
    Draw a stylised hexagonal mark:
    - dark fill with blue border
    - inner accent diamond
    - subtle glow
    """
    s = size
    # Flat-top hexagon vertices
    hex_pts = [
        (cx + s * math.cos(math.radians(a)),
         cy + s * math.sin(math.radians(a)))
        for a in range(0, 360, 60)
    ]

    # Fill with subtle gradient-like layering
    for layer in range(int(s), 0, -1):
        t = layer / s
        col = lerp_color(
            (35, 43, 54, 255),
            (22, 27, 34, 255),
            t
        )
        pts = [
            (cx + layer * math.cos(math.radians(a)),
             cy + layer * math.sin(math.radians(a)))
            for a in range(0, 360, 60)
        ]
        draw.polygon(pts, fill=col)

    # Border
    draw.polygon(hex_pts, outline=ACCENT[:3] + (200,), width=max(2, size // 18))

    # Inner diamond
    d = s * 0.42
    diamond = [
        (cx,     cy - d),
        (cx + d, cy),
        (cx,     cy + d),
        (cx - d, cy),
    ]
    draw.polygon(diamond, fill=ACCENT[:3] + (230,))

    # Tiny highlight dot
    h = s * 0.12
    draw.ellipse([cx - h, cy - h - d * 0.28,
                  cx + h, cy + h - d * 0.28],
                 fill=(255, 255, 255, 180))

    return img

# ── Logo ───────────────────────────────────────────────────────────────────────

def build_logo(width=600, height=180, scale=1):
    W, H = width * scale, height * scale
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    pad = int(16 * scale)
    radius = int(20 * scale)

    # Background card
    draw_rounded_rect(draw,
                      [pad, pad, W - pad, H - pad],
                      radius=radius,
                      fill=BG,
                      outline=BORDER[:3],
                      width=max(1, scale))

    icon_cx = int(H * 0.5)
    icon_cy = int(H * 0.5)
    icon_r  = int(H * 0.28)

    # Glow clipped to card bounds
    card = img.crop([pad, pad, W - pad, H - pad])
    glow_cx = icon_cx - pad
    glow_cy = icon_cy - pad
    card = add_glow(card, (glow_cx, glow_cy), int(icon_r * 1.6), ACCENT, 0.28)
    img.paste(card, (pad, pad))

    draw = ImageDraw.Draw(img)

    # Icon mark
    draw_icon_mark(draw, img, icon_cx, icon_cy, icon_r)
    draw = ImageDraw.Draw(img)   # refresh after composite

    # Text area
    text_x = icon_cx + icon_r + int(22 * scale)
    brand_font  = make_font(int(38 * scale))
    sub_font    = make_font_regular(int(16 * scale))

    brand_text = "YourBrand"
    sub_text   = "Your tagline here"

    # Brand name
    draw.text((text_x, int(H * 0.22)), brand_text,
              font=brand_font, fill=TEXT_PRI)

    # Accent underline
    bbox = draw.textbbox((text_x, int(H * 0.22)), brand_text, font=brand_font)
    uw = bbox[2] - bbox[0]
    uy = bbox[3] + int(4 * scale)

    draw.rectangle([text_x, uy, text_x + uw, uy + max(2, int(3 * scale))],
                   fill=ACCENT[:3])

    # Subtitle
    draw.text((text_x, int(H * 0.63)), sub_text,
              font=sub_font, fill=TEXT_MUTE)

    # Thin right-side accent bar
    bar_x = W - pad - max(3, int(4 * scale))
    draw.rectangle([bar_x, pad + radius,
                    bar_x + max(3, int(4 * scale)), H - pad - radius],
                   fill=ACCENT[:3] + (120,))

    return img

# ── Favicon mark ───────────────────────────────────────────────────────────────

def build_favicon_image(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    pad = max(1, size // 24)
    radius = max(2, size // 8)

    # Background
    draw_rounded_rect(draw,
                      [pad, pad, size - pad, size - pad],
                      radius=radius,
                      fill=BG,
                      outline=BORDER[:3],
                      width=max(1, size // 24))

    cx, cy = size // 2, size // 2
    icon_r = int(size * 0.30)

    card = img.crop([pad, pad, size - pad, size - pad])
    card = add_glow(card, (cx - pad, cy - pad), int(icon_r * 1.6), ACCENT, 0.28)
    img.paste(card, (pad, pad))

    draw = ImageDraw.Draw(img)
    draw_icon_mark(draw, img, cx, cy, icon_r)

    return img

# ── ICO writer ─────────────────────────────────────────────────────────────────

def save_ico(images_dict, path):
    """
    images_dict: {size: PIL.Image, ...}  e.g. {16: img16, 32: img32, 48: img48}
    """
    sizes = sorted(images_dict.keys())
    entries = []
    png_data_list = []

    for s in sizes:
        img = images_dict[s].convert("RGBA")
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        data = buf.getvalue()
        png_data_list.append(data)
        entries.append((s, len(data)))

    # ICO header: RESERVED(2) TYPE(2) COUNT(2)
    header = struct.pack("<HHH", 0, 1, len(sizes))

    # Directory entries (16 bytes each), offsets calculated after header + dir
    dir_size = 16 * len(sizes)
    offset = 6 + dir_size
    directory = b""
    for i, (s, data_len) in enumerate(entries):
        w = s if s < 256 else 0
        h = s if s < 256 else 0
        directory += struct.pack("<BBBBHHII",
                                 w, h,       # width, height (0 = 256)
                                 0,           # color count
                                 0,           # reserved
                                 1,           # color planes
                                 32,          # bits per pixel
                                 data_len,
                                 offset)
        offset += data_len

    with open(path, "wb") as f:
        f.write(header + directory)
        for data in png_data_list:
            f.write(data)

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    out_dir = "./logos"
    os.makedirs(out_dir, exist_ok=True)

    print("Generating logo.png  (600×180) …")
    logo = build_logo(600, 180, scale=1)
    logo.save(os.path.join(out_dir, "logo.png"))

    print("Generating logo@2x.png  (1200×360) …")
    logo2x = build_logo(600, 180, scale=2)
    logo2x.save(os.path.join(out_dir, "logo@2x.png"))

    print("Generating favicon PNGs …")
    fav16 = build_favicon_image(16)
    fav32 = build_favicon_image(32)
    fav48 = build_favicon_image(48)
    fav64 = build_favicon_image(64)
    fav128 = build_favicon_image(128)
    fav16.save(os.path.join(out_dir, "favicon-16.png"))
    fav32.save(os.path.join(out_dir, "favicon-32.png"))
    fav64.save(os.path.join(out_dir, "favicon-64.png"))
    fav128.save(os.path.join(out_dir, "favicon-128.png"))

    print("Generating favicon.ico  (48 + 64 + 128) …")
    save_ico({ 48: fav48, 64: fav64, 128: fav128},
             os.path.join(out_dir, "favicon.ico"))

    print("\nDone! Files written:")
    for name in ("logo.png", "logo@2x.png",
                 "favicon-16.png", "favicon-32.png", "favicon.ico"):
        path = os.path.join(out_dir, name)
        size_kb = os.path.getsize(path) / 1024
        print(f"  {name:<20}  {size_kb:.1f} KB")

    print("""
Customisation tips
──────────────────
• Change `brand_text` and `sub_text` near the top of build_logo().
• Swap the palette constants at the top of the file.
• The icon mark is drawn in draw_icon_mark() — replace it with an SVG
  path or raster image to use your own symbol.
• Call build_logo(scale=3) for a 1800×540 print-resolution version.
""")


if __name__ == "__main__":
    main()
