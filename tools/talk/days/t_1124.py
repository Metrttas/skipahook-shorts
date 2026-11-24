# Tagesdatei 24.11.2026 – Nachhol-Lauf (Routine 23.11. abends brach ab, 23.11. ohne Stimm-Videos -> Zähler fortlaufend: CCU Day 17, Day-X 17/16).
# CCU: games-API 24.11. ~10:35 UTC: playing 0 (= right now), Besuche 34,028, Favoriten 1,521, updated 21.11. 15:18 UTC. Season 1 endet 25.11. 18:00, Season 2 Frostbite ab 25.11.
# Tagesdatei 22.11.2026 – NUR die Stimm-Videos (Day-Slot). 12:xx -> 13:xx Schiff-Sound-Edits (specs/ship_1122.py), 19/21:xx Soccer Bomb (specs/fb_1122.py).
#   Routine 21.11. abends fiel aus (Container-Platte voll beim Klonen) -> 22.11. vormittags in der Sitzung gebaut. 21.11. kein Post ->
#   Zähler fortlaufend: CCU Day 16, Mtrix-YT/mtfgams12 Day 16, B-TT/B-YT/C-TT/C-IG Day 15.
#   python3 tools/promo/talk/talk.py tools/promo/talk/days/t_1122.py all stills|render
# CCU: Dashboard nicht angemeldet -> games-API 22.11. ~10:00 UTC: playing 1 (= "right now"), Besuche 33,909, Favoriten 1,512,
#   updated 21.11. 15:18 UTC (= Winter-Update 235-241 veröffentlicht, Winter schaltete Sa 21.11. 18:00 Berlin automatisch live).
# Themen = WINTER-UPDATE (live): Schnee-Basen + Schnee-Kiefern statt Palmen + Schneemänner (237/238), Lichterketten an Zuckerstangen-Masten
#   über den Stegen + Riesen-Weihnachtsbaum-Insel + Schneefall (235), 6 Winter-Fische bis 6. Jan. (240, Narwal = seltenster, Gewicht 5),
#   Fishing Pass Season 2 "Frostbite" ab Mi 25.11. 18:00 Berlin, Finale "S2 Aurora Line" (236), Update-Log "WINTER IS HERE!" (239),
#   Umschalten um 18:00 von selbst (241). NICHT live: Update 242 (Benachrichtigungen, nach dem Veröffentlichen gebaut).
# Bilder: neue Standbild-Clips s_w_* (stills_mk.py, FIT) aus docs/ref u235-u240 (u235-Tag-Bilder NICHT, zeigen noch Palmen).


def Z(name, start=0.3):
    return (name, start, {'max': 5.9})


END17, END18 = "See you on day seventeen!", "See you on day eighteen!"
P17 = (3, 0, 1000)

VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'cc17_tt': dict(prog=P17, speed=0.85, amb='day', lines=[
        ("Day seventeen of trying to reach a thousand players: zero online right now.", [Z('s_w_snowman')], 'DAY 17 · *0 ONLINE', {'prog': True}),
        ("But tomorrow, season two starts in my Roblox fishing game.", [Z('s_w_pass')], '*SEASON 2', {'sfx': 'reveal3'}),
        ("It's called Frostbite, and the last reward is the Aurora Line.", [Z('s_w_pass', 2.5)], 'AURORA *LINE', {'sfx': 'reveal4'}),
        ("Will you be there tomorrow? " + END18, [Z('s_w_snowman', 2.0)], '')]),
    # ================= A fbgam.es · YouTube @MD_58_PDH
    'cc17_yt': dict(prog=P17, speed=0.85, amb='night', lines=[
        ("Day seventeen on my road to one thousand players.", [Z('s_w_night')], 'DAY *17'),
        ("Right now, nobody is online. Zero.", [Z('s_w_base')], '*0 ONLINE', {'prog': True}),
        ("But my Roblox fishing game just passed thirty four thousand visits.", [Z('s_w_overview')], '*34,000 VISITS', {'sfx': 'reveal3'}),
        ("What would make you join? " + END18, [Z('s_w_night', 2.0)], '')]),
    # ================= B mtfgams · TikTok
    'dx16_b': dict(speed=0.85, amb='day', lines=[
        ("Day sixteen: the rarest winter fish in my Roblox fishing game.", [Z('s_w_fish')], 'DAY 16 · *WINTER FISH'),
        ("It's the frost narwhal.", [Z('s_w_f_narwhal')], 'FROST *NARWHAL', {'sfx': 'reveal4'}),
        ("But it's only here until January sixth.", [Z('s_w_f_narwhal', 2.0)], 'UNTIL *JAN 6'),
        ("Would you hunt for it? " + END17, [Z('s_w_fish', 2.0)], '')]),
    # ================= B mtfgams · YouTube
    'dx16_yb': dict(speed=0.85, amb='night', lines=[
        ("Day sixteen: a giant Christmas tree in my Roblox fishing game.", [Z('s_w_poster')], 'DAY 16 · *XMAS TREE'),
        ("It stands on its own little island, right between the bases.", [Z('s_w_overview')], 'TREE *ISLAND', {'sfx': 'reveal3'}),
        ("At night, it glows while the snow falls.", [Z('s_w_night')], 'COZY *NIGHTS'),
        ("Cozy or too much? " + END17, [Z('s_w_poster', 2.0)], '')]),
    # ================= C Mtrix · TikTok
    'dx16_c': dict(speed=0.85, amb='day', lines=[
        ("Day sixteen: season two of my Roblox fishing game starts tomorrow.", [Z('s_w_pass')], 'DAY 16 · *SEASON 2'),
        ("The new fishing pass is called Frostbite.", [Z('s_w_pass', 1.5)], '*FROSTBITE'),
        ("The final reward is the Aurora Line.", [Z('s_w_pass', 3.0)], 'AURORA *LINE', {'sfx': 'reveal4'}),
        ("Are you going for the whole pass? " + END17, [Z('s_w_overview')], '')]),
    # ================= C Mtrix · Instagram (REEL)
    'dx16_ic': dict(speed=0.85, amb='day', lines=[
        ("Day sixteen: two cute winter fish in my Roblox fishing game.", [Z('s_w_fish')], 'DAY 16 · *WINTER FISH'),
        ("A gingerbread koi,", [Z('s_w_f_koi')], 'GINGERBREAD *KOI', {'sfx': 'reveal2'}),
        ("and a jingle betta with little bells.", [Z('s_w_f_betta')], 'JINGLE *BETTA', {'sfx': 'reveal3'}),
        ("Which one is cuter? " + END17, [Z('s_w_fish', 2.0)], '')]),
    # ================= C Mtrix · YouTube
    'dx17_yc': dict(speed=0.85, amb='day', lines=[
        ("Day seventeen: season one of my Roblox fishing game ends tomorrow.", [Z('s_w_poster')], 'DAY 17 · *LAST DAY'),
        ("At six PM it's over, and season two, Frostbite, begins.", [Z('s_w_pass')], 'FROSTBITE *6 PM', {'sfx': 'reveal3'}),
        ("So there is just one day left for the season one rewards.", [Z('s_w_base')], '1 DAY *LEFT'),
        ("Did you finish season one? " + END18, [Z('s_w_poster', 2.0)], '')]),
    # ================= mtgames2# · YouTube @Roblox-ad5
    'cc17_m2': dict(prog=P17, speed=0.85, amb='day', lines=[
        ("Day seventeen: zero players online in my Roblox fishing game right now.", [Z('s_w_base')], 'DAY 17 · *0 ONLINE', {'prog': True}),
        ("But over fifteen hundred people favorited it.", [Z('s_w_overview')], '*1,521 FAVORITES', {'sfx': 'reveal3'}),
        ("And now everything is snowy, with snowmen on every base.", [Z('s_w_snowman')], '*SNOWMEN'),
        ("Did you favorite it yet? " + END18, [Z('s_w_base', 2.0)], '')]),
    # ================= mtfgams12 · YouTube
    'dx17_n': dict(speed=0.85, amb='day', lines=[
        ("Day seventeen: my Roblox fishing game is covered in snow.", [Z('s_w_overview')], 'DAY 17 · *SNOW'),
        ("The palm trees turned into snowy pines,", [Z('s_w_base')], 'SNOWY *PINES'),
        ("and every base got its own snowman.", [Z('s_w_snowman')], '*SNOWMEN', {'sfx': 'reveal3'}),
        ("Summer or winter map? " + END18, [Z('s_w_overview', 2.0)], '')]),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('cc17_tt', '17:33')]),
    ('7181171', 'youtube', [('cc17_yt', '17:33')]),
    ('7752397', 'tiktok', [('dx16_b', '16:09')]),
    ('7752397', 'youtube', [('dx16_yb', '16:00')]),
    ('7773777', 'tiktok', [('dx16_c', '16:15')]),
    ('7773777', 'instagram', [('dx16_ic', '16:15')]),
    ('7773777', 'youtube', [('dx17_yc', '16:15')]),
    ('7752416', 'youtube', [('cc17_m2', '16:21')]),
    ('7773832', 'youtube', [('dx17_n', '16:24')]),
]
