# Tagesdatei 15.11.2026 – TALK-Format + LOGIK-Gate (tools/promo/LOGIK.md, logic_check.py, blinde Kritiker-Agenten).
#   python3 tools/promo/talk/talk.py tools/promo/talk/days/t_1115.py all stills|render
# CCU (Dashboard 14.11. ~23:00 UTC): Average 4 (+0,8 %, Vortag 4). Besuche 32,374, Favoriten 1,433. Spiel-Text bestätigt: Aquarium verdient auch offline.
# Neuigkeit (git 13.–14.11., alles nur in Studio / NICHT live, Spiel zuletzt 10.11. aktualisiert): Open Sea 2.0 – Segelschiffe Sloop/Brigantine/Royal Galleon
#   (am Rad stehen, Schiffs-Kamera, Fernrohr), Sturm/Blitz/Strudel (Sturm = mehr Glück + Sturm-Fische), 7 Inseln (Skull Rock, Vulkan, Eis, Sturm-Turm) mit
#   Leuchtturm-Schnellreise + Entdecken-Belohnung, Funde (Sandbänke, Wracks, Flaschenpost), Geisterschiff + Sea Giants, 4 See-Schlangen-Bosse (Cartoon-Stil der Fische),
#   Fix: Wrack-Schatz zahlte nie aus. Bilder = s_*-Clips (Ken Burns aus docs/ref/sea2_*.jpg, /home/claude/stills/mk.py), damit Bild = Wort.
# Formate nach Review 14.11.: keine Zufalls-Zuordnungen, keine Stop-Spiele, Like-Leiter nur 1x (C-YT, als Spass), Rarer-or-more-common statt Higher/Lower,
#   Would-you-rather nur mit Tausch, neu: "Wie lange würde es dauern?" (1 Fisch/Sekunde, Mathe = 1/Chance) und Rangliste selten -> am seltensten.

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

VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'tk15_a1': timecalc('lotus', "One in a hundred million. That's the Moonlotus Dragon.",
                        "Say you catch one fish every second, with no luck boosts.",
                        "It would take about three years to get one. On average.",
                        "How long have you been fishing? Skip a Hook, on Roblox.", rhead='~3 *YEARS'),
    'cc11_tt': dict(prog=P4, speed=0.85, amb='day', lines=[
        ("Day eleven: pirate ships for my Roblox fishing game. Players: still four.", [S('s_ship_galleon'), ('c14_lake_long', 1.0)], 'DAY 11 · *4 PLAYERS', {'prog': True}),
                ("A small sloop, a brigantine, and a royal galleon.", [S('s_ship_sloop'), S('s_ship_brig'), S('s_ship_galleon')], 'SLOOP · BRIG · *GALLEON'),
        ("I'm still testing them in Studio. They're not out yet.", [S('s_ship_storm')], 'STUDIO *TEST'),
        ("Which ship would you sail first? See you on day twelve!", [S('s_ship_galleon', 2.5)], '')]),
    'tk15_a2': sellkeep('gshark_hold', ('golden_shark_reveal', 0.1, {'max': 1.85}),
                        "Golden Shark. One in fifty thousand. Sell it, or keep it?",
                        "Sell it, and you get the cash right now.",
                        "Keep it, and it earns cash in your aquarium. Even while you're offline.",
                        "Sell or keep? Tell me why. Skip a Hook, on Roblox."),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'tk15_ya1': rank("Five fish, ranked. Number one is one in a hundred million.", 'RARE *TO RAREST', [
        ("Number five: the Supernova Shark. One in a hundred.", 'nova'),
        ("Number four: the Golden Shark. One in fifty thousand.", 'gshark'),
        ("Number three: the Giant Blue Whale. One in five hundred thousand.", 'whale'),
        ("Number two: the Cosmic Koi. One in ten million.", 'koi'),
        ("Number one: the Moonlotus Dragon. One in a hundred million.", 'lotus'),
    ], "Which one have you caught? Skip a Hook, on Roblox.", ('g_casts_perfect', 2.0)),
    'cc11_yt': dict(prog=P4, speed=0.85, amb='day', lines=[
        ("Day eleven on my road to one thousand players.", [('c06_dock_long', 1.0)], 'DAY *11'),
        ("One thousand four hundred thirty three people favorited my Roblox fishing game. But only four play at once.", [('c03_baserow_long2', 2.0)], '*1,433 FAVORITES', {'prog': True}),
        ("So I'm testing new islands. First, this skull rock,", [S('s_isle_skull')], 'SKULL *ROCK'),
        ("a volcano island, and a frozen one.", [S('s_isle_volcano'), S('s_isle_ice')], 'FIRE + *ICE'),
        ("Which island would you visit first? See you on day twelve!", [S('s_isle_light')], '')]),
    'tk15_ya2': guess3("How rare is this Prehistoric Megalodon? Guess before I tell you.",
                       "One in a thousand, one in a hundred thousand, or one in ten million?", '1K · *100K · 10M?', 'meg', 
                       "One in a hundred thousand. Did you get it?", 'meg',
                       "Comment your guess first. Skip a Hook, on Roblox."),

    # ================= B mtfgams · TikTok
    'tk15_b1': rarer([
        ("The Giant Blue Whale is one in five hundred thousand.", 'whale', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal2'}),
        ("Is the Cosmic Dragon rarer, or more common?", 'dragon_q', '*DRAGON?', False, {}),
        ("More common. One in a hundred thousand.", 'dragon', '*MORE COMMON', True, {'sfx': 'miss'}),
        ("Now the Moonlotus Dragon. Rarer, or more common than the whale?", 'lotus_q', '*MOONLOTUS?', False, {}),
        ("Way rarer. One in a hundred million.", 'lotus', '*WAY RARER', True, {'tier': 4, 'sfx': 'record'}),
    ], "How many did you get right? Skip a Hook, on Roblox."),
    'dx10_b': dict(speed=0.85, amb='day', lines=[
        ("Day ten: I'm testing storms in my Roblox fishing game.", [S('s_storm_rain')], 'DAY 10 · *STORMS'),
        ("Lightning, rain, and whirlpools out at sea.", [S('s_storm_bolt'), S('s_storm_whirl')], '*WHIRLPOOLS'),
        ("But fishing in a storm gives you more luck. And storm-only fish.", [S('s_storm_rain', 2.5)], '*MORE LUCK'),
        ("It's in testing, not out yet. Would you fish in the storm? See you on day eleven!", [S('s_ship_storm')], '')]),
    'tk15_b2': trade(("Would you rather get a Supernova Shark for sure...", 'nova'),
                     ("...or take a one percent shot at the Cosmic Koi?", 'koi'),
                     "The Supernova is one in a hundred. The Koi is one in ten million.",
                     "Safe shark, or risky Koi? Comment it. Skip a Hook, on Roblox.", '*FOR SURE...', 'OR *1% CHANCE?'),

    # ================= B mtfgams · YouTube
    'tk15_yb1': timecalc('koi', "One in ten million. That's the Cosmic Koi.",
                         "Say you catch one fish every second, with no luck boosts.",
                         "It would take about four months to get one. On average.",
                         "Would you grind that long? Skip a Hook, on Roblox.", mid_clip=('g_casts_perfect', 6.0), rhead='~4 *MONTHS'),
    'dx10_yb': dict(speed=0.85, amb='night', lines=[
        ("Day ten: I'm testing a ghost ship for my Roblox fishing game.", [S('s_ship_ghost')], 'DAY 10 · *GHOST SHIP'),
        ("It sails through the deep sea at night.", [S('s_ship_ghost', 2.5)], '*DEEP SEA'),
        ("And giant whales swim right past your boat.", [S('s_sea_giant')], 'SEA *GIANTS'),
        ("Still testing it in Studio. Ghost ship or whales? See you on day eleven!", [S('s_rest_deep')], '')]),
    'tk15_yb2': dict(speed=0.88, amb='night', lines=[
        ("Rate this dragon from one to ten. Just on looks.", [shot('dragon_q', False)], 'RATE IT *1-10'),
        ("The Cosmic Dragon. One in a hundred thousand.", [shot('dragon')], '*1 IN 100,000', {'tier': 3, 'sfx': 'reveal3'}),
        ("Here it is up close.", [('cosmic_dragon_hold', 2.6, {'max': 4.6})], '*UP CLOSE'),
        ("Be honest. What's your number? Skip a Hook, on Roblox.", [shot('dragon_q', False)], '')]),

    # ================= C Mtrix · TikTok
    'tk15_c1': guess3("How rare is the Giant Blue Whale?",
                      "One in five thousand, one in five hundred thousand, or one in fifty million?", '5K · *500K · 50M?', 'whale',
                      "One in five hundred thousand.", 'whale',
                      "Were you close? Skip a Hook, on Roblox."),
    'dx10_c': dict(speed=0.85, amb='day', lines=[
        ("Day ten: the sea in my Roblox game was empty. I'm filling it.", [S('s_rest_deep')], 'DAY *10'),
        ("Sandbanks with palm trees,", [S('s_finds_isle')], '*SANDBANKS'),
        ("old shipwrecks,", [S('s_finds_ship')], '*SHIPWRECKS'),
        ("and bottles with messages, floating in the water.", [S('s_finds_bottle')], '*BOTTLE MAIL'),
        ("Not out yet. What should be inside the bottle? See you on day eleven!", [S('s_finds_bottle', 2.5)], '')]),
    'tk15_c2': rank("One of these four fish is one in ten million. Which one?", 'COMMON *TO RAREST', [
        ("Number four: the Supernova Shark. One in a hundred.", 'nova2'),
        ("Number three: the Golden Shark. One in fifty thousand.", 'gshark'),
        ("Number two: the Giant Blue Whale. One in five hundred thousand.", 'whale'),
        ("Number one: the Cosmic Koi. One in ten million.", 'koi'),
    ], "Did you guess it? Skip a Hook, on Roblox.", ('g_casts_dock', 6.0)),

    # ================= C Mtrix · Instagram (REEL)
    'tk15_ic1': sellkeep('whale', ('t_main_whale_splash', 1.6),
                         "You just caught the Giant Blue Whale. Sell it, or keep it?",
                         "Sell it, and the cash is yours. Right now.",
                         "Keep it, and it earns cash in your aquarium. Even while you sleep.",
                         "Sell or keep? Comment why. Skip a Hook, on Roblox."),
    'dx10_ic': dict(speed=0.85, amb='day', lines=[
        ("Day ten: I'm testing sailing ships for my Roblox fishing game.", [S('s_rest_galleon')], 'DAY 10 · *SAILING'),
        ("You stand at the wheel, and the camera follows your ship.", [S('s_ship_sail')], 'AT THE *WHEEL'),
        ("With the spyglass, you can spot wrecks far away.", [S('s_spyglass')], '*SPYGLASS'),
        ("Still in testing. What would you name your ship? See you on day eleven!", [S('s_ship_harbor')], '')]),
    'tk15_ic2': timecalc('gshark', "One in fifty thousand. That's the Golden Shark.",
                         "Say you catch one fish every second, with no luck boosts.",
                         "It would take about fourteen hours. On average.",
                         "Could you stay up that long? Skip a Hook, on Roblox.", mid_clip=('g_casts_dock', 8.0), rhead='~14 *HOURS'),

    # ================= C Mtrix · YouTube
    'tk15_yc1': trade(("Would you rather get a Golden Shark for sure...", 'gshark'),
                      ("...or take a one in ten shot at the Giant Blue Whale?", 'whale'),
                      "The shark is one in fifty thousand. The whale is ten times rarer.",
                      "Safe shark, or risky whale? Comment it. Skip a Hook, on Roblox.", '*FOR SURE...', 'OR *1 IN 10?'),
    'dx11_yc': dict(speed=0.85, amb='day', lines=[
        ("Day eleven: I'm testing new islands for my Roblox fishing game.", [S('s_game_skull')], 'DAY 11 · *7 ISLANDS'),
        ("A skull rock, a volcano, and a frozen island.", [S('s_game_skull', 2.5), S('s_game_volcano'), S('s_game_ice')], 'SKULL · LAVA · *ICE'),
        ("Every island has a lighthouse. You can use it to travel back fast.", [S('s_studio_isles')], '*LIGHTHOUSES'),
        ("Not out yet. Which island would you explore first? See you on day twelve!", [S('s_game_volcano', 2.5)], '')]),
    'tk15_yc2': ladder([
        ("Just for fun. If likes gave fish, a like gets you the Supernova Shark.", 'nova', 'LIKE = *SUPERNOVA'),
        ("Subscribe: the Golden Shark.", 'gshark', 'SUB = *GOLDEN SHARK'),
        ("Comment: the Prehistoric Megalodon.", 'meg', 'COMMENT = *MEGALODON'),
        ("Share: the Giant Blue Whale.", 'whale', 'SHARE = *WHALE'),
        ("All four: the Moonlotus Dragon. One in a hundred million.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Which one would you pick? Skip a Hook, on Roblox.", labels=LAB_YT),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'tk15_m1': rarer([
        ("The Supernova Shark is one in a hundred.", 'nova2', 'RARER OR *MORE COMMON?', True, {'sfx': 'reveal1'}),
        ("Is the Golden Shark rarer, or more common?", 'gshark', '*GOLDEN SHARK?', False, {}),
        ("Rarer. One in fifty thousand.", 'gshark_hold', '*RARER', True, {'tier': 2, 'sfx': 'reveal2'}),
        ("Now the Cosmic Koi. Rarer, or more common than the Golden Shark?", 'koi_b', '*COSMIC KOI?', False, {}),
        ("Way rarer. One in ten million.", 'koi', '*WAY RARER', True, {'tier': 4, 'sfx': 'record'}),
    ], "How many did you get right? Skip a Hook, on Roblox."),
    'cc11_m2': dict(prog=P4, speed=0.85, amb='day', lines=[
        ("Day eleven: I found a bug in my Roblox fishing game.", [S('s_finds_ship')], 'DAY 11 · *A BUG'),
        ("Four players on average, and over thirty two thousand visits.", [('c14_lake_long', 4.0)], '*4 PLAYERS', {'prog': True}),
        ("You could find treasure at a shipwreck, but it never paid out.", [S('s_finds_ship', 2.5)], '*NO REWARD'),
        ("Fixed. Now it pays out. That comes with the next update.", [S('s_finds_chest')], '*FIXED'),
        ("What should a shipwreck treasure give you? See you on day twelve!", [S('s_finds_chest', 2.5)], '')]),
    'tk15_m2': sellkeep('meg', ('ancient_reveal', 3.0, {'max': 4.4}),
                        "You just caught the Prehistoric Megalodon. Sell it, or keep it?",
                        "Sell it, and you get the cash right away.",
                        "Keep it, and it earns cash in your aquarium. Even when you're offline.",
                        "Sell or keep? Tell me why. Skip a Hook, on Roblox."),

    # ================= mtfgams12 · YouTube
    'tk15_n1': guess3("How rare is the Cosmic Koi?",
                      "One in ten thousand, one in a million, or one in ten million?", '10K · 1M · *10M?', 'koi_b',
                      "One in ten million. That's how rare the Cosmic Koi is.", 'koi',
                      "Did you guess it? Skip a Hook, on Roblox."),
    'dx11_n': dict(speed=0.85, amb='day', lines=[
        ("Day eleven: I'm testing sea serpent bosses in my Roblox fishing game.", [S('s_bossg_1')], 'DAY 11 · *SEA BOSSES'),
        ("Reefback, and Bonejaw.", [S('s_bossg_1', 2.0), S('s_bossg_2')], 'REEFBACK · *BONEJAW'),
        ("Magma Maw, and the Storm Leviathan.", [S('s_bossg_3'), S('s_bossg_4')], 'MAGMA MAW · *LEVIATHAN'),
        ("They rise out of the sea and roar. Which one looks the scariest? See you on day twelve!", [S('s_bossg_3', 2.5)], '')]),
    'tk15_n2': timecalc('meg', "One in a hundred thousand. That's the Prehistoric Megalodon.",
                        "Say you catch one fish every second, with no luck boosts.",
                        "It would take about twenty eight hours. On average.",
                        "Would you grind that long for one? Skip a Hook, on Roblox.", mid_clip=('g_casts_perfect', 8.0), rhead='~28 *HOURS'),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('tk15_a1', '12:03'), ('cc11_tt', '17:33'), ('tk15_a2', '19:03')]),
    ('7181171', 'youtube', [('tk15_ya1', '12:03'), ('cc11_yt', '17:33'), ('tk15_ya2', '19:03')]),
    ('7752397', 'tiktok', [('tk15_b1', '12:09'), ('dx10_b', '16:09'), ('tk15_b2', '19:09')]),
    ('7752397', 'youtube', [('tk15_yb1', '12:09'), ('dx10_yb', '16:00'), ('tk15_yb2', '19:30')]),
    ('7773777', 'tiktok', [('tk15_c1', '12:15'), ('dx10_c', '16:15'), ('tk15_c2', '19:15')]),
    ('7773777', 'instagram', [('tk15_ic1', '12:15'), ('dx10_ic', '16:15'), ('tk15_ic2', '19:15')]),
    ('7773777', 'youtube', [('tk15_yc1', '12:15'), ('dx11_yc', '16:15'), ('tk15_yc2', '19:15')]),
    ('7752416', 'youtube', [('tk15_m1', '12:21'), ('cc11_m2', '16:21'), ('tk15_m2', '19:21')]),
    ('7773832', 'youtube', [('tk15_n1', '12:24'), ('dx11_n', '16:24'), ('tk15_n2', '19:24')]),
]
