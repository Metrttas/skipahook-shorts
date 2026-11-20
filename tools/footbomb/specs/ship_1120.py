# Skip a Hook OPEN SEA – Schiff-Edits 20.11.2026 (neue Reihenfolgen/Hooks/Sound-Startpunkte, Clips vom 19.11.)
# Vorlage 19.11. (User: "cleane Edits, Schiff im Sturm, Piraten-Vibes", Sound pirate1 NUR für Schiff-Edits).
#   python3 fbedit.py specs/ship_1119.py <id|all> sheet|render
import json
SEA = '/home/claude/fb/sea/'
OUT = '/home/claude/fb/outship20'
B = json.load(open('/home/claude/fb/snd/beats.json'))
SND = 'snd/pirate1.wav'; PER = B[SND]['period']; DROP = B[SND]['beats'][3]
END = 'Search SKIP A HOOK on Roblox'
GOLD = {'fill': (255, 200, 40)}; CYAN = {'fill': (80, 220, 255)}; RED = {'fill': (255, 70, 90)}
# Clip-Kürzel: (Datei, Start, Zoom, Bildmitte-y)
C = {
    'day':    ('chase1', 1.0, 1.35, .5),       # Tag, Insel mit Leuchtturm voraus
    'dusk':   ('storm_chase1', 0.6, 1.5, .5),  # Regen setzt ein
    'night':  ('storm_orbit1', 1.0, 1.3, .5),  # Nacht, klar
    'storm':  ('storm_chase2', 1.2, 1.65, .45),
    'bolt':   ('storm_chase2', 4.9, 1.65, .45), # Blitz
    'bolt2':  ('storm_chase2', 1.4, 1.65, .45),
    'orbit':  ('storm_orbit2', 0.5, 1.45, .55),
    'orbit2': ('storm_orbit2', 6.0, 1.45, .55),
    'waves':  ('storm_low2', 0.3, 1.3, .55),   # große Wellen, Gischt
    'waves2': ('storm_low2', 4.0, 1.3, .55),
    'waves3': ('storm_low2', 8.0, 1.3, .55),
    'far':    ('storm_wide1', 2.0, 1.7, .5),
    'isle':   ('isle_drift1', 7.0, 1.45, .5),
    'skull':  ('skull_side1', 1.0, 1.25, .45),
    'skull2': ('skull_side1', 7.0, 1.25, .45),
    'skullw': ('skull_wide1', 2.0, 1.6, .45),
    'skulll': ('skull_low1', 1.0, 1.3, .35),
    'skulll2':('skull_low1', 6.5, 1.3, .35),
}


def sg(k, n=4, speed=1.0, fx='', dz=0.0):
    f, t, z, cy = C[k]
    d = dict(clip=SEA + f + '.mp4', t=t, n=n, speed=speed, z=z + dz, cy=cy)
    if fx: d['fx'] = fx
    return d


# Ab 21.11. (User 20.11.): Schiff-Edits dürfen auch andere Sounds nehmen, nicht jedes Mal pirate1. Schnellere Sounds = mehr Cuts
# (n zählt Beats, also wird jeder Shot bei schnellem Tempo automatisch kürzer; bei itsout/song1 lieber 2-3 Beats je Shot).
SNDS = {'pirate1': ('snd/pirate1.wav', None), 'u1': ('snd/u1.wav', 7.236), 'u3': ('snd/u3.wav', 4.323), 'u4': ('snd/u4.wav', 4.612),
        'u5': ('snd/u5.wav', 7.140), 'song1': ('snd/song1_fussball_drop.wav', 10.655), 'itsout': ('snd/itsout_finally_out.wav', 5.313)}


