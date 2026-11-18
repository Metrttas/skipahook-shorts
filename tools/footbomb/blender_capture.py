# Footbomb-Aufnahme aus Roblox Studio (18.11.2026) – in Blender per MCP execute_blender_code ausführen (einmal je Blender-Sitzung).
# Danach: builtins._fb_takef('name', 20) nimmt 20 s auf (Viewport-Mitte 1600x900, 60 fps), Ergebnis
#   Documents\Footbomb_Videos\<Datum>\name.mp4 + name.mp4.ts.json {wall0, ts}. Status: builtins._fb_takes.
# ffmpeg = SteelSeries-Build (kein rawvideo-Demuxer!) -> Bilder als QuickTime 'raw ' über stdin (eigener MOV-Kopf).
import ctypes, ctypes.wintypes as W, struct, subprocess, threading, time, os, json, builtins
import numpy as np
F = r'C:\Program Files\SteelSeries\GG\apps\moments\ffmpeg.exe'
ROOT = r'C:\Users\Admin\Documents\Footbomb_Videos\2026-11-18'
u = ctypes.windll.user32; g = ctypes.windll.gdi32
try: ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception: pass

class BIH(ctypes.Structure):
    _fields_ = [('biSize', W.DWORD), ('biWidth', W.LONG), ('biHeight', W.LONG), ('biPlanes', W.WORD), ('biBitCount', W.WORD),
                ('biCompression', W.DWORD), ('biSizeImage', W.DWORD), ('biXPelsPerMeter', W.LONG), ('biYPelsPerMeter', W.LONG),
                ('biClrUsed', W.DWORD), ('biClrImportant', W.DWORD)]

