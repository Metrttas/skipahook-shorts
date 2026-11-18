# Tagesdatei 19.11.2026 – TALK-Format + LOGIK-Gate (Routine-Lauf 18.11. ~21 Uhr). Ab 18.11.: 2x Skip a Hook je Konto (12:xx Talk + Day-X/CCU);
#   die 2 Footbomb-Posts je Konto brauchen neue Studio/Blender-Aufnahmen -> nicht in dieser Routine.
#   python3 tools/promo/talk/talk.py tools/promo/talk/days/t_1119.py all stills|render
# CCU: Dashboard nicht angemeldet -> games-API 18.11. 20:1x UTC: playing 0 (= "right now"), Besuche 33,250, Favoriten 1,486, updated 17.11. 18:23 UTC.
# Neue Bilder (stills_mk.py): s_nf_candy/crystal/rainbow + s_f_* (u230b_new_fish), s_bench_* (u232), s_gear_hooks (u230_gear).
F = {
    'nova': ('far_supernova', 5.0, 'SUPERNOVA SHARK', '1 IN 100', 7.15),
    'nova2': ('far2_supernova', 4.2, 'SUPERNOVA SHARK', '1 IN 100', 5.45),
    'nova_q': ('far_supernova', 3.2, 'SUPERNOVA SHARK', '1 IN 100', 4.8),
    'dragon_q': ('cosmic_dragon_hold', 1.4, 'COSMIC DRAGON', '1 IN 100,000', 2.5),
    'lotus_q': ('g_hold_confetti', 0.7, 'MOONLOTUS DRAGON', '1 IN 100,000,000', 1.7),
    'gshark': ('golden_shark_reveal', 0.1, 'GOLDEN SHARK', '1 IN 50,000', 1.85),
    'gshark_hold': ('golden_shark_reveal', 2.95, 'GOLDEN SHARK', '1 IN 50,000', 4.15),
    'meg': ('ancient_reveal', 0.7, 'PREHISTORIC MEGALODON', '1 IN 100,000', 3.3),
    'dragon': ('cosmic_dragon_reveal', 3.1, 'COSMIC DRAGON', '1 IN 100,000', 5.35),
    'whale': ('t_main_whale_jump', 0.3, 'GIANT BLUE WHALE', '1 IN 500,000', 1.98),
    'koi': ('koi2_splash_hover', 4.6, 'COSMIC KOI', '1 IN 10,000,000', 6.35),
    'koi_b': ('koi_hover', 0.45, 'COSMIC KOI', '1 IN 10,000,000', 2.4),
    'lotus': ('g_ethereal_moonlotus', 0.45, 'MOONLOTUS DRAGON', '1 IN 100,000,000', 2.65),
    'goldfish': ('g_mutation_goldfish', 3.9, 'GOLDFISH', 'GOLD MUTATION', 5.6),
    'paddle': ('g_paddlefish_card', 4.2, 'PADDLEFISH', 'COMMON', 5.3),
}


def shot(k, tag=True):
    c, s, n, r, mx = F[k]
    o = {'max': mx}
    if tag: o['fish'] = (n, r)
    return (c, s, o)


def tierline(txt, k, head, tier, extra=None):
    o = {'tier': tier, 'sfx': 'reveal1'}
    shots = [shot(k)]
    if extra: shots.append(shot(extra))
    return (txt, shots, head, o)


def ladder(lines, end_txt, labels=None):
    out = [tierline(t, k, h, i) for i, (t, k, h) in enumerate(lines)]
    out.append((end_txt, [shot(lines[0][1], False)], ''))
    v = dict(ladder=True, speed=0.9, amb='night', lines=out)
    if labels: v['labels'] = labels
    return v


def stop(intro, intro_head, order, after, after_head, end_txt, first='koi_b'):
    return dict(speed=0.9, amb='night', lines=[
        (intro, [shot(first, False)], intro_head),
        ("Ready? Go!", [shot(k) for k in order], 'PAUSE *NOW!', {'flick': True, 'hold': 1.6 * len(order) - 0.6}),
        (after, [shot('lotus', False)], after_head),
        (end_txt, [shot(first, False)], '')])


def groups(intro, intro_head, items, end_txt, first_clip=('g_casts_perfect', 0.5)):
    out = [(intro, [first_clip], intro_head, {'sfx': 'cast_full'})]
    for txt, head, k in items:
        out.append((txt, [shot(k)], head, {'sfx': 'ui_pop'}))
    out.append((end_txt, [first_clip], ''))
    return dict(speed=0.9, amb='night', lines=out)


