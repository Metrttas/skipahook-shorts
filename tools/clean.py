#!/usr/bin/env python3
# Clean Edits + Day-X-Devlogs (ab 06.11.2026; neu gebaut 05.11. abends – die Mittags-Fassung war nie im Bundle).
#   python3 tools/promo/motion/clean.py <tagesdatei> <id> check|render|sheet     (tagesdatei = days/k_1106.py, id = Schlüssel in VIDEOS)
#   python3 tools/promo/motion/clean.py <tagesdatei> all check|render|sheet
# Ausgabe: out/motion/<id>/<id>.mp4 (1080x1920, 30 fps, AAC), Kontaktbogen out/motion/<id>/sheet.jpg (1 Bild/s bzw. sheet-Zeiten).
# Clips: out/rec/reel/<name>.mp4 (Symlinks auf promo\clips, 1916x902, 60 fps). Musik: out/audio/fresh/<name>.wav + .json (fresh_beats.py).
#
# FORMAT 1 – CLEAN EDIT (kind='clean'): Vollbild-Spielclips, Schnitte auf dem Beat, weiche Übergänge, KEINE Stimme, Musik ist der Star.
#   dict(kind='clean', music='mtg_0611_f', hook='LINE 1|*GELBE ZEILE',
#        shots=[(clip, src, beats[, speed[, crop]]), ...],   # 1. Shot = ruhiges Intro, genau 4 Beats (Drop auf Beat 4)
#        texts=[(b0, b1, 'TEXT|*ZEILE 2'), (b0, b1, '{0-1285}|*FAVORITES')],   # Beats ab Videostart; {a-b} = Zahl rollt
#        end=(beats, 'SKIP A HOOK', 'ON ROBLOX'), hook_y=560, text_y=1180, end_y=820)   # y nur ändern, wenn Spiel-Text (PERFECT!) darunter liegt  # Endkarte auf dem Anfangs-Clip (Ausschnitt direkt VOR dem Hook-Bild -> Loop)
#   speed < 1 = Zeitlupe. crop: 'c' Mitte (Standard), 'z' enger (Punch), 'l'/'r' links/rechts der Mitte.
# FORMAT 2 – DAY-X (kind='day'): Ich-Devlog mit Stimme (am_puck, speed 0.8, pause 0.5), Karaoke-Untertitel, Musik leise darunter.
#   dict(kind='day', music='lof_0611_c', day=2, tag='TO 1,000 CCU', lines=[...Sätze...], shots=[[(clip, src[, speed[, crop]]), ...] je Satz],
#        prog=dict(a=10, b=8, goal=1000, unit='CCU', line=1))   # Balken + rollende Zahl ab Satz 'line'
# Text nur im Bereich y 250–1480 (Plattform-UI). Hook-Text ist im ersten Bild voll sichtbar (kein Einblenden bei t=0).
# LAYOUT (User 06.11.: "viel zu nah rangezoomt, voll tot"): NIE mehr enger 9:16-Ausschnitt – Spielbild breit in der Mitte (LAY),
# unscharfer Hintergrund, Texte über/unter dem Spielbild, Beat-Zoom + Blitz auf dem Drop.
import importlib.util, json, math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
REEL = os.path.join(ROOT, 'out/rec/reel')
MUS = os.path.join(ROOT, 'out/audio/fresh')
FONT = os.path.join(HERE, 'fonts/LuckiestGuy.ttf')
W, H, FPS = 1080, 1920, 30
XF = 0.18                     # Übergangsdauer
TRANS = ['fade', 'smoothup', 'zoomin', 'slideleft', 'fadewhite', 'circleopen', 'smoothdown', 'slideright']
EQ = 'eq=gamma=1.22:saturation=1.2:contrast=1.06'
CROPS = {'c': 'crop=507:902:704:0', 'z': 'crop=440:782:738:60', 'l': 'crop=507:902:560:0', 'r': 'crop=507:902:850:0'}
MUSIC_VOL_VO = 0.10           # Musik unter der Stimme (nicht erhöhen)
YEL, WHITE = (255, 216, 74), (255, 255, 255)
_font_cache = {}


def font(sz):
    if sz not in _font_cache:
        _font_cache[sz] = ImageFont.truetype(FONT, sz)
    return _font_cache[sz]


