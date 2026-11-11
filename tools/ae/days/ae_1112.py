# Tagesdatei 12.11.2026 – 27 Videos im AE-Style, HIGH-END (3–4 Beats, 5–7 Shots, ein Thema je Video, Loop-Endkarte):
#   18 Clean (k12_*) + 9 Day-X (cc8_* CCU Day 8, dx7_* Updating Day 7 B/C, dx8_* Updating Day 8 Mtrix-YT/mtfgams12).
#   python3 tools/promo/ae/ae.py tools/promo/ae/days/ae_1112.py all stills|render
# CCU (Creator Dashboard, Half-hourly average Last 1 day, 11.11. ~20:00 UTC): 4 (Vortag 2, Dashboard +79,1 %). Besuche 31,647, Favoriten 1,394,
#   games-API "updated" 2026-11-10 23:22 UTC (nach Release-Check 10.11. 21:5x) -> Classic+ / Legends / neue Rolle LIVE -> "is out".
# Neuigkeit (git 11.11., NICHT veröffentlicht -> "I coded / next update"): HUD-Gruppen (Leiste oben aufgeräumt: Shop/Upgrades/Rewards/Collection/Social),
#   Update-Log statt What's New, PERFECT/GOOD sofort (keine Verzögerung, Streak-Zeile), Welt 2 "Storm Sea" (64 Fische, 8 Zonen, Wellen = Extra-Skips,
#   Gewitter, 6 Storm-Ruten; geschlossen bis fertig).
# NEU: echte Legenden-Clips lg_* (Like-Moment-Formate aus docs/plans/VIDEO_PLAN_V2.md: Legende entkommt / gefangen).
E = {'end': True}
G = (2, 4, 1000)   # CCU gestern (2) -> heute (4), Ziel

