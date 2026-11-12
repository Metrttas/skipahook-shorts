# Tagesdatei 12.11.2026 – NEU: nur Rede-Videos (User 12.11. 01:50 "red nur noch in den Videos … bring Leute zum Liken/Teilen …
#   wenn du likest kriegst du den Fisch … keine eigenen Sounds"). 27 Videos ersetzen die AE-Videos (ae_1112, in Metricool als Entwurf).
#   python3 tools/promo/talk/talk.py tools/promo/talk/days/t_1112.py all stills|render
# Formate (je Konto verschieden, Fisch-Reihenfolge/Wortlaut je Variante neu; "nur Spaß": "this is YOUR fish", kein echtes Versprechen):
#   L = Like/Follow/Comment/Share-Leiter ("all 4 = legend"), M = Geburtsmonat = dein Fisch, P = "Stop the video" (Bilder blitzen),
#   R = Legende entkommt -> "send this to the friend who would rage", K = Pick 1, 2 or 3.
# Serien: CCU Day 8 (Average 4, gestern 2, Besuche 31,647) + Day-X 7/8 (Inhalte wie ae_1112, jetzt mit Kommentar-Frage am Ende).
# Ton: Stimme am_puck + echte Spiel-Töne (asmr_sfx) + Spiel-Atmo; keine Musik.

# Fisch-Momente (Clip, Start, Name, Seltenheit) – Zeiten aus Kontaktbögen 12.11.
F = {
    'gshark': ('golden_shark_reveal', 0.1, 'GOLDEN SHARK', 'SECRET'),
    'nova': ('far_supernova', 5.0, 'SUPERNOVA SHARK', 'SECRET'),
    'nova2': ('far2_supernova', 3.6, 'SUPERNOVA SHARK', 'SECRET'),
    'meg': ('ancient_reveal', 0.8, 'PREHISTORIC MEGALODON', 'ANCIENT'),
    'lotus': ('g_ethereal_moonlotus', 0.5, 'MOONLOTUS DRAGON', 'ETHEREAL'),
    'koi': ('koi_hover', 0.5, 'COSMIC KOI', 'SEA GIANT'),
    'whale': ('whale_title', 1.5, 'GIANT BLUE WHALE', 'SEA GIANT'),
    'dragon': ('cosmic_dragon_reveal', 3.2, 'COSMIC DRAGON', 'SECRET'),
    'colossal': ('g_hud_colossal_meg', 3.6, 'COLOSSAL MEGALODON', 'SECRET'),
    'paddle': ('g_paddlefish_card', 4.3, 'PADDLEFISH', 'COMMON'),
    'goldfish': ('g_mutation_goldfish', 3.8, 'GOLDFISH', 'GOLD'),
    'bertha': ('lg_bertha_caught', 3.2, 'BIG BERTHA', 'LEGEND'),
    'empress': ('lg_empress_hooked', 2.0, 'THE CORAL EMPRESS', 'LEGEND'),
}


def fs(k, dt=0.0):
    c, s, n, r = F[k]
    return [(c, s + dt)], (n, r)


def ladder(lines_txt, fish, heads, end_txt):
    """L: 4 Stufen + 'all four' Legende."""
    out = []
    for i, (txt, k, hd) in enumerate(zip(lines_txt, fish, heads)):
        shots, nm = fs(k)
        o = {'tier': i, 'fish': nm}
        if i == 4: o['sfx'] = 'splash'
        out.append((txt, shots, hd, o))
    out.append((end_txt, fs(fish[0], 0.4)[0], ''))
    return dict(ladder=True, speed=0.88, amb='night', lines=out)


def months(intro, order, outro, joke):
    names = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    out = [intro]
    for m, k in zip(names, order):
        shots, nm = fs(k)
        t = f'{m.capitalize()}: {nm[0].title()}.' if k != 'paddle' else f'{m.capitalize()}: a Paddlefish. {joke}'
        out.append((t, shots, '*' + m, {'fish': nm, 'sfx': 'ui_pop'}))
    out.append(outro)
    return dict(speed=0.92, pause=0.25, amb='night', lines=out)


FLICK = ['gshark', 'paddle', 'whale', 'goldfish', 'dragon', 'nova', 'bertha', 'koi', 'meg', 'lotus', 'colossal', 'empress']


