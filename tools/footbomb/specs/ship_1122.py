# Skip a Hook OPEN SEA – Schiff-Edits 22.11.2026 (Clips vom 19.11., 3. Einsatz -> User neue Aufnahmen vorschlagen).
#   Neue Startpunkte (Kürzel *2/*3/*4/*5), neue Reihenfolgen/Hooks; pirate1 auf 5 Accounts mit neuen Startbeats (11/19/23/35/47),
#   4 Accounts mit anderen User-Sounds (u1/u3/u4/u5). Shot-Längen in pirate1-Beats -> bei anderen Sounds auf gleiche Sekunden umgerechnet.
#   python3 fbedit.py specs/ship_1122.py <id|all> sheet|render
import json
SEA = '/home/claude/fb/sea/'
OUT = '/home/claude/fb/outship22'
B = json.load(open('/home/claude/fb/snd/beats.json'))
PIR = B['snd/pirate1.wav']['period']
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
    # NEU 22.11.: andere Startpunkte
    'day2':   ('chase1', 4.5, 1.35, .5),
    'dusk2':  ('storm_chase1', 3.0, 1.5, .5),
    'night2': ('storm_orbit1', 5.0, 1.3, .5),
    'storm2': ('storm_chase2', 2.6, 1.65, .45),
    'orbit3': ('storm_orbit2', 3.2, 1.45, .55),
    'waves4': ('storm_low2', 2.0, 1.3, .55),
    'waves5': ('storm_low2', 6.0, 1.3, .55),
    'far2':   ('storm_wide1', 5.5, 1.7, .5),
    'isle2':  ('isle_drift1', 3.0, 1.45, .5),
    'skull3': ('skull_side1', 4.0, 1.25, .45),
    'skullw2':('skull_wide1', 6.0, 1.6, .45),
    'skulll3':('skull_low1', 3.5, 1.3, .35),
}


def sg(k, n=4, speed=1.0, fx='', dz=0.0):
    f, t, z, cy = C[k]
    d = dict(clip=SEA + f + '.mp4', t=t, n=n, speed=speed, z=z + dz, cy=cy)
    if fx: d['fx'] = fx
    return d


SNDS = {'pirate1': ('snd/pirate1.wav', None), 'u1': ('snd/u1.wav', 7.236), 'u3': ('snd/u3.wav', 4.323), 'u4': ('snd/u4.wav', 4.612),
        'u5': ('snd/u5.wav', 7.140), 'song1': ('snd/song1_fussball_drop.wav', 10.655), 'itsout': ('snd/itsout_finally_out.wav', 5.313)}


def edit(shots, hook1, hook2, st2=GOLD, pre=3, at=3, snd='pirate1'):
    """shots: Kürzel oder (kürzel, n, speed, fx); n in pirate1-Beats (bei anderen Sounds auf ~gleiche Sekunden umgerechnet).
    Die ersten `pre` Beats laufen vor dem Drop."""
    f, drop = SNDS[snd]; per = B[f]['period']
    q = PIR / per                                     # pirate1-Beats -> Beats dieses Sounds
    segs = []
    for i, s in enumerate(shots):
        if isinstance(s, str): s = (s,)
        k = s[0]; n = s[1] if len(s) > 1 else 4; sp = s[2] if len(s) > 2 else 1.0
        fx = s[3] if len(s) > 3 else ('flash' if i == 1 else 'punch' if i % 2 == 0 and i > 0 else '')
        segs.append(sg(k, max(2, round(n * q)), sp, fx))
    nb = sum(x['n'] for x in segs)
    pre = max(2, round(pre * q))
    t0 = B[f]['beats'][at] if drop is None else drop
    return dict(sound=f, s0=t0 - pre * per, dur=nb * per, segs=segs, end=END,
                text=[(0, pre * per, hook1), (pre * per, nb * per, hook2, st2)])


VIDEOS = {
    'sh22_a':  edit([('far2', 3), 'storm2', 'orbit3', ('bolt', 2), 'waves4', 'skull3', 'waves5', ('waves3', 5)],
                    'CAPTAIN, STORM AHEAD!', 'FULL SAIL ANYWAY', GOLD, at=11),
    'sh22_ya': edit([('day2', 3), 'isle2', 'dusk2', 'storm2', ('bolt2', 2), 'waves4', 'orbit3', ('far2', 5)],
                    'THE CALM BEFORE THE STORM', 'OPEN SEA · SKIP A HOOK', CYAN, snd='u1'),
    'sh22_b':  edit([('waves5', 3), 'storm', 'far2', ('bolt2', 2), 'orbit3', 'waves4', 'skulll3', ('waves2', 5)],
                    'POV: YOUR SHIP VS THE STORM', 'WHO WINS?', RED, at=23),
    'sh22_yb': edit([('storm2', 3), 'waves5', 'orbit', ('bolt', 2), 'far', 'waves4', 'skullw2', ('orbit3', 5)],
                    'ONE SHIP. ONE STORM.', 'NO WAY BACK', GOLD, snd='u3'),
    'sh22_c':  edit([('dusk2', 3), 'storm2', 'waves4', ('bolt', 2), 'orbit2', 'far2', 'waves5', ('skull3', 5)],
                    'THE SEA GOT ANGRY...', '...SO WE SAILED FASTER', CYAN, at=35),
    'sh22_ic': edit([('isle2', 3), 'day2', 'skullw2', 'skulll3', 'storm2', ('bolt2', 2), 'waves5', ('night2', 5)],
                    'A FISHING GAME... WITH THIS?', 'PIRATE SEA ON ROBLOX', GOLD, snd='u5'),
    'sh22_yc': edit([('bolt', 3), 'waves4', 'skulll3', 'storm2', 'waves5', 'skull3', ('bolt2', 2), ('skullw2', 5)],
                    'LIGHTNING. WAVES. SKULLS.', 'JUST A NORMAL FISHING TRIP', RED, at=47),
    'sh22_m':  edit([('night2', 3), 'far2', 'storm2', 'orbit3', ('bolt', 2), 'waves5', 'waves4', ('skulll3', 5)],
                    'STORM BELT, DEAD AHEAD', 'NO TURNING BACK', RED, snd='u4'),
    'sh22_n':  edit([('day2', 3), 'isle2', 'dusk2', 'storm2', 'waves4', ('bolt2', 2), 'orbit3', ('waves5', 5)],
                    'CLEAR SKY ON THE OPEN SEA...', '...THEN THE STORM CAME', GOLD, at=19),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('sh22_a', '12:03')]), ('7181171', 'youtube', [('sh22_ya', '12:03')]),
    ('7752397', 'tiktok', [('sh22_b', '12:09')]), ('7752397', 'youtube', [('sh22_yb', '12:09')]),
    ('7773777', 'tiktok', [('sh22_c', '12:15')]), ('7773777', 'instagram', [('sh22_ic', '12:15')]), ('7773777', 'youtube', [('sh22_yc', '12:15')]),
    ('7752416', 'youtube', [('sh22_m', '12:21')]), ('7773832', 'youtube', [('sh22_n', '12:24')]),
]
