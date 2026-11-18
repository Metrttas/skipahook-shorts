-- Szenen für den DuoDirector (Stand 18.11.2026, = Studio _G.FB_SC_SRC). Felder: Rot x -43..-1, Blau x 1..43, z -91..-49 (Größe 42).
-- Regeln: Avatar "Rio" NIE (Kette zeigt echten Streamer-Namen). Ace (orange) nur im roten Team.
-- Verteidiger-Hechtsprung ~0.25 s VOR der Landung, seitlich neben der Ballbahn, hold = 3, holdPose = true (bleibt liegen).
-- Einschlag-Kamera (fixed) von der Außenseite, damit kein Verteidiger zwischen Kamera und Einschlag steht.
local D = _G.FB_DD
local SC = D.SCENES
local V = Vector3.new
SC.bike = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Leo", start = V(-31, 0, -61) },
			{ id = "r2", team = "red", avatar = "Mika", start = V(-17, 0, -83) },
			{ id = "b1", team = "blue", avatar = "Max", start = V(17, 0, -61) },
			{ id = "b2", team = "blue", avatar = "Kai", start = V(32, 0, -81) },
		},
		events = {
			{ t = 0.8, who = "b1", kind = "S_Drive", at = V(14, 0, -63), gs = 0.8, faceTo = V(-28, 0, -58) },
			{ t = 2.0, who = "r1", kind = "C_Chest", at = V(-28, 0, -59), part = "UpperTorso", fwd = 1.7, gs = 1.0 },
			{ t = 2.62, who = "r1", kind = "S_Chip", at = V(-27.5, 0, -60), gs = 0.72, faceTo = V(-15, 0, -76) },
			{ t = 3.95, who = "r2", kind = "S_Bicycle", at = V(-14, 0, -75), jump = 4.4, gs = 1.0, big = true, power = true, faceTo = V(31, 0, -56.5) },
			{ t = 4.55, endPoint = true, at = V(31, 0, -56.5) },
			{ t = 4.4, who = "b1", move = true, at = V(18, 0, -67), from = 3.4 },
			{ t = 4.2, who = "b2", move = true, at = V(31.5, 0, -67), from = 3.5 },
			{ t = 4.52, who = "b2", kind = "Dive", pose = true, at = V(31.5, 0, -61.5), dive = V(0, 0, 1), len = 4.2 },
			{ t = 5.55, who = "r2", kind = "Celebrate", pose = true, at = V(-14, 0, -75), faceTo = V(10, 0, -75), dur = 2.6 },
			{ t = 5.35, who = "r1", kind = "Emote_Clap", pose = true, at = V(-24, 0, -64), faceTo = V(-14, 0, -75) },
		},
		elim = { team = "blue", t = 4.55, wait = 0.9 },
		seq = {
			{ T0 = 0.62, cam = { type = "follow", who = "r1", back = 12, up = 6, side = -3, mix = 0.5, fov = 62 }, segs = { { 89, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 50, h = 22, track = 0.55, fov = 50, lookY = 2 }, segs = { { 96, 1 } } },
			{ cam = { type = "hero", who = "r2", angle = 105, dist = 17, h = 5.5, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 8, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 33, 0.6 } } },
			{ T0 = 4.42, cam = { type = "fixed", pos = V(14, 21, -30), at = V(29, 7, -61), fov = 56, dolly = V(-2.2, 0.8, 1.2) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 55, 1 } } },
			{ T0 = 5.45, cam = { type = "hero", who = "r2", angle = 10, dist = 11, h = 2.5, lookY = 2.5, fov = 52, orbit = -12 }, segs = { { 110, 1 } } },
		},
	}