def flick(order):
    return [(F[k][0], F[k][1] + 0.3) for k in order]


VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'tk_a1': ladder(
        ["Like this video, and this Golden Shark is yours.", "Follow, and you get a Supernova Shark instead.",
         "Comment anything, and it's a Cosmic Dragon.", "Share it with a friend, and you get the Giant Blue Whale.",
         "Do all four... and you get a real legend. Big Bertha."],
        ['gshark', 'nova', 'dragon', 'whale', 'bertha'],
        ['LIKE = *YOUR FISH', 'FOLLOW = *BETTER', 'COMMENT = *DRAGON', 'SHARE = *WHALE', 'ALL 4 = *LEGEND'],
        "Which one did you get? Search Skip a Hook on Roblox."),
    'cc8_tt': dict(prog=(2, 4, 1000), speed=0.85, amb='day', lines=[
        ("Day eight of trying to reach one thousand players in my Roblox fishing game.", [('c06_dock_long', 2.0)], 'DAY *8'),
        ("Today's average: four players. That's double yesterday.", [('c04_docktolake_long1', 0.5)], '*4 PLAYERS', {'prog': True}),
        ("The legends update is out, so I went hunting. I hooked the Coral Empress...", [('lg_empress_hooked', 0.0), ('lg_empress_hooked', 2.0)], 'CORAL *EMPRESS', {'sfx': 'bite'}),
        ("And she got away. One click away.", [('lg_empress_escape', 0.0), ('lg_empress_escape', 1.2)], 'SHE *GOT AWAY', {'sfx': 'splash'}),
        ("Can you catch her before me? Tell me in the comments. See you on day nine!", [('c06_dock_long', 6.0)], '')]),
    'tk_a2': dict(ladder=False, speed=0.9, amb='night', lines=[
        ("Stop the video at the right moment, and that fish is yours.", [('koi_hover', 0.5), ('golden_shark_reveal', 0.1)], 'STOP THE *VIDEO'),
        ("Ready? Three, two, one... stop it now!", flick(['gshark', 'paddle', 'whale', 'goldfish', 'dragon', 'nova', 'bertha', 'koi', 'meg', 'lotus', 'colossal']), 'STOP *NOW!', {'flick': True}),
        ("Got a legend? Lucky. Got the paddlefish? I'm sorry.", [('lg_bertha_caught', 4.0), ('g_paddlefish_card', 5.8)], 'WHAT DID *YOU GET?', {'sfx': 'reveal2'}),
        ("Comment what you landed on. Search Skip a Hook on Roblox.", [('koi_hover', 0.6)], '')]),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'tk_ya1': months(
        ("Your birth month decides your fish in my Roblox game.", [('g_casts_perfect', 0.5)], 'YOUR MONTH = *YOUR FISH', {'sfx': 'cast_full'}),
        ['gshark', 'nova', 'meg', 'lotus', 'koi', 'whale', 'dragon', 'colossal', 'bertha', 'empress', 'paddle', 'goldfish'],
        ("Comment your month and your fish. Search Skip a Hook on Roblox.", [('g_casts_perfect', 3.0)], ''),
        "Sorry."),
    'cc8_yt': dict(prog=(2, 4, 1000), speed=0.85, amb='day', lines=[
        ("Day eight on my road to one thousand players.", [('c22_endgate_long', 1.0)], 'DAY *8'),
        ("The average went up from two to four.", [('c19_islands_long', 2.0)], '*4 PLAYERS', {'prog': True}),
        ("Legends are live now. Big Bertha already got caught.", [('lg_bertha_caught', 3.0)], 'LEGENDS *ARE LIVE', {'sfx': 'record'}),
        ("Next is world two. You voted on Discord: the Open Sea. Your own boat, and fish you hunt.", [('c30_boat', 3.0), ('c18_galleon_long', 3.0)], 'OPEN *SEA'),
        ("What should be on the first island? Comment it. See you on day nine!", [('c22_endgate_long', 6.0)], '')]),
    'tk_ya2': dict(speed=0.88, amb='night', lines=[
        ("Pick a number. One, two, or three.", [('c14_lake_long', 1.0)], 'PICK *1, 2 OR 3'),
        ("Put it in the comments first. No cheating.", [('g_casts_dock', 2.0)], 'NO *CHEATING'),
        ("One: the Cosmic Dragon.", fs('dragon')[0], '*1', {'fish': fs('dragon')[1], 'tier': 2}),
        ("Two: a Paddlefish. Ouch.", [('g_paddlefish_card', 5.8)], '*2', {'fish': fs('paddle')[1], 'sfx': 'miss'}),
        ("Three: the Giant Blue Whale.", fs('whale')[0], '*3', {'fish': fs('whale')[1], 'tier': 3}),
        ("So, what did you get? Search Skip a Hook on Roblox.", [('c14_lake_long', 4.0)], '')]),

    # ================= B mtfgams · TikTok
    'tk_b1': dict(speed=0.88, amb='night', lines=[
        ("Quick. Pick one, two, or three.", [('g_casts_perfect', 1.0)], 'PICK *1, 2 OR 3'),
        ("Type it in the comments before you scroll.", [('g_casts_dock', 5.0)], 'COMMENT *FIRST'),
        ("One: a Goldfish. Not bad.", fs('goldfish')[0], '*1', {'fish': fs('goldfish')[1], 'tier': 0}),
        ("Two: the Supernova Shark.", fs('nova')[0], '*2', {'fish': fs('nova')[1], 'tier': 2}),
        ("Three: the Prehistoric Megalodon.", fs('meg')[0], '*3', {'fish': fs('meg')[1], 'tier': 3}),
        ("Happy with yours? Search Skip a Hook on Roblox.", [('g_casts_perfect', 4.0)], '')]),
    'dx7_b': dict(speed=0.85, amb='day', lines=[
        ("Day seven of updating my Roblox fishing game every day.", [('c06_dock_long', 4.0)], 'DAY *7'),
        ("The buttons at the top were way too much.", [('c02_basecircle_long', 2.0)], 'TOO *MUCH UI'),
        ("So I cleaned it up into five groups: shop, upgrades, rewards, collection and social.", [('c03_baserow_long1', 1.0), ('c09_wheel_long', 2.0)], '*5 GROUPS'),
        ("New buttons unlock slowly while you play. That's the next update.", [('c26_cast_catch', 1.0)], 'NEXT *UPDATE'),
        ("Cleaner or worse? Tell me in the comments. See you on day eight!", [('c06_dock_long', 8.0)], '')]),
    'tk_b2': ladder(
        ["If you like this video, the Moonlotus Dragon is yours.", "Follow me, and you get the Prehistoric Megalodon.",
         "Leave a comment, and it's the Colossal Megalodon.", "Share it, and you get the Cosmic Koi.",
         "Do all four, and you get the Coral Empress. A legend."],
        ['lotus', 'meg', 'colossal', 'koi', 'empress'],
        ['LIKE = *DRAGON', 'FOLLOW = *MEGALODON', 'COMMENT = *COLOSSAL', 'SHARE = *COSMIC KOI', 'ALL 4 = *LEGEND'],
        "Tell me which one you got. Skip a Hook, on Roblox."),

    # ================= B mtfgams · YouTube
    'tk_yb1': dict(speed=0.9, amb='night', lines=[
        ("Pause the video when I say stop. Whatever you see is your fish.", [('g_hud_golden_shark', 5.0)], 'PAUSE *TO WIN'),
        ("Ready... stop!", flick(['whale', 'koi', 'paddle', 'nova', 'empress', 'gshark', 'meg', 'goldfish', 'dragon', 'lotus']), '*STOP!', {'flick': True}),
        ("Missed it? Watch again. It's random every time you try.", [('koi_hover', 0.6)], 'TRY *AGAIN'),
        ("Comment what you got. Search Skip a Hook on Roblox.", [('g_hud_golden_shark', 5.4)], '')]),
    'dx7_yb': dict(speed=0.85, amb='day', lines=[
        ("Day seven of updating my Roblox game every day.", [('c28_reel', 0.5)], 'DAY *7'),
        ("The old reel fight felt dead. You just had to spam.", [('c26_cast_catch', 4.0)], 'NO MORE *SPAM'),
        ("So I rebuilt it. A pointer circles the reel. Tap when it hits the gold zone.", [('lg_bertha_caught', 0.0), ('c28_reel', 3.5)], '*GOLD ZONE', {'sfx': 'reel'}),
        ("Every hit makes it faster. Miss twice, and the fish is gone.", [('lg_empress_hooked', 5.0), ('c29_holdup', 1.0)], 'FASTER *EVERY HIT'),
        ("Too hard, or just right? Comment it. See you on day eight!", [('c28_reel', 4.5)], '')]),
    'tk_yb2': dict(speed=0.85, amb='day', lines=[
        ("I was one click away from a legend.", [('lg_empress_hooked', 0.0)], 'ONE CLICK *AWAY', {'sfx': 'cast_full'}),
        ("Perfect cast. Then the Coral Empress bites.", [('lg_empress_hooked', 1.8)], 'SHE *BIT', {'fish': fs('empress')[1], 'sfx': 'bite', 'tier': 4}),
        ("I reel her all the way back to the dock...", [('lg_empress_hooked', 4.2)], 'ALMOST...', {'sfx': 'reel'}),
        ("And she's gone.", [('lg_empress_escape', 0.0)], '*GONE.', {'sfx': 'splash'}),
        ("Send this to the friend who would rage the hardest.", [('lg_empress_escape', 1.2)], 'SEND THIS *TO HIM'),
        ("She's still out there. Skip a Hook, on Roblox.", [('lg_empress_hooked', 0.3)], '')]),

    # ================= C Mtrix · TikTok
    'tk_c1': dict(speed=0.85, amb='day', lines=[
        ("Would you rage if this happened to you?", [('lg_empress_hooked', 2.0)], 'WOULD YOU *RAGE?', {'sfx': 'bite'}),
        ("A legend. The Coral Empress. Right on my line.", [('lg_empress_hooked', 2.6)], '*LEGEND', {'fish': fs('empress')[1], 'tier': 4}),
        ("Reeling, reeling, almost at the dock...", [('lg_empress_hooked', 4.4)], 'REELING...', {'sfx': 'reel'}),
        ("Gone. Just gone.", [('lg_empress_escape', 0.0), ('lg_empress_escape', 1.4)], '*GONE', {'sfx': 'splash'}),
        ("Tag the friend who would throw his phone. Skip a Hook, on Roblox.", [('lg_empress_hooked', 0.2)], '')]),
    'dx7_c': dict(speed=0.85, amb='day', lines=[
        ("Day seven of updating my Roblox fishing game every day.", [('c27_longcast1', 0.5)], 'DAY *7'),
        ("Your PERFECT used to pop up way too late. Sometimes after the catch.", [('c26_cast_short', 0.5)], 'TOO *LATE', {'sfx': 'cast_soft'}),
        ("I fixed it. Now it shows the moment your hook lands.", [('lg_empress_hooked', 0.0), ('c27_longcast2', 1.0)], '*INSTANT', {'sfx': 'perfect'}),
        ("And it counts your streak. What's your best streak? Comment it. See you on day eight!", [('c27_longcast1', 5.0)], '')]),
    'tk_c2': months(
        ("Your birthday month is your fish. Let's see what you got.", [('g_casts_dock', 1.0)], 'BIRTH MONTH = *FISH', {'sfx': 'cast_full'}),
        ['whale', 'dragon', 'paddle', 'bertha', 'nova', 'goldfish', 'empress', 'koi', 'gshark', 'colossal', 'lotus', 'meg'],
        ("Drop your month in the comments. Skip a Hook, on Roblox.", [('g_casts_dock', 4.0)], ''),
        "Unlucky."),

    # ================= C Mtrix · Instagram (REEL)
    'tk_ic1': ladder(
        ["Double tap, and the Golden Shark is yours.", "Follow, and you get the Moonlotus Dragon.",
         "Comment, and you get the Supernova Shark.", "Send it to a friend, and the Cosmic Koi is yours.",
         "Do all four, and you get Big Bertha. A legend."],
        ['gshark', 'lotus', 'nova2', 'koi', 'bertha'],
        ['LIKE = *GOLDEN SHARK', 'FOLLOW = *DRAGON', 'COMMENT = *SUPERNOVA', 'SHARE = *COSMIC KOI', 'ALL 4 = *LEGEND'],
        "Which fish did you get? Skip a Hook, on Roblox."),
    'dx7_ic': dict(speed=0.85, amb='day', lines=[
        ("Day seven of updating my Roblox game every day.", [('c23_lagoon_long', 1.0)], 'DAY *7'),
        ("I want you to see what's new after every update.", [('c06_dock_long', 3.0)], "WHAT'S *NEW?"),
        ("So I built an update log. One clean window that shows every new thing.", [('c02_basecircle_long', 4.0)], 'UPDATE *LOG', {'sfx': 'ui_open'}),
        ("It comes with the next update. What should be in it first? See you on day eight!", [('c23_lagoon_long', 7.0)], '')]),
    'tk_ic2': dict(speed=0.9, amb='night', lines=[
        ("Screenshot at the right time, and that's your fish.", [('koi_hover', 0.5), ('far_supernova', 5.2)], '*SCREENSHOT IT'),
        ("Go!", flick(['paddle', 'dragon', 'empress', 'whale', 'goldfish', 'koi', 'gshark', 'colossal', 'meg', 'bertha', 'nova']), '*NOW!', {'flick': True}),
        ("Show me your screenshot in the comments.", [('far_hold', 0.6)], 'SHOW ME'),
        ("Skip a Hook, on Roblox.", [('koi_hover', 0.6)], '')]),

    # ================= C Mtrix · YouTube
    'tk_yc1': ladder(
        ["Like this, and the Cosmic Dragon is yours.", "Subscribe, and you get the Prehistoric Megalodon.",
         "Comment, and it's the Giant Blue Whale.", "Share it, and you get the Cosmic Koi.",
         "Do all four, and the Coral Empress is yours. A legend."],
        ['dragon', 'meg', 'whale', 'koi', 'empress'],
        ['LIKE = *DRAGON', 'SUB = *MEGALODON', 'COMMENT = *WHALE', 'SHARE = *COSMIC KOI', 'ALL 4 = *LEGEND'],
        "Which one did you get? Skip a Hook, on Roblox."),
    'dx8_yc': dict(speed=0.85, amb='day', lines=[
        ("Day eight of updating my Roblox fishing game every day.", [('c05_zonesfly_long1', 2.0)], 'DAY *8'),
        ("Legends of the Deep is live.", [('lg_bertha_caught', 3.0)], 'NOW *LIVE', {'sfx': 'record'}),
        ("Every half hour, a legend shows up for four minutes, and your chance doubles.", [('lg_empress_hooked', 0.0), ('lg_empress_hooked', 2.0)], '*X2 CHANCE'),
        ("I caught Big Bertha. The Coral Empress got away.", [('lg_bertha_caught', 6.0), ('lg_empress_escape', 0.5)], '*1 OF 4'),
        ("Which legend do you want next? Comment it. See you on day nine!", [('c05_zonesfly_long1', 6.0)], '')]),
    'tk_yc2': dict(speed=0.88, amb='night', lines=[
        ("One, two or three? Pick one.", [('g_casts_dock', 3.0)], 'PICK *1, 2 OR 3'),
        ("Comment your number before it shows up.", [('g_casts_perfect', 6.0)], 'COMMENT *FIRST'),
        ("One: the Moonlotus Dragon.", fs('lotus')[0], '*1', {'fish': fs('lotus')[1], 'tier': 2}),
        ("Two: the Golden Shark.", fs('gshark')[0], '*2', {'fish': fs('gshark')[1], 'tier': 1}),
        ("Three: a Goldfish. Well...", fs('goldfish')[0], '*3', {'fish': fs('goldfish')[1], 'sfx': 'miss'}),
        ("Lucky or not? Search Skip a Hook on Roblox.", [('g_casts_dock', 6.0)], '')]),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'tk_m1': dict(speed=0.9, amb='night', lines=[
        ("Stop the video right when I say now. That's your fish.", [('g_hud_golden_shark', 5.2)], 'STOP *ON NOW'),
        ("Ready... now!", flick(['koi', 'gshark', 'meg', 'paddle', 'bertha', 'whale', 'lotus', 'nova', 'goldfish', 'empress']), '*NOW!', {'flick': True}),
        ("Legend? Shark? Or the poor little paddlefish?", [('lg_bertha_caught', 5.0), ('g_paddlefish_card', 6.0)], 'WHAT DID *YOU GET?'),
        ("Comment it. Search Skip a Hook on Roblox.", [('g_hud_golden_shark', 5.6)], '')]),
    'cc8_m2': dict(prog=(2, 4, 1000), speed=0.85, amb='day', lines=[
        ("Day eight of trying to reach one thousand players.", [('c13_pete_long', 2.0)], 'DAY *8'),
        ("Average today: four. And over thirty one thousand six hundred visits.", [('c03_baserow_long2', 1.0)], '*4 PLAYERS', {'prog': True}),
        ("Legends are out. Every half hour, one shows up in its zone.", [('lg_empress_hooked', 1.8)], 'LEGEND *SIGHTED', {'sfx': 'bite'}),
        ("Big Bertha was my first. Which one gets you? Comment it. See you on day nine!", [('lg_bertha_caught', 3.5), ('c13_pete_long', 7.0)], '')]),
    'tk_m2': dict(speed=0.85, amb='day', lines=[
        ("Rate my catch from one to ten.", [('lg_bertha_caught', 0.0)], 'RATE IT *1-10', {'sfx': 'reel'}),
        ("This is Big Bertha. One of four legends in the lake.", [('lg_bertha_caught', 3.0)], '*BIG BERTHA', {'fish': fs('bertha')[1], 'tier': 4, 'sfx': 'record'}),
        ("She only shows up every half hour, for four minutes.", [('lg_bertha_caught', 6.5)], '*4 MINUTES'),
        ("Be honest. What's your rating? Skip a Hook, on Roblox.", [('lg_bertha_caught', 0.3)], '')]),

    # ================= mtfgams12 · YouTube
    'tk_n1': dict(speed=0.88, amb='night', lines=[
        ("Choose wisely. One, two, or three.", [('g_casts_perfect', 2.0)], 'CHOOSE *WISELY'),
        ("Write your number in the comments. Then keep watching.", [('g_casts_dock', 7.0)], 'NUMBER *FIRST'),
        ("One: the Colossal Megalodon.", fs('colossal')[0], '*1', {'fish': fs('colossal')[1], 'tier': 3}),
        ("Two: the Cosmic Koi.", fs('koi')[0], '*2', {'fish': fs('koi')[1], 'tier': 2}),
        ("Three: a Paddlefish. Sorry.", [('g_paddlefish_card', 5.8)], '*3', {'fish': fs('paddle')[1], 'sfx': 'miss'}),
        ("Did you win? Search Skip a Hook on Roblox.", [('g_casts_perfect', 5.0)], '')]),
    'dx8_n': dict(speed=0.85, amb='day', lines=[
        ("Day eight of updating my Roblox game every day.", [('c14_lake_long', 3.0)], 'DAY *8'),
        ("You voted on Discord, so world two is now the Open Sea.", [('c30_boat', 1.0)], 'OPEN *SEA'),
        ("Your own boat, islands, and fish schools you can find with a sonar.", [('c30_boat', 6.0), ('c19_islands_long', 2.0)], '*YOUR BOAT'),
        ("I coded the first part today. It stays closed until it's really good.", [('c18_galleon_long', 2.0)], 'NOT *YET'),
        ("What boat should I add first? Comment it. See you on day nine!", [('c14_lake_long', 7.0)], '')]),
    'tk_n2': months(
        ("The month you were born decides your fish.", [('g_casts_perfect', 3.0)], 'YOUR MONTH = *YOUR FISH', {'sfx': 'cast_full'}),
        ['koi', 'goldfish', 'bertha', 'gshark', 'paddle', 'meg', 'whale', 'empress', 'lotus', 'dragon', 'nova', 'colossal'],
        ("Tell me your month in the comments. Skip a Hook, on Roblox.", [('g_casts_perfect', 6.0)], ''),
        "That's rough."),
}

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

VIDEOS['tk_yc1']['labels'] = ['LIKE', 'SUBSCRIBE', 'COMMENT', 'SHARE', 'ALL 4']
