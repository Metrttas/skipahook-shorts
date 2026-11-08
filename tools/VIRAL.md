# Skip a Hook – Viral-Gedächtnis für Shorts (TikTok + YouTube)

User 2026-10-30 12:30: "bau dir ein Gedächtnis auf, was viral gehen könnte … jeden Tag 8 Videos posten".
Vor jedem neuen Video-Tag LESEN, nach jedem Tag die Tabelle "Was lief" ergänzen (Metricool-Analytics).

## Was 2026 funktioniert (Recherche 30.10.)
- **Hook in 1–3 s**, nie langsam anfangen, kein reiner Text-Anfang. Muster:
  - *Mitten in der Action*: das Highlight zuerst (Wal springt, Kraken-Gesicht), Erklärung danach.
  - *Offene Frage*: "Which zone would you fish in?", "Would you open it?"
  - *Kühne Behauptung*: "The rarest catch…", "Secrets most players never find"
  - *Direkte Ansprache / FOMO*: "Halloween ends TOMORROW", "Season 1 starts TODAY"
  - *POV*: "POV: your hook skips across the lake", "POV: you finally catch a Sea Giant"
  - *Wait for it / Wait for the end*: ruhig anfangen, Knall am Ende (Zuschauer bleiben -> Watch-Time)
- **Formate**: POV, Geheimnis/Versteck finden, Ranking (#3 #2 #1), "Rate this 1–10" (Kommentare!), "Pick 1/2/3"
  (Kommentare), Vorher/Nachher, satisfying/cozy Loops, seltene Fänge/Drops, Countdown zu Events.
- **Länge**: 10–15 s (hohe Abschluss-Rate). Spielname immer an derselben Stelle (Tag "SKIP A HOOK" oben links im Bild).
- **Text**: 1. Zeile Hook mit Suchwörtern ("Roblox fishing game"), 1 Satz, Frage + 👇, `Search "Skip a Hook" on Roblox`,
  4 Hashtags (#roblox #robloxfishing + Thema + #skipahook), KEIN #fyp. Emojis nur im Beschreibungstext, NICHT im Video
  (Schrift LuckiestGuy hat keine Emojis -> Kästchen).
- **Musik**: unter 10K Followern ~80 % Trend-Sounds (halten 3–7 Tage). Über die API (Metricool) kann man KEINE TikTok-Sounds
  anhängen -> eigene Beats im Trend-Stil: Brazilian Phonk / Funk (#brazilianphonk in Europa Feb–Mai 2026 +62 %, läuft bei
  Gaming-Edits). `tools/audio/phonk_beats.py` -> funk_drop (130 BPM), phonk_drift (140, halbes Tempo), funk_bounce (128, hell).
  Ruhige Videos: sah_calm_bed / sah_cozy_dock. Möglichkeit für echte Trend-Sounds: Metricool `autoPublish false` -> Push aufs
  Handy, User wählt den Sound in der TikTok-App selbst (kostet ihn ~1 min je Video).
- **Posten**: 3–5x/Tag je Konto in den ersten 90 Tagen; Wochentags 15–19 Uhr, Wochenende 10–14 + 19–22 Uhr (Zeitzone der
  Zuschauer – Roblox = viel USA). User ist mit 12–21 Uhr Berlin zufrieden. Kein "Werbung"-Schalter (User 12:30: "mein Spiel,
  juckt nicht") -> `commercialContentOwnBrand false`.
- Schlechte Videos 24–48 h stehen lassen, erst dann bewerten. Kommentare in der 1. Stunde beantworten (macht der User).
- Nicht möglich/zu teuer: Face-Cam. **Voiceover geht seit 31.10.** (Kokoro, Stimme `am_puck` Tempo 1.1 = Wahl des Users,
  clips.py `vo=[…]`): kurze Sätze, 1 Satz je Schnitt, Spielname + "Roblox" im 1. Satz (Suche/Untertitel), Frage am Ende.

## Animierte Shorts (seit 31.10. 15:3x, User: "lern gute Videos mit Animationen zu editieren", Plugins Remotion + Tweenkit installiert)
- **Remotion selbst geht hier NICHT** (npm-Registry aus der Cloud gesperrt, 403) -> eigener Renderer im Remotion-Stil:
  `tools/promo/motion/` (`build.py <id> prep|stills|render|encode`, `render.mjs` = Playwright Bild für Bild, 2 Prozesse,
  ~0,3 s/Bild -> 15 s Video in ~3 min; Seite `<id>/index.html` mit `renderAt(t)`, spring()/interpolate wie Remotion).
  Geräusche aus Tweenkits numpy-Synth (`audio_lib.py`: whoosh, tick, boom, riser, typing, bell), Stimme Kokoro mit Wort-Zeiten.
- Muster `far` ("HOW FAR CAN YOUR HOOK GO?", out/motion/far/far.mp4): Hook-Wörter ploppen zum Voiceover, Zoom-Schlag + Blitz
  bei jedem Schnitt, Distanz-Zähler rollt beim Aussprechen der Zahl (log-Skala) + Zonen-Leiste mit Haken, Zonen-Karte gleitet
  beim Zonen-Namen rein (Glanz), End Gate = Riser + Boom + Bildschirm-Wackeln + Farbblitz, Endkarte: "CAN YOU REACH IT?",
  Suchleiste tippt "Skip a Hook", grüner Play-Knopf + Finger, "Comment how far you got". Text nur da, wo er etwas Neues sagt
  (Zähler + Karte ersetzen Untertitel). Schnitt/Zähler/Karte hängen an den Kokoro-Wort-Zeiten (`VO[b].words`).
- Stolperfallen: Text-Breite mit `width: max-content` messen (sonst bei 1080 gekappt); Titel weg, BEVOR der Zähler kommt.
- **User 15:38: "sehr fresh, sehr gut" -> neuer Standard-Stil; von Zeit zu Zeit verbessern, nicht übertrieben Limit verbrauchen.
  User 15:39: "Musik bisschen zu laut", 16:16: "die Sounds viel zu laut, alles leiser" -> `MUSIC_VOL, FX_VOL = 0.06, 0.13`
  in build.py (Stimme ~-19 LUFS, Musik ~20 dB, Geräusche ~15 dB darunter; vorher 0,15 / 0,45). Nicht wieder lauter machen.**
- **Vorlage `tools/promo/motion/tpl/index.html`** + `TPL` in build.py: je Voiceover-Satz eine Szene (`head` "Zeile 1|*Zeile 2",
  `{a-b}` = Zahl rollt, `stk` = Season-Sticker aus `out/motion/stk/` (emblem, ticket_free/prem, tideline, pumpkin, ghostfish, bat –
  aus PassAtlasS1b), `card`, `boom`; letzte Szene `end` mit ask/cta). Neues Video = nur Eintrag in `TPL`, dann `prep` + `render`.
  31.10.: m1_today … m6_tracks ersetzten die 6 Season-Posts 17:30–17:42 (Medien getauscht, Texte gleich).
- **Tages-Videos ab 1.11.**: `tools/promo/motion/days/d_MMDD.py` mit `TPL_DAY = {id: dict(music=…, lines=[…], scenes=[…])}`
  (build.py liest alle Dateien dort ein), dann je id `build.py <id> prep` + `build.py <id> render` (nacheinander, render nutzt
  schon 2 Prozesse, ~2 min je Video). Schriften, Sticker und audio_lib liegen im Repo (`tools/promo/motion/fonts|stk`).
  Ideen für Szenen: Zahl rollt (`{a-b}`), Sticker, Karte, `boom` beim Höhepunkt; je Video andere Clips/Musik/Hook.

**Ausführliches Edit-Wissen: `tools/promo/EDITING.md` (Techniken, Werte, was die Vorlage kann, Checkliste) – vor jedem Video-Tag lesen.**

**Shorts-Playbook (ab 1.11., User 12:07 "bau dein Wissen weiter: posten, Beschreibungen, Hooks, Aussehen, Professionalität")**:
Artifact https://claude.ai/artifact/KgW3ijKpUZq7VwH7R512su, Text per ArtifactData get (collection "playbook", doc "main", Feld
"markdown"). Gilt vor älteren Regeln hier (Wünsche des Users zuerst). Kern aus den eigenen Zahlen: Vorlagen-Videos 30./31.10. alle
246–335 Aufrufe, persönliche Dev-Videos des Users 1.400–7.400 -> mind. die Hälfte Dev-Story in Ich-Form, 3–5 Hashtags, CTA-Zeile
nicht starr. **Muster: `days/x_dev1.py`** (Dev-Story, Hook "I MADE A ROBLOX|*FISHING GAME" auf dem Planeten-Clip, Ende = Frage
"WHAT SHOULD I ADD NEXT?" auf demselben Clip -> Loop), Video out/motion/x_dev1 (14,5 s).

## Vorlagen-Formate vom User (02.11. abends, 7 TikToks: "lern von den Videos, kopier alle Arten, je Account einzigartig, müssen viral gehen")
Ab 3.11. sind das die Grund-Formate für ALLE 9 Accounts (3 Videos/Tag/Account, mtfgams-YT 2). Je Format pro Tag nie zweimal gleich
(andere Clips, Hook, Musik, Zahlen). Originale liegen nicht im Repo (nur Beschreibung hier).
1. **"Day 1 of making my own game" (Dev-Log)**: Ich-Stimme, Untertitel 2–3 Wörter unten-mittig, kurze Feature-Clips (Eier/Zonen/Shop),
   Ende "like and comment". Bei uns: "Everything I put in my game so far", "I added X" (`n03_devlog`, d03_a*). 25 s.
2. **"50 days, 50 Roblox games" (Bewertung)**: Seltenheits-Roll im Hook (COMMON/EPIC/LEGENDARY/MYTHICAL blinkt), dann feste Kopfzeile
   + Kategorien mit Note "Graphic 9.5/10", "Replay Value 9/10", "Overall 9/10". Bei uns: "I rated my own Roblox game" (`n03_rate`) mit
   rollender Note `{1-9}/10`. 28 s.
3. **Langer Erklärer (88 s, Pet/Egg-Spiel)**: schnelle Untertitel, alle Menüs/Systeme hintereinander, Leaderboard. Bei uns kürzer:
   "How it works in 20 seconds" (`n03_howto`), Schritt je Szene.
4. **"Actually GOOD Roblox games" (Empfehlung)**: ruhige Stimme, fast nur kleine Untertitel, Emojis im Hook, düstere/epische Bilder,
   Ende = Spiel-Karte. Bei uns ehrlich mit Twist "Okay, I'm biased. I made this one." (`n03_actually`). 20 s.
5. **"NEW BOAT!" / "the BEST roblox game to play in november"**: Steigerung Stufe 4 -> 9 mit Pixel-Kopfzeile "BOAT 9 NEW!", Werte-Box
   "LUCK x92 / DAMAGE 281" -> "x200K / 650K", Rewind-Effekt, Musik ohne Stimme möglich. Bei uns: Haken 3 -> 45 Skips (`n03_hooks`),
   Zonen 2 -> 15 (`n03_zones`), weitere Ideen: Ruten, Ränge, Aquarium-Füllstand, Boote.
6. **"My Roblox game is finally OUT!"**: 9:16 schwarz, oben 2 Zeilen weiß, Mitte 16:9 Beat-Cut mit "IT'S OUT." (Buchstaben mit Bild
   gefüllt), unten "Search BEE FARM on Roblox". Bei uns `python3 tools/promo/outnow.py io_zones|io_world|io_base` + `vertical(id, top,
   bottom)` (in outnow.py) -> out/outnow/<id>_v.mp4. Nur Musik, ~21 s. Je Account andere Szenen/Reihenfolge/Texte.
7. **"Day 2 of trying to get 1,000 players"**: ECHTE Zahlen (61 visits, 1 like, Ziel-Balken 61/1,000), Ich-Story ("whoever you are …
   so I added what he wants"), Seltenheits-Leiter, "TITANIC 1/400 = 0.25%", Kommentar-Einblendung, "See you on Day 3". User 02.11.:
   echte Zahlen von Skip a Hook ja (Roblox-Besuche/Likes vom User holen; Metricool-Views gehen auch). Serie mit fortlaufendem Tag.

## Day-N-Serie (User 03.11.: "Yo guys, it's day one, day two" auf dem Rotatz-TikTok + dem YouTube-Kanal mit 500+ Abos)
- Beides Marke fbgam.es 7181171: TikTok @rotaztz11 (Ziel 10,000 Follower, Start 3,848) + YouTube (Ziel 1,000 Abos, Start 526).
- Jeden Tag 1 Folge je Kanal (eigene Fassung), feste Zeit 17:33; die Folge zählt zu den 3 Videos/Tag des Accounts (dann nur 2 andere).
- Datei `tools/promo/motion/days/s_day.py` (sd<N>_tt / sd<N>_yt). Zahlen jeden Tag frisch aus Metricool (TKEV07, YTEV01).
- Aufbau: "Yo guys, it's day N of trying to …" -> Zahl rollt "{a-b} / 10,000" -> 1 echte Neuigkeit/Spielsache -> "Search Skip a Hook on
  Roblox, and see you on day N+1!". Kommentar-Ideen der Zuschauer aufgreifen ("you asked for X"), nur Wahres.
- Day 1 = 4.11. (sd1_tt Mond-Drache/Skips, sd1_yt Weitwurf/Koi). Day 2 = 5.11. usw.

## Edit-Regelwerk (Recherche 31.10. 17:4x, User: "lern von Videos mit guten Edit-Skills, bis du ein Meister bist")
Quellen = Analysen/Daten-Artikel (Videos selbst kann ich nicht ansehen); Zahlen meist Eigenauswertungen der Autoren -> Richtwerte.
1. **Hook = Bild + Text + Ton gleichzeitig im 1. Bild** (Entscheidung fällt nach ~1,5–2 s): keine Intro, kein Logo; Zoom + Ton-Cue
   in den ersten ~0,8 s; 3–5 Wörter; Neugier-Lücke ("How far…?", "Can you…?") + auffälliges Bild zusammen wirkt am stärksten.
   **Stumm-Test**: erste 3 s ohne Ton ansehen – versteht man worum es geht? Erstes Bild = Vorschaubild -> kein Blitz/kein halbes Wort.
2. **Ohne Ton verständlich**: 50–85 % schauen stumm. Untertitel Wort für Wort (3–4 Wörter, aktives Wort gelb, 0,1–0,2 s VOR dem
   Wort, kurze Pop-Animation, kein Drehen/Springen), Kopfzeilen höchstens 4–6 Wörter und ≥ 2 s sichtbar.
3. **Alle 2–4 s ein Muster-Bruch** (Schnitt, Zoom-Schlag, neuer Text, Sticker, Karte) – aber NICHT überdrehen: MrBeast 2024
   "ultra fast paced/overstim era … doesn't even work", Szenen atmen lassen. Kein Bild-Element länger als ~8 s gleich.
4. **Schnelle Zooms 2–3 Bilder lang** (bei 60 fps ~0,05 s Anstieg, dann federn), langsamer Dauer-Zoom 1,5–2 %/s im Hintergrund.
5. **Ton**: Whoosh auf jeden Schnitt, Aufprall auf Schlüsselwörter, Meme-Sounds nur selten und genau auf dem Witz; alles LEISE
   unter der Stimme (User). Ein Ton-Cue im ersten Bild.
6. **Auszahlung früh** (Zahl/Antwort in den ersten ~3–5 s andeuten, Hauptmoment nicht erst am Ende) und **Loop**: Ende passt zum
   Anfang (gleiche Szene/Kamera oder Frage, die der Anfang beantwortet), letztes Bild 1–2 s halten -> Wiederholungen > 100 % Watchtime.
7. **Länge** 10–20 s für unsere Formate (Daten: 21–34 s ~62 % Abschluss, > 60 s ~48 %); lieber kurz + Loop als lang + leer.
8. **Sichere Zonen**: TikTok unten 15 %/oben 8 %, Reels unten 20 % + rechts 60 px, Shorts unten 12 % -> bei uns Text y 250–1480,
   rechts frei ab x 940 (passt).
- **In der Vorlage umgesetzt (tpl, 31.10. 17:5x)**: (2) Untertitel Wort für Wort automatisch aus den Kokoro-Wortzeiten (`CAPS`,
  Hook nur der Rest nach der Kopfzeile, Endkarte ohne, `cap=False` je Szene aus), (1) Zoom-Schlag im ersten Bild + leiser Boom bei 0 s,
  (3) kleiner Zoom-Schlag + Kick, wenn Zeile 2 ploppt (`punch_t`, Szenen > 1,6 s ohne boom). Schon vorher drin: Whoosh + Blitz je
  Schnitt, Dauer-Zoom, Sticker/Karte/boom, Endkarte. **Beim Schreiben der Tagesdateien beachten**: (6) Ende = Frage, die zum Hook
  zurückführt, End-Clip gern = Hook-Clip; Zahl/Antwort früh; Hooks als Neugier-Lücke formulieren.
- **Vorlage 31.10. 18:0x (User 17:49 "schau, wie die das machen")**: Schnitte auf dem Beat (`beat_sync`, BPM-Tabelle), Beat-Stupser,
  Whip-Übergang (Schiebe-Wisch beider Bilder + waagerechte Bewegungsunschärfe) mit Speed-Ramp 2,2x, abwechselnd mit Zoom-Schlag
  (`tr`), Musik-Ducking unter der Stimme (sidechaincompress), Musik-Stille 0,35 s vor jedem boom. Muster: out/motion/m1_today.

## System ab 31.10. (User 09:40: "4 Videos jeden Tag für jeden Account … 6 Accounts … 24")
- **Konten (Metricool)**: A = fbgam.es 7181171 (TikTok rotaztz11 + YouTube) · B = mtfgams 7752397 (TikTok mx100577 + YouTube) ·
  C = Mtrix 7773777 (TikTok 1tgames2 + Instagram mete.629, Reel) · mtgames2# 7752416 + mtfgams12 7773832 noch ohne Konten.
- **JEDER Account eigene Videos** (User 10:33: "Du solltest 24 machen, 4 pro Account") – nie dasselbe Video auf zwei Accounts,
  auch nicht TikTok + YouTube derselben Marke -> 6 Accounts x 4 = **24 Videos = 24 Posts am Tag**, je Post genau EIN Netz.
  Kommt ein Account dazu: +4 Videos. (31.10. 10:20–10:28 liefen noch 3 geteilte Posts -> YouTube/IG bekamen +1 um 14 Uhr.)
- **Zeiten (Berlin)**: Metricool-Bestzeiten TikTok (fbgam.es, Woche ab 1.11.): Spitzen 10, 12, 18 Uhr, dann 16–17 Uhr; Sa/So
  gleiche Form, nur niedriger. -> Slots **10:03 / 12:03 / 16:03 / 18:03** (Marke A), B +6 min, C +12 min. Am 31.10. (Update 18 Uhr):
  10:20–10:28, 12:03–12:15, (14:03–14:15 nur YouTube/IG), 16:00–16:12, 17:30–17:42 (Season-Videos). YouTube/IG gleiche Zeit wie TikTok.
- **Layout (User 09:40: "Schrift viel zu weit oben, hinter der Kamera-Insel beim iPhone nicht lesbar")** – clips.py Konstanten:
  Text nur in y 250–1480 (oben Statusleiste/Dynamic Island/"Following | For You", unten Name + Beschreibung + Musik-Zeile),
  rechts frei ab x 940 (Like-Spalte ab y ~900). Hook Mitte y 360, Spiel-Fenster y 500–1700 (9:10), Untertitel Mitte (510, 1370),
  max. Breite 880, Sneak-Peek-Bild rechts oben im Fenster (Breite 400). Nie wieder Text über y 250.
- **Ton (User 09:40: "Musik nicht so laut, man soll die Person verstehen")**: Musik 0,13 unter der Stimme (Phonk 0,15–0,16),
  Mischung auf -14 LUFS. Jede Schnitt-Szene = 1 Satz Voiceover + kurzer Untertitel (Kernwörter *gelb*).
- **Update-Videos**: höchstens 1 je Marke und Tag (User: "nicht immer ums Update … bei 1, 2, 3"). Keine Versprechen zu Inhalten,
  die vielleicht noch nicht live sind (Pete/Rod Case: beschreiben, nicht "jetzt verfügbar").
- **Geplante Aufgabe** "Skip a Hook Shorts – Videos für morgen" (trig_01G5m63t9B3yGdDxnbrNtuSq): täglich 20:47 Berlin, eigene
  Cloud-Sitzung, braucht den verbundenen PC (Bundle + Clip-Bibliothek `SkipAHook_Meshes\promo\reel`), baut + plant die 24 Videos (6 Accounts x 4)
  für den NÄCHSTEN Tag ein, meldet sich per Push. PC aus = an dem Tag keine Videos (Meldung).
- Tagesdatei `tools/promo/day_MMDD.py` (Liste VIDEOS, `R(...)` = Reel-Clip, `O(...)` = alte Aufnahme), rendern
  `python3 tools/promo/clips.py <ids>` (2 Prozesse parallel), hochladen nach skipahook-shorts `d/<Datum>/`, posten per
  `createScheduledPost` (Marke = blogId, providers = alle Netze der Marke; IG: `instagramData {type: REEL}`).

## Mehr Erkenntnisse (Recherche 30.10. 12:4x)
- **YouTube Shorts**: wichtigstes Signal "angesehen vs. weggewischt" + Retention; Loops zählen als neue Aufrufe (Ende soll
  nahtlos in den Anfang passen). Beste Längen laut 35-Mrd.-Views-Studie: ~13 s oder 60 s. Kein langsamer Anfang, keine Pausen,
  Auflösung nicht spät. Nische NICHT wechseln (immer Skip a Hook/Roblox-Angeln). Ab ~200 Shorts wächst ein Kanal stetig ->
  Menge zählt. Titel klar + Suchwörter; #Shorts nicht nötig.
- **TikTok für Spiele (Entwickler-Erfahrung)**: Hook in der 1. Sekunde; jedes Video muss ohne Vorwissen verständlich sein;
  so kurz wie möglich; nahtloser Loop; Herausforderung/Frage am Anfang ("can YOU…"); Nischen-Insider-Witze ziehen.
  **Selbstgemacht wirkt besser als zu poliert** (zu viel Produktion schnitt schlechter ab). Trend-Song bringt Schub (auch leise).
  Großer CTA ~3 s auf dem Bild ("Search SKIP A HOOK on Roblox"). Hit-Format sofort wiederholen, Flops schnell fallen lassen.
  Nach einem viralen Video ältere Videos neu hochladen. Zeit zählt (gleiches Video 30 min vs. 6 h für 4k Views):
  US-Publikum -> 8 Uhr / 14 Uhr PST = 17 Uhr / 23 Uhr Berlin. Folgen-Feed spielt kaum eine Rolle -> immer für NEUE Zuschauer.
- **Vorbild Fisch (Roblox-Angelspiel)**: Sammeln + Mutationen + Seltenheit, Trailer auf der Spielseite, X/YouTube-Clips;
  der Halloween-Event "FischFright" (zeitlich begrenzte Fische, Quest) brachte es auf die Roblox-Startseite (bis 470k gleichzeitig).
  -> Unsere stärksten Themen: Event (Halloween/Season 1), seltene/limitierte Fische, riesige Fänge, Boss, Geheimnisse.
- **Ideen-Pool für neue Videos**: "Can YOU catch this?" · "I fished for 1 hour and got…" · "Rarest fish tier list" ·
  "Things only pros know" · "Rate my aquarium" · "This is 1 in 1,000,000" (Cosmic Koi) · "Season 1 rewards ranked" ·
  "Before vs after 1 hour" (Aquarium voll) · "Every zone in 15 seconds" · Countdown zu Events · Kommentar-Antwort-Videos.

## Material (out/rec, Game-Bar-Aufnahmen 30.10., ~30 fps -> minterpolate 60 fps)
- calm (Steg-Flug Sonnenuntergang -> Nacht, Wal 34–41, Kürbis-Steg mit NPCs 42–46), main (Wurf 7–12, Sprünge übers Wasser 14–27,
  Einholen 31,7–34,5, Riesen-Sprung 38,2–41, Luft 41–50; Kinobalken; 28–31 Fehler-Kasten), beat (Docks 4,5–9, Enchant-Tisch 9,15–10,6, Sonnen-
  untergang 10,7–14,4, Fuse-Maschine 28,5–30,4 (NICHT Enchant), Kraken 22–37; Schnitte alle ~2 s), zones (Tempel 6–8, Statue 8–10, Lagune 25–27,5, Insel 27,5–30, Speedboot 30–32, Edge 22–25;
  11–19,5 RUCKELT), kraken (Höhle 5–11, Kraken taucht auf 11–15 RUCKELT -> kraken2 12,05, Spieler + Kraken 16–20, Tentakel 20–24,
  Gesicht 28–31), kraken2 (= kraken +0,25 s; 16–20 RUCKELT).
- **Material-Lage 1.11.**: Reel-Bibliothek (24 Welt-/Feature-Szenen) seit 31.10. dreimal durch – es fehlen Fang-/Gewichts-/Hook-Momente (Riesenfisch mit Zoom-out, Gewicht zählt hoch, Hook ausrüsten, Rank-Up, Nacht-Bobber, Verkaufen). Wunschliste an den User geschickt (`SkipAHook_Meshes\promo\reel\`).
- **NEU 1.11. nachmittags: große Clip-Sammlung `SkipAHook_Meshes\promo\clips\` + `index.json`** (User 12:46 "sehr großes
  Clip-Equipment"; Ablauf + Stolperfallen `tools/promo/rec/RECORDING.md`). Gleiches Format wie reel (1916x902, 60 fps, ohne Ton) ->
  in build.py als `clip='<name>'`, wenn die Datei nach `out/rec/reel/<name>.mp4` gelegt wird. `index.json` = je Clip Beschreibung,
  Tags, Dauer, `hud` (true = mit Spiel-HUD). Präfixe: `t_` Trailer (Haupt/Beat/Calm/Zones/Kraken/Enchant, alle neu in echten 60 fps),
  `g_` echtes Gameplay (Würfe, Skips, PERFECT, Bisse "SECRET/EXOTIC/SEA GIANT/MUTATION BITE", Reveal-Karten), `g_hud_` dasselbe mit HUD
  (Meter zählt), `koi*` Cosmic-Koi-Sequenz (1 in 10M), `whale_*` Wal-Jagd (Wasserski) + Titel, `ancient_*` Prehistoric Megalodon,
  `cosmic_dragon_*`, `golden_shark_reveal`, `aqua_*` Aquarium voll (+ `aqua_giant_*` Riesen ragen lustig aus dem Becken),
  `ui_*` Menüs (Store, Inventory, Gear, Luck, Index, Rank, Profile, Weekly Cup, Playtime, Pass Claim All/Cases, Rod Case 1x/10x,
  Pete, Enchant, Fuse), `pete_dock`, `whale2_*` zweite Wal-Jagd + Titanic-Karte, `far*_` Weitwürfe mit Meter-Zähler bis 2,9 T m,
  `bench_lift`, `boat_garage`. Stand 1.11.: 149 Clips, 16 min, 1 GB. FEHLT: Kraken-Raid live (Aufnahme > 400 MB), Boot-Fahrt.
  **Damit sind Dev-Storys mit echten Spielszenen möglich** – Hooks
  wie "I made the rarest fish 1 in 10,000,000", "My fish dragged me across the lake", "How far can one hook go? 2.9 TRILLION m".
- **Muster 1.11. `days/x_rare1.py` "Rarer fish = crazier catch"** (User: "gutes Video mit guter Idee mit den neuen Clips"): Steigerung
  1 in 50,000 Golden Shark -> 100,000 Megalodon -> 500,000 Wal -> 10,000,000 Cosmic Koi, Kopfzeile = rollende Zahl, Hook = Koi über dem Steg,
  Ende = gleicher Clip + Frage. Clips mit Spiel-Blitz/roten Enden vorher zusammenschneiden (`x_*`-Clips, Befehle im Kopf der Datei);
  Spiel-Karten mit Namen unten -> Szene mit `cap=False`, sonst liegen Untertitel darauf. build.py prep cacht `frames_src/` -> nach
  Clip-Wechsel `out/motion/<id>/frames_src` + `frames` löschen.
- Nach ~2–3 Tagen wiederholt sich das Material -> neue Aufnahme (PC 15 min, Windows-Aufnahme auf 60 fps stellen lassen).
- **NEU 31.10.: Reel-Bibliothek `out/rec/reel/` (24 Szenen à 4,4 s, echte 60 fps, ohne Ruckeln)**: map (Sonnenuntergang), docks,
  aquarium, fuse, wheel, pete, garage, enchant, bench, minikraken, lake, temple, trident, arch, galleon, mast, islands, skylink
  (Basen bei Nacht), planet, obelisk, endgate, lagoon1/2, rift. Stark: map, enchant, wheel, pete, minikraken, planet, endgate,
  lagoon, temple. Schwach (dunkel): lake, galleon, mast. Formate damit: "Every zone in 15 seconds", "This game is HUGE" (Muster
  `s_world`), "Rate my base 1–10", "Which zone would you fish in? 1/2/3", Pete/Aquarium/Enchant-Feature-Videos.

## AE-Style ab 9.11. (User 08.11.: ALLE Videos so "fresh" wie SkipAHook_Beispiel_AE.mp4 – ersetzt den clean.py-Look)
- **Werkzeug:** `tools/promo/ae/ae.py <tagesdatei> <id|all> stills|render` (Kopf = Format), Kern `aecore.py` (= promo\beispiel_2026-11-08\ae\render.py
  konfigurierbar gemacht). Tagesdatei `tools/promo/ae/days/ae_MMDD.py` (Muster `ae_1109.py`, enthält auch POST_PLAN), Texte `posts_MMDD.json`.
  Look: Spielbild-Band 1350 breit (y 642–1278) auf Blur-Hintergrund, Kopfzeile y 505 (Spring-Wörter, *GOLD), Karaoke y 1345, Whip/Zoom-Übergänge mit
  Motion Blur, Shake/Flash/Chromatic bei Impacts, Light Leaks, Endkarte SKIP A HOOK + "Search on Roblox"-Pill, CCU-Balken (prog). 60 fps, crf 19/max 17M, -14 LUFS.
  Clean: Hook ab Bild 1 sichtbar, Drop auf Beat 4, Schnitte 2–3 Beats -> bei >=146 BPM mind. 22 Beats planen (sonst < 9 s). Day: Stimme am_puck 0.8/0.5.
- **Render:** ~11 s Clean = ~120 s, ~21 s Day = ~250 s (2 Kerne, 2 parallel) -> 27 Videos ≈ 45 min. Schleife: /home/claude/runae.sh-Muster
  (überspringt fertige, 2 Prozesse, `timeout 570`, mehrmals aufrufen). Clips direkt aus /mnt/user-data/uploads/.../promo/clips (stagen, ~870 MB in 3 Aufrufen).
- **Stolperfallen:** keine erfundenen Zahlen im Counter (far2_meter_c zeigt 4,08M m, koi2_leap_counter eigenen Zähler) -> Counter nur mit echter Zahl.
  Spiel-Texte (PERFECT!, Titel) bleiben im Band, eigene Texte außerhalb -> keine Überlagerung. raw.githubusercontent gibt aus der Sandbox 403, Metricool lädt trotzdem.

## Clean Edits ab 5.11. (User 04.11. 21:58: "nur noch cleane edits und daily update, freshe Sounds, neue Texte")
- **Werkzeuge (neu gebaut 05.11. abends – die Mittags-Fassung vom 5.11. war NIE im Bundle, nur Videos im Shorts-Repo):**
  `tools/promo/motion/clean.py` (Kopf = Format, ein ffmpeg-Durchgang, ~40 s je Clean Edit, ~70 s je Day-Video bei 2 Kernen),
  Tagesdatei `tools/promo/motion/days/k_MMDD.py` (Muster `k_1106.py`), Musik `tools/audio/fresh_beats.py` (100 % synthetisiert).
  Lange Läufe: `timeout 585 bash runall.sh` mehrmals (Skript überspringt fertige; abgebrochene Teil-mp4 vorher löschen).
- Clean: Intro 4 Beats mit Hook (ab Bild 1 sichtbar, y 560), Drop auf Beat 4, Schnitte 2 Beats, xfade 0,18 s, Texte y 1180, Endkarte
  "SKIP A HOOK / ON ROBLOX" auf dem Anfangs-Clip direkt vor dem Hook-Bild (Loop). Day-X: dunkle Karte hinter "DAY N / Serie" + Balken
  (verdeckt PERFECT!/CAST HERE darunter), Karaoke-Untertitel y 1240, Stimme am_puck 0.8/0.5, Musik 0.10.
- **Stolperfallen:** t_main_*, t_zones_*, t_kraken_*, koi_seq_2, whale_chase_2 haben Kinobalken (y 0–110/790–902) -> clean.py erkennt das
  und schneidet 380x676 (unschärfer). c27_longcast*, c26_cast_catch, g_casts_* zeigen PERFECT!/GOOD! oben (y ~600–750) -> Hook dort mit
  `hook_y=1150, end_y=1120`. c09_wheel_* "SPIN!"-Knopf unten (nicht unter Untertitel). c12_garage_long ab 2–5 s weiß überstrahlt,
  c01_mapfly_long1 Anfang weiß, t_main_walkup 0–1,2 s schwarz, c13_pete_long 4 s gelbe Nahaufnahme, c06_dock_long 9 s Pfosten-Nahaufnahme.
  g_huge_rising/koi_seq_2 haben eigene Untertitel-Leiste unten ("Something HUGE is rising…"). Day-Videos ~-19 LUFS (etwas leise).

## CCU-Serie ("Day N of trying to reach 1,000 CCU", YT M&D + YT Rblxcntnt + TikTok @rotaztz11)
| Day | Datum | Average CCU (Dashboard, letzter Tag) | Besuche | Favoriten | Thema |
|---|---|---|---|---|---|
| 1 | 05.11. | 10 | – | – | (Mittags-Sitzung) |
| 2 | 06.11. | 8 (-20,5 %) | 28,840 | 1,285 | cc2_tt Server-Events · cc2_yt Streak-Glück · cc2_m2 erste 5 Minuten |
| 3 | 07.11. | 8 (±0, Dashboard +1,1 %) | 29,497 | 1,311 | Rework-PLAN: cc3_tt Auto-Skip · cc3_yt nur 3 Zahlen · cc3_m2 Trainings-Matte (AFK) |
| 4 | 08.11. | 11 (+55,9 % laut Dashboard) | 30,229 | 1,337 | Rework GEBAUT + veröffentlicht (games-API updated 07.11. 18:48 UTC): cc4_tt Auto-Skip/Wände · cc4_yt 3 Zahlen, Rute=Power/Haken=Luck · cc4_m2 Freunde-Boost + Welt 2 |
| 5 | 09.11. | 10 (-1, Dashboard 8,2 %) | 30,977 | 1,365 | A-Paket (geschrieben, NICHT eingebaut): cc5_tt Geschenk-Truhe · cc5_yt FTUE-Funnel · cc5_m2 Robux-Ranglisten weg -> Skips Today |

## Day-X "updating my Roblox game every day"
- Mtrix-YT + mtfgams12: Day 1 = 5.11., **Day 2 = 6.11.** (dx_yc Fish Rush/Meteor, dx_n Ziel-Silhouette) -> Day 3 = 7.11.
- B-TikTok, B-YouTube, C-TikTok, C-Instagram: **Day 1 = 6.11.** (dx_b Got away, dx_yb Meteor Fish, dx_c Morgen-Fang, dx_ic Zonen-Leiste) -> Day 2 = 7.11.
- Alles aus Update 217 "Core Loop 2.0" (unklar ob live -> "I built"). Eier sind aus (217e) -> nicht erwähnen. Für Day 3 neue Commits ansehen.
- 07.11.: Mtrix-YT/mtfgams12 **Day 3** (dx3_yc Rework-Entscheidung, dx3_n Bestenliste "Most Skips Today"); B-TT/B-YT/C-TT/C-IG **Day 2** (dx2_b Skip Simulator, dx2_yb Gold-Ringe x10, dx2_c Zonen-Wände, dx2_ic Skip-Combo). Keine neuen Update-Commits seit 217 -> alles ehrlich als PLAN aus docs/plans/BIG_REWORK.md. Nächster Tag: Day 4 bzw. Day 3; neue Commits prüfen (Rework gebaut?).
- 08.11.: Mtrix-YT/mtfgams12 **Day 4** (dx4_yc Rework fertig + Aquarium füllt sich + Welt 2, dx4_n Rank Up ohne Reset + Rod Stars); B-TT/B-YT/C-TT/C-IG **Day 3** (dx3_b Skip-Simulator +1 je Skip + Bank, dx3_yb Rute=POWER/Haken=LUCK, dx3_c Zonen-Wände, dx3_ic neues Tutorial). Quelle: git log Rework R1–R2f (6.–7.11.) + CLAUDE.md "NÄCHSTES UPDATE = WELT 2". Nächster Tag: Day 5 bzw. Day 4. **Clips zeigen noch das ALTE Spiel** -> neue Rework-Aufnahmen beim User anfragen.

- 09.11. (AE-Style): Mtrix-YT/mtfgams12 **Day 5** (dx5_yc erste Minute: Truhe + LUCKY! + Skips Today, dx5_n Skips Today/Top Power); B-TT/B-YT/C-TT/C-IG **Day 4** (dx4_b Ranglisten, dx4_yb Geschenk-Truhe, dx4_c 11-Schritte-Funnel, dx4_ic +N-Pool gegen Lag). Quelle git 17e65c2 A-Paket (nur Code+Tests, nicht eingebaut -> "coded / next update"). Nächster Tag: Day 6 bzw. Day 5.

**promo\clips am 06.11. benutzt (102 Clips, alle mit neuen Startzeiten):** siehe `days/k_1106.py`. Bibliothek ist seit 5.11. komplett mehrfach
benutzt -> NEUE AUFNAHMEN nötig (RECORDING.md), v. a. die neuen 217-Sachen (Fish Rush, Meteor, Got away, Zonen-Leiste, Morgen-Karte).

## Was lief (nach Metricool-Analytics nachtragen)
| Datum | Konto | Video | Format | Views 48h | Likes | Kommentare | Notiz |
|---|---|---|---|---|---|---|---|
| 30.10. | beide | d1_* (8) | Feature-Teaser | – | – | – | erster Tag, noch keine Daten |
| 31.10. | A | d31_a1–a4 | HUGE-Zonen · Rate my base · Pick 1/2/3 · Season 1 | – | – | – | 1. Tag mit Voiceover + neuem Layout |
| 31.10. | B | d31_b1–b4 | 15 s alle Zonen · Pete · Kraken-POV · Season 1 | – | – | – | |
| 31.10. | C | d31_c1–c4 | Nacht cozy · POV Skip · Rod Case 0,2 % · Season 1 | – | – | – | neues Konto 1tgames2 (TikTok) |
| 31.10. | A-YT | d31_ya1–ya4 | 3 Tipps seltene Fische · Wal "wait for it" · Enchant · Season 1 | – | – | – | eigene YouTube-Videos ab 12:03 |
| 31.10. | B-YT | d31_yb1–yb4 | Relaxing vibe · Kraken wacht auf · Skip-Gameplay · Season 1 | – | – | – | |
| 31.10. | C-IG | d31_yc1–yc4 | Fuse 3→1 · Glücksrad · Boot zu allen Zonen · Season 1 | – | – | – | Instagram Reels |
| 31.10. | je Konto 1 | d31_a5/a6/b5/b6/c5/c6 | Code-Teaser "gratis Rod Case" · 3 Profi-Tipps · Rate my aquarium · Welche Maschine 1/2/3 · Bis ans Ende? · 3 Sachen heute Abend | – | – | – | Nachschlag 11:35–11:45 (User 11:06), Code SEASON1 erst mit dem Release |
| 01.11. | A | d01_a1–a4 | No size limit · Gewicht = Wert · Normal vs this · 1 in 100M Moonlotus | – | – | – | Ideen-Liste des Users (Profile: A Zahlen, B Hooks, C Fortschritt); 31.10.-Abendlauf fiel aus (PC-Ordner nicht freigegeben) -> am 1.11. morgens für denselben Tag gebaut |
| 01.11. | A-YT | d01_ya1–ya4 | 3 Dinge · Price check Void 400B · Megalodon Tooth · Jede Seltenheit | – | – | – | |
| 01.11. | B | d01_b1–b4 | Boot Hook · 3 vs 45 Skips · Drop-Hooks · Fortune (Rad) | – | – | – | |
| 01.11. | B-YT | d01_yb1–yb4 | Skips erklärt · Pearl Hook · 30 Hooks · Fuse 3->1 | – | – | – | |
| 01.11. | C | d01_c1–c4 | Day 1 vs später · No rebirth · Nacht-POV · Aquarium statt verkaufen | – | – | – | |
| 01.11. | C-IG | d01_ic1–ic4 | Old Pete · 15 Ränge · Glücksrad · Weekly Cup | – | – | – | |
| 30.10.–01.11. | A (TikTok) | alle KI-Videos | Vorlagen/Ideen | 246–343 (Median ~280) | 1–16 | – | Stand 02.11. 08:30: kein Durchbruch; beste: No size limit 343/16 Likes, Season 1 338, rarer fish 315/9 |
| 02.11. | A | d02_a1–a4 | Dev: 1-in-10M-Koi · Map zu groß · Kraken-Boss · Season 1 live | – | – | – | Abendlauf 1.11. fiel aus -> 2.11. morgens gebaut, Zeiten 14/16/18/20 Uhr (12 Uhr belegt: 6 bc_*-Videos einer anderen Sitzung) |
| 31.10.–01.11. | B (TikTok mx100577) | alle | Vorlagen | 2–283 (Median ~204) | – | – | Stand 02.11. abends: kein Durchbruch; vorn "Everyone ignores this hook" (Boot) 283, Kraken-POV 282; 2 Posts mit nur 2 Views (Pete, Season) = vermutlich nicht ausgespielt |
| 31.10.–01.11. | C (TikTok 1tgames2) | alle | Vorlagen | 128–275 (Median ~255) | – | – | kein Durchbruch; vorn POV Skip 275, Can you reach the end 267; späte 17-Uhr-Posts 1.11. erst ~125 (jünger) |
| 03.11. | A | d03_a1–a3 | Dev: Old Pete offline · 4 Basis-Teile (1–4) · Enchant-Tisch | – | – | – | ab heute 3/Account, Stimme 0.8, 20–24 s, erstmals Tageslicht-Clips c* |
| 03.11. | A-YT | d03_ya1–ya3 | Dev: Aquarium 35 Fische · Biss-Arten · Speedboote | – | – | – | |
| 03.11. | B | d03_b1–b3 | Weitwurf -> Secret-Fang · Cosmic Koi · Rod Case 0,2 % -> Coral (EXPERIMENT Fehlschlag) | – | – | – | |
| 03.11. | B-YT | y03_moon, y03_cast | Moonlotus 1/100M Lagunen · Ein Wurf bis zum End Gate | – | – | – | nur 2/Tag (16:00, 19:30) |
| 03.11. | C | d03_c1–c3 | 3 Wege weiter werfen · Tag vs. Nacht (EXPERIMENT Vorher/Nachher) · Zonen-Quiz (EXPERIMENT) | – | – | – | |
| 03.11. | C-IG | d03_ic1–ic3 | Send this to… Fang · Dev Hook hüpft wie ein Stein · Season 1 | – | – | – | |
| 01.–02.11. | A (TikTok) | d01_a*, x_rare1, d02_a* | gemischt | 254–366 (Median ~290) | – | – | Stand 03.11. abends: kein Durchbruch; vorn "rarer fish, crazier catch" 366, "NO size limit" 352; Dev-Ich-Videos 2.11. (Koi 308, Map zu groß 280) nicht besser als Vorlagen |
| 01.–02.11. | B (TikTok mx100577) | d01_b*, d02_b* | gemischt | 82–286, 2.11. nur 82–124 | – | – | Konto fällt ab (Median 1.11. ~200 -> 2.11. ~95) – nicht ausgespielt? |
| 01.–02.11. | C (TikTok 1tgames2) | d01_c*, d02_c* | gemischt | 200–263 (Median ~241) | – | – | stabil, kein Durchbruch |
| 04.11. | A | e04_a1 (Fisch kämpft, 4 Kreise), e04_a2 (EXPERIMENT Warn-Hook "Don't quit after 29 min" -> Gratis-Rod-Case) | Dev | – | – | – | + Day 1 17:33 (andere Sitzung) |
| 04.11. | A-YT | e04_ya1 (Ausblick, den ich gebaut habe), e04_ya2 (Shipwreck Graveyard 6 Mrd. m) | Dev | – | – | – | + Day 1 17:33 |
| 04.11. | B | e04_b1 (Perfect-Wurf +25 %), e04_b2 (3 Supernova Sharks fusen) | Payoff | – | – | – | + bc_song1 13:09 (andere Sitzung) |
| 04.11. | B-YT | y04_kraken (Boss-Raid 100 HP/-25), y04_glitch (Mutationen Gold/Rainbow/Glitch 1 in 400 x15) | Payoff | – | – | – | 16:00 / 19:30 |
| 04.11. | C | e04_c1 (EXPERIMENT Zahlen-Quiz Zonen-Entfernungen), e04_c2 (Rate this base 1–10) | Tipps/Fragen | – | – | – | + io_bee 13:15 (andere Sitzung) |
| 04.11. | C-IG | e04_ic1 (EXPERIMENT Share-Hook Wal), e04_ic2 (Dev Aquarium bewerten), e04_ic3 (Pick 1/2/3 kosmische Orte) | Share/Community | – | – | – | |
| 03.11. | A/B/C (TikTok) | d03_* | gemischt | A 268–297 (Median ~279), B 182–210 (~209), C 220–251 (~240) | A 2–10 | – | Stand 04.11. abends: kein Durchbruch; B erholt sich (2.11. ~95 -> 3.11. ~200); A vorn "4 Basis-Teile 1–4" 297/10 Likes, C vorn "3 Wege weiter werfen" 251 |
| 05.11. | A | f05_a1 (Dev: Secret-Fisch in jeder Zone, Golden Shark), sd2_tt (Day 2: Boote, 17:33), f05_a2 (Dev: letzte Zone ohne Ende) | Dev | – | – | – | |
| 05.11. | A-YT | f05_ya1 (Dev: 12 Seltenheiten #3…#12), sd2_yt (Day 2: Bank, 528 Abos, 17:33), f05_ya2 (Dev: Leviathan Rod nur vom Kraken) | Dev | – | – | – | |
| 05.11. | B | f05_b1 (EXPERIMENT "Guess what just bit" -> Wal), f05_b2 (Koi-Sequenz 2 "the sea builds a wall"), f05_b3 (Megalodon "bad sign") | Payoff | – | – | – | |
| 05.11. | B-YT | y05_dragon (Cosmic Dragon am Rand der Karte), y05_super (Supernova Shark, rotes Wasser) | Payoff Ich-Form | – | – | – | 16:00 / 19:30 |
| 05.11. | C | f05_c1 (Pick 1/2/3 Statue/Obelisk/Ring), f05_c2 (Tipp Pete vor dem Ausloggen, 8 h), f05_c3 (EXPERIMENT "Real or fake?" Wal im Aquarium) | Tipps/Fragen | – | – | – | |
| 05.11. | C-IG | f05_ic1 (EXPERIMENT Share + Zahl: 400 Drehungen Jackpot Rod), f05_ic2 (Dev Enchant-Tisch bewerten), f05_ic3 (Share: Mutationen x3/x6/x15) | Share | – | – | – | |
| 02.11. | A-YT | d02_ya1–ya4 | Dev: zu groß fürs Aquarium (EXPERIMENT Humor) · Golden Shark Zone 1 · Wal-Wasserski · 130+ Fische | – | – | – | |
| 02.11. | B | d02_b1–b4 | Megalodon-Cutscene · Dev Weitwurf 2,86 T m · Cosmic Dragon · Wait for it Wal (EXPERIMENT) | – | – | – | |
| 02.11. | B-YT | d02_yb1–yb4 | Supernova Shark · 10 Rod Cases · Biss-Arten · Skips/Perfect | – | – | – | |
| 02.11. | C | d02_c1–c4 | Pick 1/2/3 Secrets · Dev Cutscenes · Tipp Distanz · Would you rather Kraken/Wal | – | – | – | |
| 02.11. | C-IG | d02_ic1–ic4 | Send this to… Koi (EXPERIMENT Share) · Dev schwerer = größer · 3 Dinge für Neue · Dev Speedboote | – | – | – | |
| 06.11. | alle 9 | k06_* (18 Clean) + cc2_* (CCU Day 2) + dx_* (Day 1/2) | Clean/Day-X | – | – | – | erster Tag neue Stil-Regeln, Musik fresh_beats *_0611_*; Metricool-Zahlen nicht geholt (Limit) |
| 07.11. | alle 9 | k07_* (18 Clean) + cc3_* (CCU Day 3) + dx2_*/dx3_* | Clean/Day-X | – | – | – | Musik *_0711_* (11 neue Varianten), Metricool-Zahlen wieder nicht geholt (Limit sparen) |
| 09.11. | alle 9 | k09_* (18 Clean) + cc5_* (CCU Day 5) + dx4_*/dx5_* | AE-Style | – | – | – | erster AE-Tag (ae.py), Musik *_0911_* (6 neu) + *_0811_*; Metricool-Zahlen nicht geholt (Limit) |
| 08.11. | alle 9 | k08_* (18 Clean) + cc4_* (CCU Day 4) + dx3_*/dx4_* | Clean/Day-X | – | – | – | Musik *_0811_* (11 neue Varianten); erstes Thema = echter Rework; Metricool-Zahlen nicht geholt (Limit sparen) |

**promo\clips am 02.11. benutzt (nächste Tage andere nehmen):** koi2_leap_counter, koi_seq_1, koi_seq_3, koi2_pillars, koi2_splash_hover,
koi_hover, t_main_flyover, t_main_walkup, t_zones_temple, t_zones_skyisland, t_zones_endgate, t_zones_boats, t_zones_wreck, t_kraken_face/cave/
breach/slam/title, t_main_cast_skip, t_main_underwater, t_main_whale_jump, t_main_whale_splash, g_pink_burst, g_casts_night, g_casts_dock,
g_casts_lake, g_casts_perfect, g_hud_cast_skips, g_hud_golden_shark, golden_shark_reveal, g_paddlefish_card, g_mutation_goldfish, g_exotic_bite,
g_seagiant_bite_purple, g_secret_bite_flash, g_huge_rising, g_hold_confetti, g_hud_colossal_meg, cosmic_dragon_reveal/hold, ancient_cutscene/
reveal/hold, whale2_bite, whale2_ride_a/b, whale2_counter, whale2_card_titanic, whale_title, whale_chase_1, far2_meter_a/b/c/d, far_meter_b,
far2_supernova, far_secret_bite, far_supernova, far_hold, aqua_giant_push/top/glass, aqua_full_glass, ui_pass_claimall, ui_rodcase_x10(_end),
ui_index, ui_playtime, ui_gear, bench_lift, boat_garage. **Noch frisch:** t_calm_*, t_enchant_*, t_beat_* (meist), t_main_drill/sea_flight/
whale_jump-Varianten, koi2_wall, koi_seq_2, koi2_title, koi_title, whale_chase_2, whale_finale_jump, whale2_ride_c, whale2_title, g_hud_secret_bite(_pink),
g_seagiant_bite(_gold), g_ethereal_moonlotus, g_pink_pillar_fishing, g_huge_rising2, g_perfect_cast, g_casts_dock2, aqua_full_low/push/top_*,
far_meter_a, far_meter2_*, far2_meter_e, far2_bite_catch, far_hold2, ui_rodcase_open*, ui_pass_cases, ui_store, ui_inventory, ui_luck, ui_rank,
ui_profile, ui_weeklycup, ui_playtime_case, pete_dock, ui_pete_*, ui_enchant, ui_fuse.
- Clip-Hinweise (Kontaktbögen 02.11.): t_kraken_cave 0–2,8 s schwarz, t_main_walkup/t_zones_temple/t_zones_skyisland ~1 s dunkel am Anfang;
  far2_meter_a endet bei 2,86 T m (8 s); koi2_leap_counter / koi_seq_3 haben eigenen „1 IN …“-Zähler in der Bildmitte (Untertitel liegt darüber);
  UI-Clips (Menüs) sind breit -> im 9:16-Ausschnitt nur die Mitte sichtbar (Rod-Case-Rolle, Pass) – für Menü-Videos ok, als Hook schwach.

**promo\clips am 03.11. benutzt:** c13_pete_long, c06_dock_long, ui_pete_window, ui_pete_collect, pete_dock, c02_basecircle_long, c07_aquarium_long,
c08_fuse_long, c09_wheel_long, c12_garage_long, c10_enchant_long, ui_enchant, t_enchant_night_a, t_enchant_sunset_a/b, aqua_full_push/glass/low/top_a,
g_hud_secret_bite(_pink), g_seagiant_bite(_gold), g_huge_rising2, c30_boat(_short), c14_lake_long, c03_baserow_long1/2,
far_meter_a, far2_meter_e, far2_bite_catch, g_casts_dock2, g_pink_pillar_fishing, koi_title, c33_rodcase, ui_rodcase_open1/2, c23_lagoon_long,
g_ethereal_moonlotus (x_moon), c27_longcast1/2, c15_temple_long, c19_islands_long, c22_endgate_long, far_meter2_a/b, c28_reel, c01_mapfly_long1/2,
t_calm_b/c/d/e, c24_rift_long, c16_trident_long, c21_obelisk_long, c05_zonesfly_short, c26_cast_catch, c29_holdup, t_beat_lake_glide, c20_planet_long,
c34_fishingpass, ui_pass_cases. **Noch frisch:** c04_docktolake (schwach: leeres Wasser), c05_zonesfly_long1/2 (0–3 s Wolken), c11_bench, c17_arch,
c18_galleon, c25_cosmicsea, c31_goldenhour (Golden Hour – nur zeigen, wenn live), c32_baitshop, c35_store, c06/c07/…_short, aqua_full_top_b,
far_hold2, koi2_wall, whale_chase_2, whale2_ride_c, ui_store/luck/rank/profile/weeklycup/playtime_case, t_beat_* (kurz, 1,5–2 s).
- Clip-Hinweise 03.11.: ui_rodcase_open1/2 + ui_pass_cases enden mit "Coral Rod (normal)"; g_ethereal_moonlotus ab 2,7 s weiß; t_enchant_* 0–1,5 s
  schwarz; far2_meter_e geht real bis 88 B m (nicht 25,9 M); c26_cast_catch = PERFECT -> EPIC BITE -> Fisch springt -> hochhalten (4,5–7,5 s).

**promo\clips am 04.11. benutzt:** t_main_drill, far_hold2, c01_mapfly_short, t_calm_a, ui_playtime_case, c02_basecircle_short, t_main_sea_flight,
c05_zonesfly_long1, c18_galleon_long/_short, 16_mast, 15_galleon (reel), g_casts_perfect, g_casts_lake, g_perfect_cast, c08_fuse_short, ui_fuse, 04_fuse (reel),
t_beat_fuse, t_kraken_tentacles, t_kraken_roar, t_beat_kraken_win/slam/face/tug, g_mutation_bite, 03_aquarium (reel), c07_aquarium_short, aqua_full_top_b,
c15_temple_short, c16_trident_short, c19_islands_short, c20_planet_short, c21_obelisk_short, c22_endgate_short, c25_cosmicsea_short, 20_obelisk (reel),
whale_chase_2, whale2_ride_c, whale_finale_jump. **Noch frisch:** koi2_wall, t_zones_statue/ring/obelisk/title, t_enchant_night_b, t_beat_kraken_tentacles/
break (Mitte schwarz), c04_docktolake_*, c11_bench_short, c17_arch_*, ui_store/luck/rank/profile/weeklycup/inventory (im 9:16-Ausschnitt kaum lesbar).
- **Material-Lage 04.11.: Bibliothek ist nach 4 Tagen fast durch** -> User um neue Aufnahmen gebeten (RECORDING.md): v. a. echte Fänge bei Tag,
  Kraken-Raid live, Boot-Fahrt, Mutationen (Gold/Rainbow/Glitch-Fisch), volles Aquarium mit Schild > 0 Fische (03_aquarium/c07 zeigen "0/35 Fish").
- Clip-Hinweise 04.11.: g_hud_cast2 + far_hold2 = HUD-Clips, Zonen-Label/Chat/Hinweise liegen direkt unter der Kopfzeile -> für Kopfzeilen-Szenen meiden;
  t_beat_kraken_break ab ~0,7 s fast schwarz; ui_* zeigen im Vollbild-Ausschnitt nur die Fenstermitte.

**promo\clips am 05.11. benutzt:** golden_shark_reveal (ab 2,95 s = sauber), c04_docktolake_long1/2, g_casts_dock, t_zones_temple/endgate/wreck/skyisland, c25_cosmicsea_long, c17_arch_long,
t_main_cast_skip, c03_baserow_short/long1, c30_boat, 07_garage (reel), x_moon (neu gebaut), g_paddlefish_card, g_secret_bite_flash, whale_chase_1, koi_seq_3, t_kraken_breach/cave/face/slam/title,
c11_bench_short/long, 09_bench (reel), whale2_bite, whale2_counter, whale_finale_jump, koi2_wall/pillars/leap_counter/splash_hover, ancient_cutscene/hold, g_casts_night, c05_zonesfly_long2,
c20_planet_long, c21_obelisk_long, g_casts_dock2, g_huge_rising, cosmic_dragon_reveal/hold, far_supernova, far_hold, x_statue/x_obelisk/x_ring (t_zones_* 1,6x langsamer), c13_pete_short, 06_pete (reel),
c06_dock_long, pete_dock, aqua_giant_top/push/glass, aqua_full_glass, c09_wheel_long, c02_basecircle_long, t_enchant_night_b, c10_enchant_short, 08_enchant (reel), g_mutation_goldfish, g_hold_confetti,
g_pink_pillar_fishing. **Alles in der Bibliothek ist jetzt mindestens einmal benutzt** -> neue Aufnahmen dringend (siehe 04.11.).
- Clip-Hinweise 05.11.: Titel-/Karten-Clips (x_moon 0–1,4 s "ETHEREAL!", whale2_title, koi2_title, ancient_reveal "ANCIENT", golden_shark_reveal 0–2 s "SECRET!", t_zones_title "SKIP A HOOK"
  abgeschnitten) haben Spieltext OBEN genau auf Höhe unserer Kopfzeile -> Kopfzeilen-Szenen nur auf die Teile ohne Banner legen. whale2_ride_* + far2_* + bench_lift: HUD oben stört.
  whale2_card_titanic = 0–2 s Titel, 2–3,5 s "TITANIC!", danach leere Nacht. golden_shark_reveal 2,0–2,9 s weißer Ring. c12_garage_short Anfang weiß überstrahlt. t_kraken_breach 0–2,5 s nur Höhle.

**promo\clips am 08.11. benutzt (107 Clips, neue Startzeiten):** siehe `days/k_1108.py`. Neu wieder dabei: koi2_wall/pillars/splash_hover, koi_seq_1, aqua_giant_*, c30_boat(_short), c12_garage_long, c33_rodcase, golden_shark_reveal (raus), far_supernova, cosmic_dragon_hold, t_main_drill/sea_flight/flyover.
- Clip-Hinweise 08.11.: c33_rodcase/ui_rodcase_* = Menü mit Text -> nie unter Kopfzeilen/Untertitel; far_meter_*/far2_meter_* HUD-Meter oben + PERFECT! genau auf Text-Höhe 1180 -> meiden; whale2_ride_a/whale2_counter Leiste + MISS!; ui_pete_collect Menü; g_secret_bite_flash 3 s weiß + eigene Untertitel; t_zones_statue 0,4 s unscharfe Nahaufnahme; g_hud_golden_shark ~4,5 s Weiß-Blitz; cosmic_dragon_reveal 1 s Pink-Blitz (ab 3,2 ok). Weiße/gelbe Einzelbilder im Kontaktbogen = fadewhite/zoomin-Übergänge (ok).

**promo\clips am 07.11. benutzt (109 Clips, neue Startzeiten):** siehe `days/k_1107.py`. Bibliothek ist komplett mehrfach durch -> NEUE AUFNAHMEN, spätestens wenn der Skip-Simulator-Rework gebaut ist (Auto-Skip, Zahlen, Zonen-Wände).
- Clip-Hinweise 07.11.: **t_calm_e enthält das Trailer-Logo "SKIP A HOOK"** (Mitte) -> nie unter eigenen Texten; t_calm_a 0–0,8 s fast schwarz (Endkarte!); t_kraken_roar + t_main_underwater enden mit Trailer-Titel ("SKIP A HOOK" auf Rot/Weiß); c11_bench_short Anfang = grüne Vollbild-Nahaufnahme; t_main_cast_skip/c28_reel/c26_cast_catch zeigen "PERFECT! +1 SKIP" genau an der Unterkante der Day-Karte; g_mutation_goldfish 2 s Spieltext oben (Endkarte end_y=1150).

**promo\clips am 09.11. benutzt (136 Clips, AE-Style):** siehe `tools/promo/ae/days/ae_1109.py`. Weiter nur ALTES Spiel -> Rework-Aufnahmen (Auto-Skip, 3 Zahlen, Bank, Zonen-Wände, Geschenk-Truhe) dringend (RECORDING.md).