end
SC.fake = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Ace", start = V(-25, 0, -63) },
			{ id = "r2", team = "red", avatar = "Juno", start = V(-30, 0, -82) },
			{ id = "b1", team = "blue", avatar = "Zed", start = V(14, 0, -61) },
			{ id = "b2", team = "blue", avatar = "Bo", start = V(30, 0, -79) },
		},
		events = {
			{ t = 0.6, who = "b2", kind = "S_Volley", at = V(29, 0, -77), gs = 0.85, faceTo = V(-24, 0, -64) },
			{ t = 1.75, who = "r1", kind = "C_Foot", at = V(-24, 0, -64), gs = 1.0, faceTo = V(-23, 0, -64), fwd = 1.0 },
			{ t = 2.22, who = "r1", kind = "PowerHold", pose = true, at = V(-24, 0, -64), faceTo = V(30, 0, -88), dur = 0.42, contactAt = 0.02, pre = 0.12 },
			{ t = 2.85, who = "r1", kind = "S_Volley", at = V(-23.5, 0, -64), gs = 0.95, big = true, power = true, faceTo = V(37, 0, -52.5), pre = 0.1 },
			{ t = 3.6, endPoint = true, at = V(37, 0, -52.5) },
			{ t = 2.95, who = "b2", move = true, at = V(31, 0, -85), from = 2.35 },
			{ t = 3.15, who = "b2", kind = "Dash", pose = true, at = V(31, 0, -85), faceTo = V(33, 0, -90) },
			{ t = 3.42, who = "b1", move = true, at = V(24.5, 0, -61.5), from = 2.95 },
			{ t = 3.6, who = "b1", kind = "Dive", pose = true, at = V(27, 0, -58.8), dive = V(0.6, 0, 1), len = 3.4 },
			{ t = 4.75, who = "r1", kind = "Emote_Dab", pose = true, at = V(-23.5, 0, -64), faceTo = V(-10, 0, -60) },
			{ t = 4.6, who = "r2", kind = "Emote_Clap", pose = true, at = V(-27, 0, -76), faceTo = V(-23, 0, -64) },
		},
		elim = { team = "blue", t = 3.6, wait = 0.9 },
		seq = {
			{ T0 = 1.15, cam = { type = "follow", who = "r1", back = 11, up = 5, side = 3, mix = 0.4, fov = 60 }, segs = { { 60, 1 } } },
			{ cam = { type = "hero", who = "r1", angle = 150, dist = 12, h = 3.2, abs = true, lookY = 0.5, fov = 52, orbit = 10, ballMix = 0.25 }, segs = { { 6, 1 }, { 10, 1, 0.3 }, { 34, 0.3 }, { 10, 0.3, 1 }, { 6, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 54, h = 24, track = 0.6, fov = 50, lookY = 2, x0 = 8 }, segs = { { 38, 1 }, { 8, 1, 0.2 }, { 30, 0.2 }, { 12, 0.2, 1 }, { 20, 1 } } },
			{ T0 = 3.7, cam = { type = "fixed", pos = V(16, 26, -26), at = V(30, 6, -58), fov = 55, dolly = V(1.5, 0.8, 1.5) }, segs = { { 90, 1 } } },
			{ T0 = 4.55, cam = { type = "hero", who = "r1", angle = 20, dist = 11, h = 2.8, abs = true, lookY = 0.8, fov = 52, orbit = -10 }, segs = { { 100, 1 } } },
		},
	}
end

SC.save = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Nova", start = V(-20, 0, -62) },
			{ id = "r2", team = "red", avatar = "Mika", start = V(-26, 0, -78) },
			{ id = "b1", team = "blue", avatar = "Max", start = V(14, 0, -61) },
			{ id = "b2", team = "blue", avatar = "Kai", start = V(31, 0, -79) },
		},
		events = {
			{ t = 0.55, who = "b1", kind = "S_Drive", at = V(14, 0, -61), gs = 0.9, big = true, power = true, faceTo = V(-36, 0, -85) },
			{ t = 1.45, who = "r2", kind = "S_SlideShot", at = V(-35, 0, -84), slide = V(-1, 0, -0.55), len = 6, gs = 0.8, faceTo = V(-20, 0, -66), hold = 0.7, big = true, contactAt = 0.24, fwd = 0.5 },
			{ t = 2.55, who = "r1", kind = "S_Header", at = V(-20, 0, -66), part = "Head", gs = 0.9, faceTo = V(27, 0, -76) },
			{ t = 3.55, who = "b2", kind = "S_Volley", at = V(27, 0, -76), gs = 0.9, faceTo = V(-18, 0, -73) },
			{ t = 4.6, who = "r2", kind = "S_Scissor", at = V(-18, 0, -73), jump = 3.8, gs = 1.0, big = true, power = true, faceTo = V(10, 0, -52) },
			{ t = 5.2, endPoint = true, at = V(10, 0, -52) },
			{ t = 5.08, who = "b1", kind = "S_SlideShot", pose = true, at = V(13.5, 0, -58.5), slide = V(-0.25, 0, 1), len = 4 },
			{ t = 6.1, who = "r2", kind = "Celebrate", pose = true, at = V(-18, 0, -73), faceTo = V(0, 0, -60), dur = 2.6 },
			{ t = 4.05, who = "r1", move = true, at = V(-31, 0, -58), from = 3.05 },
			{ t = 6.0, who = "r1", kind = "Emote_Flex", pose = true, at = V(-31, 0, -58), faceTo = V(-18, 0, -73) },
		},
		elim = { team = "blue", t = 5.2, wait = 0.9 },
		seq = {
			{ T0 = 0.3, cam = { type = "side", zs = 1, dist = 56, h = 24, track = 0.5, fov = 50, lookY = 2 }, segs = { { 50, 1 } } },
			{ cam = { type = "hero", who = "r2", toward = V(-1, 0, -0.55), angle = 90, dist = 12, h = 2.6, abs = true, lookY = -0.5, fov = 55, orbit = -18, ballMix = 0.3 }, segs = { { 14, 1 }, { 10, 1, 0.25 }, { 40, 0.25 }, { 10, 0.25, 1 }, { 30, 1 } } },
			{ cam = { type = "follow", who = "r1", back = 12, up = 6, side = -3, mix = 0.5, fov = 60 }, segs = { { 70, 1 } } },
			{ cam = { type = "follow", who = "b2", back = 11, up = 5.5, side = 3, mix = 0.5, fov = 60 }, segs = { { 64, 1 } } },
			{ cam = { type = "hero", who = "r2", angle = -100, dist = 15, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = -14, ballMix = 0.25 }, segs = { { 10, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.7 } } },
			{ T0 = 5.05, cam = { type = "fixed", pos = V(-2, 20, -30), at = V(12, 6, -54), fov = 55, dolly = V(1.5, 0.6, 1) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 36, 0.15 }, { 16, 0.15, 1 }, { 60, 1 } } },
			{ T0 = 6.0, cam = { type = "hero", who = "r2", angle = 15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = -12 }, segs = { { 105, 1 } } },
		},
	}
