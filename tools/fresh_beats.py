#!/usr/bin/env python3
# Skip a Hook :: frische Beats für Clean Edits + Day-X (neu gebaut 05.11.2026 abends; die Fassung vom 05.11. mittags war nie im Bundle).
#   python3 tools/audio/fresh_beats.py            -> out/audio/fresh/<name>.wav + <name>.json (alle Varianten)
#   python3 tools/audio/fresh_beats.py NAME ...   -> nur diese
# JSON: {bpm, beat (s), drop (Beat-Index des Drops, Video-Beat 4), dur, style, key}. Aufbau: Takt 1 ruhig (Pad + gefilterte Melodie),
# ab Beat 4 voller Beat. Stile: montagem (Funk-Tamborzão + Glocke), jersey (Jersey Club, 5er-Kick, Quietsch), lofi (Swing, Rhodes),
# future (Future Bass, Supersaw, Halbzeit-Snare), cine (Bumm + Streicher, episch). 100 % selbst synthetisiert -> keine Rechte-Fragen.
# JEDEN TAG 2–4 neue Varianten unten in VARIANTS anhängen (andere Tonart/BPM/Melodie-Seed/Muster), Datum im Namen.
import json, os, sys, subprocess
import numpy as np

SR = 44100
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'out/audio/fresh')
NOTES = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
MINOR = [0, 2, 3, 5, 7, 8, 10]

# name: (style, bpm, key, seed, bars)
VARIANTS = {
    # 06.11.
    'mtg_0611_f': ('montagem', 130, 'F', 61, 9),
    'jer_0611_d': ('jersey', 140, 'D', 62, 9),
    'fut_0611_a': ('future', 150, 'A', 63, 10),
    'cin_0611_e': ('cine', 100, 'E', 64, 7),
    'mtg_0611_g': ('montagem', 128, 'G#', 65, 9),
    'jer_0611_b': ('jersey', 145, 'B', 66, 10),
    'lof_0611_c': ('lofi', 82, 'C', 67, 12),
    'lof_0611_g': ('lofi', 76, 'G', 68, 11),
}


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def env(n, a=0.002, d=0.2, s=0.0, curve=1.0):
    t = np.arange(n) / SR
    e = np.exp(-t / max(d, 1e-4)) * (1 - s) + s
    na = max(1, int(a * SR))
    e[:na] *= np.linspace(0, 1, na)
    return e ** curve


def lp(x, cut):
    a = np.exp(-2 * np.pi * cut / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):  # kurz genug (wenige Sekunden je Ton)
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y


def lp_fast(x, cut):
    # Ein-Pol-Tiefpass über FFT-Näherung (für lange Spuren)
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    return np.fft.irfft(X / np.sqrt(1 + (f / cut) ** 4), len(x))


def hp_fast(x, cut):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    g = (f / cut) ** 2 / np.sqrt(1 + (f / cut) ** 4)
    return np.fft.irfft(X * g, len(x))


def kick(punch=1.0, long=0.35):
    n = int(SR * long)
    t = np.arange(n) / SR
    f = 45 + 110 * np.exp(-t / 0.035) * punch
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * env(n, 0.001, long / 2.5)
    x[:200] += np.random.RandomState(1).randn(200) * 0.3 * np.linspace(1, 0, 200)
    return np.tanh(x * 1.6)


def clap(rs, tone=190, dec=0.12):
    n = int(SR * 0.3)
    nz = hp_fast(rs.randn(n), 900)
    e = env(n, 0.001, dec)
    for k in (0.0, 0.011, 0.022):  # Klatsch-Mehrfachschlag
        i = int(k * SR)
        e[i:i + 200] += np.linspace(0.6, 0, 200)
    t = np.arange(n) / SR
    return 0.7 * nz * e / (np.abs(nz).max() + 1e-9) + 0.25 * np.sin(2 * np.pi * tone * t) * env(n, 0.001, 0.05)


def hat(rs, dec=0.03, open_=False):
    n = int(SR * (0.25 if open_ else 0.08))
    x = hp_fast(rs.randn(n), 7000)
    x /= np.abs(x).max() + 1e-9
    return x * env(n, 0.0005, 0.12 if open_ else dec) * 0.5


def bell(freq, dur=0.25):
    n = int(SR * dur)
    t = np.arange(n) / SR
    x = np.sign(np.sin(2 * np.pi * freq * t)) * 0.5 + np.sign(np.sin(2 * np.pi * freq * 1.48 * t)) * 0.4
    return lp_fast(x, 3500) * env(n, 0.001, 0.06)


