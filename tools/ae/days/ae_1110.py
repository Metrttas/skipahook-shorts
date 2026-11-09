# Tagesdatei 10.11.2026 – 27 Videos im AE-Style, HIGH-END-Regeln (User 09.11.: Shots 3–4 Beats, 5–7 Shots, ein Thema je Video, Loop-Endkarte):
#   18 Clean (k10_*) + 9 Day-X (cc6_* CCU Day 6, dx5_* Updating Day 5 B/C, dx6_* Updating Day 6 Mtrix-YT/mtfgams12).
#   python3 tools/promo/ae/ae.py tools/promo/ae/days/ae_1110.py all stills|render
# CCU (Creator Dashboard, Half-hourly average Last 1 day, 09.11. 20:1x UTC): 5 (Vortag 10, Dashboard 50,1 %). Besuche 31,260, Favoriten 1,374,
#   games-API "updated" 2026-11-08 16:05 UTC (A-Paket weiter NICHT eingebaut).
# Neuigkeit: keine neuen Spiel-Commits seit 17e65c2 (A-Paket) -> Day-X erklären je EIN echtes Rework-R2-Feature (veröffentlicht 07./08.11.:
#   Combo x1..x3, Rod Stars 5 je Rang x1,08, Big Rank +10 % Power, Freunde-Boost +10 %/Freund max 4, Zone Mastered +10 % Geld + Welcome back)
#   bzw. den ehrlichen Plan: A-Paket kommt als Nächstes, danach WELT 2 (Idee "Upside Down Sea" = nur Idee).
E = {'end': True}
G = (10, 5, 1000)   # CCU gestern (10) -> heute (5), Ziel

VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'k10_a1': dict(kind='clean', music='fut_1011_c', segs=[
        ('t_calm_a', 1.5, 4, 'THIS VIEW *HITS DIFFERENT'),
        ('t_beat_aerial', 0.2, 4, ''), ('t_beat_lake_glide', 0.1, 4, '*SUNSET'), ('t_enchant_sunset_b', 1.0, 4, ''),
        ('t_calm_b', 3.0, 4, 'CHILL *FISHING'), ('t_enchant_sunset_a', 3.0, 4, ''),
        ('t_calm_a', 5.0, 4, '', E)]),
    'cc6_tt': dict(kind='day', music='lof_1011_e', prog=G, lines=[
        ("Day six of trying to reach one thousand CCU in my Roblox fishing game.", [('c14_lake_long', 1.0), ('c04_docktolake_long1', 1.0)], 'DAY *6'),
        ("Today's average: five players. Half of yesterday.", [('c06_dock_long', 3.0)], '# *PLAYERS', {'prog': True}),
        ("That hurts. But the next update is almost ready.", [('c13_pete_long', 3.0)], 'NOT *GIVING UP'),
        ("A gift chest for new players, and fair leaderboards.", [('c29_holdup', 1.5)], 'NEXT *UPDATE'),
        ("Search Skip a Hook on Roblox. See you on day seven!", [('c14_lake_long', 6.0)], '')]),
    'k10_a2': dict(kind='clean', music='cin_1011_d', segs=[
        ('t_kraken_cave', 3.2, 4, 'BOSS RAID *STARTS NOW'),
        ('t_kraken_tentacles', 0.3, 4, ''), ('t_kraken_face', 0.5, 4, '*KRAKEN'), ('t_kraken_breach', 2.6, 3, ''),
        ('t_kraken_slam', 0.5, 4, 'PULL *TOGETHER'),
        ('t_kraken_cave', 5.5, 4, '', E)]),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'k10_ya1': dict(kind='clean', music='jer_1011_d', segs=[
        ('c04_docktolake_long1', 0.5, 4, 'WELCOME TO *MY LAKE'),
        ('c14_lake_long', 2.0, 4, ''), ('c03_baserow_long1', 1.5, 4, '*BASES'), ('c06_dock_long', 1.0, 4, ''),
        ('c05_zonesfly_long2', 4.0, 4, 'HOW FAR *WOULD YOU GO?'), ('c14_lake_long', 7.0, 4, ''),
        ('c04_docktolake_long1', 3.5, 4, '', E)]),
    'cc6_yt': dict(kind='day', music='lof_1011_c', prog=G, lines=[
        ("Day six on my road to one thousand CCU.", [('c19_islands_long', 4.0)], 'DAY *6'),
        ("The average dropped to five. Yesterday it was ten.", [('c03_baserow_long2', 1.0)], '# *PLAYERS', {'prog': True}),
        ("So what comes after this update? World two.", [('c05_zonesfly_long2', 5.0)], 'WORLD *2'),
        ("A whole new world to fish in. That's the next big update.", [('c25_cosmicsea_long', 3.0), ('c22_endgate_long', 1.0)], 'NEW *WORLD'),
        ("Search Skip a Hook on Roblox. See you on day seven!", [('c19_islands_long', 8.0)], '')]),
    'k10_ya2': dict(kind='clean', music='mtg_1011_b', segs=[
        ('aqua_giant_top', 1.0, 4, 'TOO BIG FOR *MY TANK'),
        ('aqua_giant_push', 5.0, 4, ''), ('aqua_giant_glass', 1.0, 4, '*GIANTS'), ('aqua_full_glass', 3.0, 4, ''),
        ('aqua_full_low', 3.0, 4, 'RATE IT *1-10'),
        ('aqua_giant_top', 5.5, 4, '', E)]),

    # ================= B mtfgams · TikTok
    'k10_b1': dict(kind='clean', music='fut_0911_g', segs=[
        ('koi2_wall', 0.5, 4, 'THE SEA *WENT PINK'),
        ('koi_seq_1', 1.0, 4, ''), ('koi2_pillars', 2.0, 4, '*COSMIC'), ('koi_seq_3', 4.0, 4, ''),
        ('koi_hover', 0.2, 4, '1 IN *10,000,000'), ('koi2_splash_hover', 1.0, 4, ''),
        ('koi2_wall', 4.0, 4, '', E)]),
    'dx5_b': dict(kind='day', music='lof_0911_d', lines=[
        ("Day five of updating my Roblox fishing game every day.", [('c11_bench_long', 1.0)], 'DAY *5'),
        ("In the rework, I added rod stars.", [('c06_dock_long', 1.0)], 'ROD *STARS'),
        ("Every rod can get five stars. Each star makes it eight percent stronger.", [('c28_reel', 2.0), ('c27_longcast1', 4.0)], '*+8%'),
        ("So your favorite rod keeps growing with you.", [('c26_cast_short', 0.5)], 'KEEP *IT'),
        ("Search Skip a Hook on Roblox. See you on day six!", [('c11_bench_long', 6.0)], '')]),
    'k10_b2': dict(kind='clean', music='jer_0811_a', segs=[
        ('c27_longcast1', 0.5, 4, 'HOW FAR *CAN IT GO?'),
        ('c27_longcast1', 4.0, 4, ''), ('c27_longcast2', 1.0, 4, '*FURTHER'), ('c27_longcast2', 5.5, 4, ''),
        ('c24_rift_long', 2.0, 4, 'SHARK *RIFT'), ('c19_islands_long', 2.0, 4, ''),
        ('c27_longcast1', 8.0, 4, '', E)]),

    # ================= B mtfgams · YouTube
    'k10_yb1': dict(kind='clean', music='mtg_1011_b', segs=[
        ('g_hud_golden_shark', 0.3, 4, 'GOLD WATER *MEANS...'),
        ('golden_shark_reveal', 2.95, 2, '*SECRET'), ('g_seagiant_bite_gold', 0.5, 4, ''), ('g_hold_confetti', 0.5, 4, 'GOLDEN *SHARK'),
        ('g_casts_dock2', 2.0, 4, ''), ('g_casts_dock', 3.0, 4, 'SEEN IT *YET?'),
        ('g_hud_golden_shark', 1.5, 4, '', E)]),
    'dx5_yb': dict(kind='day', music='lof_1011_e', lines=[
        ("Day five of updating my Roblox game every day.", [('c03_baserow_long1', 2.0)], 'DAY *5'),
        ("Save up double the rank cost, and a new button shows up. Big rank.", [('c11_bench_long', 5.0), ('c02_basecircle_long', 2.0)], 'BIG *RANK'),
        ("It gives you ten percent more power, forever.", [('t_main_cast_skip', 1.0)], '+10% *FOREVER'),
        ("Patience pays off.", [('c13_pete_short', 1.0)], '*PATIENCE'),
        ("Search Skip a Hook on Roblox. See you on day six!", [('c03_baserow_long1', 5.5)], '')]),
    'k10_yb2': dict(kind='clean', music='cin_0911_a', segs=[
        ('c15_temple_long', 1.0, 4, 'A KINGDOM *UNDER WATER'),
        ('c17_arch_long', 5.0, 4, ''), ('c16_trident_long', 5.0, 4, '*TRIDENT'), ('c15_temple_short', 1.0, 4, ''),
        ('c17_arch_short', 1.0, 4, 'WOULD YOU *GO IN?'),
        ('c15_temple_long', 7.0, 4, '', E)]),

    # ================= C Mtrix · TikTok
    'k10_c1': dict(kind='clean', music='fut_1011_c', segs=[
        ('c05_zonesfly_long1', 4.0, 4, 'THE MAP *NEVER ENDS'),
        ('c19_islands_long', 2.0, 4, ''), ('c20_planet_long', 2.0, 4, '*COSMIC'), ('c21_obelisk_long', 4.0, 4, ''),
        ('c22_endgate_long', 2.0, 4, 'END *GATE'), ('c25_cosmicsea_long', 6.0, 4, ''),
        ('c05_zonesfly_long1', 6.5, 4, '', E)]),
    'dx5_c': dict(kind='day', music='lof_1011_c', lines=[
        ("Day five of updating my Roblox fishing game every day.", [('c02_basecircle_short', 0.5)], 'DAY *5'),
        ("Fishing with friends now makes you stronger.", [('c03_baserow_short', 1.0)], '*FRIENDS'),
        ("Every friend in your server gives ten percent more power. Up to four friends.", [('c06_dock_short', 1.0), ('c28_reel', 5.0)], '+10% *EACH'),
        ("So bring your friends.", [('c14_lake_long', 7.0)], 'BRING *THEM'),
        ("Search Skip a Hook on Roblox. See you on day six!", [('c02_basecircle_long', 4.0)], '')]),
    'k10_c2': dict(kind='clean', music='cin_0811_c', segs=[
        ('g_casts_lake', 1.0, 4, 'FISHING AT *3AM'),
        ('g_casts_night', 1.0, 4, ''), ('t_calm_c', 4.0, 4, '*NIGHT'), ('t_calm_d', 2.0, 4, ''),
        ('g_casts_lake', 6.0, 4, 'STILL *AWAKE?'),
        ('g_casts_lake', 9.0, 4, '', E)]),

    # ================= C Mtrix · Instagram (REEL)
    'k10_ic1': dict(kind='clean', music='cin_1011_d', segs=[
        ('ancient_cutscene', 1.0, 4, 'SOMETHING *ANCIENT'),
        ('g_seagiant_bite_purple', 1.5, 3, ''), ('g_huge_rising2', 0.5, 3, ''), ('ancient_reveal', 2.4, 3, '*MEGALODON'),
        ('ancient_hold', 1.3, 4, 'COULD YOU *HOLD IT?'),
        ('ancient_cutscene', 3.5, 4, '', E)]),
    'dx5_ic': dict(kind='day', music='lof_0811_g', lines=[
        ("Day five of updating my Roblox game every day.", [('c23_lagoon_long', 6.0)], 'DAY *5'),
        ("When you master a zone, you get a big banner. Zone mastered.", [('c15_temple_long', 8.0)], 'ZONE *MASTERED'),
        ("And ten percent more cash, for good.", [('c07_aquarium_long', 2.0)], '+10% *CASH'),
        ("Plus, when you come back, your offline cash is waiting.", [('c06_dock_long', 8.0)], 'WELCOME *BACK'),
        ("Search Skip a Hook on Roblox. See you on day six!", [('c23_lagoon_long', 1.0)], '')]),
    'k10_ic2': dict(kind='clean', music='mtg_0811_c', segs=[
        ('c02_basecircle_long', 1.0, 4, 'RATE MY *BASE'),
        ('c07_aquarium_long', 3.0, 4, ''), ('c11_bench_long', 2.0, 4, '*BENCH'), ('c09_wheel_long', 3.0, 4, ''), ('c08_fuse_long', 2.0, 3, ''),
        ('c10_enchant_long', 3.0, 4, 'OUT OF *10?'),
        ('c02_basecircle_long', 6.5, 4, '', E)]),

    # ================= C Mtrix · YouTube
    'k10_yc1': dict(kind='clean', music='jer_1011_d', segs=[
        ('c30_boat', 1.0, 4, 'FULL SPEED *AHEAD'),
        ('c30_boat', 5.0, 4, ''), ('c30_boat_short', 1.0, 4, '*SPEEDBOAT'), ('c12_garage_long', 6.5, 4, ''),
        ('boat_garage', 5.0, 4, 'PICK *YOUR BOAT'), ('c30_boat', 8.5, 4, ''),
        ('c30_boat', 2.5, 4, '', E)]),
    'dx6_yc': dict(kind='day', music='lof_1011_e', lines=[
        ("Day six of updating my Roblox fishing game every day.", [('c05_zonesfly_long1', 5.0)], 'DAY *6'),
        ("Today I'm planning the next big update. World two.", [('c22_endgate_long', 4.0)], 'WORLD *2'),
        ("One idea I have: an upside down sea.", [('c25_cosmicsea_long', 5.0)], 'UPSIDE *DOWN?'),
        ("But first, the gift chest update goes in. Then world two.", [('c29_holdup', 1.0), ('c19_islands_long', 3.0)], 'STEP *BY STEP'),
        ("Search Skip a Hook on Roblox. See you on day seven!", [('c05_zonesfly_long1', 7.5)], '')]),
    'k10_yc2': dict(kind='clean', music='fut_0811_d', segs=[
        ('far_supernova', 0.5, 4, 'THE WATER *TURNED RED'),
        ('far2_supernova', 0.5, 4, ''), ('far_secret_bite', 0.5, 4, '*SECRET'), ('far_hold', 0.3, 4, 'SUPERNOVA *SHARK'),
        ('c24_rift_long', 5.0, 4, ''), ('c24_rift_short', 1.0, 4, 'SHARK *RIFT'),
        ('far_supernova', 3.5, 4, '', E)]),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'k10_m1': dict(kind='clean', music='mtg_0911_e', segs=[
        ('c26_cast_catch', 0.3, 4, 'FIRST CAST *OF THE DAY'),
        ('c26_cast_catch', 4.5, 4, ''), ('c26_cast_catch', 8.0, 4, '*CAUGHT IT'), ('c29_holdup', 1.0, 4, ''),
        ('c28_reel', 2.0, 4, 'ONE *MORE?'),
        ('c26_cast_catch', 2.2, 4, '', E)]),
    'cc6_m2': dict(kind='day', music='lof_0911_a', prog=G, lines=[
        ("Day six of trying to reach one thousand CCU.", [('t_calm_b', 1.0)], 'DAY *6'),
        ("Average today: five. But over thirty one thousand visits, and almost fourteen hundred favorites.", [('c02_basecircle_long', 4.0), ('aqua_full_glass', 2.0)], '# *PLAYERS', {'prog': True}),
        ("Thank you to everyone who played this week.", [('c06_dock_long', 6.0)], 'THANK *YOU'),
        ("Every favorite tells me to keep going.", [('c13_pete_long', 6.0)], 'KEEP *GOING'),
        ("Search Skip a Hook on Roblox. See you on day seven!", [('t_calm_b', 5.0)], '')]),
    'k10_m2': dict(kind='clean', music='cin_1011_d', segs=[
        ('t_enchant_night_b', 2.0, 4, 'MAGIC *ROD'),
        ('t_enchant_night_a', 2.0, 4, '*ENCHANT IT'), ('ui_enchant', 1.0, 4, 'LUCKY *OR STORM?'), ('ui_enchant', 5.0, 3, ''),
        ('t_enchant_night_a', 5.2, 4, ''),
        ('t_enchant_night_b', 4.5, 4, '', E)]),

    # ================= mtfgams12 · YouTube
    'k10_n1': dict(kind='clean', music='jer_0911_f', segs=[
        ('t_main_walkup', 1.5, 4, 'GRAB *YOUR ROD'),
        ('t_main_cast_skip', 1.0, 4, '*SKIP'), ('t_main_sea_flight', 1.0, 4, ''), ('t_main_flyover', 2.0, 4, ''),
        ('t_main_drill', 2.0, 4, 'BIG *ONE'), ('t_main_whale_splash', 0.5, 4, ''),
        ('t_main_walkup', 2.6, 4, '', E)]),
    'dx6_n': dict(kind='day', music='lof_1011_c', lines=[
        ("Day six of updating my Roblox game every day.", [('c28_reel', 1.0)], 'DAY *6'),
        ("Let's talk about combos.", [('c26_cast_short', 1.0)], '*COMBO'),
        ("Catch fish in a row, and your cash goes up, all the way to times three.", [('c26_cast_catch', 5.0), ('c29_holdup', 3.0)], 'UP TO *X3'),
        ("Take a long break, and the combo is gone.", [('c27_longcast1', 2.0)], "DON'T *STOP"),
        ("Search Skip a Hook on Roblox. See you on day seven!", [('c28_reel', 5.0)], '')]),
    'k10_n2': dict(kind='clean', music='fut_1011_c', segs=[
        ('g_casts_dock2', 1.0, 4, 'PERFECT *EVERY TIME?'),
        ('g_perfect_cast', 0.0, 4, ''), ('g_casts_perfect', 2.0, 4, '*PERFECT'), ('g_casts_dock', 6.0, 4, ''),
        ('g_casts_perfect', 7.0, 4, 'CAN YOU *DO IT?'), ('g_casts_dock2', 7.5, 4, ''),
        ('g_casts_dock2', 4.0, 4, '', E)]),
}

