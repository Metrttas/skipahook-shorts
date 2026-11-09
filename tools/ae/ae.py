#!/usr/bin/env python3
# AE-Style Shorts (ab 09.11.2026; User 08.11.: "alle Videos so fresh wie das AE-Beispiel" – ersetzt clean.py-Look).
#   python3 tools/promo/ae/ae.py <tagesdatei> <id|all> stills|render
# Tagesdatei = tools/promo/ae/days/ae_MMDD.py mit VIDEOS = {id: dict(...)}. Ausgabe out/ae/<id>/<id>.mp4 (1080x1920, 60 fps,
# crf 19 / max 20 Mbit, AAC, -14 LUFS) bzw. out/ae/<id>/sheet.jpg (Kontaktbogen). Kern = aecore.py (Kopie von render.py des Beispiels).
# Clips: /mnt/user-data/uploads/SkipAHook_Meshes/promo/clips/<name>.mp4 (aus promo\clips stagen). Musik: out/audio/fresh (fresh_beats.py).
#
# CLEAN (kind='clean'): keine Stimme, Musik ist der Star, Schnitte auf dem Beat.
#   dict(kind='clean', music='mtg_0911_e', segs=[(clip, src, beats, 'HEAD *GOLD', {opts}), ...])
#   1. Seg = Hook, genau 4 Beats (Drop auf Beat 4), Text ab Bild 1 voll sichtbar. Letztes Seg mit opts end=True = Endkarte.
#   HIGH-END (User 09.11.): Shots 3–4 Beats (keine 2-Beat-Hektik), 5–7 Shots, 11–15 s; Clips, die inhaltlich zusammenpassen (ein Thema/Moment
#   pro Video, gleiche Tageszeit/Zone); Ruckeln wird in aecore.load_seg automatisch entfernt (Doppelbilder raus + optischer Fluss).
#   opts: sp=0.6 (Zeitlupe), counter=(a, b) ersetzt '#' im Text, z=(1.0, 1.1), bar='rarity'.
# DAY (kind='day'): Ich-Devlog, Stimme am_puck 0.8 / Pause 0.5, Karaoke-Untertitel y 1345, Musik leise (MUSIC_VO).
#   dict(kind='day', music=..., lines=[('Satz.', [(clip, src), ...], 'HEAD *GOLD' or '', {opts}), ...], prog=(a, b, 1000))
#   Satz 0 = Hook (Kopfzeile sofort sichtbar), opts prog=True -> Zahl rollt a->b + Balken b/goal. Letzter Satz = Endkarte.
# Text nur y 250–1480: Kopfzeile y 505, Spielbild-Band y 642–1278 (Spiel-Texte bleiben IM Band), Untertitel y 1345.
import importlib.util, json, math, os, subprocess, sys
import numpy as np, cv2

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
import aecore as C
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

MUS = os.path.join(ROOT, 'out/audio/fresh')
OUT = os.path.join(ROOT, 'out/ae')
SR = 48000
MUSIC_VO = 0.10       # Musik unter der Stimme (nicht erhöhen)
VO_OFF = 0.35
TR_CYCLE = ['zoom', 'whip', 'zoom', 'whipup']   # clean: keine Blitz-Übergänge mehr in der Mitte
_clipdur = {}


def sh(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, **kw)
    if r.returncode:
        raise SystemExit('FEHLER: ' + ' '.join(map(str, cmd))[:300] + '\n' + r.stderr[-1500:].decode(errors='ignore'))
    return r.stdout


def clip_dur(name):
    if name not in _clipdur:
        p = f'{C.CLIPS}/{name}.mp4'
        if not os.path.exists(p):
            raise SystemExit(f'Clip fehlt (stagen!): {name}')
        _clipdur[name] = float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).strip())
    return _clipdur[name]


def head_list(text, h0):
    if not text:
        return []
    words = text.split()
    keys = {w.lstrip('*') for w in words if w.startswith('*')}
    return [(h0, ' '.join(w.lstrip('*') for w in words), keys)]


