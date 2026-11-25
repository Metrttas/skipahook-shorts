# Tagesdatei 25.11.2026 – Nachhol-Lauf nachmittags (Routine 24.11. abends brach ab), nur Day-Slot. CCU Day 18, Day-X 18/17.
# games-API 25.11. ~13:20 UTC: playing 0, Besuche 34,084, Favoriten 1,526, updated 21.11. Season 2 Frostbite startet heute 18:00.
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


END17, END18, END19 = "See you on day seventeen!", "See you on day eighteen!", "See you on day nineteen!"
P18 = (3, 0, 1000)

VIDEOS = {
    'cc18_tt': dict(prog=P18, speed=0.85, amb='day', lines=[
        ("Day eighteen of trying to reach a thousand players: zero online right now.", [Z('s_w_overview')], 'DAY 18 · *0 ONLINE', {'prog': True}),
        ("So here are the six winter fish in my Roblox fishing game.", [Z('s_w_fish')], '*6 WINTER FISH', {'sfx': 'reveal3'}),
        ("The snowman puffer is my favorite.", [Z('s_w_f_puffer')], 'SNOWMAN *PUFFER'),
        ("Which one would you catch first? " + END19, [Z('s_w_fish', 2.0)], '')]),
    'cc18_yt': dict(prog=P18, speed=0.85, amb='night', lines=[
        ("Day eighteen on my road to one thousand players.", [Z('s_w_night')], 'DAY *18'),
        ("Zero online right now.", [Z('s_w_base')], '*0 ONLINE', {'prog': True}),
        ("But tonight at six PM, season two starts in my Roblox fishing game.", [Z('s_w_pass')], '*SEASON 2 TONIGHT', {'sfx': 'reveal3'}),
        ("The final reward is the Aurora Line. Will you join? " + END19, [Z('s_w_pass', 2.5)], '')]),
    'dx17_b': dict(speed=0.85, amb='day', lines=[
        ("Day seventeen: season two starts tonight in my Roblox fishing game.", [Z('s_w_pass')], 'DAY 17 · *SEASON 2'),
        ("At six PM, season one ends and the Frostbite pass begins.", [Z('s_w_pass', 1.5)], '*6 PM TONIGHT', {'sfx': 'reveal3'}),
        ("The last reward is the Aurora Line.", [Z('s_w_pass', 3.0)], 'AURORA *LINE', {'sfx': 'reveal4'}),
        ("Free pass or premium? " + END18, [Z('s_w_overview')], '')]),
    'dx17_yb': dict(speed=0.85, amb='day', lines=[
        ("Day seventeen: three winter fish in my Roblox fishing game.", [Z('s_w_fish')], 'DAY 17 · *WINTER FISH'),
        ("A snowman puffer,", [Z('s_w_f_puffer')], 'SNOWMAN *PUFFER', {'sfx': 'reveal2'}),
        ("a gingerbread koi,", [Z('s_w_f_koi')], 'GINGERBREAD *KOI'),
        ("and a jingle betta. Which one wins? " + END18, [Z('s_w_f_betta')], 'JINGLE *BETTA', {'sfx': 'reveal3'})]),
    'dx17_c': dict(speed=0.85, amb='day', lines=[
        ("Day seventeen: the cutest and the rarest winter fish in my Roblox fishing game.", [Z('s_w_fish')], 'DAY 17 · *CUTE VS RARE'),
        ("Cutest: the snowman puffer.", [Z('s_w_f_puffer')], '*CUTEST', {'sfx': 'reveal2'}),
        ("Rarest: the frost narwhal.", [Z('s_w_f_narwhal')], '*RAREST', {'sfx': 'reveal4'}),
        ("Cute or rare, which one do you want? " + END18, [Z('s_w_fish', 2.0)], '')]),
    'dx17_ic': dict(speed=0.85, amb='night', lines=[
        ("Day seventeen: tonight my Roblox fishing game gets season two.", [Z('s_w_night')], 'DAY 17 · *SEASON 2'),
        ("It's called Frostbite, and it starts at six PM.", [Z('s_w_pass')], '*FROSTBITE', {'sfx': 'reveal3'}),
        ("Finish the pass to get the Aurora Line.", [Z('s_w_pass', 3.0)], 'AURORA *LINE', {'sfx': 'reveal4'}),
        ("Will you play tonight? " + END18, [Z('s_w_night', 2.0)], '')]),
    'dx18_yc': dict(speed=0.85, amb='night', lines=[
        ("Day eighteen: this is my Roblox fishing game at night in winter.", [Z('s_w_night')], 'DAY 18 · *WINTER NIGHT'),
        ("The giant Christmas tree glows on its island,", [Z('s_w_poster')], 'XMAS *TREE', {'sfx': 'reveal3'}),
        ("and the snow keeps falling on every base.", [Z('s_w_base')], '*SNOWFALL'),
        ("Day or night, when do you play? " + END19, [Z('s_w_night', 2.0)], '')]),
    'cc18_m2': dict(prog=P18, speed=0.85, amb='night', lines=[
        ("Day eighteen: zero players online in my Roblox fishing game right now.", [Z('s_w_night')], 'DAY 18 · *0 ONLINE', {'prog': True}),
        ("But there's a giant Christmas tree waiting on its own island.", [Z('s_w_poster')], 'GIANT *TREE', {'sfx': 'reveal3'}),
        ("And over fifteen hundred favorites. Thank you!", [Z('s_w_overview')], '*1,526 FAVORITES'),
        ("Will you come fish with me? " + END19, [Z('s_w_night', 2.0)], '')]),
    'dx18_n': dict(speed=0.85, amb='day', lines=[
        ("Day eighteen: season two of my Roblox fishing game starts tonight.", [Z('s_w_pass')], 'DAY 18 · *SEASON 2'),
        ("Season one ends at six PM, then Frostbite begins.", [Z('s_w_poster')], '*FROSTBITE', {'sfx': 'reveal3'}),
        ("New pass, new rewards, and the Aurora Line at the end.", [Z('s_w_pass', 3.0)], 'AURORA *LINE', {'sfx': 'reveal4'}),
        ("Are you going for it? " + END19, [Z('s_w_pass', 1.0)], '')]),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('cc18_tt', '17:33')]),
    ('7181171', 'youtube', [('cc18_yt', '17:33')]),
    ('7752397', 'tiktok', [('dx17_b', '16:09')]),
    ('7752397', 'youtube', [('dx17_yb', '16:00')]),
    ('7773777', 'tiktok', [('dx17_c', '16:15')]),
    ('7773777', 'instagram', [('dx17_ic', '16:15')]),
    ('7773777', 'youtube', [('dx18_yc', '16:15')]),
    ('7752416', 'youtube', [('cc18_m2', '16:21')]),
    ('7773832', 'youtube', [('dx18_n', '16:24')]),
]
