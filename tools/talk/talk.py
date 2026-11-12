#!/usr/bin/env python3
# TALK-Shorts (ab 12.11.2026, User 12.11. 01:50: "nur noch Videos, wo du redest … bring Leute dazu zu liken/teilen …
#   wenn du likest kriegst du den Fisch … keine Edits … deine eigenen Sounds sind scheiße … gib dir Mühe, gute Effekte").
#   python3 tools/promo/talk/talk.py <tagesdatei> <id|all|id,id> stills|render
# Tagesdatei tools/promo/talk/days/t_MMDD.py: VIDEOS = {id: dict(lines=[(satz, [(clip, src), ...], 'HEAD *GOLD', {opts}), ...], ...)}
#   Video-Optionen: ladder=True (Like/Follow/Comment/Share/All-Leiste oben), prog=(gestern, heute, ziel) (CCU-Balken),
#                   speed=0.85 (Kokoro am_puck), pause=0.35, amb='day'|'night'.
#   Satz-Optionen:  tier=k (0..4: Leiste bis k an, Symbol k springt, Spiel-Ton reveal), fish=('NAME', 'RARITY') Namens-Schild unten im Bild,
#                   flick=True (harte Schnitte im Takt der Bilder, "STOP"-Spiel), prog=True (Zahl rollt, Balken), sfx='bite'|'splash'|...
#   Letzter Satz = Endkarte (SKIP A HOOK + Search-Pill) auf dem ersten Clip.
# Look: großes Spielbild-Band y 590–1290 (statt 642–1278), Hintergrund = unscharfes Spielbild, Kopfzeile y 505, Leiste y 300,
#   Karaoke y 1345. Ton: NUR Stimme + echte Spiel-Töne (tools/audio/asmr_sfx.py = In-Game-Sprite) + Spiel-Atmo (ambience.py).
#   KEINE selbst gebaute Musik, keine synthetischen Whoosh/Impact-Töne.
import importlib.util, json, math, os, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'tools/promo/ae'))
import aecore as C
from scipy.io import wavfile

OUT = os.path.join(ROOT, 'out/talk')
SFX = os.path.join(ROOT, 'out/sfx/wav')
AMB = os.path.join(ROOT, 'out/audio/sah_ambience.wav')
AMB_REG = os.path.join(ROOT, 'out/audio/sah_ambience_regions.json')
SR = 48000
VO_OFF = 0.25

# ---------------------------------------------------------------- band geometry (bigger than AE look)
BY, BH = 590, 700
yy = np.arange(C.H)[:, None].astype(np.float32)
d_out = np.maximum(BY - yy, yy - (BY + BH))
BAND_SH = (1 - 0.55 * np.exp(-np.maximum(d_out, 0) / 70.0) * (d_out > 0)).astype(np.float32)[..., None]
LADDER = [('LIKE', (255, 45, 85)), ('FOLLOW', (60, 200, 255)), ('COMMENT', (255, 205, 40)), ('SHARE', (70, 225, 120)), ('ALL 4', (255, 170, 30))]
RAR = {'COMMON': (190, 190, 200), 'RARE': (70, 150, 255), 'EPIC': (185, 90, 255), 'LEGENDARY': (255, 170, 30), 'MYTHIC': (255, 70, 120),
       'SECRET': (255, 215, 60), 'LEGEND': (255, 120, 40), 'EXOTIC': (60, 230, 200), 'ANCIENT': (230, 120, 60), 'ETHEREAL': (180, 140, 255),
       'TITANIC': (90, 200, 255), 'GOLD': (255, 205, 60), 'SEA GIANT': (110, 210, 255)}
STATE = {}


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode:
        raise SystemExit('FEHLER: ' + ' '.join(map(str, cmd))[:300] + '\n' + r.stderr[-1500:].decode(errors='ignore'))
    return r.stdout


_cd = {}
def clip_dur(name):
    if name not in _cd:
        p = f'{C.CLIPS}/{name}.mp4'
        if not os.path.exists(p):
            raise SystemExit(f'Clip fehlt (stagen!): {name}')
        _cd[name] = float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).strip())
    return _cd[name]