VIDEOS = {
    # ================= A fbgam.es · TikTok @rotaztz11
    'k12_a1': dict(kind='clean', music='mtg_1211_d', segs=[
        ('lg_empress_hooked', 0.0, 4, 'ONE CLICK *AWAY...'),
        ('lg_empress_hooked', 2.0, 4, ''), ('lg_empress_hooked', 4.1, 3, '*REEL IT'), ('lg_empress_escape', 0.0, 3, ''),
        ('lg_empress_escape', 1.4, 4, 'WOULD YOU *RAGE?'),
        ('lg_empress_hooked', 0.3, 4, '', E)]),
    'cc8_tt': dict(kind='day', music='lof_1211_a', prog=G, lines=[
        ("Day eight of trying to reach one thousand CCU in my Roblox fishing game.", [('c06_dock_long', 2.0), ('c14_lake_long', 1.0)], 'DAY *8'),
        ("Today's average: four players. Double yesterday.", [('c04_docktolake_long1', 0.5)], '# *PLAYERS', {'prog': True}),
        ("The legends update is out. I hooked the Coral Empress...", [('lg_empress_hooked', 0.0), ('lg_empress_hooked', 2.0)], 'CORAL *EMPRESS'),
        ("And she got away. Can you catch her?", [('lg_empress_escape', 0.0), ('lg_empress_escape', 1.2)], 'SHE *GOT AWAY'),
        ("Search Skip a Hook on Roblox. See you on day nine!", [('c06_dock_long', 6.0)], '')]),
    'k12_a2': dict(kind='clean', music='fut_1211_a', segs=[
        ('c30_boat_short', 0.5, 4, 'SHIPWRECK *AHEAD'),
        ('c18_galleon_long', 1.5, 4, ''), ('c18_galleon_short', 1.0, 4, '*GALLEON'), ('c18_galleon_long', 6.0, 4, ''),
        ('c30_boat', 5.0, 4, ''), ('c18_galleon_long', 8.5, 4, 'FISH *IN THERE?'),
        ('c30_boat_short', 0.8, 4, '', E)]),

    # ================= A fbgam.es · YouTube @MD_58_PDH
    'k12_ya1': dict(kind='clean', music='jer_1211_c', segs=[
        ('lg_bertha_caught', 0.0, 4, 'LAST *PULL'),
        ('lg_bertha_caught', 1.2, 3, ''), ('lg_bertha_caught', 2.4, 4, '*LEGEND'), ('lg_bertha_caught', 6.0, 4, ''),
        ('lg_bertha_caught', 9.5, 4, 'CATCH *ALL 4?'),
        ('lg_bertha_caught', 0.2, 4, '', E)]),
    'cc8_yt': dict(kind='day', music='lof_1211_e', prog=G, lines=[
        ("Day eight on my road to one thousand CCU.", [('c22_endgate_long', 1.0)], 'DAY *8'),
        ("The average went up from two to four.", [('c19_islands_long', 2.0)], '# *PLAYERS', {'prog': True}),
        ("Legends are live now. So I started the next big thing.", [('lg_bertha_caught', 3.0)], 'LEGENDS *ARE LIVE'),
        ("World two, the Storm Sea. Sixty four new fish, and waves that give you extra skips.", [('c18_galleon_long', 3.0), ('c24_rift_long', 2.0)], '*WORLD 2'),
        ("Search Skip a Hook on Roblox. See you on day nine!", [('c22_endgate_long', 6.0)], '')]),
    'k12_ya2': dict(kind='clean', music='cin_1211_e', segs=[
        ('c19_islands_long', 1.0, 4, 'FISHING *ABOVE THE CLOUDS'),
        ('c19_islands_short', 0.5, 4, ''), ('c19_islands_short', 3.0, 4, '*SKY ISLANDS'), ('c19_islands_long', 6.5, 4, ''),
        ('c05_zonesfly_long1', 4.0, 4, 'HOW HIGH *CAN YOU GO?'),
        ('c19_islands_long', 1.3, 4, '', E)]),

    # ================= B mtfgams · TikTok
    'k12_b1': dict(kind='clean', music='fut_1211_a', segs=[
        ('t_main_drill', 0.5, 4, 'SOMETHING *BIG BIT'),
        ('t_main_underwater', 0.3, 3, ''), ('t_main_whale_jump', 0.0, 4, '*WHALE'), ('t_main_whale_splash', 0.5, 4, ''),
        ('t_main_drill', 4.0, 4, 'HOLD *ON!'),
        ('t_main_drill', 0.8, 4, '', E)]),
    'dx7_b': dict(kind='day', music='lof_1111_b', lines=[
        ("Day seven of updating my Roblox fishing game every day.", [('c06_dock_long', 4.0)], 'DAY *7'),
        ("The buttons at the top were way too much.", [('c02_basecircle_long', 2.0)], 'TOO *MUCH UI'),
        ("So I cleaned it up. Five groups: shop, upgrades, rewards, collection and social.", [('c03_baserow_long1', 1.0), ('c09_wheel_long', 2.0)], '*5 GROUPS'),
        ("New buttons unlock slowly while you play. Next update.", [('c26_cast_catch', 1.0)], 'NEXT *UPDATE'),
        ("Search Skip a Hook on Roblox. See you on day eight!", [('c06_dock_long', 8.0)], '')]),
    'k12_b2': dict(kind='clean', music='mtg_1211_d', segs=[
        ('c09_wheel_long', 1.0, 4, 'SPIN *OR SKIP?'),
        ('c09_wheel_short', 1.0, 4, ''), ('c10_enchant_long', 2.0, 4, '*ENCHANT'), ('c10_enchant_short', 1.5, 4, ''),
        ('c08_fuse_short', 1.0, 4, 'WHICH *FIRST?'),
        ('c09_wheel_long', 1.4, 4, '', E)]),

    # ================= B mtfgams · YouTube
    'k12_yb1': dict(kind='clean', music='cin_1211_e', segs=[
        ('lg_empress_hooked', 0.0, 4, 'FULL *POWER CAST'),
        ('lg_empress_hooked', 1.0, 3, ''), ('lg_empress_hooked', 2.2, 4, 'SHE *BIT'), ('lg_empress_hooked', 4.0, 4, ''),
        ('lg_empress_hooked', 5.0, 3, 'LAND *IT?'),
        ('lg_empress_hooked', 0.2, 4, '', E)]),
    'dx7_yb': dict(kind='day', music='lof_1211_a', lines=[
        ("Day seven of updating my Roblox game every day.", [('c28_reel', 0.5)], 'DAY *7'),
        ("The old reel fight felt dead. You just had to spam.", [('c26_cast_catch', 4.0)], 'NO MORE *SPAM'),
        ("So I rebuilt it. A pointer circles the reel. Tap when it hits the gold zone.", [('lg_bertha_caught', 0.0), ('c28_reel', 3.5)], '*GOLD ZONE'),
        ("Every hit makes it faster. Miss twice, and it's over.", [('lg_empress_hooked', 5.0), ('c29_holdup', 1.0)], 'FASTER *EVERY HIT'),
        ("Search Skip a Hook on Roblox. See you on day eight!", [('c28_reel', 4.5)], '')]),
    'k12_yb2': dict(kind='clean', music='jer_1211_c', segs=[
        ('c24_rift_long', 0.5, 4, 'SWIM *INTO THE JAWS'),
        ('t_beat_rift_jaws', 0.0, 4, ''), ('c24_rift_short', 1.0, 4, '*SHARK RIFT'), ('c24_rift_long', 5.0, 4, ''),
        ('c24_rift_long', 8.5, 4, 'DARE *TO CAST?'),
        ('c24_rift_long', 0.8, 4, '', E)]),

    # ================= C Mtrix · TikTok
    'k12_c1': dict(kind='clean', music='jer_1211_c', segs=[
        ('lg_empress_hooked', 2.0, 4, 'BIGGEST *BITE EVER'),
        ('lg_empress_hooked', 4.2, 3, ''), ('lg_empress_hooked', 5.0, 3, '*REEL'), ('lg_empress_escape', 0.0, 4, ''),
        ('lg_empress_escape', 1.2, 4, 'SNAP *OR LAND?'),
        ('lg_empress_hooked', 2.3, 4, '', E)]),
    'dx7_c': dict(kind='day', music='lof_1211_e', lines=[
        ("Day seven of updating my Roblox fishing game every day.", [('c27_longcast1', 0.5)], 'DAY *7'),
        ("Your PERFECT used to show up way too late. Sometimes after the catch.", [('c26_cast_short', 0.5)], 'TOO *LATE'),
        ("I fixed it. Now it pops the moment your hook lands.", [('lg_empress_hooked', 0.0), ('c27_longcast2', 1.0)], '*INSTANT'),
        ("And it counts your streak. How many can you chain?", [('c28_reel', 2.0)], '*STREAK'),
        ("Search Skip a Hook on Roblox. See you on day eight!", [('c27_longcast1', 5.0)], '')]),
    'k12_c2': dict(kind='clean', music='mtg_1111_a', segs=[
        ('aqua_full_glass', 1.0, 4, 'MY TANK *IS FULL'),
        ('aqua_full_low', 1.0, 4, ''), ('aqua_full_top_a', 0.5, 4, '*35 FISH'), ('aqua_full_push', 3.0, 4, ''),
        ('aqua_full_glass', 6.0, 4, 'BEST *FISH?'),
        ('aqua_full_glass', 1.3, 4, '', E)]),

    # ================= C Mtrix · Instagram (REEL)
    'k12_ic1': dict(kind='clean', music='mtg_1211_d', segs=[
        ('c13_pete_long', 1.0, 4, 'MEET *OLD PETE'),
        ('c13_pete_short', 0.5, 4, ''), ('c06_dock_long', 2.0, 4, '*DOCK LIFE'), ('c06_dock_short', 1.0, 4, ''),
        ('c13_pete_long', 7.0, 4, 'HE FISHES *FOR YOU'),
        ('c13_pete_long', 1.3, 4, '', E)]),
    'dx7_ic': dict(kind='day', music='lof_1111_f', lines=[
        ("Day seven of updating my Roblox game every day.", [('c23_lagoon_long', 1.0)], 'DAY *7'),
        ("I want you to see what's new after every update.", [('c06_dock_long', 3.0)], 'WHAT\'S *NEW?'),
        ("So I built an update log. One clean window that shows every new thing.", [('c02_basecircle_long', 4.0)], 'UPDATE *LOG'),
        ("It comes with the next update.", [('c29_holdup', 1.5)], 'NEXT *UPDATE'),
        ("Search Skip a Hook on Roblox. See you on day eight!", [('c23_lagoon_long', 7.0)], '')]),
    'k12_ic2': dict(kind='clean', music='fut_1111_f', segs=[
        ('c23_lagoon_long', 1.0, 4, 'HIDDEN *LAGOON'),
        ('c23_lagoon_short', 1.0, 4, ''), ('c23_lagoon_long', 5.5, 4, '*LAGOON'), ('c14_lake_long', 2.0, 4, ''),
        ('c23_lagoon_long', 9.0, 4, 'FISH *HERE?'),
        ('c23_lagoon_long', 1.3, 4, '', E)]),

    # ================= C Mtrix · YouTube
    'k12_yc1': dict(kind='clean', music='fut_1211_a', segs=[
        ('c20_planet_long', 1.0, 4, 'FISHING *IN SPACE'),
        ('c21_obelisk_long', 3.0, 4, ''), ('c20_planet_short', 1.0, 4, '*COSMIC SEA'), ('c22_endgate_long', 2.0, 4, ''),
        ('c21_obelisk_short', 1.0, 4, 'LAST *ZONE?'),
        ('c20_planet_long', 1.3, 4, '', E)]),
    'dx8_yc': dict(kind='day', music='lof_1011_e', lines=[
        ("Day eight of updating my Roblox fishing game every day.", [('c05_zonesfly_long1', 2.0)], 'DAY *8'),
        ("Legends of the Deep is live.", [('lg_bertha_caught', 3.0)], 'NOW *LIVE'),
        ("Every half hour, a legend shows up for four minutes, and your chance doubles.", [('lg_empress_hooked', 0.0), ('lg_empress_hooked', 2.0)], '*X2 CHANCE'),
        ("I caught Big Bertha. The Coral Empress got away.", [('lg_bertha_caught', 6.0), ('lg_empress_escape', 0.5)], '*1 OF 4'),
        ("Search Skip a Hook on Roblox. See you on day nine!", [('c05_zonesfly_long1', 6.0)], '')]),
    'k12_yc2': dict(kind='clean', music='cin_1111_c', segs=[
        ('g_mutation_bite', 0.2, 4, 'WAIT. *GOLD?'),
        ('g_mutation_bite', 2.0, 3, ''), ('g_mutation_goldfish', 2.3, 4, '*MUTATION'), ('g_mutation_goldfish', 4.3, 4, ''),
        ('g_casts_lake', 6.0, 4, 'LUCKY *OR NOT?'),
        ('g_mutation_bite', 0.4, 4, '', E)]),

    # ================= mtgames2# · YouTube @Roblox-ad5
    'k12_m1': dict(kind='clean', music='cin_1211_e', segs=[
        ('c26_cast_catch', 0.3, 4, 'FIRST CAST *OF THE DAY'),
        ('c26_cast_short', 1.5, 4, ''), ('c28_reel', 1.0, 4, '*SKIP SKIP'), ('c26_cast_catch', 5.2, 4, ''),
        ('c29_holdup', 1.0, 4, 'GOOD *START?'),
        ('c26_cast_catch', 0.6, 4, '', E)]),
    'cc8_m2': dict(kind='day', music='lof_1211_a', prog=G, lines=[
        ("Day eight of trying to reach one thousand CCU.", [('c13_pete_long', 2.0)], 'DAY *8'),
        ("Average today: four. And over thirty one thousand six hundred visits.", [('c03_baserow_long2', 1.0)], '# *PLAYERS', {'prog': True}),
        ("Legends are out. Every half hour, one shows up in its zone.", [('lg_empress_hooked', 1.8)], 'LEGEND *SIGHTED'),
        ("Big Bertha was my first. Which one gets you?", [('lg_bertha_caught', 3.5)], 'BIG *BERTHA'),
        ("Search Skip a Hook on Roblox. See you on day nine!", [('c13_pete_long', 7.0)], '')]),
    'k12_m2': dict(kind='clean', music='jer_1111_g', segs=[
        ('t_kraken_breach', 2.6, 4, 'THE WHOLE *SERVER VS THIS'),
        ('t_kraken_tentacles', 0.3, 4, ''), ('t_kraken_face', 0.3, 4, '*KRAKEN'), ('t_kraken_slam', 1.5, 3, ''),
        ('t_beat_kraken_tug', 0.0, 3, 'TEAM *UP'),
        ('t_kraken_breach', 2.9, 4, '', E)]),

    # ================= mtfgams12 · YouTube
    'k12_n1': dict(kind='clean', music='mtg_1211_d', segs=[
        ('c05_zonesfly_long1', 3.0, 4, 'FLY OVER *EVERY ZONE'),
        ('c05_zonesfly_long2', 1.0, 4, ''), ('c01_mapfly_long1', 3.0, 4, '*11 ZONES'), ('c05_zonesfly_short', 1.0, 4, ''),
        ('c22_endgate_short', 1.0, 4, 'THE *END GATE'),
        ('c05_zonesfly_long1', 3.3, 4, '', E)]),
    'dx8_n': dict(kind='day', music='lof_1211_e', lines=[
        ("Day eight of updating my Roblox game every day.", [('c14_lake_long', 3.0)], 'DAY *8'),
        ("Today I started world two. The Storm Sea.", [('c18_galleon_long', 1.0)], 'STORM *SEA'),
        ("Sixty four new fish in eight zones, storm rods, and thunderstorms.", [('c24_rift_long', 4.0), ('c18_galleon_long', 6.0)], '*64 FISH'),
        ("It stays closed until it's really finished.", [('c22_endgate_long', 3.0)], 'NOT *YET'),
        ("Search Skip a Hook on Roblox. See you on day nine!", [('c14_lake_long', 7.0)], '')]),
    'k12_n2': dict(kind='clean', music='jer_1211_c', segs=[
        ('cosmic_dragon_reveal', 3.2, 4, 'A *DRAGON BIT'),
        ('cosmic_dragon_hold', 0.5, 4, ''), ('cosmic_dragon_hold', 2.5, 4, '*SECRET'), ('g_pink_burst', 0.5, 3, ''),
        ('g_pink_pillar_fishing', 3.0, 4, '1 IN *100,000'),
        ('cosmic_dragon_reveal', 3.4, 4, '', E)]),
}

