# Soccer Bomb 20.11.2026 – 18 Edits (Clips vom 19.11.), halb Einzel-Storys, halb COMBOS (User 20.11.: "Edits, wo mehrere gute Clips aneinander gepackt sind, kommt besser").
#   python3 fbedit.py specs/fb_1119.py <id|all> sheet|render
import json
CINE = '/home/claude/fb/cine/'
OUT = '/home/claude/fb/out1120'
B = json.load(open('/home/claude/fb/snd/beats.json'))
TL = json.load(open('/home/claude/fb/tl.json'))
SND = {'u1': ('snd/u1.wav', 7.236), 'u3': ('snd/u3.wav', 4.323), 'u4': ('snd/u4.wav', 4.612), 'u5': ('snd/u5.wav', 7.140),
       'song1': ('snd/song1_fussball_drop.wav', 10.655), 'itsout': ('snd/itsout_finally_out.wav', 5.313)}
RED = {'fill': (255, 70, 90)}; GOLD = {'fill': (255, 200, 40)}; CYAN = {'fill': (80, 220, 255)}
END = 'Search SOCCER BOMB on Roblox'
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


KICK = {'airwar': 'SCORPION', 'airsave': 'SCORPION', 'airwar2': 'SCORPION', 'scorp': 'SCORPION', 'slidesave': 'BICYCLE KICK',
        'bike': 'BICYCLE KICK', 'slidechain': 'TORNADO KICK', 'tornado': 'TORNADO KICK', 'flyhead': 'DIVING HEADER'}


def combo(scenes, snd, hook, st=GOLD, labels=None, build=2):
    """Mehrere beste Momente direkt hintereinander: je Clip kurzer Anlauf, Schuss in Zeitlupe, Einschlag."""
    f, drop = SND[snd]; per = B[f]['period']
    segs = []; text = []; k = 0
    for i, s in enumerate(scenes):
        S = SC[s]
        segs.append(seg(s, S['K'] - build * per * 1.1, build, 1.1, fx='flash' if i else ''))
        n2 = max(2, round((S['I'] - S['K']) / per / 0.75))
        segs.append(seg(s, S['K'], n2, (S['I'] - S['K']) / (n2 * per), fx='flash'))
        segs.append(seg(s, S['I'] - 0.02, 2, 1.0, fx='punch'))
        n = build + n2 + 2
        lab = labels[i] if labels else KICK[s]
        text.append((k * per, (k + n) * per, lab, dict(st, size=120, y=1590)))
        k += n
    text.insert(0, (0, k * per, hook, st))
    return dict(sound=f, s0=drop - build * per, dur=k * per, segs=segs, end=END, text=text)


VIDEOS = {
    # A fbgam.es TikTok
    'fb20_a1': combo(['scorp', 'bike', 'tornado', 'flyhead'], 'u1', '4 FINISHES. PICK ONE', GOLD, labels=('1', '2', '3', '4')),
    'fb20_a2': story('slidechain', 'song1', 'HE SLID IN TWICE...', 'AND STILL LOST', RED),
    # A fbgam.es YouTube
    'fb20_ya1': story('airwar2', 'u5', 'BICYCLE. SCISSOR. VOLLEY.', 'SCORPION TO END IT', CYAN),
    'fb20_ya2': combo(['airsave', 'slidesave', 'tornado', 'airwar', 'bike'], 'u3', 'EVERY KICK IN SOCCER BOMB', CYAN),
    # B mtfgams TikTok
    'fb20_b1': combo(['airwar2', 'scorp', 'airsave'], 'itsout', '3 SCORPIONS IN A ROW', RED),
    'fb20_b2': story('bike', 'u4', 'HE CHESTS IT DOWN...', 'BICYCLE KICK', GOLD, pre=6),
    # B mtfgams YouTube
    'fb20_yb1': story('airwar', 'u1', 'KEEP IT IN THE AIR...', 'SCORPION KICK', GOLD),
    'fb20_yb2': combo(['tornado', 'slidechain', 'flyhead', 'slidesave'], 'song1', 'SOCCER BOMB HIGHLIGHTS', GOLD),
    # C Mtrix TikTok
    'fb20_c1': story('tornado', 'u3', 'THE NO-LOOK PASS...', 'INTO A TORNADO KICK', RED, cold=True, pre=6),
    'fb20_c2': combo(['bike', 'airwar', 'slidechain', 'scorp'], 'u5', 'WHICH ONE IS THE BEST?', CYAN, labels=('1', '2', '3', '4')),
    # C Mtrix Instagram
    'fb20_ic1': combo(['slidesave', 'airwar2', 'tornado'], 'u4', 'SLIDE. FLIP. SPIN.', RED),
    'fb20_ic2': story('airsave', 'song1', 'NOT ONE TOUCH ON THE GROUND', 'UNTIL THE SCORPION', GOLD, cold=True),
    # C Mtrix YouTube
    'fb20_yc1': story('flyhead', 'itsout', 'THE CROSS WAS PERFECT...', 'DIVING HEADER', CYAN, cold=True, pre=6),
    'fb20_yc2': combo(['scorp', 'bike', 'tornado', 'slidesave'], 'u1', 'KICKS THAT SHOULDN\'T WORK', RED),
    # mtgames2# YouTube
    'fb20_m1': combo(['flyhead', 'bike', 'airwar2'], 'u5', 'HEADER, BICYCLE OR SCORPION?', GOLD, labels=('1', '2', '3')),
    'fb20_m2': story('slidesave', 'u3', 'LAST SECOND SLIDE SAVE...', 'THEN A BICYCLE KICK', RED, cold=True),
    # mtfgams12 YouTube
    'fb20_n1': story('scorp', 'u5', 'ONE HEADER PASS...', 'SCORPION KICK', GOLD, pre=6),
    'fb20_n2': combo(['airwar', 'tornado', 'bike'], 'song1', 'NOBODY LETS IT DROP', CYAN),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('fb20_a1', '19:03'), ('fb20_a2', '21:03')]),
    ('7181171', 'youtube', [('fb20_ya1', '19:03'), ('fb20_ya2', '21:03')]),
    ('7752397', 'tiktok', [('fb20_b1', '19:09'), ('fb20_b2', '21:09')]),
    ('7752397', 'youtube', [('fb20_yb1', '19:30'), ('fb20_yb2', '21:30')]),
    ('7773777', 'tiktok', [('fb20_c1', '19:15'), ('fb20_c2', '21:15')]),
    ('7773777', 'instagram', [('fb20_ic1', '19:15'), ('fb20_ic2', '21:15')]),
    ('7773777', 'youtube', [('fb20_yc1', '19:15'), ('fb20_yc2', '21:15')]),
    ('7752416', 'youtube', [('fb20_m1', '19:21'), ('fb20_m2', '21:21')]),
    ('7773832', 'youtube', [('fb20_n1', '19:24'), ('fb20_n2', '21:24')]),
]