end

SC.scorp = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Leo", start = V(-27, 0, -64) },
			{ id = "r2", team = "red", avatar = "Juno", start = V(-16, 0, -84) },
			{ id = "b1", team = "blue", avatar = "Zed", start = V(16, 0, -64) },
			{ id = "b2", team = "blue", avatar = "Bo", start = V(30, 0, -80) },
		},
		events = {
			{ t = 0.7, who = "b1", kind = "S_Chip", at = V(16, 0, -64), gs = 0.8, faceTo = V(-25, 0, -68) },
			{ t = 2.05, who = "r1", kind = "C_Head", at = V(-25, 0, -68), part = "Head", gs = 0.9, faceTo = V(-13, 0, -80) },
			{ t = 3.25, who = "r2", kind = "S_Scorpion", at = V(-13, 0, -80), jump = 2.5, gs = 1.0, big = true, power = true, faceTo = V(30, 0, -56) },
			{ t = 3.85, endPoint = true, at = V(30, 0, -56) },
			{ t = 3.0, who = "b1", move = true, at = V(14, 0, -77), from = 1.6 },
			{ t = 3.3, who = "b2", move = true, at = V(27, 0, -67), from = 2.6 },
			{ t = 3.6, who = "b2", kind = "Dive", pose = true, at = V(27, 0, -61.5), dive = V(0.2, 0, 1), len = 3.4, hold = 3, holdPose = true },
			{ t = 4.9, who = "r2", kind = "Celebrate", pose = true, at = V(-13, 0, -80), faceTo = V(0, 0, -72), dur = 2.6 },
			{ t = 4.7, who = "r1", kind = "Emote_Dab", pose = true, at = V(-24, 0, -70), faceTo = V(-13, 0, -80) },
		},
		elim = { team = "blue", t = 3.85, wait = 0.9 },
		seq = {
			{ T0 = 0.4, cam = { type = "follow", who = "r1", back = 12, up = 6, side = -3, mix = 0.5, fov = 62 }, segs = { { 120, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 50, h = 22, track = 0.55, fov = 50, lookY = 2 }, segs = { { 30, 1 } } },
			{ cam = { type = "hero", who = "r2", angle = 105, dist = 16, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 8, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 30, 0.6 } } },
			{ T0 = 3.72, cam = { type = "fixed", pos = V(44, 20, -42), at = V(30, 4, -57), fov = 56, dolly = V(1.5, 0.8, 1.5) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 4.75, cam = { type = "hero", who = "r2", angle = 15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = -12 }, segs = { { 110, 1 } } },
		},
	}
end

