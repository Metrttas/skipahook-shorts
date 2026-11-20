#!/usr/bin/env python3
"""Wiederholungs-Check je Account (User 20.11.: "nicht so ähnlich, sonst denkt die Plattform, ich bin ein Spammer – wenigstens nicht auf demselben Account").
   python3 check_repeat.py specs/fb_1121.py,specs/ship_1121.py specs/fb_1120.py,specs/ship_1120.py [specs/fb_1119.py,specs/ship_1119.py]
   Erstes Argument = neuer Tag (Specs mit Komma), danach Vortage (neueste zuerst). Account = (Marke, Netz).
   STOP: gleicher Clip oder Sound zweimal am Tag auf einem Account; Hook-Text, den der Account schon hatte;
         Sound, den der Account GESTERN schon hatte (User 20.11.: "nicht am selben Tag, nicht auf 2 Tage, nach 2 Tagen wieder ok").
         Ausnahme: --sounds-leer, wenn wirklich alle Sounds verbraucht sind (User: "dann kannst du auch wieder benutzen").
   WARN: Soccer-Bomb-Einzel-Story mit derselben Szene wie gestern; Soccer-Bomb-Combo zu > 50 % wie eine Combo von gestern."""
import sys, importlib.util, collections
args = [a for a in sys.argv[1:] if not a.startswith('--')]
SND_OK = '--sounds-leer' in sys.argv
def load(p):
    sp = importlib.util.spec_from_file_location(p.replace('/', '_'), p); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
def info(specs):
    acc = collections.defaultdict(list)
    for p in specs.split(','):
        m = load(p)
        for b, net, items in m.POST_PLAN:
            for vid, _ in items:
                v = m.VIDEOS[vid]
                clips = sorted({x['clip'].split('/')[-1][:-4] for x in v['segs']})
                hooks = {t[2] for t in v['text'] if len(t[2]) > 3 and not (len(t) > 3 and 'size' in t[3])}  # Combo-Labels zählen nicht
                ship = any('/sea/' in x['clip'] for x in v['segs'])
                acc[(b, net)].append(dict(vid=vid, clips=clips, snd=v['sound'].split('/')[-1], hooks=hooks, combo=len(clips) > 1, ship=ship))
    return acc
new = info(args[0]); old = [info(a) for a in args[1:]]
bad = 0
def stop(*a):
    global bad; print('STOP', *a); bad += 1
for a, L in sorted(new.items()):
    for k, n in collections.Counter(x for v in L for x in v['clips']).items():
        if n > 1: stop(a, 'Clip zweimal am Tag:', k)
    for k, n in collections.Counter(v['snd'] for v in L).items():
        if n > 1: stop(a, 'Sound zweimal am Tag:', k)
    for d, O in enumerate(old):
        P = O.get(a, [])
        for v in L:
            for p in P:
                if v['hooks'] & p['hooks']: stop(a, v['vid'], 'Hook wie', p['vid'], v['hooks'] & p['hooks'])
                if d == 0 and v['snd'] == p['snd']:
                    if SND_OK: print('WARN', a, v['vid'], 'Sound wie gestern', p['vid'], v['snd'], '(alle Sounds verbraucht)')
                    else: stop(a, v['vid'], 'Sound schon gestern auf dem Account', p['vid'], v['snd'])
                if d == 0 and not v['ship'] and not p['ship']:
                    if not v['combo'] and not p['combo'] and v['clips'] == p['clips']: print('WARN', a, v['vid'], 'gleiche Einzel-Story wie gestern', p['vid'], v['clips'])
                    if v['combo'] and p['combo'] and len(set(v['clips']) & set(p['clips'])) > len(v['clips']) / 2: print('WARN', a, v['vid'], 'Combo fast wie gestern', p['vid'])
print('OK' if not bad else f'{bad} STOP')
sys.exit(1 if bad else 0)
