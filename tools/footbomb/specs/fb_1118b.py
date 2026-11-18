# Footbomb 18.11.2026 v2 – 18 Edits aus 7 gescripteten Kino-Szenen (DuoDirector), nur Sounds des Users.
#   python3 fbedit.py specs/fb_1118b.py <id|all> sheet|render
import json
CINE = '/home/claude/fb/cine/'
OUT = '/home/claude/fb/out1118b'
B = json.load(open('/home/claude/fb/snd/beats.json'))
SND = {'u1': ('snd/u1.wav', 7.236), 'u3': ('snd/u3.wav', 4.323), 'u4': ('snd/u4.wav', 4.612), 'u5': ('snd/u5.wav', 7.140),
       'song1': ('snd/song1_fussball_drop.wav', 10.655), 'itsout': ('snd/itsout_finally_out.wav', 5.313)}
RED = {'fill': (255, 70, 90)}; GOLD = {'fill': (255, 200, 40)}; CYAN = {'fill': (80, 220, 255)}

# Szene: Datei, K = Schuss-Kontakt (s im Clip), I = Einschlag, C = Jubel-Start, E = Ende, z = Zoom-Basis
SC = {
    'bike':    dict(f='bike_v2', K=3.50, I=5.10, C=7.20, E=9.00, z=1.27),
    'fake':    dict(f='fake_v1', K=2.22, I=3.50, C=5.42, E=7.05, z=1.27, zk=1.6, cyk=.47),
    'save':    dict(f='save_v1', K=5.03, I=6.32, C=8.35, E=10.05, z=1.27),
    'scorp':   dict(f='scorp_v3', K=3.48, I=4.47, C=6.48, E=8.28, z=1.27),
    'tornado': dict(f='tornado_v3', K=2.77, I=4.02, C=6.03, E=7.83, z=1.27),
    'rally':   dict(f='rally_v3', K=5.25, I=6.30, C=8.32, E=10.1, z=1.27),
    'flyhead': dict(f='flyhead_v3', K=3.60, I=4.65, C=6.65, E=8.45, z=1.27),
}


def seg(s, t, n, speed=1.0, z=None, cy=.5, fx=''):
    d = dict(clip=CINE + SC[s]['f'] + '.mp4', t=max(0.0, t), n=n, speed=speed, z=z or SC[s]['z'], cy=cy)
    if fx: d['fx'] = fx
    return d


def story(s, snd, hook1, hook2, st2=RED, cold=False, pre=None):
    f, drop = SND[snd]; per = B[f]['period']; S = SC[s]
    K, I, C, E = S['K'], S['I'], S['C'], S['E']
    segs = []
    if cold:  # Einschlag zuerst (2 Beats), dann die ganze Aktion
        segs.append(seg(s, I - 0.1, 2, 0.8, fx='flash'))
    nb = pre or min(8, int(K / per / 0.95))
    nb = max(4, nb - (nb % 2))
    t0 = max(0.0, K - nb * per)
    segs.append(seg(s, t0, nb, (K - t0) / (nb * per)))
    n2 = max(2, round((I - K) / per))
    segs.append(seg(s, K, n2, (I - K) / (n2 * per), z=S.get('zk'), cy=S.get('cyk', .5), fx='flash'))
    segs.append(seg(s, I - 0.02, 3, 1.0, z=S.get('zk', S['z']) * 0.95 if S.get('zk') else None, cy=S.get('cyk', .5), fx='punch'))
    segs.append(seg(s, K - 0.45, 4, 0.8, z=(S.get('zk') or S['z']) + 0.06, cy=S.get('cyk', .5), fx='flash'))
    nc = 4
    segs.append(seg(s, C, nc, min(1.0, (E - C) / (nc * per))))
    npre = (2 if cold else 0) + nb
    post = sum(x['n'] for x in segs) - npre
    return dict(sound=f, s0=drop - npre * per, dur=(npre + post) * per, segs=segs, end='Search FOOTBOMB on Roblox',
                text=[(0, npre * per, hook1), (npre * per, (npre + post) * per, hook2, st2)])