SC.tornado = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Ace", start = V(-20, 0, -61) },
			{ id = "r2", team = "red", avatar = "Mika", start = V(-32, 0, -80) },
			{ id = "b1", team = "blue", avatar = "Max", start = V(17, 0, -68) },
			{ id = "b2", team = "blue", avatar = "Kai", start = V(32, 0, -77) },
		},
		events = {
			{ t = 0.6, who = "b2", kind = "S_Volley", at = V(31, 0, -77), gs = 0.85, faceTo = V(-21, 0, -63) },
			{ t = 1.85, who = "r1", kind = "C_Chest", at = V(-21, 0, -63), part = "UpperTorso", fwd = 1.5, gs = 1.0, faceTo = V(20, 0, -66) },
			{ t = 2.45, who = "r1", kind = "S_Heel", at = V(-21.5, 0, -63.5), back = true, gs = 0.8, faceTo = V(-29, 0, -78) },
			{ t = 3.55, who = "r2", kind = "S_Tornado", at = V(-29, 0, -78), jump = 3, gs = 1.0, big = true, power = true, faceTo = V(36, 0, -85) },
			{ t = 4.15, endPoint = true, at = V(36, 0, -85) },
			{ t = 3.4, who = "b1", move = true, at = V(9, 0, -73), from = 2.4 },
			{ t = 3.86, who = "b1", kind = "Dive", pose = true, at = V(9, 0, -75.5), dive = V(0, 0, -1), len = 3, hold = 3, holdPose = true },
			{ t = 3.75, who = "b2", move = true, at = V(29.5, 0, -78), from = 3.2 },
			{ t = 3.98, who = "b2", kind = "Dive", pose = true, at = V(31, 0, -80.5), dive = V(0.6, 0, -1), len = 3, hold = 3, holdPose = true },
			{ t = 5.2, who = "r2", kind = "Celebrate", pose = true, at = V(-29, 0, -78), faceTo = V(-15, 0, -70), dur = 2.6 },
			{ t = 5.0, who = "r1", kind = "Emote_Flex", pose = true, at = V(-22, 0, -66), faceTo = V(-29, 0, -78) },
		},
		elim = { team = "blue", t = 4.15, wait = 0.9 },
		seq = {
			{ T0 = 1.2, cam = { type = "follow", who = "r1", back = 12, up = 6, side = 3, mix = 0.45, fov = 62 }, segs = { { 93, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 50, h = 22, track = 0.55, fov = 50, lookY = 2 }, segs = { { 30, 1 } } },
			{ cam = { type = "hero", who = "r2", angle = 100, dist = 16, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 8, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 30, 0.6 } } },
			{ T0 = 4.02, cam = { type = "fixed", pos = V(48, 20, -66), at = V(35, 4, -84), fov = 56, dolly = V(1.5, 0.8, 1.5) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 5.05, cam = { type = "hero", who = "r2", angle = 15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = -12 }, segs = { { 110, 1 } } },
		},
	}
end

SC.rally = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Leo", start = V(-18, 0, -70) },
			{ id = "r2", team = "red", avatar = "Nova", start = V(-30, 0, -80) },
			{ id = "b1", team = "blue", avatar = "Kai", start = V(18, 0, -70) },
			{ id = "b2", team = "blue", avatar = "Zed", start = V(28, 0, -60) },
		},
		events = {
			{ t = 0.5, who = "b1", kind = "S_Volley", at = V(18, 0, -70), gs = 0.85, faceTo = V(-20, 0, -74) },
			{ t = 1.6, who = "r1", kind = "S_Volley", at = V(-20, 0, -74), gs = 0.85, faceTo = V(26, 0, -62) },
			{ t = 2.7, who = "b2", kind = "S_Header", at = V(26, 0, -62), part = "Head", gs = 0.85, faceTo = V(-28, 0, -82) },
			{ t = 3.85, who = "r2", kind = "C_Head", at = V(-28, 0, -82), part = "Head", gs = 0.9, faceTo = V(-14, 0, -73) },
			{ t = 5.0, who = "r1", kind = "S_AxeSpike", at = V(-14, 0, -73), jump = 3.5, gs = 1.0, big = true, power = true, faceTo = V(31, 0, -87) },
			{ t = 5.45, endPoint = true, at = V(31, 0, -87) },
			{ t = 4.7, who = "b1", move = true, at = V(19, 0, -77), from = 3.2 },
			{ t = 5.2, who = "b1", kind = "Dive", pose = true, at = V(24, 0, -79), dive = V(0.5, 0, -1), len = 3.4, hold = 3, holdPose = true },
			{ t = 4.6, who = "b2", move = true, at = V(24, 0, -66), from = 3.3 },
			{ t = 6.3, who = "r1", kind = "Celebrate", pose = true, at = V(-14, 0, -73), faceTo = V(-2, 0, -66), dur = 2.6 },
			{ t = 6.2, who = "r2", kind = "Emote_Clap", pose = true, at = V(-27, 0, -80), faceTo = V(-14, 0, -73) },
		},
		elim = { team = "blue", t = 5.45, wait = 0.9 },
		seq = {
			{ T0 = 0.25, cam = { type = "side", zs = 1, dist = 58, h = 26, track = 0.45, fov = 50, lookY = 2 }, segs = { { 105, 1 } } },
			{ cam = { type = "follow", who = "b2", back = 11, up = 5.5, side = 3, mix = 0.5, fov = 60 }, segs = { { 54, 1 } } },
			{ cam = { type = "follow", who = "r2", back = 12, up = 6, side = -3, mix = 0.5, fov = 60 }, segs = { { 84, 1 } } },
			{ cam = { type = "hero", who = "r1", angle = 100, dist = 15, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 30, 1 }, { 12, 1, 0.2 }, { 50, 0.2 }, { 12, 0.2, 0.7 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 25, 0.6 } } },
			{ T0 = 5.35, cam = { type = "fixed", pos = V(46, 20, -66), at = V(31, 4, -86), fov = 56, dolly = V(1.5, 0.8, 1.5) }, segs = { { 6, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 6.2, cam = { type = "hero", who = "r1", angle = 15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = -12 }, segs = { { 110, 1 } } },
		},
	}
