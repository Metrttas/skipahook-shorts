# Skip a Hook OPEN SEA – Schiff-Edits 19.11.2026 (User: "cleane Edits, Schiff im Sturm, Piraten-Vibes", Sound pirate1 NUR für Schiff-Edits).
#   python3 fbedit.py specs/ship_1119.py <id|all> sheet|render
import json
SEA = '/home/claude/fb/sea/'
OUT = '/home/claude/fb/outship'
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


def edit(shots, hook1, hook2, st2=GOLD, pre=3):
    """shots: Liste von Kürzeln oder (kürzel, n, speed, fx). Die ersten `pre` Beats laufen vor dem Drop."""
    segs = []
    for i, s in enumerate(shots):
        if isinstance(s, str): s = (s,)
        k = s[0]; n = s[1] if len(s) > 1 else 4; sp = s[2] if len(s) > 2 else 1.0
        fx = s[3] if len(s) > 3 else ('flash' if i == 1 else 'punch' if i % 2 == 0 and i > 0 else '')
        segs.append(sg(k, n, sp, fx))
    nb = sum(x['n'] for x in segs)
    return dict(sound=SND, s0=DROP - pre * PER, dur=nb * PER, segs=segs, end=END,
                text=[(0, pre * PER, hook1), (pre * PER, nb * PER, hook2, st2)])


VIDEOS = {
    'sh_a':  edit([('day', 3), 'dusk', 'storm', ('bolt', 2), 'waves', 'orbit', 'waves2', ('skulll', 5)], 'CALM SEA...', 'THEN THE STORM HIT', RED),
    'sh_ya': edit([('night', 3), 'waves', 'bolt', 'orbit2', 'skull', 'waves3', 'skulll', ('far', 5)], 'POV: YOUR OWN PIRATE SHIP', 'SKIP A HOOK · OPEN SEA', GOLD),
    'sh_b':  edit([('skulll', 3), 'skull', 'skullw', 'skull2', 'night', 'storm', ('bolt', 2), ('waves', 6)], 'SKULL ISLAND AFTER DARK', 'WOULD YOU SAIL HERE?', CYAN),
    'sh_yb': edit([('waves', 3), 'orbit', 'bolt2', 'waves2', 'storm', 'orbit2', 'waves3', ('skulll2', 5)], 'SAILING INTO THE STORM', 'ON ROBLOX', GOLD),
    'sh_c':  edit([('isle', 3), 'night', 'skull', 'skulll', 'dusk', ('bolt', 2), 'waves', ('orbit', 6)], 'SET SAIL TONIGHT', 'THE OPEN SEA IS LIVE', CYAN),
    'sh_ic': edit([('orbit2', 3), 'waves2', 'bolt', 'storm', 'skull2', 'skulll', 'night', ('far', 5)], 'PIRATE MODE: ON', 'SKIP A HOOK · OPEN SEA', RED),
    'sh_yc': edit([('day', 3), 'isle', 'night', 'skullw', 'skulll', 'storm', ('bolt2', 2), ('waves3', 6)], 'FROM SUNSHINE...', '...TO THE STORM BELT', GOLD),
    'sh_m':  edit([('skull2', 3), 'skulll2', 'waves', 'bolt', 'orbit', 'waves2', 'night', ('skull', 5)], 'CAPTAIN OF THE ROYAL GALLEON', 'SKIP A HOOK ON ROBLOX', CYAN),
    'sh_n':  edit([('storm', 3), 'waves3', 'orbit2', ('bolt2', 2), 'waves', 'skulll', 'skullw', ('isle', 6)], 'ONLY REAL CAPTAINS SAIL HERE', 'STORM BELT · OPEN SEA', RED),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('sh_a', '18:03')]), ('7181171', 'youtube', [('sh_ya', '18:03')]),
    ('7752397', 'tiktok', [('sh_b', '18:09')]), ('7752397', 'youtube', [('sh_yb', '18:09')]),
    ('7773777', 'tiktok', [('sh_c', '18:15')]), ('7773777', 'instagram', [('sh_ic', '18:15')]), ('7773777', 'youtube', [('sh_yc', '18:15')]),
    ('7752416', 'youtube', [('sh_m', '18:21')]), ('7773832', 'youtube', [('sh_n', '18:24')]),
]
