# Tagesdatei 18.11.2026 – TALK-Format + LOGIK-Gate (Routine-Lauf 18.11. ~04 Uhr; 17.11. fiel aus -> Day-Zähler laufen fortlaufend weiter).
#   python3 tools/promo/talk/talk.py tools/promo/talk/days/t_1118.py all stills|render
# CCU: Dashboard nicht angemeldet -> games-API 18.11. 03:1x UTC: playing 4 (= "right now"), Besuche 33,201, Favoriten 1,484,
#   updated 17.11. 18:23 UTC = OPEN-SEA-RELEASE LIVE (eigener Meer-Server, 7 Inseln, 4 Bosse, Zonen 16-19 Candy/Crystal/Dino/Rainbow).
# Bilder: neue s_*-Standbild-Clips aus docs/ref (u234 Poster/Update-Log, u230_studio Zonen, u231 Höhle, u233 Regenbogen-Bank) via stills_mk.py.
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


VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'tk18_a1': timecalc('gshark', "One in fifty thousand. That's the Golden Shark.",
                        "Say you catch one fish every second, with no luck boosts.",
                        "It would take about fourteen hours to get one. On average.",
                        "Fourteen hours for one shark. Would you? Skip a Hook, a fishing game on Roblox.", mid_clip=('g_casts_lake', 3.0), rhead='~14 *HOURS'),
    'cc13_tt': dict(prog=P13, speed=0.85, amb='day', lines=[
        ("Day thirteen: my Roblox fishing game just got its biggest update ever.", [Z('s_poster')], 'DAY 13 · *OPEN SEA'),
        ("The Open Sea is out. You sail your own ship.", [Z('s_ship_sail')], '*OUT NOW'),
        ("Four players were online when I made this. At four in the morning.", [('c23_lagoon_long', 2.0)], '*4 ONLINE', {'prog': True}),
        ("Would you set sail tonight? " + END14, [Z('s_ship_harbor')], '')]),
    'tk18_a2': rank("Four fish, ranked. The last one is the rarest.", 'RARE *TO RAREST', [
        ("Number four: the Golden Shark. One in fifty thousand.", 'gshark'),
        ("Number three: the Cosmic Dragon. One in a hundred thousand.", 'dragon'),
        ("Number two: the Giant Blue Whale. One in five hundred thousand.", 'whale'),
        ("Number one: the Cosmic Koi. One in ten million.", 'koi'),
    ], "Which one have you caught? Skip a Hook, a fishing game on Roblox.", ('g_casts_night', 3.0)),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'tk18_ya1': rarer([
        ("The Prehistoric Megalodon is one in a hundred thousand.", 'meg', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal2'}),
        ("Is the Golden Shark rarer, or more common?", 'gshark_hold', '*GOLDEN SHARK?', False, {}),
        ("More common. One in fifty thousand.", 'gshark', '*MORE COMMON', True, {'sfx': 'miss'}),
        ("Now the Cosmic Koi. Rarer, or more common than the Megalodon?", 'koi_b', '*COSMIC KOI?', False, {}),
        ("Way rarer. One in ten million.", 'koi', '*WAY RARER', True, {'tier': 4, 'sfx': 'record'}),
    ], "Two for two? Skip a Hook, a fishing game on Roblox."),
    'cc13_yt': dict(prog=P13, speed=0.85, amb='day', lines=[
        ("Day thirteen on my road to one thousand players.", [('c06_dock_long', 3.0)], 'DAY *13'),
        ("Yesterday I released the Open Sea update.", [Z('s_ulog')], '*OPEN SEA'),
        ("Seven islands, and four giant sea bosses.", [Z('s_game_skull'), Z('s_bossg_1')], '7 ISLANDS · *4 BOSSES'),
        ("Thirty three thousand visits so far. Four players online right now.", [('c03_baserow_long2', 4.0)], '33K *VISITS', {'prog': True}),
        ("Which boss would you fight first? " + END14, [Z('s_bossg_4')], '')]),
    'tk18_ya2': sellkeep('meg', ('ancient_reveal', 0.7, {'max': 3.3}),
                         "You just caught the Prehistoric Megalodon. Sell it, or keep it?",
                         "Sell it, and the cash is yours right away.",
                         "Keep it, and it makes cash in your aquarium. Even when you're offline.",
                         "Quick cash or slow cash? Comment it. Skip a Hook, a fishing game on Roblox."),

    # ================= B mtfgams · TikTok
    'tk18_b1': guess3("How rare is the Cosmic Dragon? Guess before I say it.",
                      "One in a thousand, one in a hundred thousand, or one in ten million?", '1K · *100K · 10M?', 'dragon_q',
                      "One in a hundred thousand. Did you get it?", 'dragon',
                      "Drop your guess below. Skip a Hook, a fishing game on Roblox."),
    'dx12_b': dict(speed=0.85, amb='day', lines=[
        ("Day twelve: you can sail your own ship in my Roblox fishing game.", [Z('s_ship_sail')], 'DAY 12 · *YOUR SHIP'),
        ("The Open Sea update came out yesterday.", [Z('s_poster')], '*OUT NOW'),
        ("There's a small sloop, a brigantine,", [Z('s_ship_sloop'), Z('s_ship_brig')], 'SLOOP · *BRIGANTINE'),
        ("and a royal galleon.", [Z('s_ship_galleon')], 'ROYAL *GALLEON'),
        ("Which one are you saving for? " + END13, [Z('s_ship_sail', 2.5)], '')]),
    'tk18_b2': trade(("Would you rather get a Cosmic Dragon for sure...", 'dragon'),
                     ("...or take a one in a hundred shot at the Cosmic Koi?", 'koi'),
                     "The dragon is one in a hundred thousand. The Koi is a hundred times rarer.",
                     "Safe pick or the gamble? Comment it. Skip a Hook, a fishing game on Roblox.", '*FOR SURE...', 'OR *1 IN 100?'),

    # ================= B mtfgams · YouTube
    'tk18_yb1': rarer([
        ("The Golden Shark is one in fifty thousand.", 'gshark', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal2'}),
        ("Is the Giant Blue Whale rarer, or more common?", 'whale', '*BLUE WHALE?', False, {}),
        ("Rarer. One in five hundred thousand.", 'whale', '*RARER', True, {'tier': 3, 'sfx': 'reveal3'}),
        ("Now the Supernova Shark. Rarer, or more common than the whale?", 'nova_q', '*SUPERNOVA?', False, {}),
        ("Way more common. One in a hundred.", 'nova', '*WAY MORE COMMON', True, {'sfx': 'miss'}),
    ], "How many did you get? Skip a Hook, a fishing game on Roblox."),
    'dx12_yb': dict(speed=0.85, amb='day', lines=[
        ("Day twelve: the Open Sea is live in my Roblox fishing game.", [Z('s_ulog')], 'DAY 12 · *OPEN SEA'),
        ("When you set sail, you jump to a new server, made just for the sea.", [Z('s_ship_harbor')], '*NEW SERVER'),
        ("The old world doesn't load out there, so it runs smoother.", [Z('s_rest_deep')], '*SMOOTHER'),
        ("Did the jump work for you? " + END13, [Z('s_ship_harbor', 2.5)], '')]),
    'tk18_yb2': timecalc('lotus', "One in a hundred million. That's the Moonlotus Dragon.",
                         "Say you catch one fish every second, with no luck boosts.",
                         "It would take over three years to get one. On average.",
                         "Three years for one dragon. Still want it? Skip a Hook, a fishing game on Roblox.", mid_clip=('g_casts_night', 2.0), rhead='3+ *YEARS'),

    # ================= C Mtrix · TikTok
    'tk18_c1': rarer([
        ("The Cosmic Dragon is one in a hundred thousand.", 'dragon', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal2'}),
        ("Is the Moonlotus Dragon rarer, or more common?", 'lotus_q', '*MOONLOTUS?', False, {}),
        ("Rarer. One in a hundred million.", 'lotus', '*RARER', True, {'tier': 4, 'sfx': 'record'}),
        ("Now the Golden Shark. Rarer, or more common than the Cosmic Dragon?", 'gshark_hold', '*GOLDEN SHARK?', False, {}),
        ("More common. One in fifty thousand.", 'gshark', '*MORE COMMON', True, {'sfx': 'miss'}),
    ], "Did you get both? Skip a Hook, a fishing game on Roblox."),
    'dx12_c': dict(speed=0.85, amb='day', lines=[
        ("Day twelve: I closed the roof of the crystal cave in my Roblox fishing game.", [Z('s_z_cave')], 'DAY 12 · *CRYSTAL CAVE'),
        ("Now the light only gets in through thin cracks.", [Z('s_z_cave', 2.5)], '*THIN CRACKS'),
        ("It's live now, with three other new zones.", [Z('s_z_crystal')], '*LIVE NOW'),
        ("Too dark, or just right? " + END13, [Z('s_z_cave', 2.5)], '')]),
    'tk18_c2': sellkeep('gshark', ('golden_shark_reveal', 2.95, {'max': 4.15}),
                        "You just caught the Golden Shark. Sell it, or keep it?",
                        "Sell it, and you get the cash right now.",
                        "Keep it, and it earns cash in your aquarium. Even while you sleep.",
                        "Sell or keep? Tell me why. Skip a Hook, a fishing game on Roblox."),

    # ================= C Mtrix · Instagram (REEL)
    'tk18_ic1': guess3("How rare is the Cosmic Koi? Guess first.",
                       "One in ten thousand, one in a million, or one in ten million?", '10K · 1M · *10M?', 'koi_b',
                       "One in ten million. Were you close?", 'koi',
                       "What was your guess? Skip a Hook, a fishing game on Roblox."),
    'dx12_ic': dict(speed=0.85, amb='day', lines=[
        ("Day twelve: the last new zone in my Roblox fishing game is Rainbow Realm.", [Z('s_z_rainbow')], 'DAY 12 · *RAINBOW REALM'),
        ("Rainbows, clouds, and candy colors everywhere.", [Z('s_z_rainbow2')], '*RAINBOWS'),
        ("Even the strength bench is a rainbow now.", [Z('s_z_bench')], '*RAINBOW BENCH'),
        ("It's live. Would you fish here? " + END13, [Z('s_z_rainbow', 2.5)], '')]),
    'tk18_ic2': trade(("Would you rather get a Golden Shark for sure...", 'gshark_hold'),
                      ("...or take a one in two thousand shot at the Moonlotus Dragon?", 'lotus'),
                      "The Golden Shark is one in fifty thousand. The Moonlotus is two thousand times rarer.",
                      "Play it safe, or go for it? Comment below. Skip a Hook, a fishing game on Roblox.", '*FOR SURE...', 'OR *1 IN 2,000?'),

    # ================= C Mtrix · YouTube
    'tk18_yc1': rank("Four fish, ranked from rare to rarest.", 'RARE *TO RAREST', [
        ("Number four: the Supernova Shark. One in a hundred.", 'nova2'),
        ("Number three: the Golden Shark. One in fifty thousand.", 'gshark'),
        ("Number two: the Prehistoric Megalodon. One in a hundred thousand.", 'meg'),
        ("Number one: the Moonlotus Dragon. One in a hundred million.", 'lotus'),
    ], "Which one do you want most? Skip a Hook, a fishing game on Roblox.", ('g_casts_lake', 6.0)),
    'dx13_yc': dict(speed=0.85, amb='day', lines=[
        ("Day thirteen: my Roblox fishing game has brand new zones.", [Z('s_z_lagoonview')], 'DAY 13 · *NEW ZONES'),
        ("First, Candy Lagoon, full of sweets.", [Z('s_z_candy')], '*CANDY LAGOON'),
        ("Then the Crystal Caverns, a glowing cave.", [Z('s_z_mush')], '*CRYSTAL CAVERNS'),
        ("And Rainbow Realm, at the very end.", [Z('s_z_rainbow2')], '*RAINBOW REALM'),
        ("All live now, with new fish. Which zone first? " + END14, [Z('s_z_lagoonview', 2.5)], '')]),
    'tk18_yc2': rate('lotus_q', 'lotus', ('g_ethereal_moonlotus', 0.45, {'max': 2.65}),
                     "Rate this dragon from one to ten. Just on looks.",
                     "The Moonlotus Dragon. One in a hundred million.",
                     "The rarest fish in the game.",
                     "Be honest, what's your number? Skip a Hook, a fishing game on Roblox.", tier=4),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'tk18_m1': rarer([
        ("The Supernova Shark is one in a hundred.", 'nova', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal1'}),
        ("Is the Prehistoric Megalodon rarer, or more common?", 'meg', '*MEGALODON?', False, {}),
        ("Rarer. One in a hundred thousand.", 'meg', '*RARER', True, {'tier': 3, 'sfx': 'reveal3'}),
        ("Now the Giant Blue Whale. Rarer, or more common than the Megalodon?", 'whale', '*BLUE WHALE?', False, {}),
        ("Rarer. One in five hundred thousand.", 'whale', '*RARER', True, {'tier': 4, 'sfx': 'record'}),
    ], "How did you do? Skip a Hook, a fishing game on Roblox."),
    'cc13_m2': dict(prog=P13, speed=0.85, amb='day', lines=[
        ("Day thirteen: my Roblox fishing game has almost fifteen hundred favorites.", [('c23_lagoon_long', 4.0)], 'DAY 13 · *1,484 FAVORITES'),
        ("Yesterday the Open Sea came out.", [Z('s_poster')], '*OPEN SEA'),
        ("You get your own ship, and sail between islands.", [Z('s_ship_sail'), Z('s_game_skull')], '*YOUR OWN SHIP'),
        ("Four players were online when I made this.", [('c14_lake_long', 5.0)], '*4 ONLINE', {'prog': True}),
        ("Did you set sail yet? " + END14, [Z('s_ship_harbor', 2.5)], '')]),
    'tk18_m2': guess3("How rare is the Giant Blue Whale? Guess first.",
                      "One in fifty thousand, one in five hundred thousand, or one in fifty million?", '50K · *500K · 50M?', 'whale',
                      "One in five hundred thousand. Right?", 'whale',
                      "Comment your guess. Skip a Hook, a fishing game on Roblox."),

    # ================= mtfgams12 · YouTube
    'tk18_n1': sellkeep('dragon', ('cosmic_dragon_reveal', 3.1, {'max': 5.35}),
                        "You just caught the Cosmic Dragon. Sell it, or keep it?",
                        "Sell it, and the cash is yours. Right now.",
                        "Keep it, and it earns cash in your aquarium. Even while you're away.",
                        "Sell or keep? Comment why. Skip a Hook, a fishing game on Roblox."),
    'dx13_n': dict(speed=0.85, amb='day', lines=[
        ("Day thirteen: sea bosses are live in my Roblox fishing game.", [Z('s_bossg_1')], 'DAY 13 · *SEA BOSSES'),
        ("Reefback,", [Z('s_bossg_1', 1.5)], '*REEFBACK'),
        ("Bonejaw,", [Z('s_bossg_2')], '*BONEJAW'),
        ("Magma Maw,", [Z('s_bossg_3')], '*MAGMA MAW'),
        ("and the Storm Leviathan.", [Z('s_bossg_4')], 'STORM *LEVIATHAN'),
        ("They rise out in open water. Which one scares you most? " + END14, [Z('s_bossg_1', 2.5)], '')]),
    'tk18_n2': timecalc('nova', "One in a hundred. That's the Supernova Shark.",
                        "Say you catch one fish every second, with no luck boosts.",
                        "You'd get one in under two minutes. On average.",
                        "Rare, or not rare at all? Skip a Hook, a fishing game on Roblox.", mid_clip=('g_casts_dock', 5.0), rhead='< 2 *MINUTES'),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('tk18_a1', '12:03'), ('cc13_tt', '17:33'), ('tk18_a2', '19:03')]),
    ('7181171', 'youtube', [('tk18_ya1', '12:03'), ('cc13_yt', '17:33'), ('tk18_ya2', '19:03')]),
    ('7752397', 'tiktok', [('tk18_b1', '12:09'), ('dx12_b', '16:09'), ('tk18_b2', '19:09')]),
    ('7752397', 'youtube', [('tk18_yb1', '12:09'), ('dx12_yb', '16:00'), ('tk18_yb2', '19:30')]),
    ('7773777', 'tiktok', [('tk18_c1', '12:15'), ('dx12_c', '16:15'), ('tk18_c2', '19:15')]),
    ('7773777', 'instagram', [('tk18_ic1', '12:15'), ('dx12_ic', '16:15'), ('tk18_ic2', '19:15')]),
    ('7773777', 'youtube', [('tk18_yc1', '12:15'), ('dx13_yc', '16:15'), ('tk18_yc2', '19:15')]),
    ('7752416', 'youtube', [('tk18_m1', '12:21'), ('cc13_m2', '16:21'), ('tk18_m2', '19:21')]),
    ('7773832', 'youtube', [('tk18_n1', '12:24'), ('dx13_n', '16:24'), ('tk18_n2', '19:24')]),
]
