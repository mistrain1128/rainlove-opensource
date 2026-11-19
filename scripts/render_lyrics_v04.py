"""雨滴凝字: bilingual lyric track: per-glyph condense-in (fade + rise + defocus), sink-out."""
from pathlib import Path
import math
import re
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
FPS = 30000 / 1001
TOTAL = 7873
W, H = 1920, 1080
JP_BASE, ZH_BASE = 930, 984
FONTS = ROOT / "fonts"
JP = ImageFont.truetype(str(FONTS / "NotoSerifJP-Medium.ttf"), 52)
ZH = ImageFont.truetype(str(FONTS / "NotoSerifSC-Regular.ttf"), 34)
FILL = (247, 250, 252, 255)
EDGE = (8, 12, 18, 120)
SHADOW = (5, 8, 12, 130)
GLOW = (140, 180, 225, 70)
BLOOM = (255, 255, 255, 110)
BLUR_LEVELS = 8


def clamp(x):
    return max(0.0, min(1.0, x))


def smooth(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def frame(stamp):
    h, m, s, ms = map(int, re.split(r"[:,]", stamp))
    return round((3600 * h + 60 * m + s + ms / 1000) * FPS)


def cues():
    for block in (ROOT.parent / "lyrics" / "rainlove_ja_zh.srt").read_text(encoding="utf-8-sig").strip().split("\n\n"):
        _, times, jp, zh = block.splitlines()
        start, end = map(frame, times.split(" --> "))
        yield start, end, jp, zh


_sprites = {}


def sprites(font, ch, glow):
    key = (id(font), ch, glow)
    hit = _sprites.get(key)
    if hit:
        return hit
    stroke = 3 if glow else 1
    l, t, r, b = font.getbbox(ch, anchor="ls", stroke_width=stroke)
    pad = 12
    size = (r - l + pad * 2, b - t + pad * 2)
    pos = (pad - l, pad - t)
    base = Image.new("RGBA", size)
    if glow:
        layer = Image.new("RGBA", size)
        ImageDraw.Draw(layer).text(pos, ch, font=font, anchor="ls",
                                   fill=GLOW, stroke_width=3, stroke_fill=GLOW)
        base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(7)))
    layer = Image.new("RGBA", size)
    ImageDraw.Draw(layer).text((pos[0], pos[1] + 2), ch, font=font, anchor="ls",
                               fill=SHADOW, stroke_width=2, stroke_fill=SHADOW)
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(3.5)))
    ImageDraw.Draw(base).text(pos, ch, font=font, anchor="ls",
                              fill=FILL, stroke_width=1, stroke_fill=EDGE)
    levels = [base] + [base.filter(ImageFilter.GaussianBlur(i * 0.9))
                       for i in range(1, BLUR_LEVELS)]
    bloom = Image.new("RGBA", size)
    ImageDraw.Draw(bloom).text(pos, ch, font=font, anchor="ls",
                               fill=BLOOM, stroke_width=2, stroke_fill=BLOOM)
    bloom = bloom.filter(ImageFilter.GaussianBlur(6))
    hit = (levels, bloom, l - pad, t - pad)
    _sprites[key] = hit
    return hit


def draw(im, sprite, x, y, opacity):
    if opacity <= 0.004:
        return
    if opacity < 0.997:
        sprite = sprite.copy()
        sprite.putalpha(sprite.getchannel("A").point([round(i * opacity) for i in range(256)]))
    im.alpha_composite(sprite, (round(x), round(y)))


def row(im, text, font, baseline, t, dur, *, is_jp, glow=False):
    n = len(text)
    widths = [font.getlength(ch) for ch in text]
    tracking = (9 if n < 10 else 6.5 if n < 17 else 5) if is_jp else 3
    left = (W - sum(widths) - (n - 1) * tracking) / 2
    stag = min(0.06 if is_jp else 0.05,
               max(0.02 if is_jp else 0.015, (dur - 1.50) / max(1, n - 1)))
    flight = 0.85 if is_jp else 0.75
    rise = 10 if is_jp else 8
    maxop = 1.0 if is_jp else 0.85
    exit_start = dur - 0.55
    for i, (ch, w) in enumerate(zip(text, widths)):
        u = clamp((t - stag * i) / flight)
        if u > 0 and not ch.isspace():
            e = 1 - (1 - u) ** 2.6
            op = smooth(u) ** 1.2 * maxop
            y = baseline + rise * (1 - e)
            v = clamp((t - exit_start - 0.03 * i) / 0.5)
            bloom_op = 0.5 * math.sin(math.pi * u) ** 1.2
            if v > 0:
                op *= 1 - smooth(v)
                y += 8 * v * v
                bloom_op = max(bloom_op * (1 - v), 0.3 * math.sin(math.pi * v))
            blur = max((1 - e) * 7, v * 4)
            level = min(BLUR_LEVELS - 1, int(blur + 0.5))
            levels, bloom, ox, oy = sprites(font, ch, glow)
            if bloom_op > 0.01:
                draw(im, bloom, left + ox, y + oy, bloom_op * maxop)
            draw(im, levels[level], left + ox, y + oy, op)
        left += w + tracking


def main():
    events = tuple(cues())
    assert len(events) == 46
    assert all(a[1] <= b[0] for a, b in zip(events, events[1:]))
    ffmpeg = subprocess.Popen([
        "ffmpeg", "-v", "error", "-f", "rawvideo", "-pixel_format", "rgba",
        "-video_size", f"{W}x{H}", "-framerate", "30000/1001", "-i", "pipe:0",
        "-vf", "format=argb", "-an", "-c:v", "qtrle", "-y",
        str(ROOT / (sys.argv[1] if len(sys.argv) > 1 else "RainLove_Lyric_Track_v04.mov"))
    ], stdin=subprocess.PIPE)
    blank = bytes(W * H * 4)
    index = 0
    try:
        for f in range(TOTAL):
            while index < len(events) and f >= events[index][1]:
                index += 1
            t = f / FPS
            if index == len(events) or f < events[index][0]:
                raw = blank
            else:
                start, end, jp, zh = events[index]
                dur = (end - start) / FPS
                ct = (f - start) / FPS
                glow = ("Rainie love" in jp) or ("虹を信じてる" in jp)
                im = Image.new("RGBA", (W, H))
                row(im, jp, JP, JP_BASE, ct, dur, is_jp=True, glow=glow)
                lead = 0.18
                if ct > lead:
                    row(im, zh, ZH, ZH_BASE, ct - lead, dur - lead, is_jp=False, glow=glow)
                raw = im.tobytes()
            ffmpeg.stdin.write(raw)
    finally:
        ffmpeg.stdin.close()
    if ffmpeg.wait():
        raise RuntimeError("Lyric render failed")
    print(f"{len(events)} cues, {TOTAL} frames rendered")


if __name__ == "__main__":
    main()