def pick(intro, intro_head, second, second_head, items, end_txt, first_clip):
    out = [(intro, [first_clip], intro_head), (second, [(first_clip[0], first_clip[1] + 3.0)], second_head)]
    for i, (txt, k, bad) in enumerate(items):
        o = {'sfx': 'miss'} if bad else {'tier': 2 + i % 3}
        out.append((txt, [shot(k)], f'*{i + 1}', o))
    out.append((end_txt, [first_clip], ''))
    return dict(speed=0.9, amb='night', lines=out)

def guess(intro, k_preview, guesses, reveal, k, end_txt):
    out = [(intro, [shot(k_preview, False)], 'HOW *RARE?')]
    for txt, hd in guesses:
        out.append((txt, [shot(k_preview, False)], hd, {'sfx': 'ui_tick'}))
    out.append((reveal, [shot(k)], '*' + F[k][3].replace('1 IN ', '1 IN '), {'tier': 4, 'sfx': 'record'}))
    out.append((end_txt, [shot(k_preview, False)], ''))
    return dict(speed=0.9, amb='night', lines=out)


def hilo(rounds, end_txt):
    """rounds: [(text, k, head, tag, opts)]"""
    out = []
    for txt, k, hd, tag, o in rounds:
        out.append((txt, [shot(k, tag)], hd, o))
    out.append((end_txt, [shot(rounds[0][1], False)], ''))
    return dict(speed=0.9, amb='night', lines=out)


def rather(a, b, both, end_txt, ha, hb):
    return dict(speed=0.9, amb='night', lines=[
        (a[0], [shot(a[1], False)], ha),
        (b[0], [shot(b[1], False)], hb),
        (both, [shot(a[1]), shot(b[1])], 'THE *ODDS'),
        (end_txt, [shot(a[1], False)], '')])




SHORT = {'nova': 'SUPERNOVA', 'nova2': 'SUPERNOVA', 'gshark': 'GOLDEN SHARK', 'whale': 'BLUE WHALE', 'koi': 'COSMIC KOI', 'lotus': 'MOONLOTUS', 'meg': 'MEGALODON'}


def rank(intro, intro_head, keys, end_txt, first):
    out = [(intro, [first], intro_head, {'sfx': 'cast_full'})]
    for i, (txt, k) in enumerate(keys):
        n = len(keys) - i
        out.append((txt, [shot(k)], f'#{n} *' + SHORT.get(k, F[k][2].split()[-1]), {'tier': min(i, 4)}))
    out.append((end_txt, [first], ''))
    return dict(speed=0.9, amb='night', lines=out)


def rarer(rounds, end_txt):
    """rounds: [(text, k, head, tag, opts)] – 'rarer or more common?' statt higher/lower"""
    out = [(txt, [shot(k, tag)], hd, o) for txt, k, hd, tag, o in rounds]
    out.append((end_txt, [shot(rounds[0][1], False)], ''))
    return dict(speed=0.9, amb='night', lines=out)


def timecalc(k, intro, mid, res, end_txt, mid_clip=('g_casts_dock', 3.0), rhead=''):
    return dict(speed=0.88, amb='night', lines=[
        (intro, [shot(k)], '*' + F[k][3], {'tier': 4, 'sfx': 'record'}),
        (mid, [mid_clip], '1 FISH *EVERY SECOND', {'sfx': 'cast_full'}),
        (res, [shot(k, False)], rhead, {'sfx': 'reveal3'}),
        (end_txt, [shot(k, False)], '')])


def sellkeep(k, k_sell_clip, intro, sell, keep, end_txt):
    return dict(speed=0.88, amb='day', lines=[
        (intro, [shot(k)], 'SELL OR *KEEP?', {'sfx': 'reveal3'}),
        (sell, [k_sell_clip], '*SELL', {'sfx': 'coins'}),
        (keep, [('aqua_full_glass', 1.5)], '*KEEP'),
        (end_txt, [shot(k, False)], '')])


def trade(sure, risky, odds, end_txt, ha, hb):
    return dict(speed=0.9, amb='night', lines=[
        (sure[0], [shot(sure[1])], ha),
        (risky[0], [shot(risky[1], False)], hb),
        (odds, [shot(sure[1]), shot(risky[1])], 'THE *ODDS'),
        (end_txt, [shot(risky[1], False), shot(sure[1], False)], '')])


def guess3(intro, opts_txt, opts_head, k_q, reveal, k, end_txt, k_q2=None):
    return dict(speed=0.9, amb='night', lines=[
        (intro, [shot(k_q, False)], 'HOW *RARE?'),
        (opts_txt, [shot(k_q2 or k_q, False)], opts_head, {'sfx': 'ui_tick'}),
        (reveal, [shot(k)], '*' + F[k][3], {'tier': 4, 'sfx': 'record'}),
        (end_txt, [shot(k_q, False)], '')])


