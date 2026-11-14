#!/usr/bin/env python3
"""Logik-Check fuer TALK-Tagesdateien (VOR dem Rendern laufen lassen).

    python3 tools/talk/logic_check.py tools/talk/days/t_MMDD.py [--md out.md]

Prueft jedes Skript gegen tools/LOGIK.md und schreibt ein Storyboard (Satz | Clip | Kopfzeile),
das der Kritiker-Agent (Prompt in LOGIK.md) blind bewertet. Ergebnis: OK / WARN / STOP je Video.
Regeln = Heuristiken; Bild-Inhalt der c*-Clips kennt das Skript nicht -> dafuer ist der Agent da.
"""
import importlib.util, re, sys, collections

BAIT = re.compile(r"\b(like|follow|subscribe|share|comment)\b[^.?!]{0,40}\b(is yours|you get|it's the|yours)\b", re.I)
RANDOM = re.compile(r"(decides your fish|the one you stop on|stop the video on|first letter of your name|birthday|zodiac|"
                    r"day you were born|birth ?month|your element)", re.I)
PLAN = re.compile(r"\b(plan|planning|not built|not out|not yet|later i want|i want|comes next|phase two|will be)\b", re.I)
HILO = re.compile(r"higher or lower", re.I)
GENERIC_CTA = re.compile(r"comment it\.", re.I)


def load(path):
    spec = importlib.util.spec_from_file_location('day', path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def shown_fish(shots):
    out = []
    for s in shots:
        o = s[2] if len(s) > 2 else {}
        if isinstance(o, dict) and 'fish' in o: out.append(o['fish'][0].lower())
    return out


def check(day):
    F = getattr(day, 'F', {})
    names = sorted({v[2].lower() for v in F.values()}, key=len, reverse=True)
    rep, cta_count = {}, collections.Counter()
    for vid, v in day.VIDEOS.items():
        issues, words = [], 0
        lines = v['lines']
        for i, ln in enumerate(lines):
            txt, shots, head = ln[0], ln[1], ln[2]
            words += len(txt.split())
            low = txt.lower()
            if BAIT.search(txt):
                issues.append(('WARN', i, 'Engagement-Bait (Like/Follow = Belohnung). Plattformen drosseln das; Logik: Like gibt keinen Fisch. Max 1 pro Konto/Tag.'))
            if RANDOM.search(txt):
                issues.append(('STOP', i, 'Zufalls-Zuordnung ohne Grund (Name/Geburtstag/Sternzeichen/Stop = dein Fisch). Fremde fragen: "und?" -> kein Grund zu schauen.'))
            if PLAN.search(txt):
                issues.append(('WARN', i, 'Spricht ueber etwas Geplantes/Unsichtbares. Nur ok, wenn das Bild es WIRKLICH zeigt (Studio-Aufnahme, Skizze, Mockup) - sonst Bild != Wort.'))
            if HILO.search(txt):
                issues.append(('WARN', i, '"Higher or lower" bei Seltenheit ist doppeldeutig (hoehere Zahl = seltener?). Besser: "Rarer or more common?"'))
            said = []
            rest = low
            for n in names:
                if n in rest: said.append(n); rest = rest.replace(n, ' ')
            shown = shown_fish(shots)
            for n in said:
                if shown and n not in shown:
                    issues.append(('STOP', i, f'Bild != Wort: Stimme sagt "{n}", Bild zeigt {shown}.'))
            if i == 0 and len(txt.split()) > 14:
                issues.append(('WARN', i, f'Hook-Satz zu lang ({len(txt.split())} Woerter, Ziel <= ~10 = ~2-3 s).'))
        if GENERIC_CTA.search(lines[-1][0]) or GENERIC_CTA.search(lines[-2][0] if len(lines) > 1 else ''):
            cta_count['comment it'] += 1
        spd = v.get('speed', 0.9)
        secs = words / (2.6 * spd) + 0.35 * len(lines)
        if secs < 13:
            issues.append(('WARN', -1, f'~{secs:.0f} s lang - fuer Shorts kaum Watchtime, Payoff evtl. zu duenn.'))
        rep[vid] = (issues, secs)
    return rep, cta_count


def storyboard(day, rep):
    out = []
    for vid, v in day.VIDEOS.items():
        issues, secs = rep[vid]
        lvl = 'STOP' if any(x[0] == 'STOP' for x in issues) else ('WARN' if issues else 'OK')
        out.append(f'\n## {vid}  [{lvl}]  ~{secs:.0f} s')
        out.append('| # | Stimme | Bild (Clip @ s) | Kopfzeile |')
        out.append('|---|---|---|---|')
        for i, ln in enumerate(v['lines']):
            shots = ', '.join(f"{s[0]}@{s[1]}" + (f" [{s[2]['fish'][0]}]" if len(s) > 2 and isinstance(s[2], dict) and 'fish' in s[2] else '')
                              for s in ln[1])
            out.append(f"| {i} | {ln[0]} | {shots} | {ln[2].replace('*', '')} |")
        for lv, i, msg in issues:
            out.append(f"- **{lv}** Zeile {i}: {msg}")
    return '\n'.join(out)


if __name__ == '__main__':
    day = load(sys.argv[1])
    rep, cta = check(day)
    md = storyboard(day, rep)
    n = collections.Counter('STOP' if any(x[0] == 'STOP' for x in r[0]) else ('WARN' if r[0] else 'OK') for r in rep.values())
    head = f"# Logik-Check {sys.argv[1]}\nOK {n['OK']} | WARN {n['WARN']} | STOP {n['STOP']} | gleiche CTA 'Comment it.' in {cta['comment it']} von {len(rep)} Videos\n"
    if '--md' in sys.argv:
        open(sys.argv[sys.argv.index('--md') + 1], 'w').write(head + md)
    print(head)
    for vid, (iss, _) in rep.items():
        for lv, i, msg in iss:
            if lv == 'STOP': print(f'{vid:10s} STOP z{i}: {msg}')
    sys.exit(1 if n['STOP'] else 0)
