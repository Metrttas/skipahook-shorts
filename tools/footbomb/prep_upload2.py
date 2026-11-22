#!/usr/bin/env python3
# 22.11.2026: Chrome-Upload (GitHub-Web) nimmt max ~10,4 MB je Aufruf -> Videos auf <= 9,6 MB bringen.
# 2-Pass-x264 mit Zielbitrate aus der Dauer (Ton wird kopiert). Ergebnis nach /home/claude/up/<name>.mp4
#   python3 prep_upload2.py <mp4> [<mp4> ...]
import os, sys, subprocess, tempfile
TARGET = 9.1e6          # Bytes, Puffer zu 9,6 MB
CAP = 9_600_000
os.makedirs('/home/claude/up', exist_ok=True)
for src in sys.argv[1:]:
    name = os.path.basename(src); out = os.path.join('/home/claude/up', name)
    if os.path.getsize(src) <= CAP:
        subprocess.run(['cp', src, out], check=True); print(name, os.path.getsize(out), 'copy', flush=True); continue
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src],
                               capture_output=True, text=True).stdout)
    abr = int(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a:0', '-show_entries', 'stream=bit_rate', '-of', 'csv=p=0', src],
                             capture_output=True, text=True).stdout.strip() or 192000)
    target = TARGET
    for attempt in range(3):
        vb = int(target * 8 / dur - abr - 60_000)          # Obergrenze über VBV (1 Durchgang, ~halbe Rechenzeit von 2-Pass)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-c:v', 'libx264', '-preset', 'medium', '-crf', '19',
                        '-maxrate', str(vb), '-bufsize', str(vb), '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart', out], check=True)
        sz = os.path.getsize(out)
        if sz <= CAP: break
        target *= 0.93
    print(name, sz, f'{vb / 1e6:.1f} Mbit/s', f'{dur:.1f}s', 'OK' if sz <= CAP else 'ZU GROSS', flush=True)
