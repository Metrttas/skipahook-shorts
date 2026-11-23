# Soccer Bomb 23.11.2026 – Nachhol-Lauf am Nachmittag (Routine 22.11. abends brach ab), nur 19:xx/21:xx. Sounds je Account != 22.11.
# Soccer Bomb 22.11.2026 – 18 Edits (Clips vom 19.11., 3. Einsatz -> User neue Aufnahmen vorschlagen).
#   Je Account 1 Einzel-Story + 1 Combo, Story-Szene je Account neu, Combo <= 1/3 wie am 20.11., Sounds je Account anders als am 20.11.
#   (21.11. kein Post -> Vortag fuer check_repeat = specs/empty_1121.py)
#   python3 fbedit.py specs/fb_1122.py <id|all> sheet|render
import json
CINE = '/home/claude/fb/cine/'
OUT = '/home/claude/fb/out1123'
B = json.load(open('/home/claude/fb/snd/beats.json'))
TL = json.load(open('/home/claude/fb/tl.json'))
SND = {'u1': ('snd/u1.wav', 7.236), 'u3': ('snd/u3.wav', 4.323), 'u4': ('snd/u4.wav', 4.612), 'u5': ('snd/u5.wav', 7.140),
       'song1': ('snd/song1_fussball_drop.wav', 10.655), 'itsout': ('snd/itsout_finally_out.wav', 5.313)}
RED = {'fill': (255, 70, 90)}; GOLD = {'fill': (255, 200, 40)}; CYAN = {'fill': (80, 220, 255)}
END = 'Search SOCCER BOMB on Roblox'
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
    if S['R'] is not None and pre is None:
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


N4 = ('1', '2', '3', '4'); N3 = ('1', '2', '3')
VIDEOS = {
    # A fbgam.es TikTok (22.: u4, itsout)
    'fb23_a1': story('bike', 'u1', 'HE LIFTS IT OVER HIS HEAD...', 'AND FLIPS IT BACK', CYAN, pre=6),
    'fb23_a2': combo(['scorp', 'flyhead', 'tornado'], 'u5', 'NO ONE COULD DEFEND THESE', GOLD),
    # A fbgam.es YouTube (22.: song1, u4, Schiff u1)
    'fb23_ya1': story('slidesave', 'u3', 'FULL SLIDE ON THE LINE...', 'AND HIS TEAMMATE FLIPS IT', RED, cold=True),
    'fb23_ya2': combo(['airwar', 'airsave', 'tornado', 'airwar2'], 'u5', 'NOTHING TOUCHES THE GROUND', CYAN),
    # B mtfgams TikTok (22.: u1, u5)
    'fb23_b1': story('airwar2', 'u3', 'BICYCLE. SCISSOR. HEADER. VOLLEY.', 'GUESS THE LAST ONE', GOLD, pre=8),
    'fb23_b2': combo(['bike', 'scorp', 'slidechain'], 'song1', 'FLIP, SCORPION OR SPIN?', RED, labels=N3),
    # B mtfgams YouTube (22.: itsout, u5, Schiff u3)
    'fb23_yb1': story('slidechain', 'u4', 'ONE SAVE WASN\'T ENOUGH...', 'SO HE SLID AGAIN', CYAN),
    'fb23_yb2': combo(['flyhead', 'tornado', 'airwar', 'slidesave'], 'u1', 'WATCH THE LAST ONE', GOLD),
    # C Mtrix TikTok (22.: song1, u1)
    'fb23_c1': story('scorp', 'u4', 'ONE HEADER UP...', 'ONE SCORPION DOWN', RED, cold=True, pre=6),
    'fb23_c2': combo(['bike', 'slidechain', 'airwar'], 'itsout', 'TOO QUICK FOR THE DEFENSE', CYAN),
    # C Mtrix Instagram (22.: u3, itsout, Schiff u5)
    'fb23_ic1': story('tornado', 'u1', 'HE DIDN\'T EVEN LOOK...', 'THEN THE TORNADO KICK', GOLD, pre=6),
    'fb23_ic2': combo(['airsave', 'slidesave', 'airwar2'], 'u4', 'SAVE IT OR LOSE IT', RED),
    # C Mtrix YouTube (22.: u5, u3)
    'fb23_yc1': story('bike', 'itsout', 'BALL ON HIS CHEST...', 'BICYCLE KICK!', CYAN, cold=True, pre=6),
    'fb23_yc2': combo(['scorp', 'flyhead', 'tornado', 'slidesave'], 'u4', 'RANK THESE 1 TO 4', GOLD, labels=N4),
    # mtgames2# YouTube (22.: u1, song1, Schiff u4)
    'fb23_m1': story('airwar', 'u3', 'THREE TOUCHES IN THE AIR...', 'THE FOURTH IS A SCORPION', RED),
    'fb23_m2': combo(['bike', 'flyhead', 'airwar2'], 'u5', 'BEST GOAL OF THE DAY?', CYAN, labels=N3),
    # mtfgams12 YouTube (22.: u3, u4)
    'fb23_n1': story('airsave', 'u1', 'IT NEVER HIT THE GROUND...', 'UNTIL THE SCORPION', GOLD, cold=True),
    'fb23_n2': combo(['tornado', 'bike', 'airwar'], 'itsout', 'SPIN, FLIP, SCORPION', RED),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('fb23_a1', '19:03'), ('fb23_a2', '21:03')]),
    ('7181171', 'youtube', [('fb23_ya1', '19:03'), ('fb23_ya2', '21:03')]),
    ('7752397', 'tiktok', [('fb23_b1', '19:09'), ('fb23_b2', '21:09')]),
    ('7752397', 'youtube', [('fb23_yb1', '19:30'), ('fb23_yb2', '21:30')]),
    ('7773777', 'tiktok', [('fb23_c1', '19:15'), ('fb23_c2', '21:15')]),
    ('7773777', 'instagram', [('fb23_ic1', '19:15'), ('fb23_ic2', '21:15')]),
    ('7773777', 'youtube', [('fb23_yc1', '19:15'), ('fb23_yc2', '21:15')]),
    ('7752416', 'youtube', [('fb23_m1', '19:21'), ('fb23_m2', '21:21')]),
    ('7773832', 'youtube', [('fb23_n1', '19:24'), ('fb23_n2', '21:24')]),
]