class Grab:
    def __init__(s, x, y, sw, sh, w, h, bits=24):
        s.x, s.y, s.sw, s.sh, s.w, s.h = x, y, sw, sh, w, h
        s.sdc = u.GetDC(0); s.mdc = g.CreateCompatibleDC(s.sdc)
        s.bmp = g.CreateCompatibleBitmap(s.sdc, w, h); g.SelectObject(s.mdc, s.bmp); g.SetStretchBltMode(s.mdc, 3)
        s.bi = BIH(); s.bi.biSize = ctypes.sizeof(BIH); s.bi.biWidth = w; s.bi.biHeight = h; s.bi.biPlanes = 1; s.bi.biBitCount = bits
        s.stride = ((w * bits // 8 + 3) // 4) * 4; s.buf = ctypes.create_string_buffer(s.stride * h)
    def grab(s):
        if s.sw == s.w and s.sh == s.h: g.BitBlt(s.mdc, 0, 0, s.w, s.h, s.sdc, s.x, s.y, 0x00CC0020)
        else: g.StretchBlt(s.mdc, 0, 0, s.w, s.h, s.sdc, s.x, s.y, s.sw, s.sh, 0x00CC0020)
        g.GetDIBits(s.mdc, s.bmp, 0, s.h, s.buf, ctypes.byref(s.bi), 0)
        return s.buf
    def close(s):
        g.DeleteObject(s.bmp); g.DeleteDC(s.mdc); u.ReleaseDC(0, s.sdc)
builtins._FBGrab2 = Grab

def box(t, *p):
    d = b''.join(p); return struct.pack('>I', 8 + len(d)) + t + d
def full(t, v, fl, *p): return box(t, struct.pack('>I', (v << 24) | fl), *p)

def mov_header(w, h, n, fps=60):
    fsz = w * h * 3
    mat = b''.join(struct.pack('>iii', *r) for r in [[0x10000, 0, 0], [0, 0x10000, 0], [0, 0, 0x40000000]])
    mvhd = full(b'mvhd', 0, 0, struct.pack('>IIII', 0, 0, fps, n), struct.pack('>IH', 0x10000, 0x100), b'\0' * 10, mat, b'\0' * 24, struct.pack('>I', 2))
    tkhd = full(b'tkhd', 0, 3, struct.pack('>IIIII', 0, 0, 1, 0, n), b'\0' * 8, struct.pack('>hhhH', 0, 0, 0, 0), mat, struct.pack('>II', w << 16, h << 16))
    mdhd = full(b'mdhd', 0, 0, struct.pack('>IIII', 0, 0, fps, n), struct.pack('>HH', 0, 0))
    hdlr = full(b'hdlr', 0, 0, b'mhlr', b'vide', b'\0' * 12, b'\0')
    vmhd = full(b'vmhd', 0, 1, b'\0' * 8)
    dinf = box(b'dinf', full(b'dref', 0, 0, struct.pack('>I', 1), full(b'alis', 0, 1)))
    entry = box(b'raw ', b'\0' * 6, struct.pack('>H', 1), struct.pack('>HH', 0, 0), b'\0' * 4, struct.pack('>II', 0, 512), struct.pack('>HH', w, h),
                struct.pack('>II', 0x480000, 0x480000), struct.pack('>I', 0), struct.pack('>H', 1), b'\0' * 32, struct.pack('>hh', 24, -1))
    stsd = full(b'stsd', 0, 0, struct.pack('>I', 1), entry)
    stts = full(b'stts', 0, 0, struct.pack('>III', 1, n, 1)); stsc = full(b'stsc', 0, 0, struct.pack('>IIII', 1, 1, n, 1))
    stsz = full(b'stsz', 0, 0, struct.pack('>II', fsz, n))
    def build(off):
        stbl = box(b'stbl', stsd, stts, stsc, stsz, full(b'co64', 0, 0, struct.pack('>IQ', 1, off)))
        moov = box(b'moov', mvhd, box(b'trak', tkhd, box(b'mdia', mdhd, hdlr, box(b'minf', vmhd, dinf, stbl))))
        return box(b'ftyp', b'qt  ', struct.pack('>I', 0x200), b'qt  ') + moov
    pre = build(0); pre = build(len(pre) + 16)
    return pre + struct.pack('>I', 1) + b'mdat' + struct.pack('>Q', 16 + fsz * n)

def enc_frames(frames, w, h, stride, out):
    p = subprocess.Popen([F, '-hide_banner', '-loglevel', 'error', '-y', '-f', 'mov', '-i', 'pipe:0', '-c:v', 'h264_nvenc', '-preset', 'p5',
                          '-rc', 'vbr', '-cq', '16', '-b:v', '45M', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    err = []; tr = threading.Thread(target=lambda: err.append(p.stderr.read()), daemon=True); tr.start()
    p.stdin.write(mov_header(w, h, len(frames)))
    for i in range(len(frames)):
        a = np.frombuffer(frames[i], np.uint8)[:stride * h].reshape(h, stride)[:, :w * 3].reshape(h, w, 3)[::-1, :, ::-1]
        p.stdin.write(np.ascontiguousarray(a).tobytes()); frames[i] = None
    p.stdin.close(); p.wait(timeout=120); tr.join(timeout=5)
    return p.returncode, (err[0] if err else b'').decode(errors='ignore')[-300:]

builtins._fb_takes = getattr(builtins, '_fb_takes', {})
def take(name, secs, x=4320, y=774, w=1600, h=900):   # x/y = Mitte des Studio-Viewports auf dem 2. Monitor (2560x1184 ab 3840/632)
    secs = min(secs, 20); os.makedirs(ROOT, exist_ok=True)
    G = Grab(x, y, w, h, w, h); stride = G.stride; frames = []; ts = []; wall0 = time.time(); t0 = time.perf_counter()
    while time.perf_counter() - t0 <= secs:
        frames.append(bytes(G.grab())); ts.append(time.perf_counter() - t0)
    G.close()
    st = {'state': 'enc', 'n': len(ts), 'wall0': wall0}; builtins._fb_takes[name] = st
    out = os.path.join(ROOT, name + '.mp4'); json.dump({'wall0': wall0, 'ts': ts}, open(out + '.ts.json', 'w'))
    def bg():
        rc, e = enc_frames(frames, w, h, stride, out); st.update(rc=rc, err=e, state='done')
    threading.Thread(target=bg, daemon=True).start()
    return st
builtins._fb_takef = take
result = {'ok': 1}
