#!/usr/bin/env python3
# Footbomb-Edits (ab 18.11.2026, User: "Querformat, bisschen näher rangezoomt, oben und unten blurry, man soll mehr sehen",
#   nur SEINE Sounds, Schnitt auf dem Beat, ein Satz oben wie in den Volley-Bomb-TikToks).
#   python3 fbedit.py <spec.py> <id|all> [sheet|render]
# Spec: VIDEOS = {id: dict(sound='snd/u3.wav', s0=0.0, dur=14.0, segs=[dict(clip, t, n, speed, z, cx, cy, fx), ...],
#                          text=[(t0, t1, 'TEAM PLAYS', style)], end='Search FOOTBOMB on Roblox')}
#   segs: n = Länge in Beats (Beat-Raster aus beats.json des Sounds ab s0), t = Startzeit im Clip (s), speed (0.5 = Zeitlupe),
#         z = Zoom (>= 1.25 = Band füllt sich), cx/cy = Bildmitte im Quellbild (0..1), fx: 'flash' | 'punch' | 'shake'.
# Look: Band 1080 x 760 (y 600-1360) mit dem Spielbild, darüber/darunter dasselbe Bild groß + stark unscharf + dunkler.
import sys, os, json, math, subprocess, importlib.util
import numpy as np, cv2
sys.path.insert(0, '/home/claude/sah/tools/promo/ae')
import aecore as C

_sc = {}
def S(spr, k):  # Sprite (RGB premultipliziert 0..1) -> BGR 0..255, Alpha bleibt 0..1
    key = (id(spr), k)
    if key not in _sc:
        a = spr[k].copy(); a[..., :3] = a[..., 2::-1] * 255; _sc[key] = a
    return _sc[key]

W, H, FPS = 1080, 1920, 60
BY, BH = 600, 760
ASP = W / BH
HERE = os.path.dirname(os.path.abspath(__file__))
BEATS = json.load(open(os.path.join(HERE, 'snd/beats.json')))


class Clip:
    def __init__(s, path):
        s.path = path; s.cap = cv2.VideoCapture(path); s.fps = s.cap.get(cv2.CAP_PROP_FPS) or 60
        s.n = int(s.cap.get(cv2.CAP_PROP_FRAME_COUNT)); s.pos = -1; s.last = None; s.cache = {}
        tsf = path + '.ts.json'
        s.ts = None
        if os.path.exists(tsf):
            d = json.load(open(tsf)); d = d['ts'] if isinstance(d, dict) else d
            if len(d) == s.n: s.ts = np.array(d)       # echte Aufnahmezeiten (VFR-Ausgleich)

    def _get(s, i):
        i = max(0, min(s.n - 1, i))
        if i in s.cache: return s.cache[i]
        if i < s.pos or i > s.pos + 30:
            s.cap.set(cv2.CAP_PROP_POS_FRAMES, i); s.pos = i - 1
        while s.pos < i:
            ok, fr = s.cap.read()
            if not ok: break
            s.pos += 1; s.last = fr
            s.cache[s.pos] = fr
            if len(s.cache) > 8: s.cache.pop(min(s.cache))
        return s.cache.get(i, s.last)

    def frame_at(s, t):
        # Zwischenbild-Mischung: echte Zeitachse (ts) + weiche Zeitlupe
        if s.ts is not None:
            j = int(np.searchsorted(s.ts, t)) - 1
            j = max(0, min(len(s.ts) - 2, j))
            a = (t - s.ts[j]) / max(1e-6, s.ts[j + 1] - s.ts[j])
        else:
            f = t * s.fps; j = int(math.floor(f)); a = f - j
        a = min(max(a, 0.0), 1.0)
        A = s._get(j)
        if a < 0.12: return A
        B = s._get(j + 1)
        if a > 0.88: return B
        return cv2.addWeighted(A, 1 - a, B, a, 0)