# Konto -> (Metricool-Blog, Netz, [(id, Uhrzeit)])
POST_PLAN = [
    ('7181171', 'tiktok', [('k10_a1', '12:03'), ('cc6_tt', '17:33'), ('k10_a2', '19:03')]),
    ('7181171', 'youtube', [('k10_ya1', '12:03'), ('cc6_yt', '17:33'), ('k10_ya2', '19:03')]),
    ('7752397', 'tiktok', [('k10_b1', '12:09'), ('dx5_b', '16:09'), ('k10_b2', '19:09')]),
    ('7752397', 'youtube', [('k10_yb1', '12:09'), ('dx5_yb', '16:00'), ('k10_yb2', '19:30')]),
    ('7773777', 'tiktok', [('k10_c1', '12:15'), ('dx5_c', '16:15'), ('k10_c2', '19:15')]),
    ('7773777', 'instagram', [('k10_ic1', '12:15'), ('dx5_ic', '16:15'), ('k10_ic2', '19:15')]),
    ('7773777', 'youtube', [('k10_yc1', '12:15'), ('dx6_yc', '16:15'), ('k10_yc2', '19:15')]),
    ('7752416', 'youtube', [('k10_m1', '12:21'), ('cc6_m2', '16:21'), ('k10_m2', '19:21')]),
    ('7773832', 'youtube', [('k10_n1', '12:24'), ('dx6_n', '16:24'), ('k10_n2', '19:24')]),
]
