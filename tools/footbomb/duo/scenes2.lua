-- Szenen 19.11.2026 (User: "krassere Clips: in der Luft gegeneinander 2-3 Pässe, dann Scorpion; Verteidiger GRÄTSCHEN zum Saven
-- statt gerade zum Ball zu springen; das Spiel heißt Foot Bomb"). Nach scenes.lua laden (= Studio _G.FB_SC2_SRC).
-- 1) Alle alten Szenen: Verteidiger-"Dive" -> Grätsche (S_SlideShot als Pose, bleibt liegen).
-- 2) Neue Szenen: airwar, slidesave, airsave, slidechain.
local D = _G.FB_DD
local SC = D.SCENES
local V = Vector3.new

for _, name in { "bike", "fake", "scorp", "tornado", "rally", "flyhead", "save" } do
	local f = SC[name]
	if f and not SC[name .. "_dive"] then
		SC[name .. "_dive"] = f
		SC[name] = function()
			local s = f()
			for _, e in s.events do
				if e.kind == "Dive" then
					e.kind = "S_SlideShot"
					e.slide = e.dive
					e.dive = nil
					e.len = math.max(e.len or 4, 4.5)
					e.hold = 3
					e.holdPose = true
					e.t = e.t - 0.05
				end
			end
			return s
		end
	end
end

local function slideMiss(who, t, at, dir, len)
	return { t = t, who = who, kind = "S_SlideShot", pose = true, at = at, slide = dir, len = len or 5, hold = 3, holdPose = true }
end

-- Luft-Duell: Volley in der Luft, Kopfball in der Luft, Ablage, Scorpion. Blau grätscht, kommt zu spät.
SC.airwar = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Sky", start = V(-22, 0, -66) },
			{ id = "r2", team = "red", avatar = "Leo", start = V(-30, 0, -82) },
			{ id = "b1", team = "blue", avatar = "Jax", start = V(20, 0, -66) },
			{ id = "b2", team = "blue", avatar = "Ivy", start = V(31, 0, -80) },
		},
		events = {
			{ t = 0.5, who = "b1", kind = "S_Volley", at = V(20, 0, -66), gs = 0.85, faceTo = V(-20, 0, -70) },
			{ t = 1.55, who = "r1", kind = "S_JumpVolley", at = V(-20, 0, -70), jump = 3.2, gs = 0.85, big = true, faceTo = V(29, 0, -77) },
			{ t = 2.65, who = "b2", kind = "S_LeapHeader", at = V(29, 0, -77), part = "Head", jump = 3.6, gs = 0.85, big = true, faceTo = V(-27, 0, -81) },
			{ t = 3.75, who = "r2", kind = "C_Head", at = V(-27, 0, -81), part = "Head", gs = 0.9, faceTo = V(-15, 0, -75) },
			{ t = 4.9, who = "r1", kind = "S_Scorpion", at = V(-15, 0, -75), jump = 2.5, gs = 1.0, big = true, power = true, faceTo = V(34, 0, -56) },
			{ t = 5.5, endPoint = true, at = V(34, 0, -56) },
			{ t = 3.0, who = "r1", move = true, at = V(-15, 0, -75), from = 2.0 },
			{ t = 2.2, who = "b1", move = true, at = V(18, 0, -70), from = 1.0 },
			{ t = 4.7, who = "b1", move = true, at = V(22, 0, -62), from = 3.6 },
			{ t = 5.0, who = "b2", move = true, at = V(31.5, 0, -64), from = 3.3 },
			slideMiss("b2", 5.38, V(33, 0, -59), V(0.2, 0, 1), 5),
			{ t = 6.5, who = "r1", kind = "Celebrate", pose = true, at = V(-15, 0, -75), faceTo = V(0, 0, -68), dur = 2.6 },
			{ t = 6.3, who = "r2", kind = "Emote_Clap", pose = true, at = V(-24, 0, -79), faceTo = V(-15, 0, -75) },
		},
		elim = { team = "blue", t = 5.5, wait = 0.9 },
		seq = {
			{ T0 = 0.25, cam = { type = "side", zs = 1, dist = 56, h = 24, track = 0.45, fov = 50, lookY = 3 }, segs = { { 72, 1 } } },
			{ cam = { type = "hero", who = "r1", angle = 120, dist = 13, h = 4.5, abs = true, lookY = 1, fov = 54, orbit = 14, ballMix = 0.3 }, segs = { { 6, 1 }, { 8, 1, 0.3 }, { 30, 0.3 }, { 10, 0.3, 1 }, { 4, 1 } } },
			{ cam = { type = "follow", who = "b2", back = 12, up = 6, side = 3, mix = 0.5, fov = 60 }, segs = { { 50, 1 } } },
			{ cam = { type = "hero", who = "b2", angle = -120, dist = 13, h = 5, abs = true, lookY = 1.5, fov = 54, orbit = -12, ballMix = 0.3 }, segs = { { 6, 1 }, { 8, 1, 0.3 }, { 30, 0.3 }, { 10, 0.3, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 54, h = 24, track = 0.45, fov = 50, lookY = 3 }, segs = { { 75, 1 } } },
			{ T0 = 4.55, cam = { type = "hero", who = "r1", angle = 105, dist = 16, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 8, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 30, 0.6 } } },
			{ T0 = 5.37, cam = { type = "fixed", pos = V(48, 20, -42), at = V(34, 4, -57), fov = 56, dolly = V(1.5, 0.8, 1.5) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 6.4, cam = { type = "hero", who = "r1", angle = 15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = -12 }, segs = { { 110, 1 } } },
		},
	}
