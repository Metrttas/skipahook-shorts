# Tagesdatei 11.11.2026 – 27 Videos im AE-Style, HIGH-END-Regeln (3–4 Beats, 5–7 Shots, ein Thema je Video, Loop-Endkarte):
#   18 Clean (k11_*) + 9 Day-X (cc7_* CCU Day 7, dx6_* Updating Day 6 B/C, dx7_* Updating Day 7 Mtrix-YT/mtfgams12).
#   python3 tools/promo/ae/ae.py tools/promo/ae/days/ae_1111.py all stills|render
# CCU (Creator Dashboard, Half-hourly average Last 1 day, 10.11. ~19:50 UTC): 2 (Vortag 5, Dashboard -56,4 %). Besuche 31,419, Favoriten 1,382,
#   games-API "updated" 2026-11-08 16:05 UTC -> Classic+/Legends NICHT veröffentlicht -> "coming in the next update" / "I coded".
# Neuigkeit (git 10.11.): Classic+ (klassisches Spiel zurück, Rework-Fortschritt bleibt), Legends of the Deep (4 Legenden Big Bertha/Old Whiskers/
#   Coral Empress/Frostjaw, Sichtungen alle 30 min 4 min lang mit x2 Chance, 3-Runden-Kampf, Trophäen-Wand), ASMR-Sounds.
# Clean-Themen rotiert: jedes Konto bekommt ein anderes Thema als am 10.11.; neue Startzeiten, neue Hooks.
E = {'end': True}
G = (5, 2, 1000)   # CCU gestern (5) -> heute (2), Ziel

VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'k11_a1': dict(kind='clean', music='fut_1111_f', segs=[
        ('koi_seq_1', 0.3, 4, 'WHY IS THE *WATER PINK?'),
        ('koi2_wall', 2.5, 4, ''), ('koi_seq_3', 1.0, 4, '*COSMIC KOI'), ('koi2_pillars', 4.0, 4, ''),
        ('koi_seq_3', 5.5, 4, ''), ('koi_hover', 0.0, 4, 'WORTH *THE WAIT?'),
        ('koi_seq_1', 3.5, 4, '', E)]),
    'cc7_tt': dict(kind='day', music='lof_1111_b', prog=G, lines=[
        ("Day seven of trying to reach one thousand CCU in my Roblox fishing game.", [('c06_dock_long', 0.5), ('c14_lake_long', 3.0)], 'DAY *7'),
        ("Today's average: two players.", [('c04_docktolake_long2', 0.5)], '# *PLAYERS', {'prog': True}),
        ("So I listened to you. The classic game is coming back.", [('c27_longcast2', 0.5)], 'CLASSIC *IS BACK'),
        ("Power bar, perfect casts, the fishing you liked. In the next update.", [('c26_cast_catch', 0.3), ('c29_holdup', 0.5)], 'NEXT *UPDATE'),
        ("Search Skip a Hook on Roblox. See you on day eight!", [('c06_dock_long', 5.0)], '')]),
    'k11_a2': dict(kind='clean', music='cin_1111_c', segs=[
        ('c15_temple_long', 4.0, 4, 'WHO BUILT *THIS?'),
        ('c16_trident_long', 1.0, 4, ''), ('c17_arch_long', 1.0, 4, '*SUNKEN TEMPLE'), ('c15_temple_short', 2.5, 4, ''),
        ('c16_trident_short', 1.0, 4, 'FISH *HERE?'),
        ('c15_temple_long', 8.0, 4, '', E)]),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'k11_ya1': dict(kind='clean', music='mtg_1111_a', segs=[
        ('c24_rift_long', 1.0, 4, 'RED WATER *MEANS RUN'),
        ('far_supernova', 2.0, 4, ''), ('far_secret_bite', 1.0, 4, '*SECRET BITE'), ('far2_supernova', 2.5, 4, ''),
        ('far_hold', 1.0, 4, 'SUPERNOVA *SHARK'), ('c24_rift_short', 2.5, 4, ''),
        ('c24_rift_long', 6.5, 4, '', E)]),
    'cc7_yt': dict(kind='day', music='lof_1011_e', prog=G, lines=[
        ("Day seven on my road to one thousand CCU.", [('c22_endgate_long', 1.5)], 'DAY *7'),
        ("The average fell to two. Yesterday it was five.", [('c19_islands_long', 6.0)], '# *PLAYERS', {'prog': True}),
        ("So I built something new. Legends of the Deep.", [('g_huge_rising2', 0.3), ('g_seagiant_bite_purple', 0.5)], 'LEGENDS *OF THE DEEP'),
        ("Four giant named fish, like Big Bertha and Frostjaw. Coming in the next update.", [('ancient_cutscene', 2.0), ('ancient_hold', 1.5)], '*4 LEGENDS'),
        ("Search Skip a Hook on Roblox. See you on day eight!", [('c22_endgate_long', 6.0)], '')]),
    'k11_ya2': dict(kind='clean', music='cin_0911_a', segs=[
        ('g_casts_night', 3.0, 4, 'ONE MORE *CAST...'),
        ('g_casts_lake', 3.0, 4, ''), ('t_calm_d', 5.0, 4, '*MIDNIGHT'), ('t_calm_c', 1.0, 4, ''),
        ('g_casts_night', 7.5, 4, 'THEN *BED. MAYBE.'),
        ('g_casts_night', 5.0, 4, '', E)]),

    # ================= B mtfgams · TikTok
    'k11_b1': dict(kind='clean', music='cin_1111_c', segs=[
        ('t_kraken_cave', 4.2, 4, 'THE LAKE *HAS A BOSS'),
        ('t_kraken_face', 1.5, 4, ''), ('t_kraken_tentacles', 1.5, 4, '*KRAKEN'), ('t_kraken_slam', 1.8, 3, ''),
        ('t_kraken_breach', 3.0, 3, 'WHOLE SERVER *VS IT'),
        ('t_kraken_cave', 6.5, 4, '', E)]),
    'dx6_b': dict(kind='day', music='lof_1111_f', lines=[
        ("Day six of updating my Roblox fishing game every day.", [('c14_lake_long', 5.0)], 'DAY *6'),
        ("I coded legend sightings.", [('g_huge_rising', 0.5)], 'LEGEND *SIGHTED'),
        ("Every thirty minutes, one legend swims in its zone for four minutes. Your chance to hook it doubles.", [('g_seagiant_bite', 0.3), ('g_exotic_bite', 0.5)], '*X2 CHANCE'),
        ("It comes in the next update.", [('c29_holdup', 2.5)], 'NEXT *UPDATE'),
        ("Search Skip a Hook on Roblox. See you on day seven!", [('c14_lake_long', 8.5)], '')]),
    'k11_b2': dict(kind='clean', music='jer_1111_g', segs=[
        ('aqua_giant_glass', 3.0, 4, 'IT DOES NOT *FIT'),
        ('aqua_giant_top', 3.0, 4, ''), ('aqua_giant_push', 1.0, 4, '*GIANT'), ('aqua_full_top_a', 1.0, 4, ''),
        ('aqua_full_push', 2.0, 4, ''), ('aqua_full_top_b', 2.0, 4, 'BIGGER *TANK?'),
        ('aqua_giant_glass', 6.0, 4, '', E)]),

    # ================= B mtfgams · YouTube
    'k11_yb1': dict(kind='clean', music='fut_1111_f', segs=[
        ('c19_islands_long', 5.0, 4, 'HOW FAR *DOES IT GO?'),
        ('c20_planet_long', 5.0, 4, ''), ('c21_obelisk_long', 1.0, 4, '*SPACE'), ('c25_cosmicsea_long', 1.0, 4, ''),
        ('c22_endgate_long', 6.0, 4, ''), ('c20_planet_short', 1.0, 4, 'END *GATE?'),
        ('c19_islands_long', 8.5, 4, '', E)]),
    'dx6_yb': dict(kind='day', music='lof_0911_d', lines=[
        ("Day six of updating my Roblox game every day.", [('c06_dock_long', 3.5)], 'DAY *6'),
        ("Hook a legend, and the fight has three rounds.", [('c28_reel', 0.5), ('c26_cast_catch', 5.5)], '*3 ROUNDS'),
        ("Lose, and it breaks free. Win, and it goes on a trophy wall at your base.", [('c29_holdup', 1.0), ('c02_basecircle_long', 1.0)], 'TROPHY *WALL'),
        ("I coded it this week. Next update.", [('c03_baserow_long2', 2.0)], 'COMING *SOON'),
        ("Search Skip a Hook on Roblox. See you on day seven!", [('c06_dock_long', 7.5)], '')]),
    'k11_yb2': dict(kind='clean', music='mtg_1011_b', segs=[
        ('c30_boat', 3.0, 4, 'NO SPEED *LIMIT'),
        ('c30_boat_short', 2.5, 4, ''), ('c30_boat', 7.0, 4, '*FULL SEND'), ('c12_garage_long', 8.0, 4, ''),
        ('c30_boat', 10.0, 4, 'WHICH BOAT *IS YOURS?'),
        ('c30_boat', 1.0, 4, '', E)]),

    # ================= C Mtrix · TikTok
    'k11_c1': dict(kind='clean', music='mtg_1111_a', segs=[
        ('g_casts_dock', 1.0, 4, 'GOLD WATER? *CAST NOW'),
        ('g_casts_dock2', 2.0, 4, ''), ('golden_shark_reveal', 2.95, 2, '*SECRET'), ('g_seagiant_bite_gold', 0.8, 4, ''),
        ('g_hold_confetti', 1.5, 4, 'SECRET *CATCH'), ('g_casts_dock', 8.0, 4, ''),
        ('g_casts_dock', 4.5, 4, '', E)]),
    'dx6_c': dict(kind='day', music='lof_1011_c', lines=[
        ("Day six of updating my Roblox fishing game every day.", [('c27_longcast1', 1.0)], 'DAY *6'),
        ("Big change. The classic game is coming back.", [('c27_longcast2', 3.0)], 'CLASSIC *IS BACK'),
        ("The power bar, perfect casts, and the reel fight.", [('c26_cast_catch', 0.5), ('c28_reel', 3.0)], '*PERFECT'),
        ("And your rework progress is not lost. It carries over.", [('c11_bench_long', 3.0)], 'NOTHING *LOST'),
        ("Search Skip a Hook on Roblox. See you on day seven!", [('c27_longcast1', 6.0)], '')]),
    'k11_c2': dict(kind='clean', music='jer_1011_d', segs=[
        ('c01_mapfly_long2', 0.5, 4, 'THIS IS *MY MAP'),
        ('c03_baserow_long2', 3.0, 4, ''), ('c04_docktolake_long2', 2.0, 4, '*THE LAKE'), ('c14_lake_short', 1.0, 4, ''),
        ('c05_zonesfly_short', 1.0, 4, ''), ('c06_dock_short', 1.0, 4, 'COME *FISH'),
        ('c01_mapfly_long2', 4.0, 4, '', E)]),

    # ================= C Mtrix · Instagram (REEL)
    'k11_ic1': dict(kind='clean', music='jer_1111_g', segs=[
        ('g_casts_perfect', 0.5, 4, 'ONE MORE *THROW'),
        ('g_perfect_cast', 0.3, 4, ''), ('g_casts_dock2', 5.0, 4, '*NIGHT SHIFT'), ('g_casts_perfect', 4.0, 4, ''),
        ('g_casts_dock2', 9.0, 4, ''), ('g_casts_perfect', 9.0, 4, 'YOUR *STREAK?'),
        ('g_casts_perfect', 2.5, 4, '', E)]),
    'dx6_ic': dict(kind='day', music='lof_1111_b', lines=[
        ("Day six of updating my Roblox game every day.", [('c23_lagoon_long', 3.0)], 'DAY *6'),
        ("Today was all about sound.", [('c28_reel', 1.5)], '*SOUND ON'),
        ("I rebuilt the skips, the cast, the bite and the reel, so every catch feels good.", [('c27_longcast2', 6.0), ('c26_cast_catch', 4.0)], '*ASMR'),
        ("You'll hear it in the next update.", [('c29_holdup', 3.0)], 'NEXT *UPDATE'),
        ("Search Skip a Hook on Roblox. See you on day seven!", [('c23_lagoon_long', 7.5)], '')]),
    'k11_ic2': dict(kind='clean', music='fut_0911_g', segs=[
        ('c27_longcast2', 1.5, 4, 'HOW FAR *CAN YOU CAST?'),
        ('c27_longcast2', 4.5, 4, ''), ('c27_longcast1', 2.0, 4, '*FURTHER'), ('c27_longcast1', 6.0, 4, ''),
        ('c23_lagoon_long', 1.0, 4, ''), ('c18_galleon_long', 2.0, 4, 'BEAT *THIS?'),
        ('c27_longcast2', 8.5, 4, '', E)]),

    # ================= C Mtrix · YouTube
    'k11_yc1': dict(kind='clean', music='jer_1111_g', segs=[
        ('t_main_walkup', 2.0, 4, 'JUST ONE *MORE CAST'),
        ('t_main_cast_skip', 2.0, 4, '*SKIP'), ('t_main_drill', 1.0, 4, ''), ('t_main_sea_flight', 3.0, 4, ''),
        ('t_main_flyover', 0.5, 4, ''), ('t_main_whale_splash', 1.0, 4, 'SEE *THAT?'),
        ('t_main_walkup', 3.2, 4, '', E)]),
    'dx7_yc': dict(kind='day', music='lof_1111_f', lines=[
        ("Day seven of updating my Roblox fishing game every day.", [('c05_zonesfly_long2', 2.0)], 'DAY *7'),
        ("Today I coded Legends of the Deep.", [('g_huge_rising', 0.3)], 'LEGENDS *OF THE DEEP'),
        ("Four named legends, each in its own zone. Big Bertha lives in the Lily Pond.", [('g_seagiant_bite_purple', 1.0), ('ancient_cutscene', 3.0)], 'BIG *BERTHA'),
        ("Old Whiskers, the Coral Empress and Frostjaw are waiting too. Next update.", [('c25_cosmicsea_long', 4.0)], '*3 MORE'),
        ("Search Skip a Hook on Roblox. See you on day eight!", [('c05_zonesfly_long2', 7.0)], '')]),
    'k11_yc2': dict(kind='clean', music='cin_1011_d', segs=[
        ('ancient_cutscene', 0.3, 4, 'DO NOT *LOOK DOWN'),
        ('g_huge_rising2', 1.0, 3, ''), ('g_seagiant_bite_purple', 2.5, 3, '*ANCIENT'), ('ancient_reveal', 3.0, 3, ''),
        ('ancient_hold', 2.0, 4, 'TOO *BIG?'),
        ('ancient_cutscene', 4.5, 4, '', E)]),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'k11_m1': dict(kind='clean', music='fut_1111_f', segs=[
        ('t_calm_b', 5.5, 4, 'NO RUSH. *JUST FISH'),
        ('t_enchant_sunset_a', 5.0, 4, ''), ('t_beat_lake_glide', 1.5, 4, '*SUNSET'), ('t_enchant_sunset_b', 3.5, 4, ''),
        ('t_calm_a', 7.5, 4, ''), ('t_beat_aerial', 2.0, 4, 'SAVE *THIS'),
        ('t_calm_b', 8.0, 4, '', E)]),
    'cc7_m2': dict(kind='day', music='lof_0911_a', prog=G, lines=[
        ("Day seven of trying to reach one thousand CCU.", [('c13_pete_long', 1.0)], 'DAY *7'),
        ("Average today: two. But over thirty one thousand visits.", [('c02_basecircle_long', 6.0)], '# *PLAYERS', {'prog': True}),
        ("Here is my plan. Every half hour, a legend shows up in the lake.", [('g_huge_rising', 0.2), ('c14_lake_long', 9.0)], 'LEGEND *SIGHTED'),
        ("Classic fishing plus legends. That's the next update.", [('c26_cast_catch', 5.0)], 'THE *PLAN'),
        ("Search Skip a Hook on Roblox. See you on day eight!", [('c13_pete_long', 7.0)], '')]),
    'k11_m2': dict(kind='clean', music='mtg_1111_a', segs=[
        ('c02_basecircle_short', 0.5, 4, 'MY BASE *AT DAY 7'),
        ('c07_aquarium_long', 6.0, 4, ''), ('c09_wheel_long', 6.0, 4, '*SPIN'), ('c08_fuse_long', 6.0, 4, ''),
        ('c10_enchant_long', 7.0, 4, ''), ('c11_bench_long', 7.5, 4, 'RATE *IT'),
        ('c02_basecircle_short', 3.0, 4, '', E)]),

    # ================= mtfgams12 · YouTube
    'k11_n1': dict(kind='clean', music='cin_1111_c', segs=[
        ('t_enchant_night_a', 1.6, 4, 'ENCHANT *AT MIDNIGHT'),
        ('t_enchant_night_b', 1.6, 4, ''), ('t_enchant_night_a', 4.0, 4, '*MAGIC'), ('t_enchant_night_b', 5.5, 4, ''),
        ('t_enchant_night_a', 6.2, 3, 'LUCKY *ROLL?'),
        ('t_enchant_night_b', 3.5, 4, '', E)]),
    'dx7_n': dict(kind='day', music='lof_1011_e', lines=[
        ("Day seven of updating my Roblox game every day.", [('c28_reel', 2.0)], 'DAY *7'),
        ("Big news. The classic game is coming back.", [('c26_cast_short', 0.3)], 'CLASSIC *IS BACK'),
        ("Your progress from the rework carries over. Nothing gets reset.", [('c11_bench_long', 6.0), ('c03_baserow_long1', 4.0)], 'NO *RESET'),
        ("And I made the fishing sounds way more satisfying.", [('c26_cast_catch', 7.0)], '*SOUND ON'),
        ("Search Skip a Hook on Roblox. See you on day eight!", [('c28_reel', 5.0)], '')]),
    'k11_n2': dict(kind='clean', music='jer_0911_f', segs=[
        ('c26_cast_catch', 0.8, 4, 'WAIT *FOR THE BITE'),
        ('c26_cast_short', 1.0, 4, ''), ('c26_cast_catch', 5.0, 4, '*BITE'), ('c28_reel', 4.0, 4, ''),
        ('c29_holdup', 2.0, 4, ''), ('c26_cast_catch', 8.5, 4, 'NICE *ONE'),
        ('c26_cast_catch', 2.8, 4, '', E)]),
}

