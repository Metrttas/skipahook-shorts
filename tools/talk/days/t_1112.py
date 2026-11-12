# Tagesdatei 12.11.2026 – TALK-Format, 2. Fassung (User 12.11. ~05:00: "Skripte machen manchmal keinen Sinn, denk nach … Stop-Spiel: Fische
#   viel zu schnell, keiner reagiert so schnell … Like/Follow-Leiter ok … Legenden-Clips NICHT benutzen, da ist ein Pop-up, man sieht den Fisch nicht").
#   python3 tools/promo/talk/talk.py tools/promo/talk/days/t_1112.py all stills|render
# Regeln dieser Fassung:
#   - KEINE lg_*-Clips (LEGEND-CAUGHT-Karte verdeckt den Fisch). Nur Momente, in denen der Fisch groß und klar zu sehen ist (Tabelle F, mit 'max' =
#     Ende des sauberen Fensters, danach Blitz/Karte).
#   - Fisch-Schild zeigt die ECHTEN Chancen aus dem Spiel (Kontaktbogen 12.11.): Supernova Shark 1 in 100, Golden Shark 1 in 50,000,
#     Prehistoric Megalodon 1 in 100,000, Cosmic Dragon 1 in 100,000, Giant Blue Whale 1 in 500,000, Cosmic Koi 1 in 10,000,000,
#     Moonlotus Dragon 1 in 100,000,000. Leiter steigt immer in der Seltenheit (logisch: mehr tun = besserer Fisch).
#   - Stop-Spiel: jeder Fisch 1,3 s mit Namens-Schild ('hold' verlängert die Stille nach "Go!").
#   - "Geburtsmonat": 4 Gruppen à 3 Monate statt 12 Monate (es gibt keine 12 verschiedenen sauberen Fisch-Clips).
# Serien: CCU Day 8 (Average 4, gestern 2, Besuche 31,647) + Day-X 7/8. dx7_b, dx7_ic, dx8_n aus Fassung 1 unverändert (keine Legenden-Clips).

