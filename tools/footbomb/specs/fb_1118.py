# Footbomb-Edits 18.11.2026 – 18 Videos (2 je Account), nur Sounds des Users, Querformat-Band + unscharfer Rand.
#   python3 fbedit.py specs/fb_1118.py <id|all> sheet|render
# Quellen: eigene Studio-Aufnahmen 18.11. (Showcase 1v1 rot/blau + Duos-Runden mit Bots, 60 fps, Kamera-Skript FBCAM)
#          + Kino-Clip aura16x9 (16.11., CinematicDirector).
import json
CAP = '/home/claude/fb/cap/'
AURA = '/home/claude/fb/src/aura16x9.mp4'
OUT = '/home/claude/fb/out1118'
B = json.load(open('/home/claude/fb/snd/beats.json'))

SND = {  # Datei, Drop (s)
    'u1': ('snd/u1.wav', 7.236), 'u3': ('snd/u3.wav', 4.323), 'u4': ('snd/u4.wav', 4.612), 'u5': ('snd/u5.wav', 7.140),
    'song1': ('snd/song1_fussball_drop.wav', 10.655), 'itsout': ('snd/itsout_finally_out.wav', 5.313),
}

M = {  # Moment: (Clip, Start s, Zoom, cy)
    'g1a': ('g1_follow_1v1', 3.2, 1.28, .5), 'g1e': ('g1_follow_1v1', 6.3, 1.32, .5),
    'g4a': ('g4_follow_1v1', 15.4, 1.28, .5), 'g4b': ('g4_follow_1v1', 18.3, 1.3, .5),
    'g2e': ('g2_follow_1v1', 0.0, 1.28, .5), 'g3e': ('g3_follow_1v1', 15.0, 1.3, .5),
    's2a': ('s2_side', 1.8, 1.3, .55), 's2e': ('s2_side', 3.3, 1.35, .55),
    'b3a': ('b3_behind_close', 13.8, 1.3, .55), 'b3e': ('b3_behind_close', 15.2, 1.35, .55),
    'o1a': ('o1_orbit', 7.6, 1.3, .55), 'o1e': ('o1_orbit', 9.3, 1.35, .55),
    'd1b': ('d1_duo', 0.8, 1.6, .5), 'd1e': ('d1_duo', 4.0, 1.6, .5),
    'd4c': ('d4_duo_side', 2.0, 1.35, .55), 'd4s': ('d4_duo_side', 7.8, 1.35, .55),
    'd2c': ('d2_duo', 2.4, 1.4, .55), 'd3c': ('d3_duo', 2.0, 1.4, .55), 'd3d': ('d3_duo', 8.0, 1.4, .55),
    'f5a': ('f5_follow', 0.5, 1.3, .5), 'f5b': ('f5_follow', 7.0, 1.3, .5), 'f5c': ('f5_follow', 12.0, 1.3, .5),
    'au_bike': (AURA, 9.4, 1.3, .5), 'au_power': (AURA, 0.0, 1.3, .5), 'au_scissor': (AURA, 6.3, 1.3, .5),
    'au_red': (AURA, 3.4, 1.3, .5), 'au_walk': (AURA, 17.6, 1.3, .5), 'au_face': (AURA, 20.2, 1.3, .45),
    'au_wide': (AURA, 21.6, 1.3, .5), 'au_charge': (AURA, 13.0, 1.3, .5),
}


def S(m, n=4, **kw):
    c, t, z, cy = M[m]
    d = dict(clip=c if c.startswith('/') else CAP + c + '.mp4', t=t, n=n, z=z, cy=cy)
    d.update(kw)
    return d


def V(snd, pre, post, segs, text, end='Search FOOTBOMB on Roblox'):
    f, drop = SND[snd]
    per = B[f]['period']
    s0 = drop - pre * per
    dur = (pre + post) * per
    return dict(sound=f, s0=s0, dur=dur, segs=segs, end=end, text=[(a * per if a >= 0 else 0, b * per, t, *st) for a, b, t, *st in text])