def sh(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode:
        raise SystemExit('FEHLER: ' + ' '.join(cmd)[:300] + '\n' + r.stderr[-1500:])
    return r.stdout


def dur_of(path):
    return float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path]).strip())


# ---------------------------------------------------------------- Text
def fmt_num(v):
    return f'{int(round(v)):,}'


def resolve(line, p):
    # {a-b} -> Zahl bei Fortschritt p
    import re
    def rep(m):
        a, b = float(m.group(1)), float(m.group(2))
        e = 1 - (1 - min(1, max(0, p))) ** 3
        return fmt_num(a + (b - a) * e)
    return re.sub(r'\{([\d.]+)-([\d.]+)\}', rep, line)


def draw_lines(img, text, cy, size=128, p_roll=1.0, scale=1.0, alpha=1.0, maxw=960):
    lines = [resolve(s, p_roll) for s in text.split('|')]
    d = ImageDraw.Draw(img)
    rows = []
    for ln in lines:
        col = YEL if ln.startswith('*') else WHITE
        ln = ln.lstrip('*')
        sz = int(size * scale)
        while sz > 30 and d.textlength(ln, font=font(sz)) > maxw:
            sz -= 4
        rows.append((ln, col, sz))
    total = sum(r[2] * 1.08 for r in rows)
    y = cy - total / 2
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    for ln, col, sz in rows:
        f = font(sz)
        w = ld.textlength(ln, font=f)
        x = (W - w) / 2
        ld.text((x + 6, y + 8), ln, font=f, fill=(0, 0, 0, 150), stroke_width=max(6, sz // 12), stroke_fill=(0, 0, 0, 150))
        ld.text((x, y), ln, font=f, fill=col + (255,), stroke_width=max(6, sz // 12), stroke_fill=(10, 10, 20, 255))
        y += sz * 1.08
    if alpha < 1:
        a = np.array(layer)
        a[..., 3] = (a[..., 3] * alpha).astype(np.uint8)
        layer = Image.fromarray(a)
    img.alpha_composite(layer)


def pop(t_since, dur=0.14):
    if t_since >= dur:
        return 1.0
    x = t_since / dur
    return 1.18 - 0.18 * x


# ---------------------------------------------------------------- Zeitplan
def plan_clean(V):
    m = json.load(open(os.path.join(MUS, V['music'] + '.json')))
    b = m['beat']
    shots = [list(s) + [None] * (5 - len(s)) for s in V['shots']]
    eb, etitle, esub = V['end']
    first = shots[0]
    sp0 = first[3] or 1.0
    end_src = max(0.0, first[1] - eb * b * sp0)
    shots.append([first[0], end_src, eb, sp0, first[4]])
    segs, t = [], 0.0
    for clip, src, beats, sp, cr in shots:
        segs.append(dict(clip=clip, src=src, t0=t, t1=t + beats * b, speed=sp or 1.0, crop=cr or 'c'))
        t += beats * b
    return m, segs, t


def plan_day(V, vo):
    blocks = vo['blocks']
    off = 0.25
    segs = []
    T = vo['duration'] + off + 0.9
    for i, blk in enumerate(blocks):
        t0 = 0.0 if i == 0 else blk['start'] + off - 0.12
        t1 = T if i == len(blocks) - 1 else blocks[i + 1]['start'] + off - 0.12
        sl = V['shots'][i]
        n = len(sl)
        for k, s in enumerate(sl):
            s = list(s) + [None] * (4 - len(s))
            segs.append(dict(clip=s[0], src=s[1], speed=s[2] or 1.0, crop=s[3] or 'c',
                             t0=t0 + (t1 - t0) * k / n, t1=t0 + (t1 - t0) * (k + 1) / n))
    return segs, T, off


def check_windows(vid, segs):
    ok = True
    for s in segs:
        p = os.path.join(REEL, s['clip'] + '.mp4')
        if not os.path.exists(p):
            print(f'  {vid}: Clip fehlt {s["clip"]}'); ok = False; continue
        need = s['src'] + (s['t1'] - s['t0'] + XF) * s['speed'] + 0.3
        d = dur_of(p)
        if need > d:
            print(f'  {vid}: {s["clip"]} src {s["src"]} braucht {need:.2f} > {d:.2f}'); ok = False
    return ok


# ---------------------------------------------------------------- Bild
_bars = {}


def has_bars(clip):
    # Trailer-Clips (t_main_*, t_zones_*, koi_seq_2 …) haben schwarze Kinobalken oben/unten (y 0–110 / 790–902)
    if clip not in _bars:
        p = os.path.join(REEL, clip + '.mp4')
        r = subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', str(min(1.0, dur_of(p) / 2)), '-i', p, '-frames:v', '1',
                            '-vf', 'crop=600:902:658:0', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True)
        a = np.frombuffer(r.stdout, np.uint8).reshape(902, 600)
        _bars[clip] = bool(a[20:100].mean() < 6 and a[805:890].mean() < 6)
    return _bars[clip]


# Layout ab 06.11. (User: "viel zu nah rangezoomt … voll tot"): Spielbild BREIT (fast 1:1 aus der Aufnahme, kaum vergrößert)
# in der Mitte, dahinter dasselbe Bild unscharf + dunkel; Texte darüber/darunter statt aufs Spiel. Leben: Zoom-Puls auf jedem Beat
# nach dem Drop + langsamer Push-in + weißer Blitz auf dem Drop.
LAY = {'clean': dict(fw=1080, fh=886, fy=470), 'day': dict(fw=1080, fh=760, fy=620)}


def crop_for(clip, mode, aspect):
    h, y = (676, 112) if has_bars(clip) else (902, 0)
    if mode == 'z':
        y += int(h * 0.075); h = int(h * 0.85)
    h = h // 2 * 2
    w = min(1916, int(h * aspect) // 2 * 2)
    x = (1916 - w) // 2 + {'c': 0, 'z': 0, 'l': -120, 'r': 120}[mode]
    return f'crop={w}:{h}:{max(0, min(1916 - w, x))}:{y}'


def graph_video(vid, segs, kind, beat, drop, T):
    """Ein Durchgang: Shots (breiter Ausschnitt) -> xfade-Kette -> Beat-Zoom -> unscharfer Hintergrund + Spielbild in der Mitte."""
    L_ = LAY[kind]
    FW, FH, FY = L_['fw'], L_['fh'], L_['fy']
    inp, fc = [], []
    n = len(segs)
    for i, s in enumerate(segs):
        L = s['t1'] - s['t0'] + (XF / 2 if i > 0 else 0) + (XF / 2 if i < n - 1 else 0)
        inp += ['-ss', f"{s['src']:.3f}", '-t', f"{L * s['speed'] + 0.1:.3f}", '-i', os.path.join(REEL, s['clip'] + '.mp4')]
        fc.append(f"[{i}:v]setpts=(PTS-STARTPTS)/{s['speed']},fps={FPS},{crop_for(s['clip'], s['crop'], FW / FH)},"
                  f"scale={FW}:{FH}:flags=bicubic,{EQ},setsar=1,trim=duration={L:.3f},setpts=PTS-STARTPTS[s{i}]")
    prev = '[s0]'
    for i in range(1, n):
        tr = TRANS[(sum(map(ord, vid)) + i) % len(TRANS)]
        fc.append(f"{prev}[s{i}]xfade=transition={tr}:duration={XF}:offset={segs[i]['t0'] - XF / 2:.3f}[x{i}]")
        prev = f'[x{i}]'
    amp = 0.07 if kind == 'clean' else 0.025
    z = f"1+{amp}*exp(-9*mod(it-{drop:.3f}\\,{beat:.4f}))*gte(it\\,{drop:.3f})+0.05*it/{T:.2f}"
    fc.append(f"{prev}zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={FW}x{FH}:fps={FPS},setsar=1,split[fg][bs]")
    fc.append(f"[bs]scale=-2:480,crop=270:480,boxblur=8:2,eq=brightness=-0.16:saturation=1.3,scale={W}:{H}[bg]")
    fc.append(f"[bg][fg]overlay=0:{FY}[comp]")
    return inp, fc, '[comp]'


def overlay_clean(V, m, T):
    b = m['beat']
    D = 4 * b
    items = [(0, 4, V['hook'], True)] + [(t0, t1, tx, False) for t0, t1, tx in V.get('texts', [])]
    eb, etitle, esub = V['end']
    t_end0 = T - eb * b
    FY, FH = LAY['clean']['fy'], LAY['clean']['fh']
    y_top, y_bot = (250 + FY) / 2, FY + FH + 70

    def frame(t):
        img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        for b0, b1, tx, is_hook in items:
            a0, a1 = b0 * b, b1 * b
            if a0 <= t < a1 and t < t_end0:
                since = t - a0
                sc = 1.0 if is_hook and b0 == 0 else pop(since)
                fade = min(1.0, (a1 - t) / 0.12)
                if is_hook:
                    draw_lines(img, tx, y_top, 100, scale=sc, alpha=fade)
                else:
                    draw_lines(img, tx, y_bot, 84, p_roll=since / 0.8, scale=sc, alpha=fade)
        if t >= t_end0:
            since = t - t_end0
            draw_lines(img, '*' + etitle, y_top, 124, scale=pop(since, 0.16))
            if since > b:
                draw_lines(img, esub, y_bot, 80, scale=pop(since - b))
        if D <= t < D + 0.16:  # Blitz auf dem Drop
            fl = Image.new('RGBA', (W, H), (255, 255, 255, int(150 * (1 - (t - D) / 0.16))))
            img = Image.alpha_composite(fl, img)
        return img
    return frame


def overlay_day(V, vo, T, off):
    blocks = vo['blocks']
    words = []
    for bi, blk in enumerate(blocks):
        ws = blk['words']
        # Gruppen à 2–3 Wörter
        g = []
        for w in ws:
            g.append(w)
            if len(g) == 3 or (len(g) == 2 and len(w['w']) > 7) or w['w'][-1:] in '.,!?':
                words.append(g); g = []
        if g:
            words.append(g)
    pr = V.get('prog')
    p_t0 = blocks[pr['line']]['start'] + off if pr else None

    def frame(t):
        img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        # Kopf: DAY N + Serie (ab Bild 1 voll sichtbar)
        draw_lines(img, f"DAY {V['day']}|*{V['tag']}", 352, 96)
        # Fortschritt
        if pr and t >= p_t0:
            since = t - p_t0
            e = 1 - (1 - min(1, since / 1.0)) ** 3
            v = pr['a'] + (pr['b'] - pr['a']) * e
            x0, x1, y0 = 140, 940, 470
            d.rounded_rectangle([x0, y0, x1, y0 + 44], 22, fill=(15, 20, 35, 220), outline=(255, 255, 255, 255), width=5)
            frac = max(0.012, min(1, v / pr['goal']))
            d.rounded_rectangle([x0 + 7, y0 + 7, x0 + 7 + (x1 - x0 - 14) * frac, y0 + 37], 15, fill=YEL + (255,))
            txt = f"{fmt_num(v)} / {fmt_num(pr['goal'])} {pr['unit']}"
            draw_lines(img, txt, 566, 58)
        # Untertitel (Karaoke)
        tt = t - off
        for g in words:
            if g[0]['start'] - 0.05 <= tt < g[-1]['end'] + 0.12 or (g is words[-1] and tt >= g[0]['start']):
                f = font(84)
                parts = [w['w'].upper() for w in g]
                sp = d.textlength(' ', font=f)
                wid = [d.textlength(p, font=f) for p in parts]
                tot = sum(wid) + sp * (len(parts) - 1)
                sz = 84
                if tot > 980:
                    sz = int(84 * 980 / tot); f = font(sz)
                    wid = [d.textlength(p, font=f) for p in parts]; sp = d.textlength(' ', font=f); tot = sum(wid) + sp * (len(parts) - 1)
                x = (W - tot) / 2
                y = LAY['day']['fy'] + LAY['day']['fh'] + 28
                for p, w_, ww in zip(parts, g, wid):
                    col = YEL if w_['start'] <= tt < w_['end'] + 0.05 else WHITE
                    d.text((x + 5, y + 7), p, font=f, fill=(0, 0, 0, 140), stroke_width=8, stroke_fill=(0, 0, 0, 140))
                    d.text((x, y), p, font=f, fill=col + (255,), stroke_width=8, stroke_fill=(10, 10, 20, 255))
                    x += ww + sp
                break
        return img
    return frame


def render(vid, V, day_file_dir):
    outdir = os.path.join(ROOT, 'out/motion', vid)
    os.makedirs(outdir, exist_ok=True)
    music = os.path.join(MUS, V['music'] + '.wav')
    if V['kind'] == 'clean':
        m, segs, T = plan_clean(V)
        frame = overlay_clean(V, m, T)
        vo_path = None
    else:
        vo_path = os.path.join(outdir, 'vo.wav')
        js = os.path.join(outdir, 'vo.json')
        if not os.path.exists(js) or json.load(open(js)).get('lines') != V['lines']:
            sh(['python3', '-I', os.path.join(ROOT, 'tools/voice/kokoro_tts.py'), '--voice', 'am_puck', '--speed', '0.8', '--pause', '0.5',
                '--out', vo_path, '--json', js] + V['lines'])
            d = json.load(open(js)); d['lines'] = V['lines']; json.dump(d, open(js, 'w'))
        vo = json.load(open(js))
        segs, T, off = plan_day(V, vo)
        frame = overlay_day(V, vo, T, off)
    if not check_windows(vid, segs):
        raise SystemExit(f'{vid}: Clip-Fenster prüfen')
    mj = json.load(open(os.path.join(MUS, V['music'] + '.json')))
    inp, fc, vlab = graph_video(vid, segs, V['kind'], mj['beat'], 4 * mj['beat'] if V['kind'] == 'clean' else 0.0, T)
    n = len(segs)
    nfr = int(round(T * FPS))
    out = os.path.join(outdir, vid + '.mp4')
    if vo_path:
        a_in = ['-i', music, '-i', vo_path]
        af = (f"[{n + 1}:a]volume={MUSIC_VOL_VO},atrim=0:{T:.3f},afade=t=out:st={T - 0.8:.3f}:d=0.8[mu];"
              f"[{n + 2}:a]adelay={int(off * 1000)}|{int(off * 1000)},apad[vox];[mu][vox]amix=inputs=2:duration=first:normalize=0[a]")
    else:
        a_in = ['-i', music]
        af = f"[{n + 1}:a]atrim=0:{T:.3f},afade=t=out:st={T - 0.5:.3f}:d=0.5[a]"
    fc.append(f'{vlab}[{n}:v]overlay=0:0:format=auto,format=yuv420p[v]')
    fc.append(af)
    cmd = (['ffmpeg', '-y', '-loglevel', 'error'] + inp + ['-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-']
           + a_in + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]', '-t', f'{T:.3f}', '-c:v', 'libx264', '-preset', 'veryfast',
                     '-crf', '19', '-r', str(FPS), '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out])
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    last, last_img = None, None
    try:
        for i in range(nfr):
            p.stdin.write(frame(i / FPS).tobytes())
        p.stdin.close()
    except BrokenPipeError:
        raise SystemExit(p.stderr.read().decode()[-1500:])
    err = p.stderr.read().decode()
    if p.wait():
        raise SystemExit(err[-1500:])
    print(f'{vid}: {T:.1f} s -> {out}')
    return out


def sheet(vid, times=None):
    outdir = os.path.join(ROOT, 'out/motion', vid)
    mp4 = os.path.join(outdir, vid + '.mp4')
    T = dur_of(mp4)
    times = times or [0.0] + [t + 0.5 for t in range(int(T))]
    ims = []
    for t in times:
        r = subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', f'{min(t, T - 0.05):.2f}', '-i', mp4, '-frames:v', '1', '-vf', 'scale=216:384',
                            '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True)
        ims.append(Image.frombytes('RGB', (216, 384), r.stdout))
    cols = 8
    rows = math.ceil(len(ims) / cols)
    S = Image.new('RGB', (cols * 216, rows * 384), (40, 40, 40))
    for i, im in enumerate(ims):
        S.paste(im, ((i % cols) * 216, (i // cols) * 384))
    p = os.path.join(outdir, 'sheet.jpg')
    S.save(p, quality=80)
    return p


def load_day(path):
    spec = importlib.util.spec_from_file_location('dayfile', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.VIDEOS


if __name__ == '__main__':
    dayf, vid, cmd = sys.argv[1], sys.argv[2], sys.argv[3]
    VIDS = load_day(dayf)
    ids = list(VIDS) if vid == 'all' else vid.split(',')
    for v in ids:
        V = VIDS[v]
        if cmd == 'check':
            if V['kind'] == 'clean':
                m, segs, T = plan_clean(V)
                print(v, f'{T:.1f}s', 'ok' if check_windows(v, segs) else 'FEHLER')
            else:
                print(v, 'day (Fenster erst beim Rendern, Zeiten aus der Stimme)')
        elif cmd == 'render':
            render(v, V, os.path.dirname(dayf))
            print(sheet(v))
        elif cmd == 'sheet':
            print(sheet(v))