F = {
    'nova': ('far_supernova', 5.0, 'SUPERNOVA SHARK', '1 IN 100', 7.6),
    'nova2': ('far2_supernova', 4.2, 'SUPERNOVA SHARK', '1 IN 100', 5.9),
    'gshark': ('golden_shark_reveal', 0.1, 'GOLDEN SHARK', '1 IN 50,000', 1.9),
    'gshark_hold': ('golden_shark_reveal', 2.95, 'GOLDEN SHARK', '1 IN 50,000', 4.15),
    'meg': ('ancient_reveal', 0.7, 'PREHISTORIC MEGALODON', '1 IN 100,000', 3.3),
    'dragon': ('cosmic_dragon_reveal', 3.1, 'COSMIC DRAGON', '1 IN 100,000', 5.35),
    'whale': ('t_main_whale_jump', 0.3, 'GIANT BLUE WHALE', '1 IN 500,000', 1.98),
    'koi': ('koi2_splash_hover', 4.6, 'COSMIC KOI', '1 IN 10,000,000', 6.7),
    'koi_b': ('koi_hover', 0.45, 'COSMIC KOI', '1 IN 10,000,000', 2.7),
    'lotus': ('g_ethereal_moonlotus', 0.45, 'MOONLOTUS DRAGON', '1 IN 100,000,000', 2.65),
    'goldfish': ('g_mutation_goldfish', 3.9, 'GOLDFISH', 'GOLD MUTATION', 5.6),
    'paddle': ('g_paddlefish_card', 4.2, 'PADDLEFISH', 'COMMON', 5.5),
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
        ("Ready? Go!", [shot(k) for k in order], 'PAUSE *NOW!', {'flick': True, 'hold': 1.3 * len(order) - 0.6}),
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


VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'tk_a1': ladder([
        ("Like this video, and this Supernova Shark is yours.", 'nova', 'LIKE = *YOUR FISH'),
        ("Follow, and you get a Golden Shark. One in fifty thousand.", 'gshark', 'FOLLOW = *BETTER'),
        ("Comment, and it's a Cosmic Dragon. One in a hundred thousand.", 'dragon', 'COMMENT = *DRAGON'),
        ("Share it, and the Giant Blue Whale is yours. One in half a million.", 'whale', 'SHARE = *WHALE'),
        ("Do all four, and you get the rarest fish in my game. The Moonlotus Dragon. One in a hundred million.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Which one did you get? Skip a Hook, on Roblox."),
    'cc8_tt': dict(prog=(2, 4, 1000), speed=0.85, amb='day', lines=[
        ("Day eight of trying to get one thousand players into my Roblox fishing game.", [('c06_dock_long', 2.0)], 'DAY *8'),
        ("Yesterday, the average was two players. Today, it's four.", [('c04_docktolake_long1', 0.5)], '*4 PLAYERS', {'prog': True}),
        ("The new legends update is out. Every thirty minutes, a giant legend shows up in the lake.", [('c14_lake_long', 1.0), ('c27_longcast1', 1.0)], 'LEGENDS *ARE OUT', {'sfx': 'bite'}),
        ("Help me get to one thousand. Play one round, and tell me what you caught. See you on day nine!", [('c06_dock_long', 6.0)], '')]),
    'tk_a2': stop("Pause the video while the fish are changing. The one you stop on is yours.", 'PAUSE = *YOUR FISH',
                  ['gshark', 'paddle', 'whale', 'nova', 'dragon', 'goldfish', 'koi'],
                  "Which one did you get? Tell me in the comments.", 'WHAT DID *YOU GET?',
                  "Skip a Hook, on Roblox."),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'tk_ya1': groups("Your birth month decides your fish in my Roblox game.", 'BIRTH MONTH = *YOUR FISH', [
        ("January, February, March: the Golden Shark.", '*JAN - MAR', 'gshark'),
        ("April, May, June: the Cosmic Dragon.", '*APR - JUN', 'dragon'),
        ("July, August, September: the Giant Blue Whale.", '*JUL - SEP', 'whale'),
        ("October, November, December: the Cosmic Koi. One in ten million.", '*OCT - DEC', 'koi'),
    ], "Which month are you? Comment it. Skip a Hook, on Roblox."),
    'cc8_yt': dict(prog=(2, 4, 1000), speed=0.85, amb='day', lines=[
        ("Day eight on my road to one thousand players.", [('c22_endgate_long', 1.0)], 'DAY *8'),
        ("The average went up from two to four.", [('c19_islands_long', 2.0)], '*4 PLAYERS', {'prog': True}),
        ("Legends are live now. Four giant fish, each in its own zone.", [('c15_temple_long', 2.0), ('c19_islands_long', 6.0)], 'LEGENDS *ARE LIVE'),
        ("Next is world two. You voted on Discord: the Open Sea. Your own boat, and fish you hunt.", [('c30_boat', 3.0), ('c18_galleon_long', 3.0)], 'OPEN *SEA'),
        ("What should be on the first island? Comment it. See you on day nine!", [('c22_endgate_long', 6.0)], '')]),
    'tk_ya2': pick("Pick a number. One, two, or three.", 'PICK *1, 2 OR 3',
                   "Comment it before you see them. No cheating.", 'NO *CHEATING', [
                       ("One: the Cosmic Dragon.", 'dragon', False),
                       ("Two: a Paddlefish. Ouch.", 'paddle', True),
                       ("Three: the Giant Blue Whale.", 'whale', False),
                   ], "So, what did you get? Skip a Hook, on Roblox.", ('g_casts_dock', 1.0)),

    # ================= B mtfgams · TikTok
    'tk_b1': pick("Quick. Pick one, two, or three.", 'PICK *1, 2 OR 3',
                  "Type your number in the comments before you scroll.", 'COMMENT *FIRST', [
                      ("One: a Goldfish. Not bad.", 'goldfish', True),
                      ("Two: the Supernova Shark.", 'nova2', False),
                      ("Three: the Prehistoric Megalodon. One in a hundred thousand.", 'meg', False),
                  ], "Happy with your number? Skip a Hook, on Roblox.", ('g_casts_perfect', 1.0)),
    'tk_b2': ladder([
        ("Every button you press on this video gets you a fish. Like: the Golden Shark.", 'gshark', 'LIKE = *GOLDEN SHARK'),
        ("Follow: the Prehistoric Megalodon.", 'meg', 'FOLLOW = *MEGALODON'),
        ("Comment: the Giant Blue Whale.", 'whale', 'COMMENT = *WHALE'),
        ("Share: the Cosmic Koi. One in ten million.", 'koi', 'SHARE = *COSMIC KOI'),
        ("All four? The Moonlotus Dragon. One in a hundred million.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Count your buttons and tell me your fish. Skip a Hook, on Roblox."),

    # ================= B mtfgams · YouTube
    'tk_yb1': stop("Tap to pause while the fish change. Whatever you land on is your catch.", 'TAP = *YOUR CATCH',
                   ['whale', 'goldfish', 'nova', 'koi', 'paddle', 'gshark', 'meg'],
                   "Missed it? Watch again. Then comment what you got.", 'TRY *AGAIN',
                   "Skip a Hook, on Roblox."),
    'dx7_yb': dict(speed=0.85, amb='day', lines=[
        ("Day seven of updating my Roblox game every day.", [('c28_reel', 0.5)], 'DAY *7'),
        ("The old reel fight felt dead. You could just spam.", [('c26_cast_catch', 4.0)], 'NO MORE *SPAM'),
        ("So I rebuilt it. A pointer circles the reel, and you tap when it's in the gold zone.", [('c28_reel', 3.5), ('c26_cast_catch', 6.0)], '*GOLD ZONE', {'sfx': 'reel'}),
        ("Every hit makes it faster. Tap too early, and it's a miss.", [('c29_holdup', 1.0)], 'FASTER *EVERY HIT'),
        ("Too hard, or just right? Comment it. See you on day eight!", [('c28_reel', 4.5)], '')]),
    'tk_yb2': dict(speed=0.88, amb='night', lines=[
        ("Rate this catch from one to ten.", [('koi2_splash_hover', 0.2, {'max': 1.6})], 'RATE IT *1-10'),
        ("The Cosmic Koi. One in ten million.", [shot('koi')], '*COSMIC KOI', {'tier': 4, 'sfx': 'record'}),
        ("It's so big, it floats over the whole dock.", [shot('koi_b', False)], 'TOO *BIG'),
        ("Be honest. What's your number? Skip a Hook, on Roblox.", [('koi2_splash_hover', 0.2, {'max': 1.6})], '')]),

    # ================= C Mtrix · TikTok
    'tk_c1': dict(speed=0.88, amb='night', lines=[
        ("You just caught a Golden Shark. Do you sell it, or keep it?", [shot('gshark'), shot('gshark_hold', False)], 'SELL OR *KEEP?', {'sfx': 'reveal3'}),
        ("Sell it, and you get the cash right now.", [shot('gshark_hold', False)], '*SELL', {'sfx': 'coins'}),
        ("Keep it, and it swims in your aquarium and earns money, even when you're offline.", [('aqua_full_glass', 2.0)], '*KEEP'),
        ("Comment sell or keep. Skip a Hook, on Roblox.", [shot('gshark', False)], '')]),
    'dx7_c': dict(speed=0.85, amb='day', lines=[
        ("Day seven of updating my Roblox fishing game every day.", [('c27_longcast1', 0.5)], 'DAY *7'),
        ("Your PERFECT used to pop up way too late. Sometimes after the catch.", [('c26_cast_short', 0.5)], 'TOO *LATE', {'sfx': 'cast_soft'}),
        ("I fixed it. Now it shows the moment your hook lands.", [('c27_longcast2', 1.0), ('c26_cast_short', 2.0)], '*INSTANT', {'sfx': 'perfect'}),
        ("And it counts your streak. What's your best streak? Comment it. See you on day eight!", [('c27_longcast1', 5.0)], '')]),
    'tk_c2': groups("The first letter of your name decides your fish.", 'YOUR NAME = *YOUR FISH', [
        ("A to F: the Supernova Shark.", '*A - F', 'nova'),
        ("G to L: the Prehistoric Megalodon.", '*G - L', 'meg'),
        ("M to R: the Golden Shark.", '*M - R', 'gshark'),
        ("S to Z: the Moonlotus Dragon. One in a hundred million.", '*S - Z', 'lotus'),
    ], "Drop your first letter in the comments. Skip a Hook, on Roblox.", ('g_casts_dock', 1.0)),

    # ================= C Mtrix · Instagram (REEL)
    'tk_ic1': ladder([
        ("Double tap, and this Golden Shark is yours.", 'gshark', 'LIKE = *GOLDEN SHARK'),
        ("Follow, and it's a Cosmic Dragon.", 'dragon', 'FOLLOW = *DRAGON'),
        ("Leave a comment, and the Giant Blue Whale is yours.", 'whale', 'COMMENT = *WHALE'),
        ("Send this to a friend, and you both get the Cosmic Koi.", 'koi', 'SEND = *COSMIC KOI'),
        ("Do all four, and the Moonlotus Dragon is yours. One in a hundred million.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Which fish did you get? Skip a Hook, on Roblox.", labels=['LIKE', 'FOLLOW', 'COMMENT', 'SEND', 'ALL 4']),
    'tk_ic2': stop("Screenshot while the fish are changing. Whatever is on your screenshot is yours.", '*SCREENSHOT IT',
                   ['paddle', 'dragon', 'koi', 'goldfish', 'whale', 'gshark', 'nova'],
                   "Show me what you got in the comments.", 'SHOW *ME',
                   "Skip a Hook, on Roblox.", first='koi'),

    # ================= C Mtrix · YouTube
    'tk_yc1': ladder([
        ("Like this Short, and the Supernova Shark is yours.", 'nova', 'LIKE = *SUPERNOVA'),
        ("Subscribe, and you get the Prehistoric Megalodon.", 'meg', 'SUB = *MEGALODON'),
        ("Comment, and it's the Giant Blue Whale.", 'whale', 'COMMENT = *WHALE'),
        ("Share it, and the Cosmic Koi is yours. One in ten million.", 'koi', 'SHARE = *COSMIC KOI'),
        ("Do all four, and you get the rarest fish in the game. The Moonlotus Dragon.", 'lotus', 'ALL 4 = *RAREST'),
    ], "Which one did you get? Skip a Hook, on Roblox.", labels=['LIKE', 'SUBSCRIBE', 'COMMENT', 'SHARE', 'ALL 4']),
    'dx8_yc': dict(speed=0.85, amb='day', lines=[
        ("Day eight of updating my Roblox fishing game every day.", [('c05_zonesfly_long1', 2.0)], 'DAY *8'),
        ("Legends of the Deep is live.", [('c14_lake_long', 1.0)], 'NOW *LIVE', {'sfx': 'record'}),
        ("Every half hour, a legend shows up for four minutes, and your chance to hook it doubles.", [('c23_lagoon_long', 2.0), ('c15_temple_long', 3.0)], '*X2 CHANCE'),
        ("Four legends: Big Bertha, Old Whiskers, the Coral Empress and Frostjaw.", [('c19_islands_long', 2.0), ('c24_rift_long', 3.0)], '*4 LEGENDS'),
        ("Which one do you want to catch first? Comment it. See you on day nine!", [('c05_zonesfly_long1', 6.0)], '')]),
    'tk_yc2': pick("One, two, or three? Pick one.", 'PICK *1, 2 OR 3',
                   "Comment your number before it shows up.", 'COMMENT *FIRST', [
                       ("One: the Moonlotus Dragon. One in a hundred million.", 'lotus', False),
                       ("Two: the Golden Shark.", 'gshark', False),
                       ("Three: a Goldfish. Well...", 'goldfish', True),
                   ], "Lucky or not? Skip a Hook, on Roblox.", ('g_casts_dock', 3.0)),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'tk_m1': stop("Stop the video on a fish. That's your catch for today.", 'STOP = *YOUR CATCH',
                  ['koi', 'gshark', 'meg', 'paddle', 'whale', 'lotus', 'goldfish'],
                  "Rare one, or the poor little paddlefish? Comment it.", 'WHAT DID *YOU GET?',
                  "Skip a Hook, on Roblox.", first='gshark'),
    'cc8_m2': dict(prog=(2, 4, 1000), speed=0.85, amb='day', lines=[
        ("Day eight of trying to reach one thousand players.", [('c13_pete_long', 2.0)], 'DAY *8'),
        ("Average today: four. And over thirty one thousand six hundred visits.", [('c03_baserow_long2', 1.0)], '*4 PLAYERS', {'prog': True}),
        ("Every half hour, a legend shows up in its zone, and your chance to hook it doubles.", [('c23_lagoon_long', 1.0), ('c14_lake_long', 4.0)], 'LEGEND *SIGHTED', {'sfx': 'bite'}),
        ("Have you seen one yet? Comment it. See you on day nine!", [('c13_pete_long', 7.0)], '')]),
    'tk_m2': dict(speed=0.88, amb='night', lines=[
        ("Rate this fish from one to ten.", [shot('lotus', False)], 'RATE IT *1-10'),
        ("The Moonlotus Dragon. Ethereal. One in a hundred million.", [('g_hold_confetti', 0.7, {'max': 1.95, 'fish': ('MOONLOTUS DRAGON', '1 IN 100,000,000')})], '*1 IN 100M', {'tier': 4, 'sfx': 'record'}),
        ("One of the rarest fish in my whole game.", [shot('lotus')], '*ETHEREAL'),
        ("Be honest. What's your rating? Skip a Hook, on Roblox.", [shot('lotus', False)], '')]),

    # ================= mtfgams12 · YouTube
    'tk_n1': pick("Choose wisely. One, two, or three.", 'CHOOSE *WISELY',
                  "Write your number in the comments. Then keep watching.", 'NUMBER *FIRST', [
                      ("One: the Cosmic Koi. One in ten million.", 'koi', False),
                      ("Two: a Paddlefish. Sorry.", 'paddle', True),
                      ("Three: the Cosmic Dragon.", 'dragon', False),
                  ], "Did you win? Skip a Hook, on Roblox.", ('g_casts_perfect', 2.0)),
    'tk_n2': groups("The last number of your birth year decides your fish.", 'BIRTH YEAR = *YOUR FISH', [
        ("Zero, one or two: the Giant Blue Whale.", '*0 - 2', 'whale'),
        ("Three, four or five: the Cosmic Dragon.", '*3 - 5', 'dragon'),
        ("Six or seven: the Supernova Shark.", '*6 - 7', 'nova'),
        ("Eight or nine: the Cosmic Koi. One in ten million.", '*8 - 9', 'koi'),
    ], "Tell me your number in the comments. Skip a Hook, on Roblox.", ('g_casts_dock', 5.0)),
}

# aus Fassung 1 unverändert übernommen (keine Legenden-Clips, Skript ok)
KEEP = ['dx7_b', 'dx7_ic', 'dx8_n']

POST_PLAN = [
    ('7181171', 'tiktok', [('tk_a1', '12:03'), ('cc8_tt', '17:33'), ('tk_a2', '19:03')]),
    ('7181171', 'youtube', [('tk_ya1', '12:03'), ('cc8_yt', '17:33'), ('tk_ya2', '19:03')]),
    ('7752397', 'tiktok', [('tk_b1', '12:09'), ('dx7_b', '16:09'), ('tk_b2', '19:09')]),
    ('7752397', 'youtube', [('tk_yb1', '12:09'), ('dx7_yb', '16:00'), ('tk_yb2', '19:30')]),
    ('7773777', 'tiktok', [('tk_c1', '12:15'), ('dx7_c', '16:15'), ('tk_c2', '19:15')]),
    ('7773777', 'instagram', [('tk_ic1', '12:15'), ('dx7_ic', '16:15'), ('tk_ic2', '19:15')]),
    ('7773777', 'youtube', [('tk_yc1', '12:15'), ('dx8_yc', '16:15'), ('tk_yc2', '19:15')]),
    ('7752416', 'youtube', [('tk_m1', '12:21'), ('cc8_m2', '16:21'), ('tk_m2', '19:21')]),
    ('7773832', 'youtube', [('tk_n1', '12:24'), ('dx8_n', '16:24'), ('tk_n2', '19:24')]),
]