# ---------------------------------------------------------------- icons (drawn once, premultiplied RGBA float)
def _icon(kind, col, size=118):
    S = size * 4
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((6, 6, S - 6, S - 6), fill=col + (255,), outline=(255, 255, 255, 255), width=int(S * 0.045))
    w = (255, 255, 255, 255); c = S / 2
    if kind == 'LIKE':
        r = S * 0.13
        d.ellipse((c - 2 * r, c - 1.55 * r, c, c + 0.45 * r), fill=w); d.ellipse((c, c - 1.55 * r, c + 2 * r, c + 0.45 * r), fill=w)
        d.polygon([(c - 1.93 * r, c - 0.25 * r), (c + 1.93 * r, c - 0.25 * r), (c, c + 2.05 * r)], fill=w)
    elif kind == 'FOLLOW':
        r = S * 0.09
        d.ellipse((c - 1.6 * r - r, c - 2.2 * r, c - 1.6 * r + r, c - 0.2 * r), fill=w)
        d.pieslice((c - 1.6 * r - 2 * r, c + 0.1 * r, c - 1.6 * r + 2 * r, c + 4.1 * r), 180, 360, fill=w)
        t = S * 0.035; px = c + 1.6 * r
        d.rectangle((px - t, c - 1.6 * r, px + t, c + 0.8 * r), fill=w); d.rectangle((px - 1.2 * r, c - 0.4 * r - t, px + 1.2 * r, c - 0.4 * r + t), fill=w)
    elif kind == 'COMMENT':
        r = S * 0.24
        d.rounded_rectangle((c - r, c - 0.75 * r, c + r, c + 0.55 * r), int(r * 0.35), fill=w)
        d.polygon([(c - 0.45 * r, c + 0.5 * r), (c - 0.6 * r, c + 0.95 * r), (c - 0.05 * r, c + 0.5 * r)], fill=w)
        for k in (-1, 0, 1):
            d.ellipse((c + k * 0.45 * r - 0.11 * r, c - 0.21 * r, c + k * 0.45 * r + 0.11 * r, c + 0.01 * r), fill=col + (255,))
    elif kind == 'SHARE':
        r = S * 0.22
        d.polygon([(c + 0.95 * r, c - 0.15 * r), (c + 0.05 * r, c - 0.95 * r), (c + 0.05 * r, c - 0.5 * r), (c - 0.9 * r, c - 0.3 * r),
                   (c - 0.95 * r, c + 0.75 * r), (c - 0.45 * r, c + 0.15 * r), (c + 0.05 * r, c + 0.2 * r), (c + 0.05 * r, c + 0.65 * r)], fill=w)
    else:  # crown
        r = S * 0.22
        d.polygon([(c - r, c + 0.5 * r), (c - r, c - 0.55 * r), (c - 0.5 * r, c), (c, c - 0.85 * r), (c + 0.5 * r, c), (c + r, c - 0.55 * r),
                   (c + r, c + 0.5 * r)], fill=w)
        d.rectangle((c - r, c + 0.62 * r, c + r, c + 0.82 * r), fill=w)
    im = im.resize((size, size), Image.LANCZOS)
    return C.to_premul(im)


def _glow(col, size=200):
    g = np.zeros((size, size, 4), np.float32); y, x = np.mgrid[:size, :size]
    r = np.exp(-((x - size / 2) ** 2 + (y - size / 2) ** 2) / (2 * (size * 0.2) ** 2))
    for k in range(3): g[..., k] = r * col[k] / 255
    g[..., 3] = r
    return g


def draw_ladder(fr, T):
    """Leiste oben: 5 Symbole, an bis zum aktuellen tier, aktuelles springt + glüht."""
    tiers = STATE['tiers']       # list of (t0, k)
    cur, t0 = -1, 0.0
    for tt, k in tiers:
        if T >= tt: cur, t0 = k, tt
    if 'icons' not in C._cache:
        C._cache['icons'] = [(_icon(n, col), _icon(n, (60, 60, 75)), _glow(col)) for n, col in LADDER]
    icons = C._cache['icons']
    a_in = 1.0
    xs = [C.W / 2 + (i - 2) * 196 for i in range(5)]
    cy = 272
    for i, (on, off, gl) in enumerate(icons):
        lit = i <= cur
        sc = 0.9
        if i == cur:
            lt = T - t0
            sc = 1.0 + 0.45 * (1 - C.spring(lt, 3.2, 0.35)) + 0.1
            C.blit(fr, gl, xs[i], cy, 1.6 + 0.15 * math.sin(T * 7), 0, 0.9 * a_in, add=True)
        elif lit:
            sc = 0.95
        C.blit(fr, on if lit else off, xs[i], cy, sc * (0.6 + 0.4 * a_in), 0, a_in * (1 if lit else 0.75))
        lab = C.text_sprite(STATE.get('labels', [n for n, _ in LADDER])[i], 34, C.F_BLACK_I, fill=LADDER[i][1] if lit else (150, 150, 165), stroke=6)
        C.blit(fr, lab['img'], xs[i], cy + 76, 1, 0, a_in)


