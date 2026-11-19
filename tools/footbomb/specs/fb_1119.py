# Foot Bomb 19.11.2026 – 18 Edits aus 9 neuen Aufnahmen (DuoDirector, Grätschen statt Hechtsprung, Luft-Duelle), nur Sounds des Users.
#   python3 fbedit.py specs/fb_1119.py <id|all> sheet|render
import json
CINE = '/home/claude/fb/cine/'
OUT = '/home/claude/fb/out1119b'
B = json.load(open('/home/claude/fb/snd/beats.json'))
TL = json.load(open('/home/claude/fb/tl.json'))
SND = {'u1': ('snd/u1.wav', 7.236), 'u3': ('snd/u3.wav', 4.323), 'u4': ('snd/u4.wav', 4.612), 'u5': ('snd/u5.wav', 7.140),
       'song1': ('snd/song1_fussball_drop.wav', 10.655), 'itsout': ('snd/itsout_finally_out.wav', 5.313)}
RED = {'fill': (255, 70, 90)}; GOLD = {'fill': (255, 200, 40)}; CYAN = {'fill': (80, 220, 255)}
END = 'Search FOOT BOMB on Roblox'
# R = Clip-Zeit, ab der die Aktion gezeigt wird (lange Luft-Ballwechsel ganz zeigen)
R = {'airwar_v2': 0.9, 'airsave_v1': 0.9, 'airwar2_b2': 1.0, 'slidesave_b2': 0.3, 'slidechain_v1': 0.3}
SC = {}
for f, v in TL.items():
    SC[f.split('_')[0]] = dict(f=f, K=v['K'], I=v['I'], C=v['C'], E=v['E'], z=1.27, R=R.get(f))


def seg(s, t, n, speed=1.0, z=None, cy=.5, fx=''):
    d = dict(clip=CINE + SC[s]['f'] + '.mp4', t=max(0.0, t), n=n, speed=speed, z=z or SC[s]['z'], cy=cy)
    if fx: d['fx'] = fx
    return d


def story(s, snd, hook1, hook2, st2=RED, cold=False, pre=None):
    f, drop = SND[snd]; per = B[f]['period']; S = SC[s]
    K, I, C, E = S['K'], S['I'], S['C'], S['E']
    segs = []
    if cold:
        segs.append(seg(s, I - 0.1, 2, 0.8, fx='flash'))
    if S['R'] is not None and pre is None:   # ganzer Ballwechsel, max ~1.25x Tempo
        nb = max(4, round((K - S['R']) / per / 1.2))
    else:
        nb = pre or min(8, int(K / per / 0.95))
    nb = max(4, nb - (nb % 2))
    t0 = max(0.0, K - nb * per * min(1.3, (K - (S['R'] or 0)) / (nb * per))) if S['R'] is not None and pre is None else max(0.0, K - nb * per)
    segs.append(seg(s, t0, nb, (K - t0) / (nb * per)))
    n2 = max(2, round((I - K) / per))
    segs.append(seg(s, K, n2, (I - K) / (n2 * per), fx='flash'))
    segs.append(seg(s, I - 0.02, 3, 1.0, fx='punch'))
    segs.append(seg(s, K - 0.45, 4, 0.8, z=S['z'] + 0.06, fx='flash'))
    nc = 4
    segs.append(seg(s, C, nc, min(1.0, (E - C) / (nc * per))))
    npre = (2 if cold else 0) + nb
    post = sum(x['n'] for x in segs) - npre
    return dict(sound=f, s0=drop - npre * per, dur=(npre + post) * per, segs=segs, end=END,
                text=[(0, npre * per, hook1), (npre * per, (npre + post) * per, hook2, st2)])


def montage(scenes, snd, hook, st=GOLD, labels=('1', '2', '3')):
    f, drop = SND[snd]; per = B[f]['period']
    segs = []; text = []; k = 0
    for i, s in enumerate(scenes):
        S = SC[s]
        segs.append(seg(s, S['K'] - 3 * per, 3))
        n2 = max(2, round((S['I'] - S['K']) / per))
        segs.append(seg(s, S['K'], n2, (S['I'] - S['K']) / (n2 * per), fx='flash'))
        segs.append(seg(s, S['I'] - 0.02, 2, 1.0, fx='punch'))
        n = 3 + n2 + 2
        text.append((k * per, (k + n) * per, labels[i], dict(GOLD, size=170, y=1360 + 230)))
        k += n
    text.insert(0, (0, k * per, hook, st))
    pre = 3
    return dict(sound=f, s0=drop - pre * per, dur=k * per, segs=segs, end=END, text=text)