def pluck(freq, dur, bright=4000, saw=True):
    n = int(SR * dur)
    t = np.arange(n) / SR
    if saw:
        x = 2 * ((t * freq) % 1) - 1 + 0.5 * (2 * ((t * freq * 1.005) % 1) - 1)
    else:
        x = np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(4 * np.pi * freq * t)
    return lp_fast(x, bright) * env(n, 0.003, dur * 0.35)


def supersaw(freqs, dur, cut=2500, rs=None):
    n = int(SR * dur)
    t = np.arange(n) / SR
    x = np.zeros(n)
    for f in freqs:
        for d in (-0.012, -0.005, 0, 0.006, 0.013):
            ph = rs.rand() if rs is not None else 0
            x += 2 * ((t * f * (1 + d) + ph) % 1) - 1
    x = lp_fast(x, cut) / (len(freqs) * 5)
    return x * env(n, 0.01, dur, s=0.85)


def rhodes(freqs, dur):
    n = int(SR * dur)
    t = np.arange(n) / SR
    x = np.zeros(n)
    for f in freqs:
        x += np.sin(2 * np.pi * f * t + 0.8 * np.sin(2 * np.pi * f * 2 * t) * np.exp(-t / 0.3))
    x *= (1 + 0.15 * np.sin(2 * np.pi * 4.5 * t))  # Tremolo
    return x / len(freqs) * env(n, 0.005, 0.9, s=0.2)


def sub808(freq, dur, glide_from=None):
    n = int(SR * dur)
    t = np.arange(n) / SR
    f = np.full(n, freq)
    if glide_from:
        f = freq + (glide_from - freq) * np.exp(-t / 0.05)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR)
    return np.tanh(2.2 * x) * env(n, 0.003, dur * 0.7, s=0.3)


def boom(dur=2.5):
    n = int(SR * dur)
    t = np.arange(n) / SR
    f = 30 + 60 * np.exp(-t / 0.15)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.002, 0.9)
    return np.tanh(2 * x)


def place(buf, x, at, gain=1.0):
    i = int(at * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(x))
    buf[i:j] += x[:j - i] * gain


def reverb(x, mix=0.25):
    y = x.copy()
    for d, g in ((0.031, 0.5), (0.047, 0.45), (0.071, 0.4), (0.113, 0.35), (0.157, 0.3), (0.229, 0.25)):
        k = int(d * SR)
        y[k:] += x[:-k] * g * mix
    return y