def draw_fish(fr, seg, lt):
    f = seg.get('fish')
    if not f: return
    name, rar = f
    col = RAR.get(rar, (255, 255, 255))
    key = ('fish', name, rar)
    if key not in C._cache:
        t1 = C.text_sprite(name, 58, C.F_BLACK_I, fill=(255, 255, 255), stroke=8)
        t2 = C.text_sprite(rar, 34, C.F_BLACK_I, fill=col, stroke=6)
        w = int(max(t1['tw'], t2['tw']) + 90); h = 150
        im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, w - 1, h - 1), 36, fill=(12, 12, 28, 215), outline=col + (255,), width=5)
        C._cache[key] = (C.to_premul(im), t1, t2, w)
    box, t1, t2, w = C._cache[key]
    a = C.e_out3((lt - 0.15) / 0.3)
    if a <= 0: return
    sc = 0.7 + 0.3 * C.spring(lt - 0.15, 3.4, 0.4)
    cy = BY + BH - 105
    C.blit(fr, _glow(col, 260), C.W / 2, cy, 2.2, 0, 0.35 * a, add=True)
    C.blit(fr, box, C.W / 2, cy, sc, 0, a)
    C.blit(fr, t2['img'], C.W / 2, cy - 36 * sc, sc, 0, a)
    C.blit(fr, t1['img'], C.W / 2, cy + 20 * sc, sc, 0, a)