def montage(scenes, snd, hook, st=GOLD, labels=('1', '2', '3')):
    f, drop = SND[snd]; per = B[f]['period']
    segs = []; text = []; k = 0
    for i, s in enumerate(scenes):
        S = SC[s]
        segs.append(seg(s, S['K'] - 3 * per, 3))
        n2 = max(2, round((S['I'] - S['K']) / per))
        segs.append(seg(s, S['K'], n2, (S['I'] - S['K']) / (n2 * per), z=S.get('zk'), cy=S.get('cyk', .5), fx='flash'))
        segs.append(seg(s, S['I'] - 0.02, 2, 1.0, fx='punch'))
        n = 3 + n2 + 2
        text.append((k * per, (k + n) * per, labels[i], dict(GOLD, size=170, y=1360 + 230)))
        k += n
    text.insert(0, (0, k * per, hook, st))
    pre = 3  # Drop auf dem ersten Schuss
    return dict(sound=f, s0=drop - pre * per, dur=k * per, segs=segs, end='Search FOOTBOMB on Roblox', text=text)


VIDEOS = {
    # A fbgam.es TikTok
    'fb_a1': story('bike', 'u3', 'WAIT FOR THE PASS...', 'BICYCLE KICK'),
    'fb_a2': story('fake', 'u5', 'WATCH THE FAKE...', 'KEEPER GOT COOKED', pre=4),
    # A fbgam.es YouTube
    'fb_ya1': story('save', 'song1', 'HE SAVED IT...', 'THEN DID THIS', GOLD, pre=12),
    'fb_ya2': story('scorp', 'itsout', 'HEADER TO HIS TEAMMATE...', 'SCORPION KICK', CYAN, pre=12),
    # B mtfgams TikTok
    'fb_b1': story('tornado', 'u1', 'NO-LOOK HEEL PASS...', 'TORNADO KICK', CYAN, pre=6),
    'fb_b2': story('rally', 'u3', 'NOBODY LET IT DROP...', 'AXE KICK ENDS IT', RED),
    # B mtfgams YouTube
    'fb_yb1': story('flyhead', 'u5', 'CROSS IT IN...', 'DIVING HEADER', GOLD),
    'fb_yb2': montage(['bike', 'scorp', 'tornado'], 'song1', 'PICK ONE'),
    # C Mtrix TikTok
    'fb_c1': story('scorp', 'u4', 'HOW DID THIS GO IN?', 'SCORPION KICK', RED, cold=True, pre=6),
    'fb_c2': story('rally', 'itsout', 'RATE THIS RALLY', '1 TO 10?', GOLD, cold=True, pre=16),
    # C Mtrix Instagram
    'fb_ic1': story('bike', 'u1', 'TEAM PLAY IN ROBLOX', 'BICYCLE KICK FINISH', RED, cold=True, pre=6),
    'fb_ic2': story('tornado', 'u4', 'NO LOOK PASS', 'INTO A TORNADO KICK', CYAN, cold=True, pre=4),
    # C Mtrix YouTube
    'fb_yc1': story('flyhead', 'u3', 'DUOS ON ROBLOX', 'DIVING HEADER', GOLD, cold=True, pre=6),
    'fb_yc2': montage(['save', 'rally', 'fake'], 'u1', 'CLEANEST FINISH?'),
    # mtgames2# YouTube
    'fb_m1': story('fake', 'song1', 'THE FAKE...', 'KEEPER GOT COOKED', RED, cold=True, pre=6),
    'fb_m2': montage(['flyhead', 'bike', 'scorp'], 'itsout', 'WHICH ONE IS THE BEST?'),
    # mtfgams12 YouTube
    'fb_n1': story('save', 'u5', 'LAST SECOND SAVE...', 'THEN A SCISSOR KICK', GOLD, cold=True, pre=8),
    'fb_n2': story('rally', 'u4', '2V2 RALLY ON ROBLOX', 'HE ENDED IT', RED, pre=8),
}

POST_PLAN = [
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