_clips = {}
def clip(p):
    if p not in _clips: _clips[p] = Clip(p)
    return _clips[p]


def beat_grid(sound, s0, dur):
    b = BEATS[sound]
    per = b['period']; first = b['beats'][0]
    k0 = math.ceil((s0 - first) / per - 1e-6)
    t0 = first + k0 * per - s0                  # erster Beat relativ zum Video-Start
    return [t0 + i * per for i in range(-1, int(dur / per) + 3)], per


def plan(v):
    grid, per = beat_grid(v['sound'], v.get('s0', 0.0), v['dur'])
    grid = [g for g in grid if g > -1e-6]
    if grid[0] > 0.02: grid = [0.0] + grid
    cuts = []; k = 0
    for sg in v['segs']:
        a = grid[min(k, len(grid) - 1)]; k += sg.get('n', 4)
        b = grid[min(k, len(grid) - 1)] if k < len(grid) else v['dur']
        cuts.append((a, min(b, v['dur']), sg))
    if cuts: cuts[-1] = (cuts[-1][0], v['dur'], cuts[-1][2])
    return cuts, per


def compose(src, sg, lt, per, T, v):
    z = sg.get('z', 1.35)
    fx = sg.get('fx', '')
    if 'punch' in fx or 'flash' in fx: z *= 1 + 0.06 * math.exp(-lt / 0.12)
    if sg.get('zin'): z *= 1 + sg['zin'] * C.e_io3(lt / max(0.01, sg.get('_len', 1)))
    hS, wS = src.shape[:2]
    cw = wS / z; ch = cw / ASP
    if ch > hS: ch = hS; cw = ch * ASP
    cx = sg.get('cx', 0.5) * wS; cy = sg.get('cy', 0.5) * hS
    if 'shake' in fx:
        a = 9 * math.exp(-lt / 0.18); cx += a * math.sin(lt * 90); cy += a * math.cos(lt * 77)
    x0 = min(max(cx - cw / 2, 0), wS - cw); y0 = min(max(cy - ch / 2, 0), hS - ch)
    M = np.array([[W / cw, 0, -x0 * W / cw], [0, BH / ch, -y0 * BH / ch]], np.float32)
    band = cv2.warpAffine(src, M, (W, BH), flags=cv2.INTER_AREA if z < 1.6 else cv2.INTER_CUBIC)
    # Hintergrund: ganzes Bild, Cover, stark unscharf, dunkler
    small = cv2.resize(src, (wS // 8, hS // 8), interpolation=cv2.INTER_AREA)
    sc = max(W / small.shape[1], H / small.shape[0]) * 1.08
    bg = cv2.resize(small, (int(small.shape[1] * sc), int(small.shape[0] * sc)), interpolation=cv2.INTER_LINEAR)
    oy = (bg.shape[0] - H) // 2; ox = (bg.shape[1] - W) // 2
    bg = cv2.GaussianBlur(bg[oy:oy + H, ox:ox + W], (0, 0), 18)
    fr = (bg.astype(np.float32) * 0.5)
    # weicher Schatten unter dem Band
    fr[BY - 40:BY] *= np.linspace(1, 0.6, 40)[:, None, None]
    fr[BY + BH:BY + BH + 40] *= np.linspace(0.6, 1, 40)[:, None, None]
    fr[BY:BY + BH] = band.astype(np.float32)
    if 'flash' in fx:
        fr += 255 * 0.85 * math.exp(-lt / 0.09)
    return fr


def draw_text(fr, v, T):
    for ev in v.get('text', []):
        t0, t1, txt = ev[:3]; st = ev[3] if len(ev) > 3 else {}
        if not (t0 <= T < t1): continue
        lt = T - t0
        size = st.get('size', 104)
        spr = C.text_sprite(txt, size, font=st.get('font', C.F_BLACK), fill=tuple(st.get('fill', (255, 255, 255))),
                            grad=st.get('grad'), stroke=st.get('stroke'))
        while spr['w'] > W - 40 and size > 50:
            size -= 6; spr = C.text_sprite(txt, size, font=st.get('font', C.F_BLACK), fill=tuple(st.get('fill', (255, 255, 255))), grad=st.get('grad'))
        pop = st.get('pop', True)
        s = 1.0 if not pop else (0.75 + 0.25 * C.e_out3(lt / 0.16)) * (1 + 0.04 * math.exp(-lt / 0.1))
        y = st.get('y', BY - 95)
        C.blit(fr, S(spr, 'shadow'), W / 2, y + 6, s)
        C.blit(fr, S(spr, 'img'), W / 2, y, s)
    if v.get('end'):
        # unten die Such-Pille, immer da (dezent)
        spr = C.text_sprite(v['end'], 46, font=C.F_BLACK, fill=(255, 255, 255))
        C.blit(fr, S(spr, 'shadow'), W / 2, BY + BH + 90 + 4, 1)
        C.blit(fr, S(spr, 'img'), W / 2, BY + BH + 90, 1)


def frames(v):
    cuts, per = plan(v)
    N = int(round(v['dur'] * FPS))
    ci = 0
    for n in range(N):
        T = n / FPS
        while ci < len(cuts) - 1 and T >= cuts[ci][1]: ci += 1
        a, b, sg = cuts[ci]; lt = T - a; sg['_len'] = b - a
        src = clip(sg['clip']).frame_at(sg.get('t', 0) + lt * sg.get('speed', 1.0))
        fr = compose(src, sg, lt, per, T, v)
        draw_text(fr, v, T)
        yield n, np.clip(fr, 0, 255).astype(np.uint8)


def render(v, vid, out):
    os.makedirs(out, exist_ok=True)
    tmp = os.path.join(out, vid + '.v.mp4')
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-pix_fmt', 'yuv420p', tmp], stdin=subprocess.PIPE)
    for n, fr in frames(v): p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()
    s0 = v.get('s0', 0.0)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-ss', f'{s0:.3f}', '-t', f"{v['dur']:.3f}", '-i', os.path.join(HERE, v['sound']),
                    '-filter_complex', f"[1:a]afade=t=out:st={max(0, v['dur'] - 0.25):.3f}:d=0.25,loudnorm=I=-14:TP=-1:LRA=11[a]",
                    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart',
                    os.path.join(out, vid + '.mp4')], check=True)
    os.remove(tmp)