def S(name, start=0.3):
    return (name, start, {'max': 5.9})


LAB_YT = ['LIKE', 'SUBSCRIBE', 'COMMENT', 'SHARE', 'ALL 4']
P4 = (4, 4, 1000)

def rate(q, k, close, intro, reveal, close_txt, end_txt, tier=3):
    return dict(speed=0.88, amb='night', lines=[
        (intro, [shot(q, False)], 'RATE IT *1-10'),
        (reveal, [shot(k)], '*' + F[k][3], {'tier': tier, 'sfx': 'reveal3'}),
        (close_txt, [close], '*UP CLOSE'),
        (end_txt, [shot(q, False)], '')])


P5 = (4, 6, 1000)
END12, END13 = "See you on day twelve!", "See you on day thirteen!"

P13 = (4, 4, 1000)
END13, END14 = "See you on day thirteen!", "See you on day fourteen!"


def Z(name, start=0.3):
    return (name, start, {'max': 5.9})


P14 = (4, 0, 1000)
END14, END15 = "See you on day fourteen!", "See you on day fifteen!"


VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'tk19_a': dict(speed=0.9, amb='day', lines=[
        ("Three new secret fish in my Roblox fishing game. You only get one.", [Z('s_nf_rainbow')], 'PICK *ONE', {'sfx': 'cast_full'}),
        ("Number one: the Sugarplum Dragon.", [Z('s_f_sugarplum')], '*1', {'tier': 2, 'sfx': 'reveal2'}),
        ("Number two: the Crystal Colossus.", [Z('s_f_colossus')], '*2', {'tier': 3, 'sfx': 'reveal3'}),
        ("Number three: the Dream Leviathan.", [Z('s_f_leviathan')], '*3', {'tier': 4, 'sfx': 'reveal4'}),
        ("One, two, or three? Skip a Hook, a fishing game on Roblox.", [Z('s_nf_rainbow', 2.0)], '')]),
    'cc14_tt': dict(prog=P14, speed=0.85, amb='day', lines=[
        ("Day fourteen of trying to reach a thousand players: zero online right now.", [('c14_lake_long', 2.0)], 'DAY 14 · *0 ONLINE', {'prog': True}),
        ("Two days ago my Roblox fishing game got the Open Sea update.", [Z('s_poster')], '*OPEN SEA'),
        ("It also added thirty two new fish, like the Sugarplum Dragon.", [Z('s_nf_candy'), Z('s_f_sugarplum')], '*32 NEW FISH'),
        ("Would you come fish with me? " + END15, [('c14_lake_long', 2.0)], '')]),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'tk19_ya': guess3("How rare is the Cosmic Dragon? Guess first.",
                      "One in a thousand, one in a hundred thousand, or one in ten million?", '*1K · 100K · 10M', 'dragon_q',
                      "One in a hundred thousand. Did you get it?", 'dragon',
                      "What did you guess? Skip a Hook, a fishing game on Roblox."),
    'cc14_yt': dict(prog=P14, speed=0.85, amb='day', lines=[
        ("Day fourteen on my road to one thousand players.", [('c06_dock_long', 3.0)], 'DAY *14'),
        ("Right now, nobody is online. Zero.", [('c14_lake_long', 5.0)], '*0 ONLINE', {'prog': True}),
        ("But thirty three thousand people visited, and almost fifteen hundred favorited it.", [('c03_baserow_long2', 4.0)], '33K *VISITS'),
        ("Tell me what would make you play. " + END15, [('c06_dock_long', 3.0)], '')]),

    # ================= B mtfgams · TikTok
    'tk19_b': timecalc('dragon', "One in a hundred thousand. That's the Cosmic Dragon.",
                       "Say you catch one fish every second, with no luck boosts.",
                       "It would take about twenty eight hours to get one. On average.",
                       "Twenty eight hours for one dragon. Worth it? Skip a Hook, a fishing game on Roblox.", mid_clip=('g_casts_lake', 5.0), rhead='~28 *HOURS'),
    'dx13_b': dict(speed=0.85, amb='day', lines=[
        ("Day thirteen: I made candy fish for my Roblox fishing game.", [Z('s_nf_candy')], 'DAY 13 · *CANDY FISH'),
        ("They live in the new Candy Lagoon.", [Z('s_z_candy')], '*CANDY LAGOON'),
        ("There's a Lollipop Puffer,", [Z('s_f_lollipop')], 'LOLLIPOP *PUFFER'),
        ("and a secret one: the Sugarplum Dragon.", [Z('s_f_sugarplum')], '*SECRET', {'sfx': 'reveal3'}),
        ("Which one would you catch first? " + END14, [Z('s_nf_candy', 2.0)], '')]),

    # ================= B mtfgams · YouTube
    'tk19_yb': rarer([
        ("The Supernova Shark is one in a hundred.", 'nova', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal1'}),
        ("Is the Cosmic Koi rarer than the Supernova, or more common?", 'koi_b', '*COSMIC KOI?', False, {}),
        ("Way rarer. One in ten million.", 'koi', '*WAY RARER', True, {'tier': 4, 'sfx': 'record'}),
        ("Now the Megalodon. Rarer, or more common than the Koi?", 'meg', '*MEGALODON?', False, {}),
        ("More common. One in a hundred thousand.", 'meg', '*MORE COMMON', True, {'sfx': 'miss'}),
    ], "Two out of two? Skip a Hook, a fishing game on Roblox."),
    'dx13_yb': dict(speed=0.85, amb='day', lines=[
        ("Day thirteen: these are the new cave fish in my Roblox fishing game.", [Z('s_nf_crystal')], 'DAY 13 · *CAVE FISH'),
        ("They live in the Crystal Caverns.", [Z('s_z_mush')], '*CRYSTAL CAVERNS'),
        ("Like the Prism Anglerfish,", [Z('s_f_angler')], 'PRISM *ANGLERFISH'),
        ("and the Crystal Colossus. Both are secret.", [Z('s_f_colossus')], 'BOTH *SECRET', {'sfx': 'reveal3'}),
        ("Scary or cute? " + END14, [Z('s_nf_crystal', 2.0)], '')]),

    # ================= C Mtrix · TikTok
    'tk19_c': sellkeep('koi', ('koi_hover', 0.45, {'max': 2.4}),
                       "You caught the Cosmic Koi. Sell it, or keep it?",
                       "Sell it, and you get a huge pile of cash right now.",
                       "Keep it, and it earns cash in your aquarium. Even while you're offline.",
                       "Sell or keep? Comment why. Skip a Hook, a fishing game on Roblox."),
    'dx13_c': dict(speed=0.85, amb='day', lines=[
        ("Day thirteen: rainbow fish in my Roblox fishing game.", [Z('s_nf_rainbow')], 'DAY 13 · *RAINBOW FISH'),
        ("It's the last zone in the game.", [Z('s_z_rainbow2')], '*LAST ZONE'),
        ("There's a Unicorn Swordfish,", [Z('s_f_unicorn')], 'UNICORN *SWORDFISH'),
        ("and the Dream Leviathan. Both are secret.", [Z('s_f_leviathan')], 'BOTH *SECRET', {'sfx': 'reveal4'}),
        ("Which one do you want? " + END14, [Z('s_nf_rainbow', 2.0)], '')]),

    # ================= C Mtrix · Instagram (REEL)
    'tk19_ic': rank("Four fish, ranked. The last one is the rarest.", 'RARE *TO RAREST', [
        ("Number four: the Supernova Shark. One in a hundred.", 'nova2'),
        ("Number three: the Prehistoric Megalodon. One in a hundred thousand.", 'meg'),
        ("Number two: the Giant Blue Whale. One in five hundred thousand.", 'whale'),
        ("Number one: the Moonlotus Dragon. One in a hundred million.", 'lotus'),
    ], "Which one have you caught? Skip a Hook, a fishing game on Roblox.", ('g_casts_dock', 3.0)),
    'dx13_ic': dict(speed=0.85, amb='day', lines=[
        ("Day thirteen: four new hooks in my Roblox fishing game.", [Z('s_gear_hooks')], 'DAY 13 · *NEW HOOKS'),
        ("A candy hook, a crystal hook,", [Z('s_gear_hooks', 1.0)], 'CANDY · *CRYSTAL'),
        ("a bug frozen in amber, and a rainbow prism.", [Z('s_gear_hooks', 2.5)], 'AMBER · *RAINBOW'),
        ("Which one would you use? " + END14, [Z('s_gear_hooks', 0.5)], '')]),

    # ================= C Mtrix · YouTube
    'tk19_yc': dict(speed=0.88, amb='day', lines=[
        ("Rate this new secret fish from one to ten. Just on looks.", [Z('s_f_leviathan')], 'RATE IT *1-10'),
        ("It's the Dream Leviathan, from my Roblox fishing game.", [Z('s_f_leviathan', 2.0)], 'DREAM *LEVIATHAN', {'tier': 3, 'sfx': 'reveal3'}),
        ("It only lives in Rainbow Realm, the very last zone.", [Z('s_z_rainbow')], '*RAINBOW REALM'),
        ("Be honest, what's your number? Skip a Hook, a fishing game on Roblox.", [Z('s_f_leviathan', 1.0)], '')]),
    'dx14_yc': dict(speed=0.85, amb='day', lines=[
        ("Day fourteen: the last zones of my Roblox fishing game got harder.", [Z('s_z_lagoonview')], 'DAY 14 · *HARDER'),
        ("The new hooks cost four times more,", [Z('s_gear_hooks')], '*4X PRICE'),
        ("and so do the benches where you train strength.", [Z('s_bench_rainbow')], 'BENCHES *4X'),
        ("So reaching Rainbow Realm takes real time.", [Z('s_z_rainbow2')], '*RAINBOW REALM'),
        ("Too hard, or just right? " + END15, [Z('s_z_lagoonview', 2.0)], '')]),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'tk19_m': rarer([
        ("The Golden Shark is one in fifty thousand.", 'gshark', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal2'}),
        ("Is the Cosmic Dragon rarer than the Golden Shark, or more common?", 'dragon_q', '*COSMIC DRAGON?', False, {}),
        ("Rarer. One in a hundred thousand.", 'dragon', '*RARER', True, {'tier': 3, 'sfx': 'reveal3'}),
        ("Now the Supernova Shark. Rarer, or more common than the dragon?", 'nova_q', '*SUPERNOVA?', False, {}),
        ("Way more common. One in a hundred.", 'nova', '*WAY MORE COMMON', True, {'sfx': 'miss'}),
    ], "How many did you get right? Skip a Hook, a fishing game on Roblox."),
    'cc14_m2': dict(prog=P14, speed=0.85, amb='day', lines=[
        ("Day fourteen: zero players online in my Roblox fishing game right now.", [('c23_lagoon_long', 2.0)], 'DAY 14 · *0 ONLINE', {'prog': True}),
        ("New in my fishing game: a training bench in every new zone.", [Z('s_benches')], '*NEW BENCHES'),
        ("Candy, crystal, jungle,", [Z('s_bench_candy'), Z('s_bench_crystal'), Z('s_bench_jungle')], 'CANDY · CRYSTAL · *JUNGLE'),
        ("and rainbow.", [Z('s_bench_rainbow')], '*RAINBOW'),
        ("Which bench would you train on first? " + END15, [('c23_lagoon_long', 2.0)], '')]),

    # ================= mtfgams12 · YouTube
    'tk19_n': trade(("Would you rather get a Megalodon for sure...", 'meg'),
                    ("...or one try at the Giant Blue Whale, at one in five?", 'whale'),
                    "Fair deal? The whale is five times rarer than the Megalodon.",
                    "Safe or risky? Comment it. Skip a Hook, a fishing game on Roblox.", '*FOR SURE...', 'OR *1 IN 5?'),
    'dx14_n': dict(speed=0.85, amb='day', lines=[
        ("Day fourteen: I made the new zones in my Roblox fishing game three times longer.", [Z('s_z_lagoonview')], 'DAY 14 · *3X LONGER'),
        ("Candy Lagoon goes on and on.", [Z('s_z_candy')], '*CANDY LAGOON'),
        ("In the Crystal Caverns, light only gets in through cracks.", [Z('s_z_cave')], 'CRYSTAL *CAVERNS'),
        ("Long zones or short zones? " + END15, [Z('s_z_lagoonview', 2.0)], '')]),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('tk19_a', '12:03'), ('cc14_tt', '17:33')]),
    ('7181171', 'youtube', [('tk19_ya', '12:03'), ('cc14_yt', '17:33')]),
    ('7752397', 'tiktok', [('tk19_b', '12:09'), ('dx13_b', '16:09')]),
    ('7752397', 'youtube', [('tk19_yb', '12:09'), ('dx13_yb', '16:00')]),
    ('7773777', 'tiktok', [('tk19_c', '12:15'), ('dx13_c', '16:15')]),
    ('7773777', 'instagram', [('tk19_ic', '12:15'), ('dx13_ic', '16:15')]),
    ('7773777', 'youtube', [('tk19_yc', '12:15'), ('dx14_yc', '16:15')]),
    ('7752416', 'youtube', [('tk19_m', '12:21'), ('cc14_m2', '16:21')]),
    ('7773832', 'youtube', [('tk19_n', '12:24'), ('dx14_n', '16:24')]),
]
