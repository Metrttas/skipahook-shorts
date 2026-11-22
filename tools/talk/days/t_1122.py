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


END16, END17 = "See you on day sixteen!", "See you on day seventeen!"
P16 = (3, 1, 1000)

VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'cc16_tt': dict(prog=P16, speed=0.85, amb='night', lines=[
        ("Day sixteen of trying to reach a thousand players: one player online right now.", [Z('s_w_night')], 'DAY 16 · *1 ONLINE', {'prog': True}),
        ("But yesterday, winter came to my Roblox fishing game.", [Z('s_w_overview')], 'WINTER *IS HERE', {'sfx': 'reveal3'}),
        ("Snow on every base, Christmas trees and lights over the docks.", [Z('s_w_base')], '*SNOW EVERYWHERE'),
        ("Would you play it in winter? " + END17, [Z('s_w_night', 2.0)], '')]),
    # ================= A fbgam.es · YouTube @MD_58_PDH
    'cc16_yt': dict(prog=P16, speed=0.85, amb='day', lines=[
        ("Day sixteen on my road to one thousand players.", [Z('s_w_poster')], 'DAY *16'),
        ("One person is online right now.", [Z('s_w_base')], '*1 ONLINE', {'prog': True}),
        ("Almost thirty four thousand visits, and over fifteen hundred favorites.", [Z('s_w_overview')], '*33,909 VISITS', {'sfx': 'reveal3'}),
        ("Yesterday I added the winter update. What should come next? " + END17, [Z('s_w_poster', 2.0)], '')]),
    # ================= B mtfgams · TikTok
    'dx15_b': dict(speed=0.85, amb='day', lines=[
        ("Day fifteen: my Roblox fishing game turned into winter.", [Z('s_w_overview')], 'DAY 15 · *WINTER'),
        ("Every base is covered in snow, and the palm trees became snowy pines.", [Z('s_w_base')], '*SNOW BASES'),
        ("There are even snowmen.", [Z('s_w_snowman')], '*SNOWMEN', {'sfx': 'reveal3'}),
        ("Summer or winter, which looks better? " + END16, [Z('s_w_overview', 2.0)], '')]),
    # ================= B mtfgams · YouTube
    'dx15_yb': dict(speed=0.85, amb='day', lines=[
        ("Day fifteen: my Roblox fishing game gets season two.", [Z('s_w_pass')], 'DAY 15 · *SEASON 2'),
        ("The new fishing pass is called Frostbite, and it starts this Wednesday.", [Z('s_w_pass', 2.0)], '*FROSTBITE'),
        ("The final reward is a new fishing line, the Aurora Line.", [Z('s_w_pass', 3.5)], 'AURORA *LINE', {'sfx': 'reveal4'}),
        ("Free pass or premium, which one do you go for? " + END16, [Z('s_w_pass', 1.0)], '')]),
    # ================= C Mtrix · TikTok
    'dx15_c': dict(speed=0.85, amb='night', lines=[
        ("Day fifteen: I added winter lights to my Roblox fishing game.", [Z('s_w_night')], 'DAY 15 · *LIGHTS'),
        ("Candy cane poles with string lights now line every dock,", [Z('s_w_base')], '*STRING LIGHTS'),
        ("and at night, they glow while the snow keeps falling.", [Z('s_w_night', 2.0)], 'COZY *NIGHTS', {'sfx': 'reveal3'}),
        ("Day or night, when do you fish? " + END16, [Z('s_w_overview')], '')]),
    # ================= C Mtrix · Instagram (REEL)
    'dx15_ic': dict(speed=0.85, amb='day', lines=[
        ("Day fifteen: my Roblox fishing game switched to winter by itself.", [Z('s_w_log')], 'DAY 15 · *WINTER'),
        ("Yesterday at six PM, the whole map turned white at once.", [Z('s_w_overview')], '*6 PM', {'sfx': 'reveal3'}),
        ("Snowy pines, Christmas trees and snowmen on the bases.", [Z('s_w_snowman')], '*SNOWMEN'),
        ("Do you like winter updates? " + END16, [Z('s_w_poster')], '')]),
    # ================= C Mtrix · YouTube
    'dx16_yc': dict(speed=0.85, amb='day', lines=[
        ("Day sixteen: six winter fish just arrived in my Roblox fishing game.", [Z('s_w_fish')], 'DAY 16 · *WINTER FISH'),
        ("A snowman puffer,", [Z('s_w_f_puffer')], 'SNOWMAN *PUFFER'),
        ("a gingerbread koi,", [Z('s_w_f_koi')], 'GINGERBREAD *KOI'),
        ("a jingle betta with little bells,", [Z('s_w_f_betta')], 'JINGLE *BETTA'),
        ("and the rarest one, the frost narwhal. They're only here until January sixth.", [Z('s_w_f_narwhal')], 'FROST *NARWHAL', {'sfx': 'reveal4'}),
        ("Which one do you want? " + END17, [Z('s_w_fish', 2.0)], '')]),
    # ================= mtgames2# · YouTube @Roblox-ad5
    'cc16_m2': dict(prog=P16, speed=0.85, amb='day', lines=[
        ("Day sixteen: one player online in my Roblox fishing game right now.", [Z('s_w_snowman')], 'DAY 16 · *1 ONLINE', {'prog': True}),
        ("So I gave it a winter update, with six new winter fish.", [Z('s_w_fish')], '*6 WINTER FISH', {'sfx': 'reveal3'}),
        ("The rarest one is the frost narwhal.", [Z('s_w_f_narwhal')], 'FROST *NARWHAL', {'sfx': 'reveal4'}),
        ("Would you come catch one? " + END17, [Z('s_w_fish', 2.0)], '')]),
    # ================= mtfgams12 · YouTube
    'dx16_n': dict(speed=0.85, amb='night', lines=[
        ("Day sixteen: there's a Christmas island in my Roblox fishing game now.", [Z('s_w_poster')], 'DAY 16 · *XMAS ISLAND'),
        ("A giant Christmas tree, right between the bases.", [Z('s_w_overview')], 'GIANT *TREE', {'sfx': 'reveal3'}),
        ("At night, the lights glow and the snow keeps falling.", [Z('s_w_night')], 'COZY *NIGHTS'),
        ("Would you go fishing there? " + END17, [Z('s_w_poster', 2.0)], '')]),
}

POST_PLAN = [
    ('7181171', 'tiktok', [('cc16_tt', '17:33')]),
    ('7181171', 'youtube', [('cc16_yt', '17:33')]),
    ('7752397', 'tiktok', [('dx15_b', '16:09')]),
    ('7752397', 'youtube', [('dx15_yb', '16:00')]),
    ('7773777', 'tiktok', [('dx15_c', '16:15')]),
    ('7773777', 'instagram', [('dx15_ic', '16:15')]),
    ('7773777', 'youtube', [('dx16_yc', '16:15')]),
    ('7752416', 'youtube', [('cc16_m2', '16:21')]),
    ('7773832', 'youtube', [('dx16_n', '16:24')]),
]
