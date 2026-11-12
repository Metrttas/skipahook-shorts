# Tagesdatei 13.11.2026 – TALK-Format 2. Fassung (Regeln siehe Kopf t_1112.py: keine lg_*-Clips, Fisch groß + klar, echte Chancen, Stop-Spiel
#   jetzt 1,6 s je Fisch). Neue Formate: Rarity raten (guess), Higher or Lower (hilo), Would you rather (rather), Lieblingsfarbe/Jahreszeit (groups).
#   python3 tools/promo/talk/talk.py tools/promo/talk/days/t_1113.py all stills|render
# CCU (Dashboard 12.11. ~21:00 Berlin): Average 3 (Vortag 4, -17,6 %). Besuche 31,831, Favoriten 1,405, games-API updated 10.11. (nichts Neues live).
# Neuigkeit (git 12.11.): Welt 2 = OPEN SEA (Discord-Abstimmung) Phase 1 GEBAUT + in Studio getestet, NICHT veröffentlicht: Inseln Sunny Harbor /
#   Coral Cove (Lv 3) / Driftwood Isle (Lv 10), eigenes Boot mit Laderaum, Händler -> Doubloons, Schwärme normal/glitzernd/golden + Sonar,
#   Events Lucky Pool + Shark Hunt, Captain-Level. -> "I built / I'm testing / coming", nie "live".

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


LAB_YT = ['LIKE', 'SUBSCRIBE', 'COMMENT', 'SHARE', 'ALL 4']

VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'tk13_a1': guess("Guess how rare this fish is. Comment your guess before I tell you.", 'koi_b',
                     [("One in a thousand?", '1 IN *1,000?'), ("One in a million?", '1 IN *1,000,000?')],
                     "It's one in ten million. The Cosmic Koi.", 'koi',
                     "How close was your guess? Skip a Hook, on Roblox."),
    'cc9_tt': dict(prog=(4, 3, 1000), speed=0.85, amb='day', lines=[
        ("Day nine of trying to get one thousand players into my Roblox fishing game.", [('c06_dock_long', 3.0)], 'DAY *9'),
        ("Today's average: three. Yesterday it was four.", [('c04_docktolake_long1', 1.0)], '*3 PLAYERS', {'prog': True}),
        ("So I'm building something big. You voted for it on Discord: the Open Sea.", [('c30_boat', 2.0)], 'OPEN *SEA'),
        ("Your own boat, islands to explore, and fish you have to hunt.", [('c30_boat', 7.0), ('c19_islands_long', 3.0)], '*YOUR BOAT'),
        ("Would that make you play? Tell me in the comments. See you on day ten!", [('c06_dock_long', 7.0)], '')]),
    'tk13_a2': ladder([
        ("Like this video, and you get a Golden Shark. One in fifty thousand.", 'gshark', 'LIKE = *GOLDEN SHARK'),
        ("Follow, and it's the Prehistoric Megalodon.", 'meg', 'FOLLOW = *MEGALODON'),
        ("Comment, and the Giant Blue Whale is yours.", 'whale', 'COMMENT = *WHALE'),
        ("Share it, and you get the Cosmic Koi. One in ten million.", 'koi', 'SHARE = *COSMIC KOI'),
        ("Do all four, and you get the Moonlotus Dragon. One in a hundred million.", 'lotus', 'ALL 4 = *RAREST'),
    ], "What did you get? Skip a Hook, on Roblox."),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'tk13_ya1': stop("Pause the video while the fish change. Whatever you stop on is yours.", 'PAUSE = *YOUR FISH',
                     ['whale', 'paddle', 'dragon', 'koi', 'goldfish', 'gshark'],
                     "Which one did you land on? Comment it.", 'WHAT DID *YOU GET?',
                     "Skip a Hook, on Roblox.", first='koi'),
    'cc9_yt': dict(prog=(4, 3, 1000), speed=0.85, amb='day', lines=[
        ("Day nine on my road to one thousand players.", [('c22_endgate_long', 2.0)], 'DAY *9'),
        ("The average dropped from four to three. But we're almost at thirty two thousand visits.", [('c19_islands_long', 2.0)], '*3 PLAYERS', {'prog': True}),
        ("Today I tested the Open Sea for the first time. Three islands: Sunny Harbor, Coral Cove and Driftwood Isle.", [('c19_islands_long', 6.0), ('c23_lagoon_long', 2.0)], '*3 ISLANDS'),
        ("You sell your fish at a merchant, and you get a new coin: Doubloons.", [('c30_boat', 4.0)], '*DOUBLOONS', {'sfx': 'coins'}),
        ("What should the fourth island be? Comment it. See you on day ten!", [('c22_endgate_long', 6.0)], '')]),
    'tk13_ya2': hilo([
        ("Higher or lower? The Golden Shark is one in fifty thousand.", 'gshark', 'HIGHER OR *LOWER?', True, {'sfx': 'reveal2'}),
        ("Is the Supernova Shark rarer? Comment higher or lower.", 'nova_q', '*SUPERNOVA?', False, {}),
        ("Lower! It's only one in a hundred.", 'nova', '*LOWER', True, {'sfx': 'miss'}),
        ("Now the Cosmic Koi. Higher or lower?", 'koi_b', '*COSMIC KOI?', False, {}),
        ("Higher! One in ten million.", 'koi', '*HIGHER', True, {'tier': 4, 'sfx': 'record'}),
    ], "How many did you get right? Skip a Hook, on Roblox."),

    # ================= B mtfgams · TikTok
    'tk13_b1': stop("Screenshot while the fish are changing. The fish on your screenshot is yours.", '*SCREENSHOT IT',
                    ['gshark', 'goldfish', 'whale', 'nova', 'lotus', 'paddle'],
                    "Show me your screenshot in the comments.", 'SHOW *ME',
                    "Skip a Hook, on Roblox.", first='gshark'),
    'dx8_b': dict(speed=0.85, amb='day', lines=[
        ("Day eight of updating my Roblox fishing game every day.", [('c06_dock_long', 5.0)], 'DAY *8'),
        ("World two gets its own money. Doubloons.", [('c30_boat', 3.0)], '*DOUBLOONS', {'sfx': 'coins'}),
        ("You only get them by selling fish in the Open Sea. So everyone starts fresh there.", [('c19_islands_long', 4.0), ('c30_boat_short', 1.0)], 'EVERYONE *STARTS FRESH'),
        ("I built it this week. It comes when world two opens.", [('c18_galleon_long', 2.0)], '*COMING SOON'),
        ("Fair, or should your old money count? Comment it. See you on day nine!", [('c06_dock_long', 8.0)], '')]),
    'tk13_b2': rather(("Would you rather catch the Giant Blue Whale...", 'whale'), ("...or the Cosmic Dragon?", 'dragon'),
                      "The whale is one in half a million. The dragon is one in a hundred thousand.",
                      "Whale or dragon? Comment it. Skip a Hook, on Roblox.", 'WOULD YOU *RATHER', '*OR...'),

    # ================= B mtfgams · YouTube
    'tk13_yb1': ladder([
        ("Like this Short, and the Supernova Shark is yours.", 'nova', 'LIKE = *SUPERNOVA'),
        ("Subscribe, and you get the Cosmic Dragon.", 'dragon', 'SUB = *DRAGON'),
        ("Comment, and it's the Giant Blue Whale. One in half a million.", 'whale', 'COMMENT = *WHALE'),
        ("Share it, and the Cosmic Koi is yours.", 'koi', 'SHARE = *COSMIC KOI'),
        ("Do all four, and you get the rarest fish in my game. The Moonlotus Dragon.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Which one did you get? Skip a Hook, on Roblox.", labels=LAB_YT),
    'dx8_yb': dict(speed=0.85, amb='day', lines=[
        ("Day eight of updating my Roblox game every day.", [('c30_boat_short', 0.5)], 'DAY *8'),
        ("In the Open Sea, your boat has a cargo hold.", [('c30_boat', 2.0)], 'CARGO *HOLD'),
        ("When it's full, you sail back to a merchant and sell. Bigger boats carry more fish.", [('c30_boat', 6.0), ('c18_galleon_long', 5.0)], 'BIGGER BOAT = *MORE FISH'),
        ("Fast boat, or big boat? Comment it. See you on day nine!", [('c30_boat_short', 2.0)], '')]),
    'tk13_yb2': groups("The season you were born in decides your fish.", 'BIRTH SEASON = *YOUR FISH', [
        ("Spring: the Golden Shark.", '*SPRING', 'gshark'),
        ("Summer: the Supernova Shark.", '*SUMMER', 'nova'),
        ("Autumn: the Cosmic Dragon.", '*AUTUMN', 'dragon'),
        ("Winter: the Giant Blue Whale.", '*WINTER', 'whale'),
    ], "Which season are you? Comment it. Skip a Hook, on Roblox.", ('g_casts_dock', 2.0)),

    # ================= C Mtrix · TikTok
    'tk13_c1': ladder([
        ("Like this video, and this Supernova Shark is yours.", 'nova', 'LIKE = *YOUR FISH'),
        ("Follow, and you get a Golden Shark.", 'gshark', 'FOLLOW = *GOLDEN SHARK'),
        ("Comment, and it's the Prehistoric Megalodon. One in a hundred thousand.", 'meg', 'COMMENT = *MEGALODON'),
        ("Share it, and the Cosmic Koi is yours. One in ten million.", 'koi', 'SHARE = *COSMIC KOI'),
        ("Do all four, and the Moonlotus Dragon is yours. One in a hundred million.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Tell me which fish you got. Skip a Hook, on Roblox."),
    'dx8_c': dict(speed=0.85, amb='day', lines=[
        ("Day eight of updating my Roblox fishing game every day.", [('c14_lake_long', 2.0)], 'DAY *8'),
        ("In the Open Sea, fish swim in schools.", [('c14_lake_long', 6.0)], 'FISH *SCHOOLS'),
        ("So I added a sonar. It shows schools, islands and events near your boat.", [('c30_boat', 3.0), ('c19_islands_long', 5.0)], '*SONAR'),
        ("Find a golden school, and you can catch gold fish.", [('g_hud_golden_shark', 0.8, {'max': 1.95})], 'GOLDEN *SCHOOL'),
        ("Would you hunt for a golden school? Comment it. See you on day nine!", [('c14_lake_long', 8.0)], '')]),
    'tk13_c2': guess("How rare do you think this fish is? Comment a number first.", 'lotus_q',
                     [("One in a hundred thousand?", '1 IN *100,000?'), ("One in ten million?", '1 IN *10,000,000?')],
                     "It's one in a hundred million. The Moonlotus Dragon.", 'lotus',
                     "Did anyone guess that? Skip a Hook, on Roblox."),

    # ================= C Mtrix · Instagram (REEL)
    'tk13_ic1': dict(speed=0.88, amb='night', lines=[
        ("You just caught a Cosmic Dragon. Do you sell it, or keep it?", [shot('dragon'), ('cosmic_dragon_hold', 1.4, {'max': 2.5})], 'SELL OR *KEEP?', {'sfx': 'reveal3'}),
        ("Sell it, and you get the cash right now.", [('cosmic_dragon_hold', 1.5, {'max': 2.5})], '*SELL', {'sfx': 'coins'}),
        ("Keep it, and it swims in your aquarium and earns money, even when you're offline.", [('aqua_full_glass', 5.0)], '*KEEP'),
        ("Comment sell or keep. Skip a Hook, on Roblox.", [shot('dragon', False)], '')]),
    'dx8_ic': dict(speed=0.85, amb='day', lines=[
        ("Day eight of updating my Roblox game every day.", [('c23_lagoon_long', 2.0)], 'DAY *8'),
        ("I asked on Discord what world two should be.", [('c03_baserow_long1', 2.0)], 'YOU *VOTED'),
        ("Your answer: sail your own boat and hunt fish.", [('c30_boat', 5.0)], 'YOUR *OWN BOAT'),
        ("So that's what I'm building now. The Open Sea.", [('c19_islands_long', 7.0)], 'OPEN *SEA'),
        ("What should I add first? Comment it. See you on day nine!", [('c23_lagoon_long', 8.0)], '')]),
    'tk13_ic2': groups("Your favorite color decides your fish.", 'YOUR COLOR = *YOUR FISH', [
        ("Orange: the Supernova Shark.", '*ORANGE', 'nova'),
        ("Yellow: the Golden Shark.", '*YELLOW', 'gshark'),
        ("Purple: the Cosmic Dragon.", '*PURPLE', 'dragon'),
        ("Blue: the Giant Blue Whale.", '*BLUE', 'whale'),
    ], "What's your color? Comment it. Skip a Hook, on Roblox.", ('g_casts_perfect', 4.0)),

    # ================= C Mtrix · YouTube
    'tk13_yc1': stop("Stop the video on a fish. That's your catch.", 'STOP = *YOUR CATCH',
                     ['nova', 'koi', 'paddle', 'meg', 'whale', 'goldfish'],
                     "Lucky, or the poor paddlefish? Comment what you got.", 'WHAT DID *YOU GET?',
                     "Skip a Hook, on Roblox."),
    'dx9_yc': dict(speed=0.85, amb='day', lines=[
        ("Day nine of updating my Roblox fishing game every day.", [('c05_zonesfly_long1', 3.0)], 'DAY *9'),
        ("In the Open Sea, fish don't bite everywhere.", [('c14_lake_long', 3.0)], 'NOT *EVERYWHERE'),
        ("You drive your boat to a school of fish. Normal, sparkling, or golden.", [('c30_boat', 2.0), ('g_hud_golden_shark', 0.8, {'max': 1.95})], '*3 SCHOOLS'),
        ("The rarer the school, the better the fish.", [('c19_islands_long', 4.0)], 'RARER *SCHOOL'),
        ("Would you chase a golden school? Comment it. See you on day ten!", [('c05_zonesfly_long1', 7.0)], '')]),
    'tk13_yc2': dict(speed=0.88, amb='day', lines=[
        ("Rate this catch from one to ten.", [shot('whale', False)], 'RATE IT *1-10'),
        ("The Giant Blue Whale. One in half a million.", [shot('whale')], '*1 IN 500K', {'tier': 4, 'sfx': 'splash'}),
        ("It jumped right out of the water, next to my dock.", [('t_main_whale_splash', 1.2)], 'NEXT TO *MY DOCK'),
        ("Be honest. What's your number? Skip a Hook, on Roblox.", [shot('whale', False)], '')]),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'tk13_m1': hilo([
        ("Higher or lower? The Giant Blue Whale is one in half a million.", 'whale', 'HIGHER OR *LOWER?', True, {'sfx': 'splash'}),
        ("Is the Cosmic Dragon rarer? Comment higher or lower.", 'dragon_q', '*DRAGON?', False, {}),
        ("Lower! One in a hundred thousand.", 'dragon', '*LOWER', True, {'sfx': 'miss'}),
        ("Now the Moonlotus Dragon. Higher or lower?", 'lotus_q', '*MOONLOTUS?', False, {}),
        ("Higher! One in a hundred million.", 'lotus', '*HIGHER', True, {'tier': 4, 'sfx': 'record'}),
    ], "How many did you get right? Skip a Hook, on Roblox."),
    'cc9_m2': dict(prog=(4, 3, 1000), speed=0.85, amb='day', lines=[
        ("Day nine of trying to reach one thousand players.", [('c13_pete_long', 3.0)], 'DAY *9'),
        ("Average today: three. And one thousand four hundred favorites.", [('c03_baserow_long2', 2.0)], '*3 PLAYERS', {'prog': True}),
        ("Next, boats you can drive across a whole sea. From a free rowboat, up to a speedboat.", [('c30_boat', 1.0), ('c30_boat_short', 2.0)], 'YOUR *BOAT'),
        ("Which boat would you buy first? Comment it. See you on day ten!", [('c13_pete_long', 7.0)], '')]),
    'tk13_m2': ladder([
        ("Like this, and the Golden Shark is yours.", 'gshark', 'LIKE = *GOLDEN SHARK'),
        ("Subscribe, and you get the Cosmic Dragon.", 'dragon', 'SUB = *DRAGON'),
        ("Comment, and it's the Giant Blue Whale.", 'whale', 'COMMENT = *WHALE'),
        ("Share it, and the Cosmic Koi is yours. One in ten million.", 'koi', 'SHARE = *COSMIC KOI'),
        ("Do all four, and you get the Moonlotus Dragon. One in a hundred million.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Which one is yours? Skip a Hook, on Roblox.", labels=LAB_YT),

    # ================= mtfgams12 · YouTube
    'tk13_n1': rather(("Would you rather catch the Cosmic Koi...", 'koi'), ("...or the Moonlotus Dragon?", 'lotus'),
                      "The koi is one in ten million. The dragon is one in a hundred million.",
                      "Koi or dragon? Comment it. Skip a Hook, on Roblox.", 'WOULD YOU *RATHER', '*OR...'),
    'dx9_n': dict(speed=0.85, amb='day', lines=[
        ("Day nine of updating my Roblox game every day.", [('c14_lake_long', 4.0)], 'DAY *9'),
        ("In the Open Sea, every catch gives you captain XP.", [('c30_boat', 3.0)], 'CAPTAIN *XP'),
        ("A higher level unlocks new islands, like Coral Cove and Driftwood Isle.", [('c19_islands_long', 2.0), ('c23_lagoon_long', 4.0)], 'NEW *ISLANDS'),
        ("And there are events at sea: a Lucky Pool, and a Shark Hunt.", [('c24_rift_long', 3.0)], '*SHARK HUNT'),
        ("Which event do you want first? Comment it. See you on day ten!", [('c14_lake_long', 8.0)], '')]),
    'tk13_n2': guess("Guess how rare this fish is. Comment before I say it.", 'whale',
                     [("One in ten thousand?", '1 IN *10,000?'), ("One in a hundred thousand?", '1 IN *100,000?')],
                     "It's one in half a million. The Giant Blue Whale.", 'whale',
                     "Did you get it? Skip a Hook, on Roblox."),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('tk13_a1', '12:03'), ('cc9_tt', '17:33'), ('tk13_a2', '19:03')]),
    ('7181171', 'youtube', [('tk13_ya1', '12:03'), ('cc9_yt', '17:33'), ('tk13_ya2', '19:03')]),
    ('7752397', 'tiktok', [('tk13_b1', '12:09'), ('dx8_b', '16:09'), ('tk13_b2', '19:09')]),
    ('7752397', 'youtube', [('tk13_yb1', '12:09'), ('dx8_yb', '16:00'), ('tk13_yb2', '19:30')]),
    ('7773777', 'tiktok', [('tk13_c1', '12:15'), ('dx8_c', '16:15'), ('tk13_c2', '19:15')]),
    ('7773777', 'instagram', [('tk13_ic1', '12:15'), ('dx8_ic', '16:15'), ('tk13_ic2', '19:15')]),
    ('7773777', 'youtube', [('tk13_yc1', '12:15'), ('dx9_yc', '16:15'), ('tk13_yc2', '19:15')]),
    ('7752416', 'youtube', [('tk13_m1', '12:21'), ('cc9_m2', '16:21'), ('tk13_m2', '19:21')]),
    ('7773832', 'youtube', [('tk13_n1', '12:24'), ('dx9_n', '16:24'), ('tk13_n2', '19:24')]),
]
