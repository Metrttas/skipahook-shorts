# Tagesdatei 09.11.2026 – 27 Videos im AE-Style (User 08.11.: alles wie SkipAHook_Beispiel_AE.mp4):
#   18 Clean (k09_*) + 9 Day-X (cc5_* CCU Day 5, dx4_* Updating Day 4 B/C, dx5_* Updating Day 5 Mtrix-YT/mtfgams12).
#   python3 tools/promo/ae/ae.py tools/promo/ae/days/ae_1109.py all stills|render
# CCU (Creator Dashboard, Half-hourly average Last 1 day, 08.11. 20:0x UTC): 10 (Vortag 11). Besuche 30,977, Favoriten 1,365,
#   games-API "updated" 2026-11-08 16:05 UTC, Name "Skip a Hook [REWORK]".
# Neuigkeit (git 17e65c2, 08.11. abends): A-Paket GESCHRIEBEN + getestet, aber NOCH NICHT im Spiel eingebaut -> "I'm coding / next update":
#   Geschenk-Truhe (Wooden Rod, x2 Power) für Neue, Ranglisten SKIPS TODAY + TOP POWER statt Robux-Ranglisten, Funnel (wo hören Neue auf),
#   "+N"-Zahlen aus einem Pool (weniger Lag). Clips zeigen weiter das ALTE Spiel (keine Rework-Aufnahmen).
E = {'end': True}
G = (11, 10, 1000)   # CCU gestern (11) -> heute (10), Ziel

VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'k09_a1': dict(kind='clean', music='mtg_0911_e', segs=[
        ('c26_cast_short', 0.3, 4, 'ONE *CAST'),
        ('t_main_cast_skip', 2.0, 2, '*SKIP'), ('c27_longcast2', 3.5, 2, '*SKIP'), ('g_perfect_cast', 0.0, 2, '*SKIP...'),
        ('t_beat_aerial', 0.5, 3, 'HOW FAR *NOW?'), ('c04_docktolake_short', 1.0, 3, ''), ('far2_meter_c', 3.0, 4, 'KEEP *GOING'),
        ('c26_cast_short', 0.0, 4, '', E)]),
    'cc5_tt': dict(kind='day', music='lof_0911_d', prog=G, lines=[
        ("Day five of trying to reach one thousand CCU in my Roblox fishing game.", [('c05_zonesfly_long2', 3.5), ('t_beat_aerial', 0.5)], 'DAY *5'),
        ("Today's average: ten players. One less than yesterday.", [('c03_baserow_short', 0.5)], '# *PLAYERS', {'prog': True}),
        ("So tonight I coded a gift chest for every new player.", [('c08_fuse_short', 0.5), ('g_hold_confetti', 0.5)], 'GIFT *CHEST'),
        ("It pops open and gives you a free wooden rod.", [('c29_holdup', 0.5)], 'FREE *ROD'),
        ("Search Skip a Hook on Roblox. See you on day six!", [('c14_lake_short', 0.5)], '')]),
    'k09_a2': dict(kind='clean', music='fut_0911_g', segs=[
        ('whale_chase_2', 2.0, 4, 'IT PULLED *MY BOAT'),
        ('whale2_ride_b', 3.0, 2, ''), ('whale_title', 1.5, 2, '*WHALE'), ('whale2_ride_a', 5.0, 2, ''),
        ('t_main_whale_jump', 0.0, 2, ''), ('whale_finale_jump', 1.0, 3, '*TITANIC'), ('whale2_card_titanic', 2.0, 3, ''),
        ('whale_chase_2', 0.5, 4, '', E)]),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'k09_ya1': dict(kind='clean', music='cin_0911_a', segs=[
        ('t_kraken_title', 0.8, 4, 'IT WOKE *UP'),
        ('t_beat_kraken_face', 0.0, 2, ''), ('t_kraken_roar', 0.3, 2, '*KRAKEN'), ('t_beat_kraken_tentacles', 0.0, 2, ''),
        ('t_beat_kraken_slam', 0.0, 2, 'HIT *IT'), ('t_beat_minikraken', 0.0, 2, ''),
        ('t_kraken_title', 3.0, 4, '', E)]),
    'cc5_yt': dict(kind='day', music='lof_0911_a', prog=G, lines=[
        ("Day five on my road to one thousand CCU.", [('t_main_walkup', 1.5), ('c06_dock_short', 0.5)], 'DAY *5'),
        ("The average today is ten. Yesterday it was eleven.", [('aqua_full_top_a', 0.5)], '# *PLAYERS', {'prog': True}),
        ("So I'm fixing the first minutes for new players.", [('c02_basecircle_short', 0.3), ('c13_pete_short', 0.5)], 'FIRST *MINUTES'),
        ("Every step a new player takes is tracked now, so I can see where people quit.", [('c11_bench_short', 2.0), ('c15_temple_short', 0.5)], 'WHERE *PEOPLE QUIT'),
        ("Search Skip a Hook on Roblox. See you on day six!", [('c19_islands_short', 0.5)], '')]),
    'k09_ya2': dict(kind='clean', music='jer_0911_f', segs=[
        ('koi_seq_2', 1.0, 4, 'THIS FISH IS *COSMIC'),
        ('koi_hover', 0.2, 2, ''), ('koi2_leap_counter', 1.0, 3, 'ULTRA *RARE'), ('koi2_title', 3.0, 2, ''),
        ('koi_seq_3', 2.0, 2, '*KOI'), ('koi2_splash_hover', 4.0, 3, ''), ('koi_seq_2', 6.0, 2, ''),
        ('koi_seq_2', 0.4, 4, '', E)]),

    # ================= B mtfgams · TikTok
    'k09_b1': dict(kind='clean', music='mtg_0811_g', segs=[
        ('g_hud_secret_bite_pink', 0.5, 4, 'PINK *BITE...'),
        ('g_pink_burst', 0.3, 2, '*SECRET'), ('g_pink_pillar_fishing', 3.0, 2, ''), ('g_exotic_bite', 0.5, 2, ''),
        ('g_mutation_bite', 0.5, 2, '*MUTATION'), ('g_mutation_goldfish', 2.5, 2, ''), ('g_pink_pillar_fishing', 7.0, 2, 'WOULD YOU *KEEP IT?'),
        ('g_hud_secret_bite_pink', 0.0, 4, '', E)]),
    'dx4_b': dict(kind='day', music='lof_0811_f', lines=[
        ("Day four of updating my Roblox fishing game every day.", [('c01_mapfly_short', 1.0), ('t_zones_title', 0.3)], 'DAY *4'),
        ("Today I coded new leaderboards.", [('c03_baserow_long1', 1.0)], 'NEW *BOARDS'),
        ("The Robux boards are gone. Now it's most skips today, and top power.", [('t_main_cast_skip', 0.5), ('c11_bench_short', 1.5)], 'SKIPS *TODAY'),
        ("Anyone can be number one, just by playing.", [('c28_reel', 1.0)], 'JUST *PLAY'),
        ("Search Skip a Hook on Roblox. See you on day five!", [('c22_endgate_short', 0.5)], '')]),
    'k09_b2': dict(kind='clean', music='jer_0811_e', segs=[
        ('t_zones_temple', 1.2, 4, 'EVERY ZONE *IS FURTHER'),
        ('t_zones_statue', 0.5, 2, ''), ('t_zones_wreck', 0.2, 2, ''), ('t_zones_lagoon', 0.2, 2, ''), ('t_zones_ring', 0.2, 2, ''),
        ('t_zones_obelisk', 0.2, 2, ''), ('c20_planet_short', 1.0, 3, 'LAST ONE *HAS NO END'), ('c22_endgate_short', 1.0, 3, ''),
        ('t_zones_temple', 2.5, 4, '', E)]),

    # ================= B mtfgams · YouTube
    'k09_yb1': dict(kind='clean', music='cin_0811_g', segs=[
        ('g_huge_rising', 0.3, 4, 'WAIT FOR *IT...'),
        ('g_seagiant_bite_gold', 0.5, 2, ''), ('ancient_reveal', 1.2, 2, '*ANCIENT'), ('ancient_hold', 0.5, 2, ''),
        ('g_hud_colossal_meg', 2.0, 2, '*COLOSSAL'), ('golden_shark_reveal', 2.95, 2, ''),
        ('g_huge_rising', 2.5, 4, '', E)]),
    'dx4_yb': dict(kind='day', music='lof_0911_a', lines=[
        ("Day four of updating my Roblox game every day.", [('t_enchant_sunset_a', 2.0)], 'DAY *4'),
        ("New players will get a gift chest.", [('c07_aquarium_short', 0.5)], 'GIFT *CHEST'),
        ("It shakes three times, then opens by itself. Inside: a wooden rod with double power.", [('c33_rodcase', 2.0), ('c29_holdup', 1.0)], 'X2 *POWER'),
        ("It's coded and tested. It goes in with the next update.", [('c10_enchant_short', 0.5)], 'NEXT *UPDATE'),
        ("Search Skip a Hook on Roblox. See you on day five!", [('t_enchant_sunset_b', 2.5)], '')]),
    'k09_yb2': dict(kind='clean', music='fut_0811_b', segs=[
        ('c18_galleon_long', 2.0, 4, 'MY BOAT *COLLECTION'),
        ('c18_galleon_short', 1.0, 2, ''), ('boat_garage', 2.0, 2, ''), ('c12_garage_short', 2.5, 2, ''),
        ('c30_boat_short', 0.5, 2, '*FAST'), ('t_zones_boats', 0.5, 2, ''), ('c30_boat_short', 2.8, 2, ''), ('c18_galleon_long', 7.0, 3, 'PICK *ONE'),
        ('c18_galleon_long', 0.5, 4, '', E)]),

    # ================= C Mtrix · TikTok
    'k09_c1': dict(kind='clean', music='jer_0911_f', segs=[
        ('aqua_full_push', 0.5, 4, 'MY *AQUARIUM'),
        ('aqua_full_low', 1.0, 2, ''), ('aqua_giant_push', 3.0, 2, '*TOO BIG'), ('aqua_full_top_b', 1.0, 2, ''),
        ('aqua_giant_glass', 4.0, 2, ''), ('c07_aquarium_short', 1.0, 2, ''), ('aqua_full_top_a', 3.0, 3, 'RATE IT *1-10'),
        ('aqua_full_push', 4.0, 4, '', E)]),
    'dx4_c': dict(kind='day', music='lof_0811_b', lines=[
        ("Day four of updating my Roblox fishing game every day.", [('c17_arch_short', 0.5), ('c16_trident_long', 3.0)], 'DAY *4'),
        ("I want new players to never feel lost.", [('c04_docktolake_short', 0.5)], 'NEVER *LOST'),
        ("So the game now tracks eleven steps, from first cast to coming back on day two.", [('c26_cast_short', 0.5), ('c21_obelisk_short', 0.5)], '11 *STEPS'),
        ("Then I fix the step where most people quit.", [('c14_lake_short', 1.0)], 'FIX *IT'),
        ("Search Skip a Hook on Roblox. See you on day five!", [('c25_cosmicsea_short', 0.5)], '')]),
    'k09_c2': dict(kind='clean', music='cin_0811_g', segs=[
        ('t_calm_e', 0.2, 4, 'COZY *NIGHT'),
        ('t_enchant_night_a', 2.0, 2, ''), ('t_enchant_night_b', 2.5, 2, ''), ('g_casts_night', 4.0, 2, '*CHILL'),
        ('t_main_underwater', 0.3, 2, ''), ('t_enchant_night_a', 5.5, 2, ''),
        ('t_enchant_night_b', 5.5, 4, '', E)]),

    # ================= C Mtrix · Instagram (REEL)
    'k09_ic1': dict(kind='clean', music='mtg_0911_e', segs=[
        ('c32_baitshop', 1.0, 4, 'BAIT *SHOP'),
        ('c35_store', 1.0, 2, ''), ('ui_luck', 0.5, 2, '*LUCK'), ('c09_wheel_short', 0.5, 2, ''),
        ('ui_rodcase_open2', 3.0, 2, ''), ('c31_goldenhour', 2.0, 3, 'MORE *LUCK?'), ('c32_baitshop', 5.0, 3, ''),
        ('c32_baitshop', 0.2, 4, '', E)]),
    'dx4_ic': dict(kind='day', music='lof_0911_d', lines=[
        ("Day four of updating my Roblox game every day.", [('c15_temple_short', 0.5), ('t_beat_showcase', 0.0)], 'DAY *4'),
        ("Every skip shows a little plus number.", [('c27_longcast1', 4.0)], '*+1'),
        ("Before, each one was a new object. Lots of skips meant lag.", [('g_casts_perfect', 3.0)], 'NO MORE *LAG'),
        ("Now they come from a small pool and get reused. Smoother on phones.", [('c28_reel', 3.0), ('c06_dock_short', 1.0)], '*SMOOTHER'),
        ("Search Skip a Hook on Roblox. See you on day five!", [('c23_lagoon_short', 0.5)], '')]),
    'k09_ic2': dict(kind='clean', music='fut_0811_b', segs=[
        ('cosmic_dragon_reveal', 3.2, 4, 'EDGE OF *THE MAP'),
        ('c25_cosmicsea_short', 1.0, 2, ''), ('cosmic_dragon_hold', 1.0, 2, '*DRAGON'), ('c24_rift_short', 1.0, 2, ''),
        ('t_beat_rift_jaws', 0.0, 2, ''), ('c20_planet_short', 2.5, 2, ''), ('c25_cosmicsea_short', 3.0, 3, 'WOULD YOU *GO?'), ('cosmic_dragon_reveal', 4.0, 2, ''),
        ('cosmic_dragon_hold', 3.0, 4, '', E)]),

    # ================= C Mtrix · YouTube
    'k09_yc1': dict(kind='clean', music='fut_0911_g', segs=[
        ('far2_bite_catch', 1.0, 4, 'SO FAR *OUT'),
        ('far2_meter_d', 4.0, 2, ''), ('far_meter_b', 5.0, 2, ''), ('far_hold', 0.5, 2, '*SECRET'),
        ('far2_meter_e', 6.0, 2, ''), ('far_hold2', 1.0, 2, ''), ('far2_meter_d', 8.0, 2, ''), ('far2_bite_catch', 6.0, 3, 'GO *FURTHER'),
        ('far2_bite_catch', 0.2, 4, '', E)]),
    'dx5_yc': dict(kind='day', music='lof_0811_f', lines=[
        ("Day five of updating my Roblox fishing game every day.", [('c01_mapfly_long1', 3.0)], 'DAY *5'),
        ("Today I worked on the first minute.", [('c26_cast_short', 0.5)], 'FIRST *MINUTE'),
        ("New players will get a gift chest with a wooden rod, and their first catch says lucky!", [('c08_fuse_short', 0.5), ('g_hold_confetti', 0.5)], '*LUCKY!'),
        ("The leaderboards now show skips today instead of Robux.", [('c03_baserow_short', 0.5)], 'SKIPS *TODAY'),
        ("Search Skip a Hook on Roblox. See you on day six!", [('c05_zonesfly_short', 0.5)], '')]),
    'k09_yc2': dict(kind='clean', music='mtg_0811_g', segs=[
        ('c16_trident_long', 1.0, 4, 'NEW *ZONE?'),
        ('c17_arch_long', 2.0, 2, ''), ('c21_obelisk_short', 1.0, 2, ''), ('c16_trident_short', 1.0, 2, '*TRIDENT'),
        ('c15_temple_long', 4.0, 2, ''), ('c17_arch_short', 1.5, 2, ''), ('c19_islands_short', 1.0, 3, 'WHICH ONE *NEXT?'),
        ('c16_trident_long', 7.0, 4, '', E)]),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'k09_m1': dict(kind='clean', music='cin_0911_a', segs=[
        ('c13_pete_long', 1.0, 4, 'OLD *PETE'),
        ('pete_dock', 2.0, 2, ''), ('c13_pete_short', 1.0, 2, ''), ('ui_pete_window', 3.0, 2, '8 *HOURS'),
        ('c06_dock_long', 2.0, 2, ''), ('c13_pete_long', 6.0, 2, ''),
        ('c13_pete_long', 0.2, 4, '', E)]),
    'cc5_m2': dict(kind='day', music='lof_0811_b', prog=G, lines=[
        ("Day five of trying to reach one thousand CCU.", [('c05_zonesfly_short', 0.5), ('t_zones_endgate', 0.3)], 'DAY *5'),
        ("Average today: ten. Almost thirty one thousand visits, and over thirteen hundred favorites.", [('c02_basecircle_short', 0.5), ('aqua_full_low', 0.5)], '# *PLAYERS', {'prog': True}),
        ("I'm also changing the leaderboards. No more Robux boards.", [('c03_baserow_long2', 2.0)], 'NO *ROBUX'),
        ("Most skips today wins. Fair for everyone.", [('t_main_cast_skip', 3.0)], '*FAIR'),
        ("Search Skip a Hook on Roblox. See you on day six!", [('c22_endgate_long', 6.0)], '')]),
    'k09_m2': dict(kind='clean', music='jer_0911_f', segs=[
        ('ancient_cutscene', 0.5, 4, 'THE SEA *WOKE UP'),
        ('g_seagiant_bite_purple', 0.5, 2, ''), ('ancient_reveal', 1.5, 2, ''), ('g_huge_rising2', 0.5, 2, '*ANCIENT'),
        ('t_beat_dive', 0.0, 2, ''), ('ancient_hold', 1.5, 2, ''), ('g_seagiant_bite', 1.5, 3, 'COULD YOU *CATCH IT?'),
        ('ancient_cutscene', 3.0, 4, '', E)]),

    # ================= mtfgams12 · YouTube
    'k09_n1': dict(kind='clean', music='fut_0911_g', segs=[
        ('c09_wheel_long', 1.0, 4, 'SPIN *THE WHEEL'),
        ('c09_wheel_short', 2.0, 2, ''), ('ui_playtime', 2.0, 2, ''), ('c09_wheel_long', 5.0, 2, '*JACKPOT?'),
        ('ui_pass_claimall', 3.0, 2, ''), ('c34_fishingpass', 2.0, 3, ''), ('c09_wheel_long', 8.0, 3, ''),
        ('c09_wheel_long', 0.3, 4, '', E)]),
    'dx5_n': dict(kind='day', music='lof_0911_d', lines=[
        ("Day five of updating my Roblox game every day.", [('t_calm_e', 0.0), ('c06_dock_short', 1.5)], 'DAY *5'),
        ("Two new leaderboards: skips today, and top power.", [('c11_bench_long', 6.0)], 'TOP *POWER'),
        ("Skips today resets every day, so tomorrow you can be first.", [('c27_longcast2', 6.0)], 'RESETS *DAILY'),
        ("And new players get a free rod from a gift chest.", [('c29_holdup', 2.5)], 'FREE *ROD'),
        ("Search Skip a Hook on Roblox. See you on day six!", [('c14_lake_long', 6.0)], '')]),
    'k09_n2': dict(kind='clean', music='mtg_0911_e', segs=[
        ('g_hud_cast_skips', 2.0, 4, 'COUNT THE *SKIPS'),
        ('g_casts_dock', 6.0, 2, '*1'), ('g_casts_lake', 7.0, 2, '*2'), ('g_casts_perfect', 8.0, 2, '*3'),
        ('c27_longcast1', 8.0, 3, 'HOW MANY *CAN YOU?'), ('g_hud_cast2', 4.0, 3, ''),
        ('g_hud_cast_skips', 0.5, 4, '', E)]),
}