def mk_seg(clip, src, dur, head, o, first, k):
    sp = o.get('sp', 1.0)
    need = dur * sp + 0.25
    cd = clip_dur(clip)
    if src + need > cd:
        print(f'  ! {clip}: src {src} + {need:.2f} > {cd:.2f} -> src {max(0, cd - need):.2f}')
        src = max(0.0, cd - need)
    z = o.get('z', (1.0, 1.08) if k % 2 == 0 else (1.06, 1.0))
    s = dict(clip=clip, src=src, dur=dur, z=z, head=head_list(head, -0.8 if first else 0.1))
    if sp != 1.0:
        s['ramp'] = [(0, 0), (dur, dur * sp)]
    if 'counter' in o:
        s['counter'] = o['counter']
    if o.get('bar'):
        s['bar'] = o['bar']
    if o.get('end'):
        s['endcard'] = True
        s['head'] = []
    return s


def configure(segs, impacts, leaks, chunks, prog=None, seed=0):
    C.SEGS = segs
    C.starts = np.cumsum([0] + [s['dur'] for s in segs]).tolist()
    C.TOTAL = C.starts[-1]
    C.NF = int(round(C.TOTAL * C.FPS))
    C.CUTS = C.starts[1:-1]
    kinds = []
    for i, _ in enumerate(C.CUTS):
        if segs[i + 1].get('endcard'):
            kinds.append('zoom')
        else:
            kinds.append(TR_CYCLE[(i + seed) % len(TR_CYCLE)])
    C.TRANS = dict(zip(C.CUTS, kinds))
    C.IMPACTS = impacts
    C.LEAKS = leaks
    C.CHUNKS = chunks
    C._cache.pop('title', None)

    def bar_hook(fr, s, lt):
        if s['bar'] == 'prog' and prog:
            prog_bar(fr, lt, prog)
        else:
            C.rarity_bar(fr, lt)
    C.BAR_HOOK = bar_hook