# Konto -> (Metricool-Blog, Netz, [(id, Uhrzeit)])
POST_PLAN = [
    ('7181171', 'tiktok', [('k12_a1', '12:03'), ('cc8_tt', '17:33'), ('k12_a2', '19:03')]),
    ('7181171', 'youtube', [('k12_ya1', '12:03'), ('cc8_yt', '17:33'), ('k12_ya2', '19:03')]),
    ('7752397', 'tiktok', [('k12_b1', '12:09'), ('dx7_b', '16:09'), ('k12_b2', '19:09')]),
    ('7752397', 'youtube', [('k12_yb1', '12:09'), ('dx7_yb', '16:00'), ('k12_yb2', '19:30')]),
    ('7773777', 'tiktok', [('k12_c1', '12:15'), ('dx7_c', '16:15'), ('k12_c2', '19:15')]),
    ('7773777', 'instagram', [('k12_ic1', '12:15'), ('dx7_ic', '16:15'), ('k12_ic2', '19:15')]),
    ('7773777', 'youtube', [('k12_yc1', '12:15'), ('dx8_yc', '16:15'), ('k12_yc2', '19:15')]),
    ('7752416', 'youtube', [('k12_m1', '12:21'), ('cc8_m2', '16:21'), ('k12_m2', '19:21')]),
    ('7773832', 'youtube', [('k12_n1', '12:24'), ('dx8_n', '16:24'), ('k12_n2', '19:24')]),
]