end

-- Grätschen-Save hinten in der Ecke, Abpraller zum Mitspieler, Fallrückzieher. Rot grätscht zu zweit, beide zu spät.
SC.slidesave = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Ace", start = V(-18, 0, -66) },
			{ id = "r2", team = "red", avatar = "Finn", start = V(-30, 0, -80) },
			{ id = "b1", team = "blue", avatar = "Max", start = V(16, 0, -63) },
			{ id = "b2", team = "blue", avatar = "Nyx", start = V(26, 0, -76) },
		},
		events = {
			{ t = 0.5, who = "r1", kind = "S_Drive", at = V(-18, 0, -66), gs = 0.9, big = true, power = true, faceTo = V(32, 0, -85) },
			{ t = 1.5, who = "b2", kind = "S_SlideShot", at = V(31, 0, -84), slide = V(0.45, 0, -1), len = 6, gs = 0.8, faceTo = V(17, 0, -67), hold = 0.7, big = true, contactAt = 0.24, fwd = 0.5 },
			{ t = 2.85, who = "b1", kind = "S_Bicycle", at = V(17, 0, -67), jump = 4.2, gs = 1.0, big = true, power = true, faceTo = V(-33, 0, -55) },
			{ t = 3.45, endPoint = true, at = V(-33, 0, -55) },
			{ t = 2.6, who = "r1", move = true, at = V(-24, 0, -63), from = 1.3 },
			slideMiss("r1", 3.33, V(-29.5, 0, -58.5), V(-0.75, 0, 0.66), 5),
			{ t = 2.9, who = "r2", move = true, at = V(-35, 0, -66), from = 1.6 },
			slideMiss("r2", 3.38, V(-35.5, 0, -60.5), V(-0.1, 0, 1), 4.5),
			{ t = 4.5, who = "b1", kind = "Celebrate", pose = true, at = V(17, 0, -67), faceTo = V(5, 0, -64), dur = 2.6 },
			{ t = 4.4, who = "b2", kind = "Emote_Flex", pose = true, at = V(31, 0, -80), faceTo = V(17, 0, -67) },
		},
		elim = { team = "red", t = 3.45, wait = 0.9 },
		seq = {
			{ T0 = 0.2, cam = { type = "follow", who = "r1", back = 12, up = 6, side = -3, mix = 0.45, fov = 62 }, segs = { { 54, 1 } } },
			{ cam = { type = "hero", who = "b2", toward = V(0.45, 0, -1), angle = 90, dist = 12, h = 2.8, abs = true, lookY = -0.5, fov = 55, orbit = 16, ballMix = 0.3 }, segs = { { 8, 1 }, { 12, 1, 0.2 }, { 45, 0.2 }, { 10, 0.2, 1 }, { 6, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 52, h = 22, track = 0.5, fov = 50, lookY = 3 }, segs = { { 40, 1 } } },
			{ T0 = 2.5, cam = { type = "hero", who = "b1", angle = -105, dist = 17, h = 5.5, abs = true, lookY = -0.5, fov = 52, orbit = -12, ballMix = 0.25 }, segs = { { 8, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = -4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 30, 0.6 } } },
			{ T0 = 3.32, cam = { type = "fixed", pos = V(-48, 20, -42), at = V(-33, 4, -57), fov = 56, dolly = V(-1.5, 0.8, 1.5) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 4.4, cam = { type = "hero", who = "b1", angle = -15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = 12 }, segs = { { 110, 1 } } },
		},
	}
end

-- Luft-Pässe hin und her, Grätschen-Save von Rot hinten, dann Scorpion.
SC.airsave = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Nova", start = V(-21, 0, -66) },
			{ id = "r2", team = "red", avatar = "Mika", start = V(-30, 0, -82) },
			{ id = "b1", team = "blue", avatar = "Kai", start = V(20, 0, -66) },
			{ id = "b2", team = "blue", avatar = "Zed", start = V(30, 0, -82) },
		},
		events = {
			{ t = 0.5, who = "b1", kind = "S_Chip", at = V(20, 0, -66), gs = 0.8, faceTo = V(-21, 0, -66) },
			{ t = 1.75, who = "r1", kind = "S_JumpVolley", at = V(-21, 0, -66), jump = 3.2, gs = 0.85, big = true, faceTo = V(24, 0, -72) },
			{ t = 2.85, who = "b1", kind = "S_LeapHeader", at = V(24, 0, -72), part = "Head", jump = 3.6, gs = 0.85, big = true, faceTo = V(-26, 0, -76) },
			{ t = 3.95, who = "r2", kind = "S_LeapHeader", at = V(-26, 0, -76), part = "Head", jump = 3.4, gs = 0.85, big = true, faceTo = V(28, 0, -83) },
			{ t = 5.05, who = "b2", kind = "S_Volley", at = V(28, 0, -83), gs = 0.9, big = true, power = true, faceTo = V(-35, 0, -86) },
			{ t = 6.05, who = "r1", kind = "S_SlideShot", at = V(-35, 0, -85), slide = V(-1, 0, -0.4), len = 6, gs = 0.8, faceTo = V(-18, 0, -72), hold = 0.7, big = true, contactAt = 0.24, fwd = 0.5 },
			{ t = 7.3, who = "r2", kind = "S_Scorpion", at = V(-18, 0, -72), jump = 2.5, gs = 1.0, big = true, power = true, faceTo = V(33, 0, -57) },
			{ t = 7.9, endPoint = true, at = V(33, 0, -57) },
			{ t = 1.3, who = "b1", move = true, at = V(24, 0, -72), from = 0.9 },
			{ t = 5.2, who = "r2", move = true, at = V(-18, 0, -72), from = 4.3 },
			{ t = 6.5, who = "b1", move = true, at = V(21, 0, -62), from = 3.3 },
			{ t = 7.0, who = "b2", move = true, at = V(31, 0, -65), from = 5.6 },
			slideMiss("b2", 7.78, V(32.5, 0, -60), V(0.1, 0, 1), 5),
			{ t = 8.9, who = "r2", kind = "Celebrate", pose = true, at = V(-18, 0, -72), faceTo = V(-5, 0, -68), dur = 2.6 },
			{ t = 8.8, who = "r1", kind = "Emote_Clap", pose = true, at = V(-33, 0, -82), faceTo = V(-18, 0, -72) },
		},
		elim = { team = "blue", t = 7.9, wait = 0.9 },
		seq = {
			{ T0 = 0.3, cam = { type = "side", zs = 1, dist = 56, h = 24, track = 0.45, fov = 50, lookY = 3 }, segs = { { 78, 1 } } },
			{ cam = { type = "hero", who = "r1", angle = 120, dist = 13, h = 4.5, abs = true, lookY = 1, fov = 54, orbit = 14, ballMix = 0.3 }, segs = { { 6, 1 }, { 8, 1, 0.3 }, { 30, 0.3 }, { 10, 0.3, 1 } } },
			{ cam = { type = "follow", who = "b1", back = 12, up = 6, side = 3, mix = 0.5, fov = 60 }, segs = { { 60, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 54, h = 24, track = 0.45, fov = 50, lookY = 3 }, segs = { { 60, 1 } } },
			{ cam = { type = "follow", who = "b2", back = 12, up = 6, side = 3, mix = 0.5, fov = 60 }, segs = { { 66, 1 } } },
			{ T0 = 5.7, cam = { type = "hero", who = "r1", toward = V(-1, 0, -0.4), angle = 90, dist = 12, h = 2.6, abs = true, lookY = -0.5, fov = 55, orbit = -18, ballMix = 0.3 }, segs = { { 12, 1 }, { 10, 1, 0.25 }, { 40, 0.25 }, { 10, 0.25, 1 }, { 20, 1 } } },
			{ cam = { type = "follow", who = "r2", back = 12, up = 6, side = -3, mix = 0.5, fov = 60 }, segs = { { 24, 1 } } },
			{ T0 = 6.95, cam = { type = "hero", who = "r2", angle = 105, dist = 16, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = 12, ballMix = 0.25 }, segs = { { 8, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = 4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 30, 0.6 } } },
			{ T0 = 7.77, cam = { type = "fixed", pos = V(47, 20, -43), at = V(33, 4, -58), fov = 56, dolly = V(1.5, 0.8, 1.5) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 8.85, cam = { type = "hero", who = "r2", angle = 15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = -12 }, segs = { { 110, 1 } } },
		},
	}
end

-- Zwei Grätschen-Saves (erst Rot, dann Blau), dann Tornado-Kick von Blau. Rot grätscht, zu spät.
SC.slidechain = function()
	return {
		fieldSize = 42,
		players = {
			{ id = "r1", team = "red", avatar = "Ace", start = V(-22, 0, -64) },
			{ id = "r2", team = "red", avatar = "Juno", start = V(-32, 0, -78) },
			{ id = "b1", team = "blue", avatar = "Ren", start = V(18, 0, -64) },
			{ id = "b2", team = "blue", avatar = "Bo", start = V(29, 0, -72) },
		},
		events = {
			{ t = 0.5, who = "b1", kind = "S_Drive", at = V(18, 0, -64), gs = 0.9, big = true, power = true, faceTo = V(-36, 0, -85) },
			{ t = 1.55, who = "r2", kind = "S_SlideShot", at = V(-36, 0, -85), slide = V(-0.9, 0, -0.45), len = 6, gs = 0.8, faceTo = V(-20, 0, -68), hold = 0.7, big = true, contactAt = 0.24, fwd = 0.5 },
			{ t = 2.85, who = "r1", kind = "S_Volley", at = V(-20, 0, -68), gs = 0.9, big = true, power = true, faceTo = V(36, 0, -62) },
			{ t = 3.85, who = "b2", kind = "S_SlideShot", at = V(36, 0, -62), slide = V(0.7, 0, 0.7), len = 6, gs = 0.8, faceTo = V(19, 0, -72), hold = 0.7, big = true, contactAt = 0.24, fwd = 0.5 },
			{ t = 5.1, who = "b1", kind = "S_Tornado", at = V(19, 0, -72), jump = 3, gs = 1.0, big = true, power = true, faceTo = V(-34, 0, -56) },
			{ t = 5.7, endPoint = true, at = V(-34, 0, -56) },
			{ t = 2.4, who = "b1", move = true, at = V(19, 0, -72), from = 1.0 },
			{ t = 4.9, who = "r1", move = true, at = V(-26, 0, -63), from = 3.4 },
			slideMiss("r1", 5.58, V(-31, 0, -59), V(-0.6, 0, 0.8), 5),
			{ t = 6.7, who = "b1", kind = "Celebrate", pose = true, at = V(19, 0, -72), faceTo = V(8, 0, -68), dur = 2.6 },
			{ t = 6.6, who = "b2", kind = "Emote_Dab", pose = true, at = V(36, 0, -60), faceTo = V(19, 0, -72) },
		},
		elim = { team = "red", t = 5.7, wait = 0.9 },
		seq = {
			{ T0 = 0.25, cam = { type = "follow", who = "b1", back = 12, up = 6, side = 3, mix = 0.45, fov = 62 }, segs = { { 48, 1 } } },
			{ T0 = 1.1, cam = { type = "hero", who = "r2", toward = V(-0.9, 0, -0.45), angle = 90, dist = 12, h = 2.6, abs = true, lookY = -0.5, fov = 55, orbit = -18, ballMix = 0.3 }, segs = { { 12, 1 }, { 10, 1, 0.25 }, { 40, 0.25 }, { 10, 0.25, 1 }, { 20, 1 } } },
			{ cam = { type = "follow", who = "r1", back = 12, up = 6, side = -3, mix = 0.5, fov = 60 }, segs = { { 60, 1 } } },
			{ T0 = 3.45, cam = { type = "hero", who = "b2", toward = V(0.7, 0, 0.7), angle = -90, dist = 12, h = 2.6, abs = true, lookY = -0.5, fov = 55, orbit = 18, ballMix = 0.3 }, segs = { { 12, 1 }, { 10, 1, 0.25 }, { 40, 0.25 }, { 10, 0.25, 1 }, { 20, 1 } } },
			{ cam = { type = "side", zs = 1, dist = 52, h = 22, track = 0.5, fov = 50, lookY = 3 }, segs = { { 24, 1 } } },
			{ T0 = 4.75, cam = { type = "hero", who = "b1", angle = -100, dist = 16, h = 5, abs = true, lookY = -0.5, fov = 52, orbit = -12, ballMix = 0.25 }, segs = { { 8, 1 }, { 12, 1, 0.18 }, { 50, 0.18 }, { 10, 0.18, 0.6 } } },
			{ cam = { type = "ball", back = 11, up = 3.5, side = -4, fov = 66, lag = 0.2, noTrail = true }, segs = { { 30, 0.6 } } },
			{ T0 = 5.57, cam = { type = "fixed", pos = V(-48, 20, -43), at = V(-34, 4, -57), fov = 56, dolly = V(-1.5, 0.8, 1.5) }, segs = { { 8, 1 }, { 10, 1, 0.15 }, { 40, 0.15 }, { 20, 0.15, 1 }, { 50, 1 } } },
			{ T0 = 6.65, cam = { type = "hero", who = "b1", angle = -15, dist = 11, h = 2.6, abs = true, lookY = 0.6, fov = 52, orbit = 12 }, segs = { { 110, 1 } } },
		},
	}
end

return true
