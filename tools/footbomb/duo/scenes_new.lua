
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
			{ t = 3.0, who = "b1", move = true, at = V(12, 0, -62), from = 1.6 },
			{ t = 3.55, who = "b2", move = true, at = V(28, 0, -66), from = 2.9 },
			{ t = 3.85, who = "b2", kind = "Dive", pose = true, at = V(28, 0, -60.5), dive = V(0.2, 0, 1), len = 3.4 },
			{ t = 4.9, who = "r2", kind = "Celebrate", pose = true, at = V(-13, 0, -80), faceTo = V(0, 0, -72), dur = 2.6 },
			{ t = 4.7, who = "r1", kind = "Emote_Dab", pose = true, at = V(-24, 0, -70), faceTo = V(-13, 0, -80) },
		},
		elim = { team = "blue", t = 3.85, wait = 0.9 },
		seq = {
			{ T0 = 0.4, cam = { type = "follow", who = "r1", back = 12, up = 6, side = -3, mix = 0.5, fov = 62 }, segs = { { 120, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 50, h = 22, track = 0.55, fov = 50, lookY = 2 }, segs = { { 30, 1 } } },
			{ cam = { type = "hero", who = "r2", angle = 105, dist = 16, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 8, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 30, 0.6 } } },
			{ T0 = 3.72, cam = { type = "fixed", pos = V(12, 21, -32), at = V(28, 6, -58), fov = 56, dolly = V(-2, 0.8, 1.2) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
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
			{ t = 3.86, who = "b1", kind = "Dive", pose = true, at = V(9, 0, -77), dive = V(0, 0, -1), len = 3 },
			{ t = 3.9, who = "b2", move = true, at = V(32, 0, -81), from = 3.3 },
			{ t = 4.05, who = "b2", kind = "Dash", pose = true, at = V(32, 0, -81), faceTo = V(36, 0, -86) },
			{ t = 5.2, who = "r2", kind = "Celebrate", pose = true, at = V(-29, 0, -78), faceTo = V(-15, 0, -70), dur = 2.6 },
			{ t = 5.0, who = "r1", kind = "Emote_Flex", pose = true, at = V(-22, 0, -66), faceTo = V(-29, 0, -78) },
		},
		elim = { team = "blue", t = 4.15, wait = 0.9 },
		seq = {
			{ T0 = 1.2, cam = { type = "follow", who = "r1", back = 12, up = 6, side = 3, mix = 0.45, fov = 62 }, segs = { { 93, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 50, h = 22, track = 0.55, fov = 50, lookY = 2 }, segs = { { 30, 1 } } },
			{ cam = { type = "hero", who = "r2", angle = 100, dist = 16, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 8, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 30, 0.6 } } },
			{ T0 = 4.02, cam = { type = "fixed", pos = V(20, 22, -56), at = V(35, 5, -83), fov = 56, dolly = V(1.5, 0.8, 1.5) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 5.05, cam = { type = "hero", who = "r2", angle = 15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = -12 }, segs = { { 110, 1 } } },
		},
	}
end

SC.rally = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Nova", start = V(-18, 0, -70) },
			{ id = "r2", team = "red", avatar = "Leo", start = V(-30, 0, -80) },
			{ id = "b1", team = "blue", avatar = "Ace", start = V(18, 0, -70) },
			{ id = "b2", team = "blue", avatar = "Zed", start = V(28, 0, -60) },
		},
		events = {
			{ t = 0.5, who = "b1", kind = "S_Volley", at = V(18, 0, -70), gs = 0.85, faceTo = V(-20, 0, -74) },
			{ t = 1.6, who = "r1", kind = "S_Volley", at = V(-20, 0, -74), gs = 0.85, faceTo = V(26, 0, -62) },
			{ t = 2.7, who = "b2", kind = "S_Header", at = V(26, 0, -62), part = "Head", gs = 0.85, faceTo = V(-28, 0, -82) },
			{ t = 3.85, who = "r2", kind = "C_Head", at = V(-28, 0, -82), part = "Head", gs = 0.9, faceTo = V(-14, 0, -73) },
			{ t = 5.0, who = "r1", kind = "S_AxeSpike", at = V(-14, 0, -73), jump = 3.5, gs = 1.0, big = true, power = true, faceTo = V(22, 0, -88) },
			{ t = 5.45, endPoint = true, at = V(22, 0, -88) },
			{ t = 4.5, who = "b1", move = true, at = V(18, 0, -79), from = 3.2 },
			{ t = 5.45, who = "b1", kind = "Dive", pose = true, at = V(20, 0, -83.5), dive = V(0.3, 0, -1), len = 3.4 },
			{ t = 4.6, who = "b2", move = true, at = V(24, 0, -66), from = 3.3 },
			{ t = 6.3, who = "r1", kind = "Emote_Flex", pose = true, at = V(-14, 0, -73), faceTo = V(-2, 0, -66) },
			{ t = 6.2, who = "r2", kind = "Emote_Clap", pose = true, at = V(-27, 0, -80), faceTo = V(-14, 0, -73) },
		},
		elim = { team = "blue", t = 5.45, wait = 0.9 },
		seq = {
			{ T0 = 0.25, cam = { type = "side", zs = 1, dist = 58, h = 26, track = 0.45, fov = 50, lookY = 2 }, segs = { { 105, 1 } } },
			{ cam = { type = "follow", who = "b2", back = 11, up = 5.5, side = 3, mix = 0.5, fov = 60 }, segs = { { 54, 1 } } },
			{ cam = { type = "follow", who = "r2", back = 12, up = 6, side = -3, mix = 0.5, fov = 60 }, segs = { { 84, 1 } } },
			{ cam = { type = "hero", who = "r1", angle = 100, dist = 15, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 30, 1 }, { 12, 1, 0.2 }, { 50, 0.2 }, { 12, 0.2, 0.7 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 25, 0.6 } } },
			{ T0 = 5.35, cam = { type = "fixed", pos = V(8, 22, -66), at = V(22, 5, -86), fov = 56, dolly = V(1.5, 0.8, 1.5) }, segs = { { 6, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
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
			{ t = 3.95, endPoint = true, at = V(32, 0, -88) },
			{ t = 3.0, who = "b1", move = true, at = V(12, 0, -68), from = 1.4 },
			{ t = 3.6, who = "b2", move = true, at = V(31, 0, -79), from = 3.0 },
			{ t = 3.95, who = "b2", kind = "Dive", pose = true, at = V(31, 0, -84), dive = V(0.2, 0, -1), len = 3 },
			{ t = 5.0, who = "r2", kind = "Celebrate", pose = true, at = V(-10, 0, -73), faceTo = V(-20, 0, -64), dur = 2.6 },
			{ t = 4.8, who = "r1", kind = "Emote_Clap", pose = true, at = V(-28, 0, -61), faceTo = V(-10, 0, -73) },
		},
		elim = { team = "blue", t = 3.95, wait = 0.9 },
		seq = {
			{ T0 = 0.3, cam = { type = "follow", who = "r1", back = 12, up = 6, side = -3, mix = 0.5, fov = 62 }, segs = { { 132, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 50, h = 22, track = 0.55, fov = 50, lookY = 2 }, segs = { { 27, 1 } } },
			{ cam = { type = "hero", who = "r2", angle = 100, dist = 14, h = 4, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 15, 1 }, { 12, 1, 0.2 }, { 50, 0.2 }, { 10, 0.2, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 25, 0.6 } } },
			{ T0 = 3.83, cam = { type = "fixed", pos = V(16, 22, -60), at = V(31, 5, -86), fov = 56, dolly = V(1.5, 0.8, 1.5) }, segs = { { 7, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 4.9, cam = { type = "hero", who = "r2", angle = 15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = -12 }, segs = { { 110, 1 } } },
		},
	}
end
