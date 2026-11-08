#!/usr/bin/env python3
"""AE-Style-Kern (aus promo\\beispiel_2026-11-08\\ae\\render.py, User 08.11.: alle Videos im After-Effects-Style).
Wird von ae.py konfiguriert (SEGS/starts/TRANS/IMPACTS/LEAKS/CHUNKS). Nicht direkt aufrufen."""
import sys, os, json, math, subprocess
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy.interpolate import PchipInterpolator

W, H, FPS = 1080, 1920, 60
MW, MH = 1540, 726                 # master res for clip frames
FG_W0, FG_H, FG_Y = 1350, 636, 642 # game band: ~80% of width visible
CLIPS = "/mnt/user-data/uploads/SkipAHook_Meshes/promo/clips"
F_BLACK_I = "/usr/share/fonts/opentype/inter/InterDisplay-BlackItalic.otf"
F_BLACK = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
HEAD_Y = 505      # headline centre (safe zone, below camera island)
SUB_Y = 1345      # captions centre (above bottom UI)
GOLD = ((255, 240, 120), (255, 166, 30))
CYAN = (90, 220, 255)

SEGS = []; starts = [0.0]; TOTAL = 1.0; NF = 1; CUTS = []; TRANS = {}; IMPACTS = []; LEAKS = []; CHUNKS = []

# ---------------------------------------------------------------- easing
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def e_out3(x): x = clamp(x); return 1 - (1 - x) ** 3
def e_in3(x): x = clamp(x); return x ** 3
def e_io3(x): x = clamp(x); return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
def e_outexpo(x): x = clamp(x); return 1 if x >= 1 else 1 - 2 ** (-10 * x)
def spring(t, f=3.2, z=0.42):
    """0->1 damped spring (t seconds)."""
    if t <= 0: return 0.0
    w = 2 * math.pi * f; wd = w * math.sqrt(1 - z * z)
    return 1 - math.exp(-z * w * t) * (math.cos(wd * t) + z * w / wd * math.sin(wd * t))

# ---------------------------------------------------------------- sprites
_cache = {}
def _font(path, size):
    k = (path, size)
    if k not in _cache: _cache[k] = ImageFont.truetype(path, size)
    return _cache[k]

def to_premul(img):
    a = np.asarray(img).astype(np.float32) / 255.0
    a[..., :3] *= a[..., 3:4]
    return a

def text_sprite(text, size, font=F_BLACK_I, grad=None, fill=(255, 255, 255), stroke=None, glow=None):
    key = ("t", text, size, font, grad, fill, stroke, glow)
    if key in _cache: return _cache[key]
    f = _font(font, size)
    sw = stroke if stroke is not None else max(4, size // 11)
    asc, desc = f.getmetrics()
    tw = f.getlength(text)
    pad = sw + 34; extra = int(size * 0.18)
    w, h = int(tw + 2 * pad + extra), int(asc + desc + 2 * pad)
    base = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(base)
    d.text((pad, pad), text, font=f, fill=(12, 10, 24, 255), stroke_width=sw, stroke_fill=(12, 10, 24, 255))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).text((pad, pad), text, font=f, fill=255)
    if grad:
        g = np.zeros((h, w, 4), np.uint8)
        t = np.linspace(0, 1, h)[:, None]
        top = pad + asc * 0.25; bot = pad + asc
        tt = np.clip((np.arange(h) - top) / (bot - top), 0, 1)[:, None]
        for c in range(3): g[..., c] = (grad[0][c] * (1 - tt) + grad[1][c] * tt).astype(np.uint8)
        g[..., 3] = 255
        base.paste(Image.fromarray(g, "RGBA"), (0, 0), mask)
    else:
        base.paste(Image.new("RGBA", (w, h), fill + (255,)), (0, 0), mask)
    alpha = base.split()[3]
    sh = Image.new("RGBA", (w, h), (0, 0, 0, 0)); sh.putalpha(alpha.filter(ImageFilter.GaussianBlur(9)).point(lambda v: int(v * 0.6)))
    spr = dict(img=to_premul(base), shadow=to_premul(sh), w=w, h=h, tw=tw, pad=pad, asc=asc, extra=extra, size=size)
    if glow:
        gl = Image.new("RGBA", (w, h), glow + (0,))
        gl.putalpha(mask.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(size * 0.22)))
        spr["glow"] = to_premul(gl)
    _cache[key] = spr
    return spr

