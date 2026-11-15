# Tagesdatei 16.11.2026 – TALK-Format + LOGIK-Gate.
#   python3 tools/promo/talk/talk.py tools/promo/talk/days/t_1116.py all stills|render
# CCU (Dashboard 15.11. ~20:05 UTC): Average 6 (+30,3 %, Vortag 4). Besuche 32,663, Favoriten 1,446, games-API updated 10.11. (= Open Sea NICHT live).
# Neuigkeit (git 15.11., nur Studio): Boss-Kampf 2.0 (Harpune, 3 Phasen, Abtauchen, Angriffe mit Warnung), Bosse erscheinen zwischen den Inseln,
#   Sturmfahrt (Brecher, Wasser im Boot, Lecks, Eimer/Hammer, Swamped -> Strand), Werft-Upgrades (Tempo/Laderaum/Wind Boost), Welt 1 im Meer aus (41 -> 58 FPS).
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

VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'tk16_a1': rarer([
        ("The Golden Shark is one in fifty thousand.", 'gshark', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal2'}),
        ("Is the Cosmic Dragon rarer, or more common?", 'dragon_q', '*DRAGON?', False, {}),
        ("Rarer. One in a hundred thousand.", 'dragon', '*RARER', True, {'tier': 3, 'sfx': 'reveal3'}),
        ("Now the Supernova Shark. Rarer, or more common than the Golden Shark?", 'nova_q', '*SUPERNOVA?', False, {}),
        ("Way more common. One in a hundred.", 'nova', '*WAY MORE COMMON', True, {'sfx': 'miss'}),
    ], "Did you get both right? Skip a Hook, a fishing game on Roblox."),
    'cc12_tt': dict(prog=P5, speed=0.85, amb='day', lines=[
        ("Day twelve: six players on average in my Roblox fishing game. Up from four.", [('c14_lake_long', 2.0)], 'DAY 12 · *6 PLAYERS', {'prog': True}),
        ("Today I'm testing boss fights out at sea.", [S('s_bossg_1')], '*BOSS FIGHTS'),
        ("You fight a giant sea serpent, and it fights back in three phases.", [S('s_bossg_3'), S('s_bossg_4')], '*3 PHASES'),
        ("Still in Studio, not out yet. Would you fight this one? " + END13, [S('s_bossg_2')], '')]),
    'tk16_a2': guess3("How rare is the Golden Shark? Guess before I tell you.",
                      "One in five thousand, one in fifty thousand, or one in five million?", '5K · *50K · 5M?', 'gshark_hold',
                      "One in fifty thousand. Were you right?", 'gshark',
                      "Comment your guess. Skip a Hook, a fishing game on Roblox."),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'tk16_ya1': trade(("Would you rather get a Supernova Shark for sure...", 'nova2'),
                      ("...or take a one percent shot at the Golden Shark?", 'gshark'),
                      "Normally, the Supernova is one in a hundred. The Golden Shark is one in fifty thousand.",
                      "Sure thing, or the gamble? Comment it. Skip a Hook, a fishing game on Roblox.", '*FOR SURE...', 'OR *1 IN 100?'),
    'cc12_yt': dict(prog=P5, speed=0.85, amb='day', lines=[
        ("Day twelve on my road to one thousand players.", [('c06_dock_long', 3.0)], 'DAY *12'),
        ("Six players on average now, up from four.", [('c03_baserow_long2', 4.0)], '*6 PLAYERS', {'prog': True}),
        ("Now I'm testing storms that hit your ship with huge waves.", [S('s_ship_storm'), S('s_waves_game')], '*HUGE WAVES'),
        ("If your boat fills with water, it sinks, and you wash up on a beach.", [S('s_finds_isle')], '*WASHED UP'),
        ("Not out yet. Would you sail into the storm? " + END13, [S('s_ship_storm', 2.5)], '')]),
    'tk16_ya2': rate('koi_b', 'koi', ('koi2_splash_hover', 3.6, {'max': 6.35}),
                     "Rate this fish from one to ten. Just on looks.",
                     "The Cosmic Koi. One in ten million.",
                     "Look at it glow.",
                     "Be honest, what's your number? Skip a Hook, a fishing game on Roblox.", tier=4),

    # ================= B mtfgams · TikTok
    'tk16_b1': rank("Four fish, ranked. Guess which one is the rarest.", 'COMMON *TO RAREST', [
        ("Number four: the Supernova Shark. One in a hundred.", 'nova2'),
        ("Number three: the Golden Shark. One in fifty thousand.", 'gshark'),
        ("Number two: the Cosmic Dragon. One in a hundred thousand.", 'dragon'),
        ("Number one: the Giant Blue Whale. One in five hundred thousand.", 'whale'),
    ], "Did you guess the whale? Skip a Hook, a fishing game on Roblox.", ('g_casts_lake', 2.0)),
    'dx11_b': dict(speed=0.85, amb='day', lines=[
        ("Day eleven: the open sea made my Roblox fishing game lag.", [S('s_rest_deep')], 'DAY 11 · *LAG'),
        ("So while you sail, the old world behind you now switches off.", [S('s_ship_sail')], '*OLD WORLD OFF'),
        ("In my Studio test, that took it from forty one to fifty eight frames per second.", [S('s_rest_galleon')], '41 → *58 FPS'),
        ("Not out yet. Should I fix lag first, or add more stuff? See you on day twelve!", [S('s_rest_deep', 2.5)], '')]),
    'tk16_b2': timecalc('whale', "One in five hundred thousand. That's the Giant Blue Whale.",
                        "Say you catch one fish every second, with no luck boosts.",
                        "It would take almost six days to get one. On average.",
                        "Six days nonstop. Would you do it? Skip a Hook, a fishing game on Roblox.", mid_clip=('g_casts_lake', 5.0), rhead='~6 *DAYS'),

    # ================= B mtfgams · YouTube
    'tk16_yb1': guess3("How rare is the Moonlotus Dragon? Guess first.",
                       "One in a million, one in a hundred million, or one in a billion?", '1M · *100M · 1B?', 'lotus_q',
                       "One in a hundred million. The rarest fish in the game.", 'lotus',
                       "How close were you? Skip a Hook, a fishing game on Roblox."),
    'dx11_yb': dict(speed=0.85, amb='night', lines=[
        ("Day eleven: I'm testing rough storms in my Roblox fishing game.", [S('s_storm_rain')], 'DAY 11 · *STORMS'),
        ("Huge waves crash over your ship.", [S('s_ship_storm'), S('s_waves_game')], '*HUGE WAVES'),
        ("Too much water, and your boat sinks. You wash up on a beach.", [S('s_finds_isle')], '*WASHED UP'),
        ("Still in testing. Would you sail into this storm? See you on day twelve!", [S('s_ship_storm', 2.5)], '')]),
    'tk16_yb2': sellkeep('dragon', ('cosmic_dragon_reveal', 3.1, {'max': 5.35}),
                         "You just caught the Cosmic Dragon. Sell it, or keep it?",
                         "Sell it, and you get the cash right now.",
                         "Keep it, and it earns cash in your aquarium. Even while you're offline.",
                         "Sell or keep? Tell me why. Skip a Hook, a fishing game on Roblox."),

    # ================= C Mtrix · TikTok
    'tk16_c1': trade(("Would you rather get a Golden Shark for sure...", 'gshark_hold'),
                     ("...or take a fifty fifty shot at the Prehistoric Megalodon?", 'meg'),
                     "The Golden Shark is one in fifty thousand. The Megalodon is twice as rare.",
                     "Play it safe, or flip the coin? Pick one below. Skip a Hook, a fishing game on Roblox.", '*FOR SURE...', 'OR *50/50?'),
    'dx11_c': dict(speed=0.85, amb='day', lines=[
        ("Day eleven: I'm testing ship upgrades for my Roblox fishing game.", [S('s_ship_harbor')], 'DAY 11 · *SHIPYARD'),
        ("You upgrade your ship. More speed,", [S('s_ship_sail')], '*SPEED'),
        ("and more room for the fish you catch.", [S('s_rest_galleon')], '*MORE ROOM'),
        ("Not out yet. Speed or room first? See you on day twelve!", [S('s_ship_harbor', 2.5)], '')]),
    'tk16_c2': rate('meg', 'meg', ('ancient_reveal', 2.4, {'max': 4.4}),
                    "Rate this catch from one to ten.",
                    "The Prehistoric Megalodon. One in a hundred thousand.",
                    "Look at the size of it.",
                    "What's your number? Skip a Hook, a fishing game on Roblox."),

    # ================= C Mtrix · Instagram (REEL)
    'tk16_ic1': rarer([
        ("The Supernova Shark is one in a hundred.", 'nova', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal1'}),
        ("Is the Cosmic Dragon rarer, or more common?", 'dragon_q', '*DRAGON?', False, {}),
        ("Rarer. One in a hundred thousand.", 'dragon', '*RARER', True, {'tier': 3, 'sfx': 'reveal3'}),
        ("Now the Cosmic Koi. Rarer, or more common than the dragon?", 'koi_b', '*COSMIC KOI?', False, {}),
        ("Way rarer. One in ten million.", 'koi', '*WAY RARER', True, {'tier': 4, 'sfx': 'record'}),
    ], "How many did you get? Skip a Hook, a fishing game on Roblox."),
    'dx11_ic': dict(speed=0.85, amb='day', lines=[
        ("Day eleven: I'm testing three ships for my Roblox fishing game.", [S('s_ships_bl')], 'DAY 11 · *3 SHIPS'),
        ("A small sloop,", [S('s_ship_sloop')], '*SLOOP'),
        ("a brigantine,", [S('s_ship_brig')], '*BRIGANTINE'),
        ("and a royal galleon.", [S('s_ship_galleon')], 'ROYAL *GALLEON'),
        ("Not out yet. Which one would you sail? See you on day twelve!", [S('s_rest_galleon')], '')]),
    'tk16_ic2': rank("Four fish, ranked. Number one is one in a hundred million.", 'RARE *TO RAREST', [
        ("Number four: the Supernova Shark. One in a hundred.", 'nova2'),
        ("Number three: the Prehistoric Megalodon. One in a hundred thousand.", 'meg'),
        ("Number two: the Cosmic Koi. One in ten million.", 'koi'),
        ("Number one: the Moonlotus Dragon. One in a hundred million.", 'lotus'),
    ], "Which one do you want most? Skip a Hook, a fishing game on Roblox.", ('g_casts_night', 2.0)),

    # ================= C Mtrix · YouTube
    'tk16_yc1': timecalc('dragon', "One in a hundred thousand. That's the Cosmic Dragon.",
                         "Say you catch one fish every second, with no luck boosts.",
                         "It would take about twenty eight hours. On average.",
                         "Could you stay awake that long? Skip a Hook, a fishing game on Roblox.", mid_clip=('g_casts_night', 6.0), rhead='~28 *HOURS'),
    'dx12_yc': dict(speed=0.85, amb='day', lines=[
        ("Day twelve: I'm testing boss fights for my Roblox fishing game.", [S('s_bossg_4')], 'DAY 12 · *BOSS FIGHTS'),
        ("Each sea serpent fights in three phases, and dives under the water.", [S('s_bossg_3'), S('s_bossg_1')], '*3 PHASES'),
        ("Before a big attack, you get a warning. Then you dodge.", [S('s_bossg_2')], '*DODGE'),
        ("Not out yet. Would you fight it? " + END13, [S('s_bossg_4', 2.5)], '')]),
    'tk16_yc2': sellkeep('koi', ('koi_hover', 0.45, {'max': 2.4}),
                         "You just caught the Cosmic Koi. Sell it, or keep it?",
                         "Sell it, and the cash is yours. Right now.",
                         "Keep it, and it earns cash in your aquarium. Even while you sleep.",
                         "Sell or keep? Comment why. Skip a Hook, a fishing game on Roblox."),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'tk16_m1': timecalc('koi', "One in ten million. That's the Cosmic Koi.",
                        "Say you catch one fish every second, with no luck boosts.",
                        "It would take about four months to get one. On average.",
                        "Four months for one fish. Worth it? Skip a Hook, a fishing game on Roblox.", mid_clip=('g_casts_dock', 4.0), rhead='~4 *MONTHS'),
    'cc12_m2': dict(prog=P5, speed=0.85, amb='day', lines=[
        ("Day twelve: my Roblox fishing game hit six players on average.", [('c23_lagoon_long', 2.0)], 'DAY 12 · *6 PLAYERS', {'prog': True}),
        ("In my tests, sea bosses showed up right next to the islands.", [S('s_studio_isles')], '*TOO CLOSE'),
        ("Now they rise out in open water, between the islands.", [S('s_bossg_2')], '*OPEN WATER'),
        ("Would you sail out there? " + END13, [S('s_bossg_1', 2.5)], '')]),
    'tk16_m2': trade(("Would you rather get a Prehistoric Megalodon for sure...", 'meg'),
                     ("...or take a one in a thousand shot at the Moonlotus Dragon?", 'lotus'),
                     "The Megalodon is one in a hundred thousand. The Moonlotus is a thousand times rarer.",
                     "Safe or risky? Tell me below. Skip a Hook, a fishing game on Roblox.", '*FOR SURE...', 'OR *1 IN 1,000?'),

    # ================= mtfgams12 · YouTube
    'tk16_n1': rate('dragon_q', 'dragon', ('cosmic_dragon_hold', 2.6, {'max': 4.6}),
                    "Rate this dragon from one to ten. Just on looks.",
                    "The Cosmic Dragon. One in a hundred thousand.",
                    "Here it is up close.",
                    "Be honest. What's your number? Skip a Hook, a fishing game on Roblox."),
    'dx12_n': dict(speed=0.85, amb='night', lines=[
        ("Day twelve: storms in my Roblox fishing game now fight back.", [S('s_ship_storm')], 'DAY 12 · *STORMS'),
        ("Fishing in a storm gives you more luck.", [S('s_storm_rain')], '*MORE LUCK'),
        ("But big waves break over your ship, and it can sink.", [S('s_waves_game'), S('s_ship_storm', 2.5)], '*IT CAN SINK'),
        ("Still testing. Would you risk it for more luck? " + END13, [S('s_storm_rain', 2.5)], '')]),
    'tk16_n2': rarer([
        ("The Cosmic Koi is one in ten million.", 'koi', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal3'}),
        ("Is the Giant Blue Whale rarer, or more common?", 'whale', '*BLUE WHALE?', False, {}),
        ("More common. One in five hundred thousand.", 'whale', '*MORE COMMON', True, {'sfx': 'miss'}),
        ("Now the Moonlotus Dragon. Rarer, or more common than the Koi?", 'lotus_q', '*MOONLOTUS?', False, {}),
        ("Rarer. One in a hundred million.", 'lotus', '*RARER', True, {'tier': 4, 'sfx': 'record'}),
    ], "How many did you get right? Skip a Hook, a fishing game on Roblox."),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('tk16_a1', '12:03'), ('cc12_tt', '17:33'), ('tk16_a2', '19:03')]),
    ('7181171', 'youtube', [('tk16_ya1', '12:03'), ('cc12_yt', '17:33'), ('tk16_ya2', '19:03')]),
    ('7752397', 'tiktok', [('tk16_b1', '12:09'), ('dx11_b', '16:09'), ('tk16_b2', '19:09')]),
    ('7752397', 'youtube', [('tk16_yb1', '12:09'), ('dx11_yb', '16:00'), ('tk16_yb2', '19:30')]),
    ('7773777', 'tiktok', [('tk16_c1', '12:15'), ('dx11_c', '16:15'), ('tk16_c2', '19:15')]),
    ('7773777', 'instagram', [('tk16_ic1', '12:15'), ('dx11_ic', '16:15'), ('tk16_ic2', '19:15')]),
    ('7773777', 'youtube', [('tk16_yc1', '12:15'), ('dx12_yc', '16:15'), ('tk16_yc2', '19:15')]),
    ('7752416', 'youtube', [('tk16_m1', '12:21'), ('cc12_m2', '16:21'), ('tk16_m2', '19:21')]),
    ('7773832', 'youtube', [('tk16_n1', '12:24'), ('dx12_n', '16:24'), ('tk16_n2', '19:24')]),
]
