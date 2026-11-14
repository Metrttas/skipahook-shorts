# LOGIK.md – Macht das Video Sinn? (Pflicht vor jedem Render, ab 15.11.2026)

User 14.11.: "Manche Videos machen nicht mal Sinn. Du musst die Logik dahinter verstehen von dem, was du postest.
Schau auf GitHub nach Repos / Prompts / mehreren Agenten fuers Video-Cutting."

## Was die Repos machen (Recherche 14.11.)
| Repo | Was wir uebernehmen |
|---|---|
| [browser-use/video-use](https://github.com/browser-use/video-use) | Ablauf **Inventar -> Plan -> Freigabe -> Render -> Selbst-Pruefung am FERTIGEN Video** (an jeder Schnittkante Filmstreifen + Wellenform + Worte), max. 3 Korrektur-Runden. Harte Regeln: nie mitten im Wort schneiden, 30-ms-Fades an Schnitten, Untertitel zuletzt, nie schneiden ohne freigegebenen Plan. Parallele Sub-Agenten: einer je Animation. |
| [Cocozao940/video-editor-agent](https://github.com/Cocozao940/video-editor-agent) | Storyboard aus Transkript; QA prueft **das gerenderte MP4 (Bilder + dB + Naehte), nicht die Absicht** ("verify pixels and dB, not intentions"). Kontaktbogen zu mehreren Zeitpunkten, je Notiz Bild-Beweis. Nicht gepruefte Punkte gelten NICHT als bestanden. |
| [Q00/ReelBrain](https://github.com/Q00/ReelBrain) | Team aus 4 Rollen + Showrunner: **Story Editor** (vollstaendiger Bogen), **Retention Editor** (Hook + Tempo), **Style Editor** (Geschmack des Creators), **Continuity Editor** ("schuetzt Bedeutung, Einschraenkungen und das Ende"). Ergebnisse der Rollen sind Vorschlaege, kein Urteil; aktuelles Feedback des Users schlaegt gespeicherten Geschmack. |
| [zaddy99999/video-editing-skills](https://github.com/zaddy99999/video-editing-skills) | `verify-render`: Groesse, fps, Dauer, Lautheit, True Peak, **schwarze und eingefrorene Bilder**; Render, der schwarz startet, wird abgelehnt; Freigabe nur mit Proof-Sheet. |
| [Melvynx/video-agent-skills](https://github.com/Melvynx/video-agent-skills/) | 3 Hooks je Skript aus 22 Formeln, bewertet + Re-Hook; "Humanize"-Durchgang streicht KI-Woerter und **unbelegte Fakten**; Outlier-Recherche: Videos, die den Median ihres Kontos schlagen, wiederholte Treffer > Glueckstreffer. |
| Spiele-Marketing (hypehype, rolearn.dev, presskit.gg) | Struktur **Hook (an das Spiel gebunden) -> Gameplay, das den Hook einloest -> eine Kernaussage**. Ergebnis zuerst zeigen. Fehler: statische Textkarte als 1. Bild, langsame Kamerafahrten, Intro. |

## Die 8 Logik-Fragen (jede muss JA sein, sonst nicht rendern)
1. **Ein-Satz-Test:** Kann ich in einem Satz sagen, worum es geht UND was ein Fremder davon hat? ("Wie selten ist dieser Hai? – Ratespiel mit Aufloesung" = ja. "Dein Anfangsbuchstabe = dein Fisch" = nein: Zuordnung ist Zufall, Antwort ist "und?".)
2. **Bild = Wort:** Was die Stimme in diesem Moment sagt, ist in diesem Moment im Bild zu sehen. Spricht sie ueber den Boss/die Icons/die Inseln, muss man Boss/Icons/Inseln sehen. Sonst Satz streichen oder passendes Material aufnehmen. (14.11.: Leviathan-Plan ueber Rift-Clip, "4 neue Icons" ueber Basis-Clip, "graue Bloecke" ueber Welt-1-Clip = Bruch.)
3. **Wahr:** Jede Zahl/Funktion ist live und stimmt (Chancen-Tabelle). Geplantes heisst klar "plan" UND hat ein Bild (Studio, Skizze). Nie mehr als 1 Plan-Satz pro Video.
4. **Ursache -> Wirkung stimmt:** Keine falschen Versprechen ("Like = Golden Shark"). Like gibt keinen Fisch; Kinder merken das und fuehlen sich verarscht. Like-Leiter war Wunsch des Users (12.11.) -> erlaubt, aber max. 1 pro Konto/Tag, und klar als Spass ("if likes gave fish...").
5. **Echte Frage:** Die Frage am Ende hat zwei vertretbare Antworten (Sell vs. Keep = echter Tausch; "Golden Shark oder Megalodon?" ist keine Wahl, wenn man nichts ueber sie weiss). Rate-/Higher-Lower-Spiele: eindeutig formulieren ("rarer or more common?").
6. **Payoff im Bild:** Was der Hook verspricht, wird sichtbar eingeloest (Fang, Zahl, Vorher/Nachher) – und das Staerkste kommt am Ende.
7. **Fremder versteht es:** Wer das Spiel nie gesehen hat, versteht in ~5 s: Roblox-Angelspiel, Haken springt uebers Wasser, seltene Fische. Keine Insider-Woerter ohne Bild (Doubloon, Rank 3, Zone 12).
8. **Konsistent:** Day-Zaehler je Konto fortlaufend, CCU-Zahl echt, kein Widerspruch zu Videos vom Vortag auf demselben Konto.

## Formate: behalten / umbauen / streichen
- **Behalten (haben Logik):** Wie-selten-ist-das (Raten -> Aufloesung im Bild), Sell or Keep (echter Tausch, wenn Aquarium-Einkommen stimmt), Rate-this-catch, Day-X/CCU mit echtem Ereignis UND passendem Bild, Dev-Story in Ich-Form (beste eigene Zahlen: 1.400–7.400 Views vs. 250–350 fuer Vorlagen).
- **Umbauen:** Would-you-rather nur mit Tausch (z. B. "1 Megalodon sicher ODER 10 Wuerfe mit 1-%-Chance auf den Koi"), Higher/Lower -> "Rarer or more common?".
- **Streichen:** Anfangsbuchstabe/Geburtstag/Sternzeichen/Monat = dein Fisch, "Stop the video = your fish" (reine Zufallszuordnung, kein Grund zu schauen, keine Einloesung).
- **Neu (logisch + zeigt das Spiel):** Fail -> Fix ("Spieler fanden X doof, also hab ich Y gebaut" + Vorher/Nachher-Bild), ein Fang von Wurf bis Karte ohne Schnittluege, Spieler-Kommentar beantworten (echter Kommentar als Einblendung), "Ich hab 100 Wuerfe gemacht – so oft kam was Seltenes" (nur mit echter Zaehlung).

## Agenten-Pipeline (nach video-use + ReelBrain)
1. **Showrunner (Haupt-Sitzung):** Tagesplan, Themen je Konto, schreibt `t_MMDD.py`.
2. `python3 tools/talk/logic_check.py tools/talk/days/t_MMDD.py --md <scratch>/sb.md` -> alle STOP beheben.
3. **Kritiker-Agenten (parallel, einer je 9 Videos, BLIND – bekommen nur Storyboard + diese Datei, nicht meine Begruendung):** Prompt unten. Je Video OK/FIX/STOP + Ersatz-Satz.
4. Fixes einbauen (max. 2 Runden), dann `stills` rendern.
5. **QA-Agent am fertigen Video:** je Satz 1 Bild aus der MITTE des Satzes (Kontaktbogen) + Transkript -> "sieht man, was gesagt wird?", schwarzes/eingefrorenes Bild, Text verdeckt Fisch/Spieltext. Was nicht geprueft wurde = nicht bestanden.
6. Erst dann Metricool.

### Kritiker-Prompt (kopieren)
```
Du bist ein 13-jaehriger Roblox-Spieler, der TikTok scrollt und "Skip a Hook" (Roblox-Angelspiel) nie gesehen hat,
und zugleich ein strenger Story-Editor. Unten: Regeln (LOGIK.md) und Storyboards (Stimme | Clip-Name@Sekunde | Kopfzeile).
Clip-Namen beschreiben grob den Inhalt (c14_lake_long = See, c24_rift_long = Riss-Zone, aqua_* = Aquarium, *_reveal = Fisch-Enthuellung).
Fuer JEDES Video:
1. Ein-Satz-Test: worum geht es, was habe ich davon? (Wenn du es nicht sagen kannst -> STOP)
2. Wuerde ich nach 2 s weiterschauen? Warum/warum nicht?
3. Jede Zeile: passt das Bild zur Stimme? Ist etwas unlogisch, falsch versprochen oder nicht beantwortbar?
4. Urteil OK / FIX / STOP und bei FIX/STOP: konkret neuer Hook-Satz oder Ersatz-Zeile (Englisch, max 12 Woerter).
Sei hart. Keine Hoeflichkeit. Antworte als Tabelle.
```
