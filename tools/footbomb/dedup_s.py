# Doppelbilder (fehlende Aufnahme-Bilder, vom Encoder wiederholt) durch optischen Fluss ersetzen – STREAMING-Fassung (22.11.2026).
# Gleiches Ergebnis wie dedup.py, hält aber nur die Bilder einer Doppel-Strecke im RAM (dedup.py lud alle ~800 Bilder = ~5 GB).
# python3 dedup_s.py in.mp4 out.mp4
import sys, cv2, numpy as np, subprocess
src, dst = sys.argv[1], sys.argv[2]
cap = cv2.VideoCapture(src)
ok, first = cap.read()
h, w = first.shape[:2]
dis = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
gy, gx = np.mgrid[0:h, 0:w].astype(np.float32)
def warp(img, flow, t):
    return cv2.remap(img, gx + flow[..., 0] * t, gy + flow[..., 1] * t, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
def small(f): return cv2.resize(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), (w // 4, h // 4))
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{w}x{h}', '-r', '60', '-i', '-',
                      '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', '-pix_fmt', 'yuv420p', dst], stdin=subprocess.PIPE)
out = lambda f: p.stdin.write(f.tobytes())
good = first; last_small = small(first); out(first)
pend = []; n = 1; ndup = 0; fixed = 0
while True:
    ok, f = cap.read()
    if not ok: break
    n += 1
    s = small(f)
    isdup = float(np.mean(cv2.absdiff(s, last_small))) < 0.35
    last_small = s
    if isdup:
        pend.append(f); ndup += 1; continue
    if pend:
        if len(pend) <= 3:
            a, b = good, f; L = len(pend) + 1
            ga = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY); gb = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
            fab = dis.calc(ga, gb, None); fba = dis.calc(gb, ga, None)
            for k in range(1, L):
                t = k / L
                out(cv2.addWeighted(warp(a, fba, t), 1 - t, warp(b, fab, 1 - t), t, 0)); fixed += 1
        else:
            for q in pend: out(q)
        pend = []
    out(f); good = f
for q in pend: out(q)
p.stdin.close(); p.wait()
print(dst, 'frames', n, 'dups', ndup, 'fixed', fixed)