# Konto -> (Metricool-Blog, Netz, [(id, Uhrzeit)])
POST_PLAN = [
    ('7181171', 'tiktok', [('k11_a1', '12:03'), ('cc7_tt', '17:33'), ('k11_a2', '19:03')]),
    ('7181171', 'youtube', [('k11_ya1', '12:03'), ('cc7_yt', '17:33'), ('k11_ya2', '19:03')]),
    ('7752397', 'tiktok', [('k11_b1', '12:09'), ('dx6_b', '16:09'), ('k11_b2', '19:09')]),
    ('7752397', 'youtube', [('k11_yb1', '12:09'), ('dx6_yb', '16:00'), ('k11_yb2', '19:30')]),
    ('7773777', 'tiktok', [('k11_c1', '12:15'), ('dx6_c', '16:15'), ('k11_c2', '19:15')]),
    ('7773777', 'instagram', [('k11_ic1', '12:15'), ('dx6_ic', '16:15'), ('k11_ic2', '19:15')]),
    ('7773777', 'youtube', [('k11_yc1', '12:15'), ('dx7_yc', '16:15'), ('k11_yc2', '19:15')]),
    ('7752416', 'youtube', [('k11_m1', '12:21'), ('cc7_m2', '16:21'), ('k11_m2', '19:21')]),
    ('7773832', 'youtube', [('k11_n1', '12:24'), ('dx7_n', '16:24'), ('k11_n2', '19:24')]),
]
