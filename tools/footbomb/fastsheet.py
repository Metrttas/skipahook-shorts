#!/usr/bin/env python3
# Schneller Kontaktbogen (22.11.2026): berechnet NUR die Prüf-Bilder (Bild 1, Schnittanfang + Mitte jedes Schnitts, Ende),
# statt wie fbedit.py sheet alle ~800 Bilder zu komponieren. Eine Zeile je Video, mehrere Videos untereinander in einer Datei.
#   python3 fastsheet.py <spec.py> <id|all|id,id> <out.jpg> [thumb_w=150]
import sys, os, importlib.util, cv2, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fbedit as E

spec = importlib.util.spec_from_file_location('spec', sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
ids = list(m.VIDEOS) if sys.argv[2] == 'all' else sys.argv[2].split(',')
out = sys.argv[3]; tw = int(sys.argv[4]) if len(sys.argv) > 4 else 150; th = int(tw * 16 / 9)
rows = []
for vid in ids:
    v = m.VIDEOS[vid]; E._clips.clear()
    cuts, per = E.plan(v)
    want = sorted(set([1] + [round((a + 0.05) * E.FPS) for a, b, s in cuts] + [round((a + b) / 2 * E.FPS) for a, b, s in cuts]
                      + [int(v['dur'] * E.FPS) - 3]))
    ims = []
    for n in want:
        T = n / E.FPS
        ci = 0
        while ci < len(cuts) - 1 and T >= cuts[ci][1]: ci += 1
        a, b, sg = cuts[ci]; lt = T - a; sg['_len'] = b - a
        src = E.clip(sg['clip']).frame_at(sg.get('t', 0) + lt * sg.get('speed', 1.0))
        fr = E.compose(src, sg, lt, per, T, v); E.draw_text(fr, v, T)
        im = cv2.resize(np.clip(fr, 0, 255).astype(np.uint8), (tw, th), interpolation=cv2.INTER_AREA)
        cv2.putText(im, f'{T:.1f}', (3, th - 6), 0, 0.4, (0, 255, 255), 1)
        ims.append(im)
    row = np.hstack(ims)
    lab = np.zeros((22, row.shape[1], 3), np.uint8)
    cv2.putText(lab, f"{vid}  {v['sound'].split('/')[-1]}  {v['dur']:.1f}s  cuts {len(cuts)}", (4, 16), 0, 0.5, (0, 255, 255), 1)
    rows.append(np.vstack([lab, row]))
W = max(r.shape[1] for r in rows)
rows = [cv2.copyMakeBorder(r, 0, 4, 0, W - r.shape[1], cv2.BORDER_CONSTANT) for r in rows]
cv2.imwrite(out, np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 78])
print('ok', out)