def build(name, style, bpm, key, seed, bars):
    rs = np.random.RandomState(seed)
    beat = 60.0 / bpm
    s16 = beat / 4
    n = int(SR * (bars * 4 * beat + 2.5))
    drums, bass, mel, pad = (np.zeros(n) for _ in range(4))
    root = 48 + NOTES[key]
    # Akkordfolge (Moll) – je Seed andere Stufen
    prog_opts = [[0, 5, 3, 4], [0, 3, 5, 4], [0, 5, 6, 4], [0, 6, 3, 4], [0, 2, 5, 4]]
    prog = prog_opts[rs.randint(len(prog_opts))]

    def deg(d, octave=0):
        return root + MINOR[d % 7] + 12 * (d // 7 + octave)

    # Melodie-Motiv (8 Achtel), zufällig aus der Skala, je Seed anders
    motif = [rs.choice([0, 2, 4, 4, 7, 5, 3, 9, 7, 6]) if rs.rand() > 0.22 else None for _ in range(8)]
    motif[0] = motif[0] if motif[0] is not None else 4
    kpat = {
        'montagem': [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        'jersey': [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        'future': [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        'lofi': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        'cine': [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    }[style]
    if rs.rand() > 0.5 and style in ('montagem', 'jersey'):
        kpat = kpat[8:] + kpat[:8]
        kpat[0] = 1
    K = kick(1.0 if style != 'lofi' else 0.6, 0.45 if style in ('future', 'cine') else 0.3)
    swing = 0.12 * s16 if style == 'lofi' else 0.0
    for bar in range(bars):
        t_bar = bar * 4 * beat
        chord_deg = prog[bar % 4]
        chord = [deg(chord_deg), deg(chord_deg + 2), deg(chord_deg + 4)]
        intro = bar == 0
        # Pad / Akkorde
        if style in ('future', 'cine'):
            place(pad, supersaw([hz(m + 12) for m in chord], 4 * beat, 1200 if intro else 3200, rs), t_bar, 0.55)
        elif style == 'lofi':
            place(pad, rhodes([hz(m + 12) for m in chord] + [hz(chord[0] + 22)], 4 * beat), t_bar, 0.5)
        else:
            place(pad, supersaw([hz(m + 12) for m in chord], 4 * beat, 900, rs), t_bar, 0.25)
        for st in range(16):
            t = t_bar + st * s16 + (swing if st % 2 else 0)
            if not intro:
                if kpat[st]:
                    place(drums, K, t, 0.95)
                    if style != 'cine':
                        place(bass, sub808(hz(chord[0] - 12), 3 * s16 if style != 'future' else 6 * s16,
                                           glide_from=hz(chord[0]) if st == 0 and bar % 2 else None), t, 0.6)
                # Snare/Clap
                if style == 'montagem' and st in (4, 12):
                    place(drums, clap(rs), t, 0.55)
                if style == 'montagem' and st in (3, 7, 11, 14) and rs.rand() > 0.3:
                    place(mel, bell(hz(deg(motif[st % 8] or 0, 2))), t, 0.32)
                if style == 'jersey':
                    if st in (4, 12) or (st == 14 and bar % 2):
                        place(drums, clap(rs, 210, 0.09), t, 0.55)
                    if st % 2 == 0:
                        place(drums, hat(rs), t, 0.35)
                if style == 'future':
                    if st == 8:
                        place(drums, clap(rs, 200, 0.2), t, 0.7)
                    if st % 2 == 0:
                        place(drums, hat(rs, open_=(st == 6)), t, 0.25)
                if style == 'lofi':
                    if st in (4, 12):
                        place(drums, clap(rs, 170, 0.07), t, 0.35)
                    if st % 2 == 0:
                        place(drums, hat(rs, 0.02), t, 0.18)
                if style == 'cine':
                    if st == 0 and bar % 2 == 1:
                        place(drums, boom(), t, 0.8)
                    if st in (4, 12):
                        place(drums, clap(rs, 120, 0.25), t, 0.35)
                    if st % 4 == 2:
                        place(drums, hat(rs), t, 0.15)
            # Melodie auf Achteln (Intro gefiltert)
            if st % 2 == 0:
                m = motif[(st // 2 + (bar % 2) * 3) % 8]
                if m is not None and (style != 'montagem' or intro or st % 4 == 0):
                    f = hz(deg(chord_deg + m, 1 if style != 'lofi' else 1))
                    if style == 'lofi':
                        place(mel, pluck(f, 2 * s16 * 1.6, 1800, saw=False), t, 0.22)
                    elif style == 'cine':
                        place(mel, supersaw([f], 2 * s16, 2400, rs), t, 0.35)
                    else:
                        place(mel, pluck(f, 2 * s16 * 1.4, 1600 if intro else 4500), t, 0.3)
    # Sidechain (Pad + Melodie ducken auf den Kick)
    duck = np.ones(n)
    for bar in range(1, bars):
        for st in range(16):
            if kpat[st]:
                i = int((bar * 4 * beat + st * s16) * SR)
                m = int(0.18 * SR)
                if i < n:
                    seg = 1 - 0.6 * np.exp(-np.arange(min(m, n - i)) / SR / 0.06)
                    duck[i:i + len(seg)] = np.minimum(duck[i:i + len(seg)], seg)
    pad = reverb(pad, 0.3) * duck
    mel = reverb(mel, 0.35 if style in ('lofi', 'cine') else 0.2) * (duck * 0.5 + 0.5)
    mix = drums + bass + pad + mel
    # Intro-Takt: Tiefpass-Gefühl -> leiser Hochpass-Hauch, Riser in den Drop
    i_drop = int(4 * beat * SR)
    rise = hp_fast(rs.randn(i_drop), 3000) * np.linspace(0, 0.12, i_drop) ** 1.5
    mix[:i_drop] = mix[:i_drop] * 0.7 + rise
    if style == 'lofi':  # Plattenknistern
        crack = (rs.rand(n) > 0.9993) * rs.randn(n) * 0.25
        mix += lp_fast(crack, 3000) + hp_fast(rs.randn(n), 4000) * 0.004
    # Ende ausblenden
    fo = int(1.2 * SR)
    end = int(bars * 4 * beat * SR)
    mix[end - fo:end] *= np.linspace(1, 0, fo)
    mix[end:] = 0
    mix = mix[:end]
    mix = np.tanh(mix / (np.abs(mix).max() + 1e-9) * 1.4) * 0.89
    os.makedirs(OUT, exist_ok=True)
    wav = os.path.join(OUT, name + '.wav')
    pcm = (mix * 32767).astype('<i2').tobytes()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '1', '-i', '-',
                    '-af', 'loudnorm=I=-14:TP=-1.0', '-ar', str(SR), '-ac', '2', wav], input=pcm, check=True)
    meta = dict(name=name, style=style, bpm=bpm, beat=beat, drop=4, dur=end / SR, key=key + 'm', seed=seed)
    json.dump(meta, open(os.path.join(OUT, name + '.json'), 'w'))
    return wav


if __name__ == '__main__':
    names = sys.argv[1:] or list(VARIANTS)
    for nm in names:
        print(build(nm, *VARIANTS[nm]))