def edit(shots, hook1, hook2, st2=GOLD, pre=3, at=3, snd='pirate1'):
    """shots: Liste von Kürzeln oder (kürzel, n, speed, fx). Die ersten `pre` Beats laufen vor dem Drop."""
    segs = []
    for i, s in enumerate(shots):
        if isinstance(s, str): s = (s,)
        k = s[0]; n = s[1] if len(s) > 1 else 4; sp = s[2] if len(s) > 2 else 1.0
        fx = s[3] if len(s) > 3 else ('flash' if i == 1 else 'punch' if i % 2 == 0 and i > 0 else '')
        segs.append(sg(k, n, sp, fx))
    nb = sum(x['n'] for x in segs)
    f, drop = SNDS[snd]; per = B[f]['period']
    t0 = B[f]['beats'][at] if drop is None else drop
    return dict(sound=f, s0=t0 - pre * per, dur=nb * per, segs=segs, end=END,
                text=[(0, pre * per, hook1), (pre * per, nb * per, hook2, st2)])


VIDEOS = {
    'sh20_a':  edit([('skulll', 3), 'skullw', 'night', ('bolt2', 2), 'waves2', 'orbit', 'waves3', ('far', 5)], 'WOULD YOU SAIL THROUGH THIS?', 'STORM BELT · OPEN SEA', CYAN, at=27),
    'sh20_ya': edit([('isle', 3), 'day', 'dusk', 'storm', ('bolt', 2), 'waves', 'orbit2', ('skull', 5)], 'IT STARTED AS A NORMAL TRIP...', 'THEN THE SKY TURNED', RED),
    'sh20_b':  edit([('far', 3), 'waves', 'orbit', ('bolt', 2), 'storm', 'skulll2', 'skull', ('night', 5)], 'POV: LIGHTNING EVERYWHERE', 'KEEP SAILING, CAPTAIN', GOLD, at=15),
    'sh20_yb': edit([('night', 3), 'skull2', 'skulll', 'skullw', 'waves3', 'storm', ('bolt2', 2), ('orbit', 6)], 'THE SKULL WAS WATCHING US', 'SKIP A HOOK · OPEN SEA', RED, at=39),
    'sh20_c':  edit([('waves2', 3), 'storm', ('bolt', 2), 'orbit2', 'waves', 'skull2', 'isle', ('day', 5)], 'WE MADE IT THROUGH...', 'BARELY', CYAN, at=27),
    'sh20_ic': edit([('day', 3), 'isle', 'skullw', 'skull', 'night', 'waves2', ('bolt2', 2), ('waves3', 6)], 'ROBLOX FISHING GAME...', '...WITH A PIRATE OCEAN', GOLD, at=15),
    'sh20_yc': edit([('orbit', 3), 'waves3', 'far', 'bolt', 'skulll2', 'night', 'storm', ('waves', 5)], 'NO MAP. NO LIGHT. ONLY WAVES.', 'OPEN SEA', RED, at=39),
    'sh20_m':  edit([('dusk', 3), 'storm', 'waves', ('bolt2', 2), 'orbit2', 'skulll', 'skullw', ('isle', 6)], 'RAIN STARTS FALLING...', 'HOLD THE WHEEL', CYAN, at=27),
    'sh20_n':  edit([('skull', 3), 'skulll2', 'night', 'far', 'waves2', ('bolt', 2), 'orbit', ('waves3', 5)], 'SAILING PAST SKULL ISLAND', 'AT MIDNIGHT', GOLD, at=15),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('sh20_a', '12:03')]), ('7181171', 'youtube', [('sh20_ya', '12:03')]),
    ('7752397', 'tiktok', [('sh20_b', '12:09')]), ('7752397', 'youtube', [('sh20_yb', '12:09')]),
    ('7773777', 'tiktok', [('sh20_c', '12:15')]), ('7773777', 'instagram', [('sh20_ic', '12:15')]), ('7773777', 'youtube', [('sh20_yc', '12:15')]),
    ('7752416', 'youtube', [('sh20_m', '12:21')]), ('7773832', 'youtube', [('sh20_n', '12:24')]),
]