def sheet(v, vid, out):
    os.makedirs(out, exist_ok=True)
    cuts, per = plan(v)
    want = sorted(set([round((a + 0.05) * FPS) for a, b, s in cuts] + [round((a + b) / 2 * FPS) for a, b, s in cuts]))
    ims = []
    for n, fr in frames(v):
        if n in want: ims.append(cv2.resize(fr, (216, 384), interpolation=cv2.INTER_AREA))
    cols = 10; rows = (len(ims) + cols - 1) // cols
    S = np.zeros((rows * 384, cols * 216, 3), np.uint8)
    for i, im in enumerate(ims): S[(i // cols) * 384:(i // cols + 1) * 384, (i % cols) * 216:(i % cols + 1) * 216] = im
    cv2.imwrite(os.path.join(out, vid + '_sheet.jpg'), S, [cv2.IMWRITE_JPEG_QUALITY, 80])


if __name__ == '__main__':
    spec = importlib.util.spec_from_file_location('spec', sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    ids = list(m.VIDEOS) if sys.argv[2] == 'all' else sys.argv[2].split(',')
    mode = sys.argv[3] if len(sys.argv) > 3 else 'sheet'
    out = getattr(m, 'OUT', os.path.join(HERE, 'out'))
    for vid in ids:
        _clips.clear()
        (render if mode == 'render' else sheet)(m.VIDEOS[vid], vid, out)
        print(vid, mode, 'ok', flush=True)