def draw_prog(fr, T):
    p = STATE.get('prog')
    if not p: return
    t0, (a, b, goal) = p
    lt = T - t0
    if lt < 0: return
    bw, bh, cy = 640, 30, 330
    key = ('pbar2', bw)
    if key not in C._cache:
        trk = Image.new('RGBA', (bw + 12, bh + 12), (0, 0, 0, 0))
        ImageDraw.Draw(trk).rounded_rectangle((0, 0, bw + 11, bh + 11), (bh + 12) // 2, fill=(10, 10, 25, 210), outline=(255, 255, 255, 140), width=3)
        C._cache[key] = C.to_premul(trk)
    al = C.e_out3(lt / 0.35)
    C.blit(fr, C._cache[key], C.W / 2, cy, 0.9 + 0.1 * al, 0, al)
    l1 = C.text_sprite('0', 32, C.F_BLACK_I, fill=(210, 210, 220), stroke=5)
    l2 = C.text_sprite(f'{goal:,} CCU', 32, C.F_BLACK_I, grad=C.GOLD, stroke=5, glow=C.GOLD[1])
    C.blit(fr, l1['img'], C.W / 2 - bw / 2 - 26 - l1['tw'] / 2, cy + 2, 1, 0, al)
    C.blit(fr, l2['img'], C.W / 2, cy + 52, 1, 0, al)
    pr = C.e_io3((lt - 0.35) / 1.0)
    v = a + (b - a) * pr
    fw = max(16, int(bw * v / goal))
    x0, y0 = int(C.W / 2 - bw / 2), int(cy - bh / 2)
    roi = fr[y0:y0 + bh, x0:x0 + fw]
    roi *= 0.0; roi += np.array([1.0, 0.78, 0.2], np.float32)
    C.blit(fr, _glow((255, 220, 120), 120), x0 + fw, cy, 1.0 + 0.25 * math.sin(lt * 8), 0, al, add=True)


def render_talk(T):
    i = max(k for k in range(len(C.SEGS)) if C.starts[k] <= T) if T < C.TOTAL else len(C.SEGS) - 1
    s = C.SEGS[i]; lt = T - C.starts[i]
    if '_frames' not in s:
        for o in C.SEGS:
            if o is not s and o.get('_keep') is None: o.pop('_frames', None)
        C.load_seg(i)
    src = C.get_src(s, lt)
    bgz = 1.06 + 0.04 * lt / s['dur']
    cw = int(C.MH * C.W / C.H / bgz); ch = int(C.MH / bgz)
    x0 = (C.MW - cw) // 2; y0 = (C.MH - ch) // 2
    small = cv2.resize(src[y0:y0 + ch, x0:x0 + cw], (90, 160), interpolation=cv2.INTER_AREA)
    small = cv2.GaussianBlur(small, (0, 0), 5)
    bg = cv2.resize(small, (C.W, C.H), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255 * 0.42
    bg *= BAND_SH
    z = s['z'][0] + (s['z'][1] - s['z'][0]) * C.e_io3(lt / s['dur'])
    sc = BH / C.MH * z
    M = np.array([[sc, 0, C.W / 2 - C.MW * sc / 2], [0, sc, BH / 2 - C.MH * sc / 2]], np.float32)
    fg = cv2.warpAffine(src, M, (C.W, BH), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    fgf = C.grade(fg)
    if s.get('endcard'):
        e = C.e_out3((lt - 0.05) / 0.5)
        if e > 0:
            fgf = cv2.GaussianBlur(fgf, (0, 0), 0.1 + 7 * e); fgf *= 1 - 0.5 * e
    bg[BY:BY + BH] = fgf
    bg[BY:BY + 4] = bg[BY:BY + 4] * 0.3 + 0.7
    bg[BY + BH - 4:BY + BH] = bg[BY + BH - 4:BY + BH] * 0.3 + 0.7
    fr = bg
    if STATE.get('ladder') and not s.get('endcard'): draw_ladder(fr, T)
    if not s.get('endcard'): draw_prog(fr, T)
    if s.get('flick'):
        # "STOP!"-Rahmen pulsiert um das Bild
        p = 0.5 + 0.5 * math.sin(T * 18)
        fr[BY - 8:BY, :] = fr[BY - 8:BY, :] * (1 - p) + p * np.array([1, 0.2, 0.3], np.float32)
        fr[BY + BH:BY + BH + 8, :] = fr[BY + BH:BY + BH + 8, :] * (1 - p) + p * np.array([1, 0.2, 0.3], np.float32)
    draw_fish(fr, s, lt)
    C.draw_headline(fr, s, lt, T)
    if s.get('endcard'): C.endcard(fr, lt)
    C.draw_captions(fr, T)
    return fr


C.render_clean = render_talk


# ---------------------------------------------------------------- build
def head_list(text, h0):
    if not text: return []
    words = text.split()
    keys = {w.lstrip('*') for w in words if w.startswith('*')}
    return [(h0, ' '.join(w.lstrip('*') for w in words), keys)]


def build(v, vid):
    d = os.path.join(OUT, vid); os.makedirs(d, exist_ok=True)
    wav, js = os.path.join(d, 'vo.wav'), os.path.join(d, 'vo.json')
    texts = [ln[0] for ln in v['lines']]
    spd, pau = str(v.get('speed', 0.85)), str(v.get('pause', 0.35))
    tag = json.dumps([texts, spd, pau])
    if not (os.path.exists(js) and json.load(open(js)).get('_tag') == tag):
        sh(['python3', '-I', os.path.join(ROOT, 'tools/voice/kokoro_tts.py'), '--voice', v.get('voice', 'am_puck'), '--speed', spd,
            '--pause', pau, '--out', wav, '--json', js] + texts)
        j = json.load(open(js)); j['_tag'] = tag; json.dump(j, open(js, 'w'))
    blocks = json.load(open(js))['blocks']
    segs, line_t, k = [], [], 0
    events = []   # (t, sfx, vol)
    tiers = []
    STATE.clear()
    STATE['ladder'] = v.get('ladder', False)
    if v.get('labels'): STATE['labels'] = v['labels']
    for li, ln in enumerate(v['lines']):
        _, shots, head = ln[:3]
        o = ln[3] if len(ln) > 3 else {}
        t0 = 0.0 if li == 0 else VO_OFF + blocks[li]['start'] - 0.1
        t1 = VO_OFF + blocks[li + 1]['start'] - 0.1 if li + 1 < len(blocks) else VO_OFF + blocks[li]['end'] + 0.8
        line_t.append((t0, t1))
        last = li == len(v['lines']) - 1
        if last:
            # Endkarte nur die letzten ~2,4 s, auf dem ANFANGS-Clip (Loop); davor normales Bild zum Satz
            first = v['lines'][0][1][0]
            ec = min(2.4, t1 - t0)
            pre = (t1 - t0) - ec
            shots = (list(shots) if pre > 0.6 else []) + [first]
            n = len(shots)
            dts = ([pre / (n - 1)] * (n - 1) if n > 1 else []) + [ec if n > 1 else t1 - t0]
        else:
            n = len(shots); dts = [(t1 - t0) / n] * n
        for si, sh_ in enumerate(shots):
            clip, src = sh_[:2]
            dur = dts[si]
            cd = clip_dur(clip)
            sp = 1.0
            avail = cd - src - 0.2
            if dur > avail:                      # Clip zu kurz: erst Zeitlupe (max. 0.5x), dann Start nach vorn
                sp = max(0.5, avail / dur)
                if dur * sp > avail: src = max(0.0, cd - 0.2 - dur * sp)
            z = (1.0, 1.06) if k % 2 == 0 else (1.05, 1.0)
            if o.get('flick'): z = (1.02, 1.02)
            seg = dict(clip=clip, src=src, dur=dur, z=z, head=head_list(head if si == 0 else '', -0.8 if li == 0 else 0.05))
            if sp < 1.0: seg['ramp'] = [(0, 0), (dur, dur * sp)]
            if o.get('flick'):
                seg['flick'] = True
                seg['head'] = head_list(head, -0.8) if head else []
                events.append((t0 + sum(dts[:si]), 'ui_tick', 0.9))
            if o.get('fish') and si == len(shots) - 1 or (o.get('fish') and len(shots) == 1):
                seg['fish'] = o['fish']
            if last and si == n - 1:
                seg['endcard'] = True; seg['head'] = []
                seg['src'] = sh_[1]; seg['ramp'] = [(0, 0), (dur, dur * 0.4)]   # Endkarte ruhig, Anfangs-Clip ab seinem Start (Loop)
            segs.append(seg); k += 1
        if 'tier' in o:
            tiers.append((t0, o['tier']))
            events.append((t0, ['reveal1', 'reveal2', 'reveal3', 'reveal4', 'record'][o['tier']], 1.0))
            events.append((t0, 'ui_pop', 0.8))
        if o.get('prog'):
            STATE['prog'] = (t0, v['prog'])
            for q in range(10): events.append((t0 + 0.35 + 0.1 * q, 'ui_tick', 0.6))
        if o.get('sfx'):
            for nm in o['sfx'].split(','):
                events.append((t0 + 0.1, nm, 0.9))
        if li > 0 and not o.get('flick') and 'tier' not in o:
            events.append((t0, 'whoosh', 0.35))
    STATE['tiers'] = tiers
    # karaoke
    chunks = []
    total = line_t[-1][1]
    for bi, b in enumerate(blocks):
        ws = [(w['w'].upper(), VO_OFF + w['start'], VO_OFF + w['end']) for w in b['words']]
        groups, cur = [], []
        for w in ws:
            if cur and (len(cur) >= 3 or sum(len(x[0]) for x in cur) + len(w[0]) > 13):
                groups.append(cur); cur = []
            cur.append(w)
        if cur: groups.append(cur)
        if len(groups) > 1 and len(groups[-1]) == 1 and len(groups[-1][0][0]) <= 3:
            lg = groups.pop(); groups[-1] += lg
        nxt = VO_OFF + blocks[bi + 1]['start'] if bi + 1 < len(blocks) else total
        for gi, g in enumerate(groups):
            a = g[0][1] - 0.04
            e = groups[gi + 1][0][1] - 0.04 if gi + 1 < len(groups) else min(g[-1][2] + 0.4, nxt - 0.05)
            chunks.append(dict(words=g, t0=a, t1=e))
    # configure core
    C.SEGS = segs
    C.starts = np.cumsum([0] + [s['dur'] for s in segs]).tolist()
    C.TOTAL = C.starts[-1]; C.NF = int(round(C.TOTAL * C.FPS)); C.CUTS = C.starts[1:-1]
    C.TRANS = {}
    end_t = C.starts[-2]
    C.TRANS[end_t] = 'zoom'
    events.append((end_t + 0.1, 'zone', 0.6))
    C.IMPACTS = [(t, 0.5 + 0.12 * kk) for t, kk in tiers if t > 0.3] + [(end_t + 0.6, 0.35)]
    C.LEAKS = [(t, 0.7) for t, _ in tiers if t > 0.3]
    C.CHUNKS = chunks
    C._cache.pop('title', None)
    return dict(total=total, vo=wav, events=events, amb=v.get('amb', 'day'))


# ---------------------------------------------------------------- audio: voice + game sfx + game ambience
def load(path):
    raw = sh(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'])
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def put(buf, x, t, g=1.0):
    i = int(t * SR)
    if i < 0: x = x[-i:]; i = 0
    n = min(len(x), len(buf) - i)
    if n > 0: buf[i:i + n] += x[:n] * g


_amb = {}
def ambience(kind, N):
    if kind not in _amb:
        reg = json.load(open(AMB_REG))
        a = load(AMB)
        def cut(nm):
            s, e = reg[nm]; return a[int(s * SR):int(e * SR)]
        bed = cut('waves')
        top = cut('day' if kind == 'day' else 'night')
        L = min(len(bed), len(top)); _amb[kind] = bed[:L] * 0.8 + top[:L] * 0.6
    x = _amb[kind]
    if len(x) < N: x = np.tile(x, (N // len(x) + 1, 1))
    return x[:N]


def make_audio(plan, path):
    total = plan['total']; N = int(total * SR)
    vo = np.zeros((N, 2), np.float32); put(vo, load(plan['vo']), VO_OFF)
    sfx = np.zeros((N, 2), np.float32)
    for t, nm, g in plan['events']:
        p = os.path.join(SFX, nm + '.wav')
        if os.path.exists(p): put(sfx, load(p), t, g)
    amb = ambience(plan['amb'], N)
    env = np.abs(vo).max(axis=1); k = int(0.08 * SR); env = np.convolve(env, np.ones(k) / k, 'same')
    duck = 1 - 0.5 * np.clip(env / 0.03, 0, 1)
    t = np.arange(N) / SR
    fade = np.clip((total - t) / 0.8, 0, 1) * np.clip(t / 0.3, 0, 1)
    vo /= np.abs(vo).max() + 1e-6
    sfx /= max(1e-6, np.abs(sfx).max())
    amb /= np.abs(amb).max() + 1e-6
    mix = vo * 1.0 + sfx * 0.32 * (duck * 0.6 + 0.4)[:, None] + amb * (0.10 * duck * fade)[:, None]
    mix /= max(1.0, np.abs(mix).max() / 0.95)
    wavfile.write(path, SR, mix.astype(np.float32))


# ---------------------------------------------------------------- main
def stills(days, vid):
    plan = build(days.VIDEOS[vid], vid)
    T = C.TOTAL
    ts = [0.0] + [min(T - 0.05, x) for x in np.linspace(0.6, T - 0.2, 9)]
    ims = []
    for tt in ts:
        im = C.render_frame(int(tt * C.FPS))
        im = cv2.resize(im, (270, 480), interpolation=cv2.INTER_AREA)
        cv2.putText(im, f'{tt:.1f}', (6, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
        ims.append(im)
    sheet = np.vstack([np.hstack(ims[r * 5:(r + 1) * 5]) for r in range(2)])
    d = os.path.join(OUT, vid)
    cv2.imwrite(os.path.join(d, 'sheet.jpg'), cv2.cvtColor(sheet, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 82])
    print(vid, f'{T:.1f}s sheet ok', flush=True)


def render(days, vid):
    d = os.path.join(OUT, vid); os.makedirs(d, exist_ok=True)
    out = os.path.join(d, vid + '.mp4')
    if os.path.exists(out):
        print(vid, 'schon fertig'); return
    plan = build(days.VIDEOS[vid], vid)
    aw = os.path.join(d, 'mix.wav'); make_audio(plan, aw)
    tmp = out + '.part.mp4'
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{C.W}x{C.H}', '-r', str(C.FPS), '-i', '-',
                          '-i', aw, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-maxrate', '20M',
                          '-bufsize', '40M', '-pix_fmt', 'yuv420p', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:a', 'aac', '-b:a', '192k',
                          '-ar', '48000', '-shortest', '-movflags', '+faststart', tmp], stdin=subprocess.PIPE)
    import time; t0 = time.time()
    for n in range(C.NF):
        p.stdin.write(C.render_frame(n).tobytes())
    p.stdin.close(); p.wait()
    if p.returncode: raise SystemExit('ffmpeg Fehler ' + vid)
    os.replace(tmp, out)
    print(vid, f'{C.TOTAL:.1f}s fertig in {time.time() - t0:.0f}s', flush=True)


if __name__ == '__main__':
    spec = importlib.util.spec_from_file_location('days', sys.argv[1])
    days = importlib.util.module_from_spec(spec); spec.loader.exec_module(days)
    ids = list(days.VIDEOS) if sys.argv[2] == 'all' else sys.argv[2].split(',')
    for vid in ids:
        (stills if sys.argv[3] == 'stills' else render)(days, vid)