# Konto -> (Metricool-Blog, Netz, [(id, Uhrzeit)])
POST_PLAN = [
    ('7181171', 'tiktok', [('k09_a1', '12:03'), ('cc5_tt', '17:33'), ('k09_a2', '19:03')]),
    ('7181171', 'youtube', [('k09_ya1', '12:03'), ('cc5_yt', '17:33'), ('k09_ya2', '19:03')]),
    ('7752397', 'tiktok', [('k09_b1', '12:09'), ('dx4_b', '16:09'), ('k09_b2', '19:09')]),
    ('7752397', 'youtube', [('k09_yb1', '12:09'), ('dx4_yb', '16:00'), ('k09_yb2', '19:30')]),
    ('7773777', 'tiktok', [('k09_c1', '12:15'), ('dx4_c', '16:15'), ('k09_c2', '19:15')]),
    ('7773777', 'instagram', [('k09_ic1', '12:15'), ('dx4_ic', '16:15'), ('k09_ic2', '19:15')]),
    ('7773777', 'youtube', [('k09_yc1', '12:15'), ('dx5_yc', '16:15'), ('k09_yc2', '19:15')]),
    ('7752416', 'youtube', [('k09_m1', '12:21'), ('cc5_m2', '16:21'), ('k09_m2', '19:21')]),
    ('7773832', 'youtube', [('k09_n1', '12:24'), ('dx5_n', '16:24'), ('k09_n2', '19:24')]),
]