end

SC.flyhead = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Bo", start = V(-34, 0, -57) },
			{ id = "r2", team = "red", avatar = "Max", start = V(-18, 0, -74) },
			{ id = "b1", team = "blue", avatar = "Juno", start = V(16, 0, -60) },
			{ id = "b2", team = "blue", avatar = "Nova", start = V(30, 0, -80) },
		},
		events = {
			{ t = 0.6, who = "b1", kind = "S_Drive", at = V(16, 0, -60), gs = 0.9, faceTo = V(-33, 0, -57) },
			{ t = 1.6, who = "r1", kind = "C_Foot", at = V(-33, 0, -57), gs = 1.0, faceTo = V(-31, 0, -58), fwd = 1.0 },
			{ t = 2.2, who = "r1", kind = "S_Chip", at = V(-32.5, 0, -57.5), gs = 0.75, faceTo = V(-12, 0, -72) },
			{ t = 3.4, who = "r2", kind = "S_FlyHeader", at = V(-12, 0, -72), part = "Head", dive = V(0.94, 0, -0.34), len = 4, gs = 1.0, big = true, power = true },
			{ t = 3.95, endPoint = true, at = V(36, 0, -87) },
			{ t = 3.0, who = "b1", move = true, at = V(12, 0, -68), from = 1.4 },
			{ t = 3.4, who = "b2", move = true, at = V(27.5, 0, -77), from = 2.9 },
			{ t = 3.7, who = "b2", kind = "Dive", pose = true, at = V(27.5, 0, -79.5), dive = V(0.3, 0, -1), len = 3, hold = 3, holdPose = true },
			{ t = 5.0, who = "r2", kind = "Celebrate", pose = true, at = V(-10, 0, -73), faceTo = V(0, 0, -70), dur = 2.6 },
			{ t = 4.8, who = "r1", kind = "Emote_Clap", pose = true, at = V(-28, 0, -61), faceTo = V(-10, 0, -73) },
		},
		elim = { team = "blue", t = 3.95, wait = 0.9 },
		seq = {
			{ T0 = 0.3, cam = { type = "follow", who = "r1", back = 12, up = 6, side = -3, mix = 0.5, fov = 62 }, segs = { { 132, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 50, h = 22, track = 0.55, fov = 50, lookY = 2 }, segs = { { 27, 1 } } },
			{ cam = { type = "hero", who = "r2", angle = 100, dist = 14, h = 4, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 15, 1 }, { 12, 1, 0.2 }, { 50, 0.2 }, { 10, 0.2, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 25, 0.6 } } },
			{ T0 = 3.83, cam = { type = "fixed", pos = V(47, 20, -66), at = V(36, 4, -86), fov = 56, dolly = V(1.5, 0.8, 1.5) }, segs = { { 7, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 4.9, cam = { type = "hero", who = "r2", angle = 15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = -12 }, segs = { { 110, 1 } } },
		},
	}
end

return true