RED = {'fill': (255, 70, 90)}
GOLD = {'fill': (255, 200, 40)}
CYAN = {'fill': (80, 220, 255)}

VIDEOS = {
    # A fbgam.es TikTok
    'fb_a1': V('u3', 8, 16, [S('g1a', 4), S('g1a', 4, t=5.0), S('g4a', 4, fx='flash'), S('g4b', 4), S('g1e', 4, fx='punch'), S('o1e', 4), S('g1a', 4)],
               [(0, 8, 'THE ART OF...'), (8, 24, 'NEVER LETTING IT LAND', RED)]),
    'fb_a2': V('song1', 8, 18, [S('f5a', 4), S('d2c', 4), S('d4s', 4, fx='flash'), S('d3c', 4), S('f5b', 4), S('d4c', 3), S('f5a', 3)],
               [(0, 8, 'TEAM PLAYS'), (8, 26, 'DUOS MODE', GOLD)]),
    # A fbgam.es YouTube
    'fb_ya1': V('u1', 8, 16, [S('s2a', 4), S('s2e', 4), S('b3a', 4, fx='flash'), S('b3e', 4), S('o1a', 4), S('o1e', 4, fx='punch')],
                [(0, 8, "DON'T LET IT LAND."), (8, 24, "OR YOU'RE OUT.", RED)]),
    'fb_ya2': V('itsout', 12, 26, [S('au_walk', 6), S('au_face', 6), S('au_bike', 6, speed=0.7, fx='flash'), S('au_scissor', 6), S('au_power', 6), S('au_red', 4), S('au_wide', 4)],
                [(0, 12, 'FOOTBOMB'), (12, 38, 'PURE AURA', CYAN)]),
    # B mtfgams TikTok
    'fb_b1': V('u5', 8, 16, [S('d1b', 6), S('d1b', 2, t=2.0), S('d1e', 4, fx='flash'), S('au_bike', 4, speed=0.7), S('g4a', 4), S('g1e', 4)],
               [(0, 8, 'WAIT FOR IT...'), (8, 24, 'BICYCLE KICK', RED)]),
    'fb_b2': V('u4', 8, 14, [S('g2e', 4), S('g3e', 4), S('s2e', 4, fx='flash'), S('b3e', 4), S('o1e', 3), S('g1e', 3)],
               [(0, 8, 'ONE TOUCH.'), (8, 22, 'GAME OVER.', RED)]),
    # B mtfgams YouTube
    'fb_yb1': V('song1', 8, 18, [S('g4a', 4), S('g4b', 4), S('g1a', 4, fx='flash'), S('g1e', 4), S('g3e', 4), S('g2e', 4), S('g4a', 2)],
                [(0, 8, '1V1 ME.'), (8, 26, 'LAST FIELD STANDING', GOLD)]),
    'fb_yb2': V('u3', 8, 16, [S('d3c', 4), S('d3d', 4), S('d4s', 4, fx='flash'), S('f5c', 4), S('d2c', 4), S('f5b', 4)],
                [(0, 8, '8 PLAYERS. 4 FIELDS.'), (8, 24, "DON'T LET IT DROP", CYAN)]),
    # C Mtrix TikTok
    'fb_c1': V('u1', 8, 16, [S('o1a', 4), S('o1e', 4), S('g4a', 4, fx='flash'), S('s2a', 4), S('s2e', 4), S('b3e', 4)],
               [(0, 8, 'RATE THIS RALLY'), (8, 24, '1 TO 10?', GOLD)]),
    'fb_c2': V('itsout', 12, 24, [S('d4c', 6), S('d4s', 6), S('d3c', 6, fx='flash'), S('f5a', 6), S('d2c', 6), S('d3d', 6)],
               [(0, 12, 'DUOS ON ROBLOX'), (12, 36, 'HITS DIFFERENT', RED)]),
    # C Mtrix Instagram
    'fb_ic1': V('u5', 8, 16, [S('g1a', 4), S('g1a', 4, t=4.8), S('g1e', 4, fx='flash'), S('g4b', 4), S('b3e', 4), S('g3e', 4)],
                [(0, 8, 'HOW LONG CAN YOU'), (8, 24, 'KEEP IT UP?', GOLD)]),
    'fb_ic2': V('u4', 8, 14, [S('au_charge', 4), S('au_power', 4), S('au_bike', 4, speed=0.7, fx='flash'), S('au_scissor', 4), S('au_face', 3), S('au_walk', 3)],
                [(0, 8, 'AURA +1000'), (8, 22, 'FOOTBOMB', RED)]),
    # C Mtrix YouTube
    'fb_yc1': V('u3', 8, 16, [S('d4c', 4), S('d4s', 4), S('d4s', 4, t=8.6, speed=0.75, fx='flash'), S('f5b', 4), S('d3d', 4), S('f5c', 4)],
                [(0, 8, 'SCISSOR KICK'), (8, 24, 'IN DUOS', GOLD)]),
    'fb_yc2': V('song1', 8, 18, [S('s2a', 4), S('b3a', 4), S('g1e', 4, fx='flash'), S('o1e', 4), S('g2e', 4), S('g3e', 4), S('s2e', 2)],
                [(0, 8, 'FOOTBALL, BUT'), (8, 26, 'IF IT LANDS, YOU LOSE', RED)]),
    # mtgames2# YouTube
    'fb_m1': V('u5', 8, 16, [S('g4a', 4), S('g4b', 4), S('d1e', 4, fx='flash'), S('g1e', 4), S('o1e', 4), S('b3e', 4)],
               [(0, 8, 'CLEANEST FINISH?'), (8, 24, 'PICK ONE', GOLD)]),
    'fb_m2': V('u1', 8, 16, [S('f5a', 4), S('f5b', 4), S('d2c', 4, fx='flash'), S('d3c', 4), S('d4s', 4), S('f5c', 4)],
               [(0, 8, '2V2 ON ROBLOX'), (8, 24, 'TEAM PLAYS', RED)]),
    # mtfgams12 YouTube
    'fb_n1': V('itsout', 12, 26, [S('au_red', 6), S('au_charge', 6), S('au_power', 6, fx='flash'), S('au_bike', 6, speed=0.7), S('au_scissor', 6), S('au_face', 4), S('au_wide', 4)],
               [(0, 12, 'THE ART OF...'), (12, 38, 'THE POWER STRIKE', CYAN)]),
    'fb_n2': V('u4', 8, 14, [S('s2a', 4), S('s2e', 4), S('g1e', 4, fx='flash'), S('g3e', 4), S('b3e', 3), S('o1e', 3)],
               [(0, 8, 'ONE MISTAKE'), (8, 22, "AND YOU'RE OUT", RED)]),
}

POST_PLAN = [  # 2 Footbomb je Account, Abend
    ('7181171', 'tiktok', [('fb_a1', '19:03'), ('fb_a2', '21:03')]),
    ('7181171', 'youtube', [('fb_ya1', '19:03'), ('fb_ya2', '21:03')]),
    ('7752397', 'tiktok', [('fb_b1', '19:09'), ('fb_b2', '21:09')]),
    ('7752397', 'youtube', [('fb_yb1', '19:30'), ('fb_yb2', '21:30')]),
    ('7773777', 'tiktok', [('fb_c1', '19:15'), ('fb_c2', '21:15')]),
    ('7773777', 'instagram', [('fb_ic1', '19:15'), ('fb_ic2', '21:15')]),
    ('7773777', 'youtube', [('fb_yc1', '19:15'), ('fb_yc2', '21:15')]),
    ('7752416', 'youtube', [('fb_m1', '19:21'), ('fb_m2', '21:21')]),
    ('7773832', 'youtube', [('fb_n1', '19:24'), ('fb_n2', '21:24')]),
]
