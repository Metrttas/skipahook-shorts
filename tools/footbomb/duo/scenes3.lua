-- Szene airwar2 (19.11.2026): Fallrückzieher, Scherenschlag, Kopfball, Volley – alles in der Luft hin und her, Ablage, Scorpion von Blau.
-- Rot grätscht zu zweit, beide zu spät. Nach scenes2.lua laden (= Studio _G.FB_SC3_SRC).
local D = _G.FB_DD
local SC = D.SCENES
local V = Vector3.new
local function slideMiss(who, t, at, dir, len)
	return { t = t, who = who, kind = "S_SlideShot", pose = true, at = at, slide = dir, len = len or 5, hold = 3, holdPose = true }
end
local SLOW = { { 6, 1 }, { 8, 1, 0.3 }, { 30, 0.3 }, { 10, 0.3, 1 } }
SC.airwar2 = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Finn", start = V(-22, 0, -70) },
			{ id = "r2", team = "red", avatar = "Ivy", start = V(-31, 0, -80) },
			{ id = "b1", team = "blue", avatar = "Nyx", start = V(21, 0, -70) },
			{ id = "b2", team = "blue", avatar = "Sky", start = V(29, 0, -79) },
		},
		events = {
			{ t = 0.5, who = "r2", kind = "S_Chip", at = V(-31, 0, -80), gs = 0.8, faceTo = V(21, 0, -70) },
			{ t = 1.8, who = "b1", kind = "S_Bicycle", at = V(21, 0, -70), jump = 4.0, gs = 0.85, big = true, faceTo = V(-22, 0, -72) },
			{ t = 2.9, who = "r1", kind = "S_Scissor", at = V(-22, 0, -72), jump = 3.6, gs = 0.85, big = true, faceTo = V(29, 0, -79) },
			{ t = 4.0, who = "b2", kind = "S_LeapHeader", at = V(29, 0, -79), part = "Head", jump = 3.6, gs = 0.85, big = true, faceTo = V(-26, 0, -82) },
			{ t = 5.1, who = "r2", kind = "S_JumpVolley", at = V(-26, 0, -82), jump = 3.2, gs = 0.85, big = true, faceTo = V(17, 0, -66) },
			{ t = 6.2, who = "b1", kind = "C_Head", at = V(17, 0, -66), part = "Head", gs = 0.9, faceTo = V(27, 0, -72) },
			{ t = 7.35, who = "b2", kind = "S_Scorpion", at = V(27, 0, -72), jump = 2.5, gs = 1.0, big = true, power = true, faceTo = V(-33, 0, -57) },
			{ t = 7.95, endPoint = true, at = V(-33, 0, -57) },
			{ t = 5.5, who = "b1", move = true, at = V(17, 0, -66), from = 2.3 },
			{ t = 4.4, who = "r2", move = true, at = V(-26, 0, -82), from = 1.0 },
			{ t = 6.8, who = "b2", move = true, at = V(27, 0, -72), from = 4.5 },
			{ t = 6.4, who = "r1", move = true, at = V(-25, 0, -66), from = 3.4 },
			slideMiss("r1", 7.83, V(-26, 0, -63), V(-0.6, 0, 0.8), 5),
			{ t = 7.2, who = "r2", move = true, at = V(-37, 0, -70), from = 5.6 },
			slideMiss("r2", 7.88, V(-37.5, 0, -63), V(0.1, 0, 1), 4.5),
			{ t = 9.0, who = "b2", kind = "Celebrate", pose = true, at = V(27, 0, -72), faceTo = V(15, 0, -68), dur = 2.6 },
			{ t = 8.8, who = "b1", kind = "Emote_Clap", pose = true, at = V(17, 0, -66), faceTo = V(27, 0, -72) },
		},
		elim = { team = "red", t = 7.95, wait = 0.9 },
		seq = {
			{ T0 = 0.3, cam = { type = "side", zs = 1, dist = 56, h = 24, track = 0.45, fov = 50, lookY = 3 }, segs = { { 81, 1 } } },
			{ T0 = 1.65, cam = { type = "hero", who = "b1", angle = -120, dist = 14, h = 5, abs = true, lookY = 1, fov = 54, orbit = -14, ballMix = 0.3 }, segs = SLOW },
			{ cam = { type = "side", zs = 1, dist = 54, h = 24, track = 0.45, fov = 50, lookY = 3 }, segs = { { 39, 1 } } },
			{ T0 = 2.75, cam = { type = "hero", who = "r1", angle = 120, dist = 14, h = 5, abs = true, lookY = 1, fov = 54, orbit = 14, ballMix = 0.3 }, segs = SLOW },
			{ cam = { type = "side", zs = 1, dist = 54, h = 24, track = 0.45, fov = 50, lookY = 3 }, segs = { { 39, 1 } } },
			{ T0 = 3.85, cam = { type = "hero", who = "b2", angle = -120, dist = 13, h = 5, abs = true, lookY = 1.5, fov = 54, orbit = -12, ballMix = 0.3 }, segs = SLOW },
			{ cam = { type = "follow", who = "r2", back = 12, up = 6, side = -3, mix = 0.5, fov = 60 }, segs = { { 60, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 54, h = 24, track = 0.45, fov = 50, lookY = 3 }, segs = { { 60, 1 } } },
			{ cam = { type = "follow", who = "b2", back = 12, up = 6, side = 3, mix = 0.5, fov = 60 }, segs = { { 36, 1 } } },
			{ T0 = 7.0, cam = { type = "hero", who = "b2", angle = -105, dist = 16, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = -12, ballMix = 0.25 }, segs = { { 8, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = -4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 30, 0.6 } } },
			{ T0 = 7.82, cam = { type = "fixed", pos = V(-48, 20, -43), at = V(-33, 4, -58), fov = 56, dolly = V(-1.5, 0.8, 1.5) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 8.9, cam = { type = "hero", who = "b2", angle = -15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = 12 }, segs = { { 110, 1 } } },
		},
	}
end
return true
