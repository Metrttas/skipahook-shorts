# Soccer Bomb 24.11.2026 – Nachhol-Lauf (Routine 23.11. abends brach ab). Sounds je Account != 23.11.
# Soccer Bomb 22.11.2026 – 18 Edits (Clips vom 19.11., 3. Einsatz -> User neue Aufnahmen vorschlagen).
#   Je Account 1 Einzel-Story + 1 Combo, Story-Szene je Account neu, Combo <= 1/3 wie am 20.11., Sounds je Account anders als am 20.11.
#   (21.11. kein Post -> Vortag fuer check_repeat = specs/empty_1121.py)
#   python3 fbedit.py specs/fb_1122.py <id|all> sheet|render
import json
CINE = '/home/claude/fb/cine/'
OUT = '/home/claude/fb/out1124'
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
    # A fbgam.es TikTok (23.: u1, u5)
    'fb24_a1': story('airwar2', 'u3', 'BACK AND FORTH IN THE AIR...', 'HOW DOES IT END?', CYAN, pre=8),
    'fb24_a2': combo(['slidesave', 'airsave', 'bike'], 'itsout', 'SAVED... THEN PUNISHED', RED),
    # A fbgam.es YouTube (23.: u3, u5)
    'fb24_ya1': story('flyhead', 'u1', 'FIRST TOUCH, THEN THE CROSS...', 'HE DIVES FOR IT', GOLD, pre=6),
    'fb24_ya2': combo(['scorp', 'bike', 'slidechain'], 'u4', '3 KICKS, PICK YOUR FAVORITE', CYAN, labels=N3),
    # B mtfgams TikTok (23.: u3, song1)
    'fb24_b1': story('tornado', 'u1', 'NO-LOOK HEEL FLICK...', 'SPINNING FINISH', RED, pre=6),
    'fb24_b2': combo(['airsave', 'airwar', 'flyhead', 'slidesave'], 'u5', 'THE BALL NEVER STOPS', GOLD),
    # B mtfgams YouTube (23.: u4, u1)
    'fb24_yb1': story('scorp', 'u3', 'HE HEADS IT UP FOR HIM...', 'BACKWARDS HEEL KICK', CYAN, pre=6, cold=True),
    'fb24_yb2': combo(['bike', 'airsave', 'airwar2'], 'u5', 'WHO WINS THIS ROUND?', RED, labels=N3),
    # C Mtrix TikTok (23.: u4, itsout)
    'fb24_c1': story('airsave', 'u1', 'PASS. PASS. PASS.', 'THEN THE SCORPION', GOLD),
    'fb24_c2': combo(['tornado', 'flyhead', 'slidesave', 'airwar2'], 'u3', 'DEFENDERS HATE THIS', CYAN),
    # C Mtrix Instagram (23.: u1, u4)
    'fb24_ic1': story('airwar', 'u3', 'VOLLEY IN THE AIR...', 'SCORPION TO END IT', RED, cold=True, pre=6),
    'fb24_ic2': combo(['bike', 'scorp', 'flyhead'], 'u5', 'UPSIDE DOWN GOALS', GOLD),
    # C Mtrix YouTube (23.: itsout, u4)
    'fb24_yc1': story('slidechain', 'u1', 'HE WOULDN\'T GIVE UP...', 'BUT THE TORNADO WON', CYAN),
    'fb24_yc2': combo(['airwar', 'airsave', 'airwar2', 'bike'], 'u5', 'AIR BATTLES ONLY', RED, labels=N4),
    # mtgames2# YouTube (23.: u3, u5)
    'fb24_m1': story('slidesave', 'u4', 'ONE INCH FROM THE LINE...', 'SAVED, THEN FLIPPED', GOLD, cold=True),
    'fb24_m2': combo(['scorp', 'tornado', 'slidechain'], 'itsout', 'FAST, FASTER, FASTEST', CYAN),
    # mtfgams12 YouTube (23.: u1, itsout)
    'fb24_n1': story('flyhead', 'u4', 'HE CONTROLS IT, HE CROSSES IT...', 'DIVING HEADER!', RED, cold=True, pre=6),
    'fb24_n2': combo(['airwar2', 'slidesave', 'scorp', 'airsave'], 'u5', 'WHICH ONE IS ILLEGAL?', GOLD, labels=N4),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('fb24_a1', '19:03'), ('fb24_a2', '21:03')]),
    ('7181171', 'youtube', [('fb24_ya1', '19:03'), ('fb24_ya2', '21:03')]),
    ('7752397', 'tiktok', [('fb24_b1', '19:09'), ('fb24_b2', '21:09')]),
    ('7752397', 'youtube', [('fb24_yb1', '19:30'), ('fb24_yb2', '21:30')]),
    ('7773777', 'tiktok', [('fb24_c1', '19:15'), ('fb24_c2', '21:15')]),
    ('7773777', 'instagram', [('fb24_ic1', '19:15'), ('fb24_ic2', '21:15')]),
    ('7773777', 'youtube', [('fb24_yc1', '19:15'), ('fb24_yc2', '21:15')]),
    ('7752416', 'youtube', [('fb24_m1', '19:21'), ('fb24_m2', '21:21')]),
    ('7773832', 'youtube', [('fb24_n1', '19:24'), ('fb24_n2', '21:24')]),
]
