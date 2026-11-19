# Doppelbilder (fehlende Aufnahme-Bilder, vom Encoder wiederholt) durch optischen Fluss ersetzen.
# python3 dedup.py in.mp4 out.mp4
import sys, cv2, numpy as np, subprocess
src, dst = sys.argv[1], sys.argv[2]
cap = cv2.VideoCapture(src); F = []
while True:
    ok, f = cap.read()
    if not ok: break
    F.append(f)
n = len(F); h, w = F[0].shape[:2]
small = [cv2.resize(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), (w // 4, h // 4)) for f in F]
dup = [False] + [float(np.mean(cv2.absdiff(small[i], small[i - 1]))) < 0.35 for i in range(1, n)]
dis = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
def warp(img, flow, t):
    gy, gx = np.mgrid[0:h, 0:w].astype(np.float32)
    return cv2.remap(img, gx + flow[..., 0] * t, gy + flow[..., 1] * t, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
fixed = 0; i = 1
while i < n:
    if dup[i]:
        j = i
        while j < n and dup[j]: j += 1
        a, b = i - 1, j  # gute Bilder davor/danach
        if b < n and j - i <= 3:
            ga = cv2.cvtColor(F[a], cv2.COLOR_BGR2GRAY); gb = cv2.cvtColor(F[b], cv2.COLOR_BGR2GRAY)
            fab = dis.calc(ga, gb, None); fba = dis.calc(gb, ga, None)
            for k in range(i, j):
                t = (k - a) / (b - a)
                F[k] = cv2.addWeighted(warp(F[a], fba, t), 1 - t, warp(F[b], fab, 1 - t), t, 0)
                fixed += 1
        i = j
    else:
        i += 1
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{w}x{h}', '-r', '60', '-i', '-',
                      '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', '-pix_fmt', 'yuv420p', dst], stdin=subprocess.PIPE)
for f in F: p.stdin.write(f.tobytes())
p.stdin.close(); p.wait()
print(dst, 'frames', n, 'dups', sum(dup), 'fixed', fixed)
