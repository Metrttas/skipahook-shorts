#!/usr/bin/env python3
"""Wiederholungs-Check je Account (User 20.11.: "nicht so ähnlich, sonst denkt die Plattform, ich bin ein Spammer – wenigstens nicht auf demselben Account").
   python3 check_repeat.py specs/fb_1121.py specs/fb_1120.py [specs/fb_1119.py ...]
   Erste Spec = neuer Tag, die anderen = Vortage (neueste zuerst). Account = (Marke, Netz).
   STOP: derselbe Clip zweimal am selben Tag auf einem Account, derselbe Sound zweimal am Tag, Hook-Text wörtlich schon mal auf dem Account.
   WARN: Haupt-Clip einer Einzel-Story lief gestern auf dem Account schon als Einzel-Story; Combo hat > 50 % gleiche Clips wie eine Combo von gestern."""
import sys, importlib.util, collections
def load(p):
    sp = importlib.util.spec_from_file_location(p, p); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
def info(m):
    acc = {}
    for b, net, items in m.POST_PLAN:
        L = []
        for vid, _ in items:
            v = m.VIDEOS[vid]
            clips = sorted({x['clip'].split('/')[-1][:-4] for x in v['segs']})
            hooks = {t[2] for t in v['text'] if len(t[2]) > 3 and not (len(t) > 3 and 'size' in t[3])}  # Combo-Labels (SCORPION, 1/2/3) zählen nicht
            L.append(dict(vid=vid, clips=clips, snd=v['sound'], hooks=hooks, combo=len(clips) > 1))
        acc[(b, net)] = L
    return acc
new = info(load(sys.argv[1])); old = [info(load(p)) for p in sys.argv[2:]]
bad = 0
for a, L in new.items():
    c = collections.Counter(x for v in L for x in v['clips'])
    s = collections.Counter(v['snd'] for v in L)
    for k, n in c.items():
        if n > 1: print('STOP', a, 'Clip zweimal am Tag:', k); bad += 1
    for k, n in s.items():
        if n > 1: print('STOP', a, 'Sound zweimal am Tag:', k); bad += 1
    for d, O in enumerate(old):
        P = O.get(a, [])
        for v in L:
            for p in P:
                if v['hooks'] & p['hooks']: print('STOP', a, v['vid'], 'Hook wie', p['vid'], v['hooks'] & p['hooks']); bad += 1
                if d == 0 and not v['combo'] and not p['combo'] and v['clips'] == p['clips']: print('WARN', a, v['vid'], 'gleiche Einzel-Story wie gestern', p['vid'], v['clips'])
                if d == 0 and v['combo'] and p['combo'] and len(set(v['clips']) & set(p['clips'])) > len(v['clips']) / 2: print('WARN', a, v['vid'], 'Combo fast wie gestern', p['vid'])
print('OK' if not bad else f'{bad} STOP')
sys.exit(1 if bad else 0)
