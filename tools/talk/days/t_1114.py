# Tagesdatei 14.11.2026 – TALK-Format 2. Fassung (Regeln: keine lg_*-Clips, Fisch groß + klar, echte Chancen, Stop-Spiel 1,6 s je Fisch).
#   python3 tools/promo/talk/talk.py tools/promo/talk/days/t_1114.py all stills|render
# CCU (Dashboard 13.11. ~21:10 Berlin): Average 4 (Vortag 3, +24,0 %). Besuche 32,058 (über 32k), Favoriten 1,418, games-API updated 10.11.
# Neuigkeit: keine neuen Spiel-Commits seit 12.11. -> weitere echte Teile von Open Sea Phase 1 (git 12.11., docs/plans/WORLD2_SEA_PLAN.md):
#   Blender-Inseln mit Palmen/Felsen, neue Icons (Doubloon/Sonar/Laderaum/Kapitänsmütze), Freischaltung Rang 3 gratis + Welt-1-Boote zählen,
#   kein Doubloon-Kauf mit Robux (Owner-Entscheidung). PLAN (Phase 2, ehrlich "plan"): Boss Storm Leviathan ~1x/Stunde, ~1 % je Wurf;
#   Fish Frenzy alle 20 Min an einer Insel (doppelte Bisse); Freunde fahren mit und fangen selbst. Nichts davon ist live.
# Neue Formate 14.11.: groups nach Anfangsbuchstabe / Geburtstag-Datum / Element, guess mit Twist (Supernova nur 1 in 100).

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
    'tk14_a1': rather(("Would you rather catch the Golden Shark...", 'gshark'), ("...or the Prehistoric Megalodon?", 'meg'),
                      "The shark is one in fifty thousand. The megalodon is one in a hundred thousand.",
                      "Shark or megalodon? Comment it. Skip a Hook, on Roblox.", 'WOULD YOU *RATHER', '*OR...'),
    'cc10_tt': dict(prog=(3, 4, 1000), speed=0.85, amb='day', lines=[
        ("Day ten of trying to get one thousand players into my Roblox fishing game.", [('c04_docktolake_long1', 2.5)], 'DAY *10'),
        ("Today's average: four. Up from three yesterday.", [('c14_lake_long', 1.5)], '*4 PLAYERS', {'prog': True}),
        ("And we just passed thirty two thousand visits.", [('c03_baserow_long2', 3.0)], '*32,000 VISITS'),
        ("For the Open Sea, I'm planning a Fish Frenzy. Every twenty minutes, one island gets double bites.", [('c23_lagoon_long', 4.0), ('g_casts_dock', 6.0)], 'FISH *FRENZY'),
        ("Would you sail there for it? Comment it. See you on day eleven!", [('c04_docktolake_long1', 4.5)], '')]),
    'tk14_a2': groups("The first letter of your name decides your fish.", 'YOUR NAME = *YOUR FISH', [
        ("A to F: the Cosmic Dragon.", '*A - F', 'dragon'),
        ("G to L: the Giant Blue Whale.", '*G - L', 'whale'),
        ("M to R: the Supernova Shark.", '*M - R', 'nova2'),
        ("S to Z: the Cosmic Koi.", '*S - Z', 'koi'),
    ], "What's your letter? Comment it. Skip a Hook, on Roblox.", ('g_casts_dock', 8.0)),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'tk14_ya1': guess("Guess how rare this shark is. Comment your number first.", 'nova_q',
                      [("One in a million?", '1 IN *1,000,000?'), ("One in fifty thousand?", '1 IN *50,000?')],
                      "Nope. Only one in a hundred. The Supernova Shark.", 'nova',
                      "Did it fool you? Skip a Hook, on Roblox."),
    'cc10_yt': dict(prog=(3, 4, 1000), speed=0.85, amb='day', lines=[
        ("Day ten on my road to one thousand players.", [('c05_zonesfly_long1', 3.0)], 'DAY *10'),
        ("The average went back up, from three to four.", [('c22_endgate_long', 3.5)], '*4 PLAYERS', {'prog': True}),
        ("For the Open Sea, I modeled new cartoon islands in Blender. With palm trees and rocks.", [('c19_islands_long', 0.5), ('c23_lagoon_long', 6.0)], 'NEW *ISLANDS'),
        ("Later I want a frozen island and a volcano island.", [('c24_rift_long', 1.0)], 'ICE + *VOLCANO'),
        ("Which island would you visit first? Comment it. See you on day eleven!", [('c05_zonesfly_long1', 5.0)], '')]),
    'tk14_ya2': ladder([
        ("Like this Short, and the Golden Shark is yours. One in fifty thousand.", 'gshark', 'LIKE = *GOLDEN SHARK'),
        ("Subscribe, and you get the Cosmic Dragon.", 'dragon', 'SUB = *DRAGON'),
        ("Comment, and it's the Giant Blue Whale.", 'whale', 'COMMENT = *WHALE'),
        ("Share it, and the Cosmic Koi is yours.", 'koi', 'SHARE = *COSMIC KOI'),
        ("Do all four, and you get the Moonlotus Dragon. The rarest one.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Which one is yours? Skip a Hook, on Roblox.", labels=LAB_YT),

    # ================= B mtfgams · TikTok
    'tk14_b1': hilo([
        ("Higher or lower? The Golden Shark is one in fifty thousand.", 'gshark', 'HIGHER OR *LOWER?', True, {'sfx': 'reveal2'}),
        ("Is the Cosmic Dragon rarer? Comment higher or lower.", 'dragon_q', '*DRAGON?', False, {}),
        ("Higher! One in a hundred thousand.", 'dragon', '*HIGHER', True, {'tier': 3, 'sfx': 'reveal3'}),
        ("Now the Supernova Shark. Higher or lower?", 'nova_q', '*SUPERNOVA?', False, {}),
        ("Lower! Just one in a hundred.", 'nova', '*LOWER', True, {'sfx': 'miss'}),
    ], "Did you get both? Skip a Hook, on Roblox."),
    'dx9_b': dict(speed=0.85, amb='day', lines=[
        ("Day nine of updating my Roblox fishing game every day.", [('c14_lake_long', 5.5)], 'DAY *9'),
        ("The first Open Sea islands were just gray blocks.", [('c19_islands_long', 8.0)], 'GRAY *BLOCKS'),
        ("So I modeled real ones in Blender. Cartoon islands, palm trees and rocks.", [('c23_lagoon_long', 0.5), ('c19_islands_long', 4.5)], '*BLENDER'),
        ("They come with world two. It's not out yet.", [('c30_boat_short', 0.5)], 'NOT *OUT YET'),
        ("Palm trees, or spooky pines? Comment it. See you on day ten!", [('c14_lake_long', 9.0)], '')]),
    'tk14_b2': stop("Pause while the fish are changing. The one you stop on is yours.", 'PAUSE = *YOUR FISH',
                    ['dragon', 'goldfish', 'koi', 'meg', 'paddle', 'whale'],
                    "Rare, or the poor paddlefish? Comment it.", 'WHAT DID *YOU GET?',
                    "Skip a Hook, on Roblox.", first='koi'),

    # ================= B mtfgams · YouTube
    'tk14_yb1': dict(speed=0.88, amb='day', lines=[
        ("You just caught the Giant Blue Whale. Sell it, or keep it?", [shot('whale'), ('t_main_whale_splash', 0.4)], 'SELL OR *KEEP?', {'sfx': 'splash'}),
        ("Sell it, and you get a big pile of cash. Right now.", [('t_main_whale_splash', 1.6)], '*SELL', {'sfx': 'coins'}),
        ("Keep it, and it swims in your aquarium. And earns money, even while you sleep.", [('aqua_full_glass', 1.5)], '*KEEP'),
        ("Sell or keep? Comment it. Skip a Hook, on Roblox.", [shot('whale', False)], '')]),
    'dx9_yb': dict(speed=0.85, amb='day', lines=[
        ("Day nine of updating my Roblox game every day.", [('c24_rift_long', 0.5)], 'DAY *9'),
        ("Here's my plan for the Open Sea boss. The Storm Leviathan.", [('c24_rift_long', 5.0)], 'STORM *LEVIATHAN'),
        ("About once an hour, a storm circle shows up at sea. Every cast inside has about a one percent chance to hook it.", [('c30_boat', 5.0), ('c14_lake_long', 7.0)], '*1% CHANCE'),
        ("It's a plan for phase two. Not built yet.", [('c18_galleon_long', 6.0)], 'PHASE *2'),
        ("Would you fight it with friends? Comment it. See you on day ten!", [('c24_rift_long', 8.0)], '')]),
    'tk14_yb2': rather(("Would you rather catch the Cosmic Koi...", 'koi'), ("...or the Giant Blue Whale?", 'whale'),
                       "The koi is one in ten million. The whale is one in half a million.",
                       "Koi or whale? Comment it. Skip a Hook, on Roblox.", 'WOULD YOU *RATHER', '*OR...'),

    # ================= C Mtrix · TikTok
    'tk14_c1': groups("The day you were born decides your fish. Just the number.", 'BIRTHDAY = *YOUR FISH', [
        ("First to eighth: the Golden Shark.", '*1 - 8', 'gshark'),
        ("Ninth to sixteenth: the Prehistoric Megalodon.", '*9 - 16', 'meg'),
        ("Seventeenth to twenty-fourth: the Cosmic Dragon.", '*17 - 24', 'dragon'),
        ("Twenty-fifth to thirty-first: the Moonlotus Dragon.", '*25 - 31', 'lotus'),
    ], "Which one did you get? Comment it. Skip a Hook, on Roblox.", ('g_casts_perfect', 7.0)),
    'dx9_c': dict(speed=0.85, amb='day', lines=[
        ("Day nine of updating my Roblox fishing game every day.", [('c06_dock_long', 1.0)], 'DAY *9'),
        ("A fair rule for world two: you can't buy Doubloons with Robux.", [('c30_boat', 8.0)], 'NO *ROBUX', {'sfx': 'coins'}),
        ("You only earn them by selling fish you caught yourself.", [('g_casts_dock', 9.0)], 'EARN *THEM'),
        ("Fair, or too strict? Comment it. See you on day ten!", [('c06_dock_long', 7.5)], '')]),
    'tk14_c2': ladder([
        ("Like this video, and the Supernova Shark is yours.", 'nova2', 'LIKE = *SUPERNOVA'),
        ("Follow, and you get the Golden Shark.", 'gshark', 'FOLLOW = *GOLDEN SHARK'),
        ("Comment, and it's the Giant Blue Whale.", 'whale', 'COMMENT = *WHALE'),
        ("Share it, and you get the Cosmic Koi. One in ten million.", 'koi', 'SHARE = *COSMIC KOI'),
        ("Do all four, and the Moonlotus Dragon is yours.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Which fish did you get? Skip a Hook, on Roblox."),

    # ================= C Mtrix · Instagram (REEL)
    'tk14_ic1': hilo([
        ("Higher or lower? The Cosmic Koi is one in ten million.", 'koi', 'HIGHER OR *LOWER?', True, {'sfx': 'reveal3'}),
        ("Is the Cosmic Dragon rarer? Comment higher or lower.", 'dragon_q', '*DRAGON?', False, {}),
        ("Lower! One in a hundred thousand.", 'dragon', '*LOWER', True, {'sfx': 'miss'}),
        ("Now the Moonlotus Dragon. Higher or lower?", 'lotus_q', '*MOONLOTUS?', False, {}),
        ("Higher! One in a hundred million.", 'lotus', '*HIGHER', True, {'tier': 4, 'sfx': 'record'}),
    ], "How many did you get? Skip a Hook, on Roblox."),
    'dx9_ic': dict(speed=0.85, amb='day', lines=[
        ("Day nine of updating my Roblox game every day.", [('c23_lagoon_long', 5.0)], 'DAY *9'),
        ("World two needed its own icons.", [('c03_baserow_long1', 4.0)], 'NEW *ICONS'),
        ("So I made four: a Doubloon coin, a sonar, a cargo hold and a captain's hat.", [('c30_boat', 0.5), ('t_zones_boats', 1.0)], '*4 ICONS', {'sfx': 'ui_pop'}),
        ("Which one should get a shiny animation? Comment it. See you on day ten!", [('c23_lagoon_long', 9.0)], '')]),
    'tk14_ic2': guess("How rare is this dragon? Comment a guess first.", 'dragon_q',
                      [("One in a thousand?", '1 IN *1,000?'), ("One in a hundred million?", '1 IN *100,000,000?')],
                      "It's one in a hundred thousand. The Cosmic Dragon.", 'dragon',
                      "Were you close? Skip a Hook, on Roblox."),

    # ================= C Mtrix · YouTube
    'tk14_yc1': ladder([
        ("Like this, and the Supernova Shark is yours.", 'nova', 'LIKE = *SUPERNOVA'),
        ("Subscribe, and you get the Prehistoric Megalodon.", 'meg', 'SUB = *MEGALODON'),
        ("Comment, and it's the Giant Blue Whale.", 'whale', 'COMMENT = *WHALE'),
        ("Share it, and the Cosmic Koi is yours.", 'koi', 'SHARE = *COSMIC KOI'),
        ("Do all four, and you get the Moonlotus Dragon. One in a hundred million.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Tell me which one you got. Skip a Hook, on Roblox.", labels=LAB_YT),
    'dx10_yc': dict(speed=0.85, amb='day', lines=[
        ("Day ten of updating my Roblox fishing game every day.", [('c22_endgate_long', 0.5)], 'DAY *10'),
        ("When does the Open Sea unlock? At rank three. For free.", [('c05_zonesfly_long1', 4.0)], 'RANK *3'),
        ("And the boats you already own in world one? They count there too.", [('t_zones_boats', 0.3), ('c30_boat_short', 2.0)], 'YOUR *BOATS COUNT'),
        ("It's not out yet. I'm still testing it.", [('c18_galleon_long', 8.0)], '*TESTING'),
        ("What's your rank right now? Comment it. See you on day eleven!", [('c22_endgate_long', 7.0)], '')]),
    'tk14_yc2': groups("Your zodiac element decides your fish.", 'YOUR ELEMENT = *YOUR FISH', [
        ("Fire: the Supernova Shark.", '*FIRE', 'nova'),
        ("Water: the Giant Blue Whale.", '*WATER', 'whale'),
        ("Earth: the Prehistoric Megalodon.", '*EARTH', 'meg'),
        ("Air: the Moonlotus Dragon.", '*AIR', 'lotus'),
    ], "Which element are you? Comment it. Skip a Hook, on Roblox.", ('g_casts_dock', 5.0)),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'tk14_m1': stop("Stop the video on a fish, and it's yours.", 'STOP = *YOUR FISH',
                    ['meg', 'nova', 'whale', 'paddle', 'koi', 'dragon'],
                    "Shark, dragon, or paddlefish? Comment it.", 'WHAT DID *YOU GET?',
                    "Skip a Hook, on Roblox.", first='gshark'),
    'cc10_m2': dict(prog=(3, 4, 1000), speed=0.85, amb='day', lines=[
        ("Day ten of trying to reach one thousand players.", [('c13_pete_long', 0.5)], 'DAY *10'),
        ("Average today: four. Over thirty two thousand visits, and one thousand four hundred eighteen favorites.", [('c06_dock_long', 4.5)], '*4 PLAYERS', {'prog': True}),
        ("In the Open Sea, I want friends to ride in your boat and catch their own fish.", [('t_zones_boats', 0.2), ('c30_boat', 9.0)], 'RIDE *TOGETHER'),
        ("Who would you take with you? Comment it. See you on day eleven!", [('c13_pete_long', 5.0)], '')]),
    'tk14_m2': dict(speed=0.88, amb='night', lines=[
        ("Rate this catch from one to ten.", [shot('koi_b', False)], 'RATE IT *1-10'),
        ("The Cosmic Koi. One in ten million.", [shot('koi')], '*1 IN 10M', {'tier': 4, 'sfx': 'record'}),
        ("Look at those colors.", [('koi_hover', 1.0, {'max': 2.7})], 'THOSE *COLORS'),
        ("Be honest. What's your number? Skip a Hook, on Roblox.", [shot('koi_b', False)], '')]),

    # ================= mtfgams12 · YouTube
    'tk14_n1': ladder([
        ("Like this, and the Golden Shark is yours.", 'gshark', 'LIKE = *GOLDEN SHARK'),
        ("Subscribe, and you get the Supernova Shark.", 'nova2', 'SUB = *SUPERNOVA'),
        ("Comment, and it's the Prehistoric Megalodon.", 'meg', 'COMMENT = *MEGALODON'),
        ("Share it, and the Giant Blue Whale is yours.", 'whale', 'SHARE = *WHALE'),
        ("Do all four, and you get the Cosmic Koi. One in ten million.", 'koi', 'ALL 4 = *COSMIC KOI'),
    ], "Which one is yours? Skip a Hook, on Roblox.", labels=LAB_YT),
    'dx10_n': dict(speed=0.85, amb='day', lines=[
        ("Day ten of updating my Roblox game every day.", [('c14_lake_long', 0.5)], 'DAY *10'),
        ("Fishing alone at sea is boring. So here's my plan.", [('c30_boat', 7.0)], 'MY *PLAN'),
        ("Your friends sit in your boat, cast with you, and keep their own catches.", [('t_zones_boats', 0.2), ('c30_boat', 10.0)], 'BRING *FRIENDS'),
        ("The seats already work. Fishing from them comes next.", [('c30_boat_short', 2.5)], '*NEXT'),
        ("How many friends would you bring? Comment it. See you on day eleven!", [('c14_lake_long', 6.0)], '')]),
    'tk14_n2': dict(speed=0.88, amb='night', lines=[
        ("You caught the Prehistoric Megalodon. Do you sell it, or keep it?", [shot('meg')], 'SELL OR *KEEP?', {'sfx': 'reveal3'}),
        ("Sell it, and the cash is yours. Right away.", [('ancient_reveal', 3.0, {'max': 4.4})], '*SELL', {'sfx': 'coins'}),
        ("Keep it, and it earns money in your aquarium. Even when you're offline.", [('aqua_full_glass', 6.0)], '*KEEP'),
        ("Sell or keep? Comment it. Skip a Hook, on Roblox.", [shot('meg', False)], '')]),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('tk14_a1', '12:03'), ('cc10_tt', '17:33'), ('tk14_a2', '19:03')]),
    ('7181171', 'youtube', [('tk14_ya1', '12:03'), ('cc10_yt', '17:33'), ('tk14_ya2', '19:03')]),
    ('7752397', 'tiktok', [('tk14_b1', '12:09'), ('dx9_b', '16:09'), ('tk14_b2', '19:09')]),
    ('7752397', 'youtube', [('tk14_yb1', '12:09'), ('dx9_yb', '16:00'), ('tk14_yb2', '19:30')]),
    ('7773777', 'tiktok', [('tk14_c1', '12:15'), ('dx9_c', '16:15'), ('tk14_c2', '19:15')]),
    ('7773777', 'instagram', [('tk14_ic1', '12:15'), ('dx9_ic', '16:15'), ('tk14_ic2', '19:15')]),
    ('7773777', 'youtube', [('tk14_yc1', '12:15'), ('dx10_yc', '16:15'), ('tk14_yc2', '19:15')]),
    ('7752416', 'youtube', [('tk14_m1', '12:21'), ('cc10_m2', '16:21'), ('tk14_m2', '19:21')]),
    ('7773832', 'youtube', [('tk14_n1', '12:24'), ('dx10_n', '16:24'), ('tk14_n2', '19:24')]),
]