def prog_bar(fr, lt, prog):
    a, b, goal = prog
    bw, bh, cy = 560, 26, 612
    key = ('pbar', bw)
    if key not in C._cache:
        from PIL import Image, ImageDraw
        trk = Image.new('RGBA', (bw + 12, bh + 12), (0, 0, 0, 0))
        ImageDraw.Draw(trk).rounded_rectangle((0, 0, bw + 11, bh + 11), (bh + 12) // 2, fill=(10, 10, 25, 210), outline=(255, 255, 255, 120), width=3)
        C._cache[key] = C.to_premul(trk)
    trk = C._cache[key]
    al = C.e_out3((lt - 0.2) / 0.35)
    if al <= 0:
        return
    C.blit(fr, trk, C.W / 2, cy, 0.9 + 0.1 * al, 0, al)
    l1 = C.text_sprite('0', 30, C.F_BLACK_I, fill=(210, 210, 220), stroke=5)
    l2 = C.text_sprite(f'{goal:,}', 30, C.F_BLACK_I, grad=C.GOLD, stroke=5, glow=C.GOLD[1])
    C.blit(fr, l1['img'], C.W / 2 - bw / 2 - 24 - l1['tw'] / 2, cy + 2, 1, 0, al)
    C.blit(fr, l2['img'], C.W / 2 + bw / 2 + 24 + l2['tw'] / 2, cy + 2, 1, 0, al)
    p = C.e_io3((lt - 0.35) / 1.0)
    v = a + (b - a) * p
    fw = max(14, int(bw * v / goal))
    x0, y0 = int(C.W / 2 - bw / 2), int(cy - bh / 2)
    roi = fr[y0:y0 + bh, x0:x0 + fw]
    roi *= 0.0
    roi += np.array([1.0, 0.78, 0.2], np.float32)
    dot = C._cache.get('dot')
    if dot is None:
        d = np.zeros((90, 90, 4), np.float32); yy, xx = np.mgrid[:90, :90]
        r = np.exp(-((xx - 45) ** 2 + (yy - 45) ** 2) / (2 * 14 ** 2))
        d[..., 0] = r; d[..., 1] = r * 0.95; d[..., 2] = r * 0.8; d[..., 3] = r
        C._cache['dot'] = dot = d
    C.blit(fr, dot, x0 + fw, cy, 1.0 + 0.25 * math.sin(lt * 8), 0, al, add=True)


def music_json(name):
    return json.load(open(os.path.join(MUS, name + '.json')))


# ---------------------------------------------------------------- build one video config -> (segs, impacts, leaks, chunks, audio plan)
def build_clean(v, seed):
    mj = music_json(v['music'])
    beat = mj['beat']
    segs = []
    for k, item in enumerate(v['segs']):
        clip, src, beats, head = item[:4]
        o = item[4] if len(item) > 4 else {}
        segs.append(mk_seg(clip, src, beats * beat, head, o, k == 0, k))
    st = np.cumsum([0] + [s['dur'] for s in segs]).tolist()
    end_t = st[-2]
    impacts = [(st[1], 1.0), (end_t + 0.62, 0.55)]
    if len(st) > 6:
        impacts.append((st[len(st) // 2], 0.6))
    leaks = [(0.0, 0.7), (st[1], 1.0), (st[min(4, len(st) - 2)], 0.8), (end_t, 0.9)]
    return segs, impacts, leaks, [], dict(beat=beat, cuts=st[1:-1], end=end_t, total=st[-1], vo=None,
                                          counters=[(st[i] + 0.35, st[i] + 1.25) for i, s in enumerate(segs) if 'counter' in s])


def build_day(v, vid, seed):
    d = os.path.join(OUT, vid)
    os.makedirs(d, exist_ok=True)
    wav, js = os.path.join(d, 'vo.wav'), os.path.join(d, 'vo.json')
    texts = [ln[0] for ln in v['lines']]
    tag = json.dumps(texts)
    if not (os.path.exists(js) and json.load(open(js)).get('_tag') == tag):
        sh(['python3', '-I', os.path.join(ROOT, 'tools/voice/kokoro_tts.py'), '--voice', 'am_puck', '--speed', '0.8', '--pause', '0.5',
            '--out', wav, '--json', js] + texts)
        j = json.load(open(js)); j['_tag'] = tag; json.dump(j, open(js, 'w'))
    blocks = json.load(open(js))['blocks']
    segs, k = [], 0
    line_t = []
    for li, ln in enumerate(v['lines']):
        _, shots, head = ln[:3]
        o = ln[3] if len(ln) > 3 else {}
        t0 = 0.0 if li == 0 else VO_OFF + blocks[li]['start'] - 0.12
        t1 = VO_OFF + blocks[li + 1]['start'] - 0.12 if li + 1 < len(blocks) else VO_OFF + blocks[li]['end'] + 1.6
        line_t.append((t0, t1))
        last = li == len(v['lines']) - 1
        n = len(shots)
        for si, sh_ in enumerate(shots):
            clip, src = sh_[:2]
            so = dict(sh_[2]) if len(sh_) > 2 else {}
            hd = head if si == 0 else ''
            if si == 0:
                if o.get('prog'):
                    so['bar'] = 'prog'; so['counter'] = (v['prog'][0], v['prog'][1])
            if last and si == n - 1:
                so['end'] = True
            segs.append(mk_seg(clip, src, (t1 - t0) / n, hd, so, li == 0 and si == 0, k)); k += 1
    # karaoke chunks
    chunks = []
    total = line_t[-1][1]
    for bi, b in enumerate(blocks):
        ws = [(w['w'].upper(), VO_OFF + w['start'], VO_OFF + w['end']) for w in b['words']]
        groups, cur = [], []
        for w in ws:
            if cur and (len(cur) >= 4 or sum(len(x[0]) for x in cur) + len(w[0]) > 14):
                groups.append(cur); cur = []
            cur.append(w)
        if cur: groups.append(cur)
        if len(groups) > 1 and len(groups[-1]) == 1 and len(groups[-1][0][0]) <= 3:
            groups[-2] += groups.pop()
        nxt = VO_OFF + blocks[bi + 1]['start'] if bi + 1 < len(blocks) else total
        for gi, g in enumerate(groups):
            a = g[0][1] - 0.04
            e = groups[gi + 1][0][1] - 0.04 if gi + 1 < len(groups) else min(g[-1][2] + 0.4, nxt - 0.05)
            chunks.append(dict(words=g, t0=a, t1=e))
    st = np.cumsum([0] + [s['dur'] for s in segs]).tolist()
    end_t = line_t[-1][0]
    impacts = [(line_t[1][0], 0.7), (end_t + 0.62, 0.45)]
    leaks = [(0.0, 0.6)] + [(t0, 0.8) for t0, _ in line_t[1:]]
    pr = [i for i, ln in enumerate(v['lines']) if len(ln) > 3 and ln[3].get('prog')]
    counters = [(line_t[i][0] + 0.35, line_t[i][0] + 1.25) for i in pr]
    return segs, impacts, leaks, chunks, dict(cuts=st[1:-1], end=end_t, total=total, vo=wav, counters=counters)


# ---------------------------------------------------------------- audio
rng = np.random.default_rng(3)
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f): return sosfilt(butter(2, f, 'lowpass', fs=SR, output='sos'), x)


def load(path):
    raw = sh(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'])
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def put(buf, x, t):
    i = int(t * SR)
    if i < 0: x = x[-i:]; i = 0
    n = min(len(x), len(buf) - i)
    if n > 0: buf[i:i + n] += x[:n]


def whoosh(buf, tc, vol):
    d1, d2 = 0.22, 0.2
    n = int((d1 + d2) * SR); tt = np.arange(n) / SR
    noise = rng.normal(0, 1, n)
    lo, mid, hi = bp(noise, 300, 1200), bp(noise, 900, 3500), bp(noise, 2500, 8000)
    p = np.clip(tt / d1, 0, 1); q = np.clip((tt - d1) / d2, 0, 1)
    sw = np.where(tt < d1, p, 1 - q)
    sig = lo * (1 - sw) + mid * np.minimum(sw * 2, 1) * 0.8 + hi * sw ** 2 * 0.6
    envl = np.where(tt < d1, (tt / d1) ** 2.5, np.exp(-(tt - d1) / 0.07))
    sig = sig * envl / (np.abs(sig).max() + 1e-6) * vol
    pan = np.clip(tt / (d1 + d2), 0, 1)
    put(buf, (np.stack([sig * np.cos(pan * np.pi / 2), sig * np.sin(pan * np.pi / 2)], 1) * 1.4).astype(np.float32), tc - d1)


def impact(buf, tc, a):
    n = int(1.2 * SR); tt = np.arange(n) / SR
    f = 38 + 80 * np.exp(-tt / 0.08)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.38)
    click = lp(rng.normal(0, 1, n), 2500) * np.exp(-tt / 0.012) * 0.5
    body = bp(rng.normal(0, 1, n), 120, 900) * np.exp(-tt / 0.09) * 0.6
    sig = np.tanh((sub * 1.2 + click + body) * 1.6) * 0.42 * a
    put(buf, np.stack([sig, sig], 1).astype(np.float32), tc)


def ticks(buf, t0, t1, count, vol):
    for i in range(count):
        tc = t0 + (t1 - t0) * (1 - (1 - i / count) ** 2)
        n = int(0.03 * SR); tt = np.arange(n) / SR
        s = np.sin(2 * np.pi * 2400 * tt) * np.exp(-tt / 0.006) * vol
        put(buf, np.stack([s, s], 1).astype(np.float32), tc)


def make_audio(v, plan, impacts, path):
    total = plan['total']
    N = int(total * SR)
    mus = load(os.path.join(MUS, v['music'] + '.wav'))
    if len(mus) < N:
        mus = np.tile(mus, (N // len(mus) + 1, 1))
    mus = mus[:N]
    mus /= np.abs(mus).max() + 1e-6
    t = np.arange(N) / SR
    fade = np.clip((total - t) / 0.9, 0, 1)
    sfx = np.zeros((N, 2), np.float32)
    voice = plan['vo'] is not None
    s_vol = 0.35 if voice else 1.0          # Effekte leise (User: "Effekte viel zu laut")
    for tc in plan['cuts']:
        whoosh(sfx, tc, 0.07 * s_vol)
    for tc, a in impacts:
        impact(sfx, tc, a * 0.55 * s_vol)
    for t0, t1 in plan['counters']:
        ticks(sfx, t0, t1, 12, 0.03 * s_vol)
    if voice:
        vo = np.zeros((N, 2), np.float32)
        put(vo, load(plan['vo']), VO_OFF)
        env = np.abs(vo).max(axis=1)
        k = int(0.05 * SR); env = np.convolve(env, np.ones(k) / k, 'same')
        duck = 1 - 0.4 * np.clip(env / 0.03, 0, 1)
        mix = vo + mus * (MUSIC_VO * 2.2 * duck * fade)[:, None] + sfx
    else:
        mix = mus * (0.8 * fade)[:, None] + sfx
    mix /= max(1.0, np.abs(mix).max() / 0.95)
    wavfile.write(path, SR, mix.astype(np.float32))


# ---------------------------------------------------------------- main
def setup(days, vid, i):
    v = days.VIDEOS[vid]
    if v['kind'] == 'clean':
        segs, imp, lk, ch, plan = build_clean(v, i)
    else:
        segs, imp, lk, ch, plan = build_day(v, vid, i)
    for s in segs:
        s.pop('_frames', None)
    configure(segs, imp, lk, ch, v.get('prog'), seed=i)
    return v, plan, imp


def stills(days, vid, i):
    v, plan, imp = setup(days, vid, i)
    T = C.TOTAL
    ts = [0.0] + [min(T - 0.05, x) for x in np.linspace(0.6, T - 0.2, 8)]
    ims = []
    for tt in ts:
        im = C.render_frame(int(tt * C.FPS))
        im = cv2.resize(im, (270, 480), interpolation=cv2.INTER_AREA)
        cv2.putText(im, f'{tt:.1f}', (6, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
        ims.append(im)
    sheet = np.vstack([np.hstack(ims[r * 5:(r + 1) * 5] + [np.zeros_like(ims[0])] * (5 - len(ims[r * 5:(r + 1) * 5]))) for r in range(2)])
    d = os.path.join(OUT, vid); os.makedirs(d, exist_ok=True)
    cv2.imwrite(os.path.join(d, 'sheet.jpg'), cv2.cvtColor(sheet, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 82])
    print(vid, f'{T:.1f}s', 'sheet ok', flush=True)


def render(days, vid, i):
    d = os.path.join(OUT, vid); os.makedirs(d, exist_ok=True)
    out = os.path.join(d, vid + '.mp4')
    if os.path.exists(out):
        print(vid, 'schon fertig'); return
    v, plan, imp = setup(days, vid, i)
    aw = os.path.join(d, 'mix.wav')
    make_audio(v, plan, imp, aw)
    tmp = out + '.part.mp4'
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{C.W}x{C.H}', '-r', str(C.FPS), '-i', '-',
                          '-i', aw, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-maxrate', '17M',
                          '-bufsize', '34M', '-pix_fmt', 'yuv420p', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:a', 'aac', '-b:a', '192k',
                          '-ar', '48000', '-shortest', '-movflags', '+faststart', tmp], stdin=subprocess.PIPE)
    import time; t0 = time.time()
    for n in range(C.NF):
        p.stdin.write(C.render_frame(n).tobytes())
    p.stdin.close(); p.wait()
    if p.returncode:
        raise SystemExit('ffmpeg Fehler ' + vid)
    os.replace(tmp, out)
    print(vid, f'{C.TOTAL:.1f}s fertig in {time.time() - t0:.0f}s', flush=True)


if __name__ == '__main__':
    spec = importlib.util.spec_from_file_location('days', sys.argv[1])
    days = importlib.util.module_from_spec(spec); spec.loader.exec_module(days)
    ids = list(days.VIDEOS) if sys.argv[2] == 'all' else sys.argv[2].split(',')
    order = list(days.VIDEOS)
    for vid in ids:
        (stills if sys.argv[3] == 'stills' else render)(days, vid, order.index(vid))