def blit(dst, src, cx, cy, scale=1.0, rot=0.0, alpha=1.0, add=False):
    if alpha <= 0.003 or scale <= 0.01: return
    h, w = src.shape[:2]
    if abs(scale - 1) < 1e-3 and abs(rot) < 1e-3:
        out, ow, oh = src, w, h
    else:
        c, s = abs(math.cos(math.radians(rot))), abs(math.sin(math.radians(rot)))
        ow = int(w * scale * c + h * scale * s) + 2; oh = int(w * scale * s + h * scale * c) + 2
        M = cv2.getRotationMatrix2D((w / 2, h / 2), rot, scale)
        M[0, 2] += ow / 2 - w / 2; M[1, 2] += oh / 2 - h / 2
        out = cv2.warpAffine(src, M, (ow, oh), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    x0, y0 = int(round(cx - ow / 2)), int(round(cy - oh / 2))
    X0, Y0, X1, Y1 = max(0, x0), max(0, y0), min(dst.shape[1], x0 + ow), min(dst.shape[0], y0 + oh)
    if X1 <= X0 or Y1 <= Y0: return
    o = out[Y0 - y0:Y1 - y0, X0 - x0:X1 - x0]
    roi = dst[Y0:Y1, X0:X1]
    if add:
        roi += o[..., :3] * alpha
    else:
        a = o[..., 3:4] * alpha
        roi *= (1 - a); roi += o[..., :3] * alpha

# ---------------------------------------------------------------- layout of kinetic lines
def layout_line(words, keys, max_w=960, size0=118, min1=88, font=F_BLACK_I, glowcol=GOLD[1]):
    def mk(size):
        sp = []
        for wd in words:
            k = wd in keys
            sp.append(text_sprite(wd, size, font, grad=GOLD if k else None, glow=glowcol if k else None))
        return sp
    def width(sp, size): return sum(s["tw"] for s in sp) + _font(font, size).getlength(" ") * (len(sp) - 1)
    for size in range(size0, min1 - 1, -4):
        sp = mk(size)
        if width(sp, size) <= max_w: return [(sp, size)]
    # two lines, balanced
    best = None
    for cut in range(1, len(words)):
        a, b = words[:cut], words[cut:]
        diff = abs(len(" ".join(a)) - len(" ".join(b)))
        if best is None or diff < best[0]: best = (diff, cut)
    cut = best[1]
    for size in range(104, 50, -4):
        la, lb = mk(size)[:cut], mk(size)[cut:]
        if max(width(la, size), width(lb, size)) <= max_w: return [(la, size), (lb, size)]
    return [(mk(56), 56)]

def place_lines(lines, cy, font=F_BLACK_I):
    """returns list of (sprite, x_center, y_center, index)"""
    out = []; idx = 0
    lh = lines[0][1] * 1.06
    y_first = cy - (len(lines) - 1) * lh / 2
    for li, (sp, size) in enumerate(lines):
        f = _font(font, size)
        space = f.getlength(" ")
        tot = sum(s["tw"] for s in sp) + space * (len(sp) - 1)
        x = W / 2 - tot / 2
        ly = y_first + li * lh
        cap = size * 0.73
        for s in sp:
            xc = x + s["tw"] / 2 + s["extra"] / 2
            baseline = ly + cap / 2
            yc = baseline - (s["pad"] + s["asc"]) + s["h"] / 2
            out.append((s, xc, yc, idx)); idx += 1
            x += s["tw"] + space
    return out

# ---------------------------------------------------------------- subtitles (karaoke chunks)
def draw_captions(fr, T):
    for ch in CHUNKS:
        if not (ch["t0"] <= T < ch["t1"]): continue
        size = 66
        words = ch["words"]
        f = _font(F_BLACK, size)
        sp_w = [text_sprite(w[0], size, F_BLACK, stroke=9) for w in words]
        space = f.getlength(" ")
        tot = sum(s["tw"] for s in sp_w) + space * (len(words) - 1)
        sc0 = min(1.0, 940 / tot)
        lt = T - ch["t0"]
        enter = 0.86 + 0.14 * spring(lt, 4.0, 0.5)
        x = W / 2 - tot * sc0 / 2
        for (wd, ws, we), s in zip(words, sp_w):
            active = ws - 0.02 <= T
            cur = active and (T < we + 0.05 or (wd, ws, we) == words[-1])
            spr = text_sprite(wd, size, F_BLACK, stroke=9, fill=(255, 225, 60) if cur else (255, 255, 255))
            bump = 1 + 0.12 * (1 - spring(T - ws, 5, 0.5)) * (1 if T >= ws else 0) if active else 1
            al = clamp(lt / 0.06) * (1.0 if active else 0.92)
            xc = x + s["tw"] * sc0 / 2 + s["extra"] * sc0 / 2
            yc = SUB_Y + (s["h"] / 2 - s["pad"] - s["asc"] + size * 0.365) * sc0
            sc = sc0 * enter * bump
            blit(fr, spr["shadow"], xc, yc + 6, sc, 0, al * 0.8)
            blit(fr, spr["img"], xc, yc, sc, 0, al)
            x += (s["tw"] + space) * sc0
        break

# ---------------------------------------------------------------- headline animation
BAR_HOOK = lambda fr, s, lt: rarity_bar(fr, lt)

def draw_headline(fr, seg, lt, T):
    heads = seg["head"]
    for hi, (h0, text, keys) in enumerate(heads):
        h1 = heads[hi + 1][0] if hi + 1 < len(heads) else seg["dur"] + 1
        if not (h0 <= lt < h1): continue
        t = lt - h0
        words = text.split()
        num = None
        if "counter" in seg:
            a, b = seg["counter"]
            p = e_outexpo((t - 0.35) / 0.9)
            num = str(int(round(a + (b - a) * p)))
            words = [num if w == "#" else w for w in words]
            keys = keys | {num}
        lines = layout_line(words, keys)
        placed = place_lines(lines, HEAD_Y)
        exit_p = clamp((lt - (h1 - 0.14)) / 0.14) if h1 <= seg["dur"] else 0
        for spr, xc, yc, i in placed:
            ti = t - i * 0.06
            if ti <= 0: continue
            sc = 0.25 + 0.75 * spring(ti, 3.0, 0.38)
            dy = (1 - e_out3(ti / 0.3)) * 60
            rot = (1 - e_out3(ti / 0.35)) * 10
            al = clamp(ti / 0.07)
            if num is not None and spr["tw"] == text_sprite(num, spr["size"], F_BLACK_I, grad=GOLD, glow=GOLD[1])["tw"] and t > 1.25:
                sc *= 1 + 0.18 * (1 - spring(t - 1.25, 4, 0.35))
            sc *= 1 + 0.2 * e_in3(exit_p); al *= 1 - exit_p
            yy = yc + dy
            if "glow" in spr:
                pulse = 0.75 + 0.25 * math.sin(T * 6.0)
                blit(fr, spr["glow"], xc, yy, sc * 1.02, rot, al * pulse, add=True)
            blit(fr, spr["shadow"], xc + 4, yy + 10, sc, rot, al)
            blit(fr, spr["img"], xc, yy, sc, rot, al)

# ---------------------------------------------------------------- rarity bar
def rarity_bar(fr, lt, cy=604):
    if "bar" not in _cache:
        bw, bh = 520, 22
        cols = [(170, 170, 170), (80, 220, 110), (60, 150, 255), (190, 90, 255), (255, 200, 40)]
        xs = np.linspace(0, 1, bw)
        g = np.zeros((bh, bw, 3), np.float32)
        for c in range(3):
            g[..., c] = np.interp(xs, np.linspace(0, 1, len(cols)), [k[c] for k in cols])[None, :] / 255
        m = Image.new("L", (bw, bh), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, bw - 1, bh - 1), bh // 2, fill=255)
        m = np.asarray(m).astype(np.float32)[..., None] / 255
        trk = Image.new("RGBA", (bw + 12, bh + 12), (0, 0, 0, 0))
        ImageDraw.Draw(trk).rounded_rectangle((0, 0, bw + 11, bh + 11), (bh + 12) // 2, fill=(10, 10, 25, 200), outline=(255, 255, 255, 110), width=3)
        _cache["bar"] = (g, m, to_premul(trk))
    g, m, trk = _cache["bar"]
    a = e_out3((lt - 0.3) / 0.35)
    if a <= 0: return
    blit(fr, trk, W / 2, cy, 0.9 + 0.1 * a, 0, a)
    l1 = text_sprite("COMMON", 30, F_BLACK_I, fill=(200, 200, 210), stroke=5)
    l2 = text_sprite("SECRET", 30, F_BLACK_I, grad=GOLD, stroke=5, glow=GOLD[1])
    blit(fr, l1["img"], W / 2 - 260 - 20 - l1["tw"] / 2, cy + 2, 1, 0, a)
    blit(fr, l2["glow"], W / 2 + 260 + 20 + l2["tw"] / 2, cy + 2, 1, 0, a * 0.8, add=True)
    blit(fr, l2["img"], W / 2 + 260 + 20 + l2["tw"] / 2, cy + 2, 1, 0, a)
    p = e_io3((lt - 0.55) / 2.2)
    fw = int(520 * p)
    if fw > 2:
        x0, y0 = int(W / 2 - 260), int(cy - 11)
        roi = fr[y0:y0 + 22, x0:x0 + fw]
        mm = m[:, :fw] * a
        roi *= (1 - mm); roi += g[:, :fw] * mm
        # glowing head
        dot = _cache.get("dot")
        if dot is None:
            d = np.zeros((90, 90, 4), np.float32); yy, xx = np.mgrid[:90, :90]
            r = np.exp(-((xx - 45) ** 2 + (yy - 45) ** 2) / (2 * 14 ** 2))
            d[..., 0] = r; d[..., 1] = r * 0.95; d[..., 2] = r * 0.8; d[..., 3] = r
            _cache["dot"] = dot = d
        blit(fr, dot, x0 + fw, cy, 1.0, 0, a * 0.9, add=True)

# ---------------------------------------------------------------- end card
def endcard(fr, lt):
    title = "SKIP A HOOK"
    size = 150
    if "title" not in _cache:
        f = _font(F_BLACK_I, size)
        while f.getlength(title) > 900: size -= 4; f = _font(F_BLACK_I, size)
        _cache["title"] = size
    size = _cache["title"]; f = _font(F_BLACK_I, size)
    x = W / 2 - f.getlength(title) / 2
    cy = 880
    for i, ch in enumerate(title):
        adv = f.getlength(ch)
        if ch == " ": x += adv; continue
        hook = i >= 7
        spr = text_sprite(ch, size, F_BLACK_I, grad=GOLD if hook else None, glow=GOLD[1] if hook else CYAN)
        ti = lt - 0.12 - i * 0.04
        if ti > 0:
            sc = 1 + 1.6 * (1 - e_out3(ti / 0.16))
            al = clamp(ti / 0.08)
            xc = x + spr["tw"] / 2 + spr["extra"] / 2
            yc = cy + size * 0.365 - (spr["pad"] + spr["asc"]) + spr["h"] / 2
            pulse = 0.7 + 0.3 * math.sin(lt * 5 + i * 0.5)
            blit(fr, spr["glow"], xc, yc, sc, 0, al * pulse, add=True)
            blit(fr, spr["shadow"], xc + 5, yc + 12, sc, 0, al)
            blit(fr, spr["img"], xc, yc, sc, 0, al)
        x += adv
    # pill
    if "pill" not in _cache:
        pw, ph = 700, 112
        im = Image.new("RGBA", (pw + 60, ph + 60), (0, 0, 0, 0))
        sh = Image.new("L", im.size, 0); ImageDraw.Draw(sh).rounded_rectangle((30, 40, 30 + pw, 40 + ph), ph // 2, fill=170)
        sh = sh.filter(ImageFilter.GaussianBlur(12))
        im.putalpha(sh)
        im = Image.composite(Image.new("RGBA", im.size, (0, 0, 0, 255)), Image.new("RGBA", im.size, (0, 0, 0, 0)), sh)
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((30, 30, 30 + pw, 30 + ph), ph // 2, fill=(255, 255, 255, 255))
        cx0, cy0 = 30 + 70, 30 + ph // 2
        d.ellipse((cx0 - 22, cy0 - 26, cx0 + 18, cy0 + 14), outline=(20, 20, 30, 255), width=8)
        d.line((cx0 + 12, cy0 + 8, cx0 + 30, cy0 + 26), fill=(20, 20, 30, 255), width=10)
        ft = _font(F_BLACK, 50)
        tx = "SEARCH ON ROBLOX"
        d.text((30 + 120 + (pw - 150 - ft.getlength(tx)) / 2, cy0), tx, font=ft, fill=(18, 18, 28, 255), anchor="lm")
        mask = Image.new("L", im.size, 0); ImageDraw.Draw(mask).rounded_rectangle((30, 30, 30 + pw, 30 + ph), ph // 2, fill=255)
        _cache["pill"] = (to_premul(im), np.asarray(mask).astype(np.float32) / 255)
    pill, pm = _cache["pill"]
    tp = lt - 0.75
    if tp > 0:
        sc = 0.2 + 0.8 * spring(tp, 3.0, 0.4)
        blit(fr, pill, W / 2, 1035, sc, 0, clamp(tp / 0.08))
        # shine sweep
        sp = (tp - 0.5) / 0.55
        if 0 < sp < 1 and sc > 0.95:
            hh, ww = pm.shape
            yy, xx = np.mgrid[:hh, :ww]
            pos = -150 + sp * (ww + 300)
            band = np.exp(-((xx - 0.35 * yy - pos) ** 2) / (2 * 28 ** 2)) * pm * 0.75
            sh = np.zeros((hh, ww, 4), np.float32); sh[..., :3] = band[..., None]; sh[..., 3] = band
            blit(fr, sh, W / 2, 1035, sc, 0, 1.0, add=False)

# ---------------------------------------------------------------- clip loading & per-segment rendering
def load_seg(i):
    s = SEGS[i]
    if "ramp" in s:
        k = np.array(s["ramp"], float)
        s["_r"] = PchipInterpolator(k[:, 0], k[:, 1])
    else:
        s["_r"] = lambda t: t
    ts = np.linspace(0, s["dur"], 200)
    r = np.asarray(s["_r"](ts))
    lo, hi = max(0, r.min() - 0.05), r.max() + 0.1
    start = s["src"] + lo
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{start:.3f}", "-t", f"{hi - lo:.3f}", "-i", f"{CLIPS}/{s['clip']}.mp4",
           "-vf", f"fps={FPS},scale={MW}:{MH}:flags=lanczos", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, MH, MW, 3)
    s["_frames"], s["_lo"] = fr, lo
    print(f"loaded seg {i} {s['clip']} {len(fr)} frames", flush=True)

def get_src(s, lt):
    r = float(s["_r"](lt)) - s["_lo"]
    fi = r * FPS
    n = len(s["_frames"])
    a = int(math.floor(fi)); fr_ = fi - a
    a = min(max(a, 0), n - 1); b = min(a + 1, n - 1)
    if fr_ < 0.15 or a == b: return s["_frames"][a]
    if fr_ > 0.85: return s["_frames"][b]
    return cv2.addWeighted(s["_frames"][a], 1 - fr_, s["_frames"][b], fr_, 0)

# band shadow / vignette / grain (precomputed)
yy = np.arange(H)[:, None].astype(np.float32)
d_out = np.maximum(FG_Y - yy, yy - (FG_Y + FG_H))
BAND_SH = (1 - 0.55 * np.exp(-np.maximum(d_out, 0) / 70.0) * (d_out > 0)).astype(np.float32)[..., None]
vy, vx = np.mgrid[:H, :W].astype(np.float32)
VIG = (1 - 0.42 * np.clip((((vx - W / 2) / (W * 0.75)) ** 2 + ((vy - H / 2) / (H * 0.62)) ** 2), 0, 1) ** 1.4)[..., None].astype(np.float32)
rng = np.random.default_rng(7)
GRAIN = [cv2.resize(rng.normal(0, 1, (H // 2, W // 2)).astype(np.float32), (W, H))[..., None] for _ in range(4)]
del vy, vx

def grade(fg):
    f = fg.astype(np.float32) / 255
    f = np.clip((f - 0.5) * 1.08 + 0.5 + 0.01, 0, 1)            # contrast
    l = f.mean(axis=2, keepdims=True)
    f = np.clip(l + (f - l) * 1.18, 0, 1)                         # saturation
    return f

def render_clean(T):
    i = max(k for k in range(len(SEGS)) if starts[k] <= T) if T < TOTAL else len(SEGS) - 1
    s = SEGS[i]; lt = T - starts[i]
    if "_frames" not in s:
        for o in SEGS: o.pop("_frames", None)
        load_seg(i)
    src = get_src(s, lt)
    # ---- background: blurred, darkened, slow push
    bgz = 1.06 + 0.04 * lt / s["dur"]
    cw = int(MH * W / H / bgz); ch = int(MH / bgz)
    x0 = (MW - cw) // 2; y0 = (MH - ch) // 2
    small = cv2.resize(src[y0:y0 + ch, x0:x0 + cw], (90, 160), interpolation=cv2.INTER_AREA)
    small = cv2.GaussianBlur(small, (0, 0), 5)
    bg = cv2.resize(small, (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255 * 0.5
    bg *= BAND_SH
    # ---- foreground band with camera move
    z = s["z"][0] + (s["z"][1] - s["z"][0]) * e_io3(lt / s["dur"])
    sc = FG_W0 * z / MW
    M = np.array([[sc, 0, W / 2 - MW * sc / 2], [0, sc, FG_H / 2 - MH * sc / 2]], np.float32)
    fg = cv2.warpAffine(src, M, (W, FG_H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    fgf = grade(fg)
    if s.get("endcard"):
        e = e_out3((lt - 0.05) / 0.5)
        if e > 0:
            fgf = cv2.GaussianBlur(fgf, (0, 0), 0.1 + 7 * e)
            fgf *= 1 - 0.5 * e
    bg[FG_Y:FG_Y + FG_H] = fgf
    # edge highlights
    bg[FG_Y:FG_Y + 3] = bg[FG_Y:FG_Y + 3] * 0.4 + 0.6
    bg[FG_Y + FG_H - 3:FG_Y + FG_H] = bg[FG_Y + FG_H - 3:FG_Y + FG_H] * 0.4 + 0.6
    fr = bg
    if s.get("bar"): BAR_HOOK(fr, s, lt)
    draw_headline(fr, s, lt, T)
    if s.get("endcard"): endcard(fr, lt)
    draw_captions(fr, T)
    return fr

# ---------------------------------------------------------------- whole-frame camera & FX
def cam_state(T):
    """returns zoom, tx, ty, rot, roll_x, roll_y, ca, flash"""
    z, tx, ty, rot, rx, ry, ca, fl = 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    for tc, kind in TRANS.items():
        dt = T - tc
        if -0.17 < dt < 0.24:
            if kind in ("zoom", "flash"):
                amp = 0.55 if kind == "zoom" else 0.25
                if dt < 0: z *= 1 + amp * e_in3((dt + 0.17) / 0.17)
                else: z *= 1 + amp * 1.2 * (1 - e_out3(dt / 0.24))
                if dt >= 0: fl = max(fl, (0.55 if kind == "flash" else 0.3) * (1 - e_out3(dt / 0.2)))
                ca = max(ca, 14 * (1 - abs(dt) / 0.24))
            else:
                L = W if kind == "whip" else H
                if dt < 0: off = -L * e_in3((dt + 0.17) / 0.17)
                else: off = L * (1 - e_out3(dt / 0.24))
                if kind == "whip": rx = off
                else: ry = off
                ca = max(ca, 10 * (1 - abs(dt) / 0.24))
    for ti, a in IMPACTS:
        dt = T - ti
        if 0 <= dt < 0.6:
            dec = math.exp(-dt * 7.5)
            tx += a * 22 * dec * math.sin(dt * 71 + ti)
            ty += a * 18 * dec * math.sin(dt * 59 + 1.7 + ti)
            rot += a * 1.1 * dec * math.sin(dt * 47 + ti)
            z *= 1 + a * 0.07 * (1 - e_out3(dt / 0.3))
            fl = max(fl, a * 0.45 * (1 - e_out3(dt / 0.18)))
            ca = max(ca, a * 12 * dec)
    return z, tx, ty, rot, rx, ry, ca, fl

def affine(fr, z, tx, ty, rot):
    M = cv2.getRotationMatrix2D((W / 2, H / 2), rot, z)
    M[0, 2] += tx; M[1, 2] += ty
    return cv2.warpAffine(fr, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

def leak(T):
    out = None
    for tl, a in LEAKS:
        dt = T - tl
        if -0.1 < dt < 0.7:
            env = a * math.sin(math.pi * clamp((dt + 0.1) / 0.8)) ** 2
            gy, gx = np.mgrid[:160, :90].astype(np.float32)
            cx = -20 + dt * 160; cy = 40 + dt * 60
            b = np.exp(-((gx - cx) ** 2 / (2 * 35 ** 2) + (gy - cy) ** 2 / (2 * 60 ** 2)))
            col = np.stack([b * 1.0, b * 0.55, b * 0.25], -1) * env * 0.55
            l = cv2.resize(col, (W, H), interpolation=cv2.INTER_CUBIC)
            out = l if out is None else out + l
    return out

prev_cam = None
def render_frame(n):
    global prev_cam
    T = n / FPS
    cs = cam_state(T)
    z, tx, ty, rot, rx, ry, ca, fl = cs
    fr = render_clean(T)
    # motion-blurred camera: sample sub-frame camera states when moving fast
    pcs = cam_state(T - 1 / FPS)
    dz = abs(math.log(z) - math.log(pcs[0]))
    if dz > 0.004:
        N = min(8, 2 + int(dz * 160))
        acc = np.zeros_like(fr)
        for k in range(N):
            zz = math.exp(math.log(pcs[0]) + (math.log(z) - math.log(pcs[0])) * (k + 1) / N * 1.6)
            acc += affine(fr, zz, tx, ty, rot)
        fr = acc / N
    elif abs(z - 1) > 1e-3 or abs(tx) + abs(ty) + abs(rot) > 0.05:
        fr = affine(fr, z * (1.03 if abs(tx) + abs(ty) > 0.5 else 1), tx, ty, rot)
    if abs(rx) > 0.5:
        fr = np.roll(fr, int(rx), axis=1)
        L = int(min(260, abs(rx - pcs[4]) * 1.3))
        if L > 2: fr = cv2.blur(fr, (L, 1))
    if abs(ry) > 0.5:
        fr = np.roll(fr, int(ry), axis=0)
        L = int(min(300, abs(ry - pcs[5]) * 1.3))
        if L > 2: fr = cv2.blur(fr, (1, L))
    if ca > 0.8:
        d = int(round(ca))
        r = np.roll(fr[..., 0], d, axis=1); b = np.roll(fr[..., 2], -d, axis=1)
        fr = np.stack([r, fr[..., 1], b], -1)
    lk = leak(T)
    if lk is not None: fr = 1 - (1 - fr) * (1 - np.clip(lk, 0, 1))   # screen
    if fl > 0.01: fr = fr * (1 - fl) + fl
    fr *= VIG
    fr += GRAIN[n % 4] * 0.022
    return (np.clip(fr, 0, 1) * 255 + 0.5).astype(np.uint8)

