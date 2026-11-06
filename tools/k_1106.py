# Tagesdatei 06.11.2026 – 27 Videos: 18 Clean Edits (k06_*) + 9 Day-X (cc2_* CCU-Serie Day 2, dx_* Updating-Serie).
#   python3 tools/promo/motion/clean.py tools/promo/motion/days/k_1106.py all render
# CCU (Creator Dashboard, Half-hourly average Last 1 day, 05.11. 20:55): 8 (Vortag 10, -20,5 %). Besuche 28,840, Favoriten 1,285.
# Neuigkeiten = Update 217 "Core Loop 2.0" (Commits 05.11.): Freischalten (erste 5 min weniger Knöpfe), Morgen-Fang (morgen erster Wurf
#   garantiert Epic), Streak-Glück (+10 %/Tag, max +70 %), "Got away" (seltener Fisch reißt ab, nächster Wurf +50 % Glück), Ziel-Silhouette
#   ("undiscovered here"), Zonen-Leiste, Server-Event alle 15 min abwechselnd Fish Rush (2 min, Bisse 2x schneller) / Meteor Fish.
#   Eier sind AUS (217e) -> nicht erwähnen. Ob 217 schon live ist, ist unklar -> immer "I built", nie "now live".
# Musik: fresh_beats.py Varianten *_0611_* (nie derselbe Track zweimal je Account).

CUP = (0, 0)

VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'k06_a1': dict(kind='clean', music='mtg_0611_f', hook='POV: YOUR HOOK|*NEVER STOPS',
                   shots=[('t_main_cast_skip', 1.6, 4), ('c27_longcast1', 2.0, 2), ('c27_longcast1', 5.5, 2), ('t_beat_lake_glide', 0.3, 2),
                          ('t_zones_statue', 0.1, 2, 0.8), ('t_zones_skyisland', 1.4, 2), ('c27_longcast2', 4.0, 2), ('c22_endgate_long', 2.0, 2)],
                   texts=[(8, 12, '{0-15}|*ZONES'), (16, 20, 'HOW FAR|*CAN YOU GO?')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),
    'cc2_tt': dict(kind='day', music='lof_0611_c', day=2, tag='TO 1,000 CCU', lines=[
        "Day two of trying to reach one thousand CCU in my Roblox fishing game.",
        "Yesterday we averaged ten players. Today, eight. We went down.",
        "So today I built server events. Every fifteen minutes, a fish rush or a meteor fish.",
        "During a fish rush, fish bite twice as fast.",
        "Search Skip a Hook on Roblox. See you on day three!"],
        shots=[[('c01_mapfly_long2', 0.5)], [('c06_dock_long', 0.5)], [('t_main_underwater', 0.0), ('g_casts_perfect', 3.0)],
               [('c26_cast_catch', 4.2)], [('t_calm_a', 1.0)]],
        prog=dict(a=10, b=8, goal=1000, unit='CCU', line=1)),
    'k06_a2': dict(kind='clean', music='jer_0611_d', hook='WAIT FOR|*THE WHALE',
                   shots=[('t_calm_d', 1.0, 4), ('whale_chase_2', 1.5, 2), ('whale_chase_2', 5.0, 2), ('whale_chase_2', 8.5, 2),
                          ('t_main_whale_jump', 0.0, 3, 0.7), ('t_main_whale_splash', 0.4, 3), ('whale_finale_jump', 1.2, 4, 0.8)],
                   texts=[(14, 20, '1 IN|*{1-500000}')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'k06_ya1': dict(kind='clean', music='fut_0611_a', hook='THE SKY|*HAS FISH TOO',
                    shots=[('c19_islands_long', 1.0, 4), ('t_zones_skyisland', 0.8, 2), ('c19_islands_long', 6.0, 2), ('t_beat_lake_glide', 1.0, 2),
                           ('t_main_sea_flight', 1.5, 2), ('c19_islands_long', 8.5, 2), ('t_beat_dive', 0.2, 2), ('g_casts_perfect', 6.0, 2),
                           ('g_hold_confetti', 0.5, 2)],
                    texts=[(10, 14, '{0-40000000000} M|*UP THERE'), (18, 22, 'WOULD YOU|*FISH HERE?')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),
    'cc2_yt': dict(kind='day', music='lof_0611_g', day=2, tag='TO 1,000 CCU', lines=[
        "Day two of my road to one thousand CCU.",
        "The average dropped from ten players to eight.",
        "To fix that, I built a streak bonus. Every day you come back in a row, you get ten percent more luck.",
        "After a full week, that's plus seventy percent.",
        "Search Skip a Hook on Roblox. See you on day three!"],
        shots=[[('c03_baserow_long2', 0.5)], [('t_calm_b', 2.0)], [('c11_bench_long', 1.0), ('g_seagiant_bite_gold', 0.2)],
               [('cosmic_dragon_hold', 0.3)], [('c13_pete_long', 2.0)]],
        prog=dict(a=10, b=8, goal=1000, unit='CCU', line=1)),
    'k06_ya2': dict(kind='clean', music='cin_0611_e', hook='SOMETHING HUGE|*IS RISING',
                    shots=[('t_calm_c', 2.0, 4), ('g_huge_rising', 0.6, 2), ('g_huge_rising', 2.4, 2), ('cosmic_dragon_hold', 0.4, 3),
                           ('ancient_hold', 0.3, 3), ('t_main_whale_splash', 0.3, 2)],
                    texts=[(8, 11, 'SECRET|*1 IN {1-100000}')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),

    # ================= B mtfgams · TikTok
    'k06_b1': dict(kind='clean', music='mtg_0611_g', hook='COZY FISHING|*AT SUNSET',
                   shots=[('t_calm_a', 3.0, 4), ('t_calm_b', 1.0, 2), ('t_enchant_sunset_a', 2.5, 2), ('t_calm_e', 0.5, 2),
                          ('t_calm_b', 5.5, 2), ('t_beat_aerial', 0.5, 2), ('c03_baserow_long1', 1.0, 2), ('t_calm_c', 5.0, 2)],
                   texts=[(14, 20, 'RATE THE VIBE|*1-10')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),
    'dx_b': dict(kind='day', music='lof_0611_c', day=1, tag='UPDATING MY GAME', lines=[
        "Day one of updating my Roblox fishing game every day.",
        "This is update two hundred seventeen.",
        "Today I added something painful. Sometimes a really rare fish breaks your line and gets away.",
        "But your next cast gets fifty percent more luck.",
        "Search Skip a Hook on Roblox. See you on day two!"],
        shots=[[('c06_dock_long', 1.0)], [('c02_basecircle_long', 2.0)], [('t_main_drill', 0.5), ('g_exotic_bite', 0.0), ('g_seagiant_bite_gold', 0.3)],
               [('g_casts_perfect', 0.5)], [('c06_dock_long', 6.0)]]),
    'k06_b2': dict(kind='clean', music='cin_0611_e', hook='THE KRAKEN|*WOKE UP',
                   shots=[('t_kraken_tentacles', 0.3, 4), ('t_kraken_roar', 0.4, 2), ('t_kraken_face', 0.6, 2), ('t_beat_kraken_tug', 0.2, 2),
                          ('t_beat_minikraken', 0.1, 2), ('t_kraken_slam', 1.0, 2), ('t_beat_kraken_slam', 0.1, 2)],
                   texts=[(8, 12, '{0-100} HP|*BOSS RAID'), (14, 18, 'WHO WINS?')], end=(3, 'SKIP A HOOK', 'ON ROBLOX')),

    # ================= B mtfgams · YouTube
    'k06_yb1': dict(kind='clean', music='jer_0611_b', hook='MY AQUARIUM|*IS TOO SMALL',
                    shots=[('aqua_giant_push', 1.0, 4), ('aqua_giant_push', 4.5, 2), ('aqua_full_low', 1.0, 2), ('aqua_giant_glass', 2.0, 2),
                           ('koi_hover', 0.3, 2), ('aqua_full_low', 4.5, 2), ('aqua_giant_top', 4.0, 2), ('aqua_giant_glass', 6.0, 2)],
                    texts=[(8, 12, 'WHALE IN|*THE TANK'), (16, 20, 'WHAT WOULD|*YOU ADD?')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),
    'dx_yb': dict(kind='day', music='lof_0611_g', day=1, tag='UPDATING MY GAME', lines=[
        "Day one of updating my Roblox fishing game every day.",
        "Update two hundred seventeen.",
        "Today I built meteor fish. A meteor crashes into the lake.",
        "The first player to fish at that spot gets a rare fish.",
        "Search Skip a Hook on Roblox. See you on day two!"],
        shots=[[('c14_lake_long', 1.0)], [('c03_baserow_long1', 1.0)], [('t_main_sea_flight', 0.3), ('g_huge_rising', 0.3)],
               [('c26_cast_catch', 1.0), ('c29_holdup', 1.0)], [('t_calm_c', 0.5)]]),
    'k06_yb2': dict(kind='clean', music='fut_0611_a', hook='IS THERE AN END|*TO THIS MAP?',
                    shots=[('t_main_sea_flight', 0.3, 4), ('c25_cosmicsea_short', 0.3, 2), ('t_zones_ring', 0.2, 2), ('t_zones_obelisk', 0.2, 2),
                           ('c21_obelisk_short', 1.0, 2), ('c20_planet_long', 3.0, 2), ('t_zones_endgate', 0.3, 2), ('c22_endgate_long', 6.0, 4)],
                    texts=[(12, 16, 'THE COSMIC|*SEA'), (20, 24, 'THE END|*GATE')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),

    # ================= C Mtrix · TikTok
    'k06_c1': dict(kind='clean', music='jer_0611_d', hook='ONE CAST.|*EVERY ZONE.',
                   shots=[('c27_longcast1', 0.5, 4), ('c27_longcast1', 8.0, 2), ('c27_longcast2', 1.0, 2), ('t_zones_statue', 0.5, 2, 0.8),
                          ('c24_rift_short', 0.5, 2), ('c27_longcast2', 7.0, 2), ('t_zones_endgate', 1.0, 2), ('c25_cosmicsea_long', 3.0, 2)],
                   texts=[(8, 12, '{0-1000000000} M'), (16, 20, '*STILL FLYING')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),
    'dx_c': dict(kind='day', music='lof_0611_c', day=1, tag='UPDATING MY GAME', lines=[
        "Day one of updating my Roblox fishing game every day.",
        "Today: update two hundred seventeen.",
        "After ten minutes of fishing, you get a card. Come back tomorrow, and your first cast is a guaranteed epic.",
        "I want you to have a reason to come back.",
        "Search Skip a Hook on Roblox. See you on day two!"],
        shots=[[('c04_docktolake_long1', 0.5)], [('c07_aquarium_long', 2.0)], [('g_casts_dock2', 1.0), ('c29_holdup', 0.3)],
               [('t_calm_a', 4.0)], [('c06_dock_long', 5.0)]]),
    'k06_c2': dict(kind='clean', music='mtg_0611_f', hook='NIGHT FISHING|*HITS DIFFERENT',
                   shots=[('t_calm_c', 6.0, 4), ('t_calm_d', 4.0, 2), ('g_casts_perfect', 8.0, 2), ('g_casts_lake', 2.0, 2),
                          ('g_seagiant_bite_gold', 0.5, 2), ('t_calm_d', 7.0, 2), ('g_casts_night', 3.0, 2), ('koi_hover', 1.2, 2)],
                   texts=[(12, 16, 'SEA GIANT|*BITE')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),

    # ================= C Mtrix · Instagram (Reel)
    'k06_ic1': dict(kind='clean', music='fut_0611_a', hook='SKIP IT|*FURTHER',
                    shots=[('t_main_cast_skip', 0.3, 4), ('c28_reel', 0.5, 2), ('c28_reel', 3.5, 2), ('g_casts_perfect', 1.5, 2),
                           ('t_main_cast_skip', 3.8, 2), ('c26_cast_short', 1.0, 2), ('c26_cast_catch', 5.0, 2), ('c29_holdup', 2.0, 4)],
                    texts=[(10, 14, 'MORE SKIPS|*= RARER FISH')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),
    'dx_ic': dict(kind='day', music='lof_0611_g', day=1, tag='UPDATING MY GAME', lines=[
        "Day one of updating my Roblox fishing game every day.",
        "Update two hundred seventeen.",
        "Today I added a zone bar. It shows how close your cast is to the next zone.",
        "When it fills up, it turns gold.",
        "Search Skip a Hook on Roblox. See you on day two!"],
        shots=[[('c03_baserow_long2', 3.5)], [('c23_lagoon_long', 1.0)], [('c27_longcast1', 3.0), ('t_zones_skyisland', 0.3)],
               [('c05_zonesfly_long1', 3.5)], [('t_calm_b', 4.5)]]),
    'k06_ic2': dict(kind='clean', music='mtg_0611_g', hook='THIS KOI IS|*1 IN 10,000,000',
                    shots=[('koi_hover', 0.2, 4), ('koi_seq_2', 0.5, 2), ('koi_seq_2', 3.0, 2), ('aqua_giant_glass', 4.0, 2),
                           ('koi_seq_1', 1.0, 2), ('koi_seq_2', 8.0, 2), ('aqua_giant_push', 6.5, 2)],
                    texts=[(12, 16, 'EVERY FISH|*CAN FEEL IT')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),

    # ================= C Mtrix · YouTube
    'k06_yc1': dict(kind='clean', music='cin_0611_e', hook='THE SUNKEN|*KINGDOM',
                    shots=[('c15_temple_long', 1.0, 4), ('c16_trident_long', 2.0, 2), ('t_zones_statue', 0.2, 2, 0.8), ('c17_arch_short', 0.5, 2),
                           ('c15_temple_long', 7.0, 2), ('t_zones_temple', 1.5, 2)],
                    texts=[(8, 12, '{0-1000000000} M|*DOWN')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),
    'dx_yc': dict(kind='day', music='lof_0611_c', day=2, tag='UPDATING MY GAME', lines=[
        "Day two of updating my Roblox fishing game every day.",
        "Update two hundred seventeen is the biggest one yet.",
        "I built a server event every fifteen minutes. Fish rush: two minutes where fish bite twice as fast.",
        "Then a meteor falls into the lake, with a rare fish inside.",
        "Search Skip a Hook on Roblox. See you on day three!"],
        shots=[[('c03_baserow_long2', 0.3)], [('c02_basecircle_short', 0.2)], [('g_casts_lake', 5.0), ('g_casts_dock', 6.0)],
               [('c14_lake_long', 3.0), ('g_huge_rising', 0.3)], [('c13_pete_short', 0.3)]]),
    'k06_yc2': dict(kind='clean', music='jer_0611_b', hook='BOATS IN A|*FISHING GAME?',
                    shots=[('c30_boat', 1.0, 4), ('c30_boat', 4.5, 2), ('t_zones_boats', 0.3, 2), ('c30_boat_short', 0.5, 2),
                           ('c04_docktolake_long1', 3.0, 2), ('c30_boat', 8.0, 2), ('t_zones_wreck', 0.2, 2), ('c04_docktolake_long2', 1.0, 2)],
                    texts=[(12, 16, 'FULL|*SPEED')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'k06_m1': dict(kind='clean', music='mtg_0611_f', hook='RATE MY|*BASE',
                   shots=[('c02_basecircle_long', 0.5, 4), ('c02_basecircle_long', 3.5, 2), ('c09_wheel_long', 2.0, 2), ('c11_bench_long', 3.0, 2),
                          ('c08_fuse_long', 4.0, 2), ('c07_aquarium_long', 3.0, 2), ('c10_enchant_long', 5.0, 2), ('c02_basecircle_long', 7.0, 2)],
                   texts=[(16, 20, '1-10?')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),
    'cc2_m2': dict(kind='day', music='lof_0611_g', day=2, tag='TO 1,000 CCU', lines=[
        "Day two of trying to reach one thousand players online at once.",
        "Honest update: eight on average. Yesterday it was ten.",
        "So I worked on the first five minutes. New players see fewer buttons, and unlock the rest while they play.",
        "Twenty eight thousand visits so far. Thank you.",
        "Search Skip a Hook on Roblox. See you on day three!"],
        shots=[[('c06_dock_long', 7.0), ('t_main_walkup', 2.0)], [('c14_lake_short', 0.3)], [('c04_docktolake_long2', 0.3), ('g_casts_dock2', 5.0)],
               [('c01_mapfly_short', 0.3)], [('c04_docktolake_long1', 0.5)]],
        prog=dict(a=10, b=8, goal=1000, unit='CCU', line=1)),
    'k06_m2': dict(kind='clean', music='fut_0611_a', hook='THE SHARK|*RIFT',
                   shots=[('c24_rift_long', 1.0, 4), ('t_beat_rift_jaws', 0.1, 2), ('c24_rift_long', 5.0, 2), ('t_main_underwater', 0.5, 2),
                          ('c24_rift_long', 8.0, 2), ('t_main_underwater', 2.5, 2), ('c24_rift_short', 2.0, 2), ('g_seagiant_bite_gold', 2.0, 2)],
                   texts=[(8, 12, '{0-1000000} M|*OUT'), (16, 20, 'BRAVE|*ENOUGH?')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),

    # ================= mtfgams12 · YouTube
    'k06_n1': dict(kind='clean', music='jer_0611_d', hook='CATCH OF|*THE DAY',
                   shots=[('c26_cast_catch', 0.5, 4), ('c26_cast_catch', 3.0, 2), ('g_exotic_bite', 0.4, 2), ('c26_cast_catch', 5.5, 2),
                          ('c29_holdup', 0.5, 2), ('g_hold_confetti', 1.0, 2), ('ancient_hold', 1.5, 2), ('c29_holdup', 3.0, 2)],
                   texts=[(8, 12, 'EXOTIC|*BITE'), (16, 20, 'BEST CATCH?|*COMMENT')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),
    'dx_n': dict(kind='day', music='lof_0611_c', day=2, tag='UPDATING MY GAME', lines=[
        "Day two of updating my Roblox fishing game every day.",
        "Today: update two hundred seventeen.",
        "I built a goal for the bottom left: how many fish in your zone you haven't found yet, with a little shadow of the next one.",
        "Find them all, and your zone is complete.",
        "Search Skip a Hook on Roblox. See you on day three!"],
        shots=[[('c13_pete_long', 6.0)], [('c08_fuse_long', 1.0)], [('aqua_full_low', 2.0), ('g_casts_dock', 1.0)],
               [('c05_zonesfly_long2', 3.5)], [('c03_baserow_long1', 3.5)]]),
    'k06_n2': dict(kind='clean', music='cin_0611_e', hook='WHERE WOULD|*YOU FISH?',
                   shots=[('c23_lagoon_long', 1.0, 4), ('c16_trident_short', 0.5, 2), ('c19_islands_short', 0.5, 2), ('c20_planet_short', 0.5, 2),
                          ('c23_lagoon_long', 6.0, 2), ('c21_obelisk_long', 3.0, 2)],
                   texts=[(4, 6, '1'), (6, 8, '2'), (8, 10, '3')], end=(4, 'SKIP A HOOK', 'ON ROBLOX')),
}