VIDEOS = {
    # A fbgam.es TikTok
    'fb19_a1': story('airwar', 'u3', 'VOLLEY. HEADER. ALL IN THE AIR...', 'THEN A SCORPION', RED),
    'fb19_a2': story('slidesave', 'u5', 'SLIDE SAVE ON THE LINE...', 'BICYCLE KICK', GOLD),
    # A fbgam.es YouTube
    'fb19_ya1': story('airsave', 'song1', 'NOBODY LET IT DROP...', 'SCORPION ENDS IT', CYAN),
    'fb19_ya2': montage(['airwar', 'airwar2', 'scorp'], 'itsout', 'PICK ONE'),
    # B mtfgams TikTok
    'fb19_b1': story('airwar2', 'u1', 'BICYCLE. SCISSOR. HEADER...', 'SCORPION FINISH', RED),
    'fb19_b2': story('slidechain', 'u3', 'TWO SLIDE SAVES...', 'THEN A TORNADO KICK', CYAN),
    # B mtfgams YouTube
    'fb19_yb1': story('tornado', 'u5', 'NO-LOOK HEEL PASS...', 'TORNADO KICK', CYAN, pre=6),
    'fb19_yb2': story('airsave', 'u4', 'RATE THIS RALLY', '1 TO 10?', GOLD, cold=True),
    # C Mtrix TikTok
    'fb19_c1': story('slidesave', 'u4', 'HOW DID HE SAVE THAT?', 'THEN THIS HAPPENED', RED, cold=True),
    'fb19_c2': story('airwar', 'itsout', 'AIR BATTLE IN ROBLOX', 'SCORPION ENDS IT', GOLD, cold=True),
    # C Mtrix Instagram
    'fb19_ic1': story('bike', 'u1', 'CHEST. LOB...', 'BICYCLE KICK', RED, pre=6),
    'fb19_ic2': story('airwar2', 'song1', 'THE BALL NEVER TOUCHED THE GROUND', 'UNTIL THIS', CYAN, cold=True),
    # C Mtrix YouTube
    'fb19_yc1': story('slidechain', 'u5', 'SAVE... SAVE...', 'TORNADO KICK', GOLD, cold=True),
    'fb19_yc2': story('scorp', 'u3', 'HEADER TO HIS TEAMMATE...', 'SCORPION KICK', RED, pre=6),
    # mtgames2# YouTube
    'fb19_m1': story('flyhead', 'song1', 'CROSS IT IN...', 'DIVING HEADER', GOLD, pre=6),
    'fb19_m2': montage(['slidesave', 'slidechain', 'airsave'], 'u1', 'CLEANEST FINISH?'),
    # mtfgams12 YouTube
    'fb19_n1': story('bike', 'itsout', 'WAIT FOR IT...', 'BICYCLE KICK', CYAN, cold=True, pre=6),
    'fb19_n2': story('airwar2', 'u4', '4 TOUCHES IN THE AIR', 'NO ONE LET IT DROP', RED),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('fb19_a1', '19:03'), ('fb19_a2', '21:03')]),
    ('7181171', 'youtube', [('fb19_ya1', '19:03'), ('fb19_ya2', '21:03')]),
    ('7752397', 'tiktok', [('fb19_b1', '19:09'), ('fb19_b2', '21:09')]),
    ('7752397', 'youtube', [('fb19_yb1', '19:30'), ('fb19_yb2', '21:30')]),
    ('7773777', 'tiktok', [('fb19_c1', '19:15'), ('fb19_c2', '21:15')]),
    ('7773777', 'instagram', [('fb19_ic1', '19:15'), ('fb19_ic2', '21:15')]),
    ('7773777', 'youtube', [('fb19_yc1', '19:15'), ('fb19_yc2', '21:15')]),
    ('7752416', 'youtube', [('fb19_m1', '19:21'), ('fb19_m2', '21:21')]),
    ('7773832', 'youtube', [('fb19_n1', '19:24'), ('fb19_n2', '21:24')]),
]
