-- DuoDirector (Stand 18.11.2026, = Studio _G.FB_DD_SRC). Gescriptete Footbomb-Szenen im Studio-EDIT-Modus, Bild für Bild.
-- Laden:  _G.FB_DD_SRC = <dieser Text>; _G.FB_DD = loadstring(_G.FB_DD_SRC)(); dann scenes.lua laden; D.Setup("bike"); D.Play({hold=0.1, delay=5}); D.Cleanup()
-- Posen = echte AnimController-Keyframes (Vorwärts-Kinematik auf verankerte Teile), Ball = Parabeln zwischen Kontaktpunkten.
local D = {}
local Players = game:GetService("Players")
local RS = game:GetService("ReplicatedStorage")
local SS = game:GetService("ServerStorage")
local CoreGui = game:GetService("CoreGui")
local StarterPlayer = game:GetService("StarterPlayer")
local Selection = game:GetService("Selection")

local FPS = 60
local G = Vector3.new(0, -60, 0)
local ORDER = { "Root", "Waist", "Neck", "RightShoulder", "RightElbow", "RightWrist", "LeftShoulder", "LeftElbow", "LeftWrist",
	"RightHip", "RightKnee", "RightAnkle", "LeftHip", "LeftKnee", "LeftAnkle" }
local TEAMCOL = { red = Color3.fromRGB(255, 70, 60), blue = Color3.fromRGB(70, 150, 255) }
local TEAMHOT = { red = Color3.fromRGB(255, 190, 120), blue = Color3.fromRGB(170, 230, 255) }
local GRASS = { red = { Color3.fromRGB(226, 70, 66), Color3.fromRGB(204, 56, 56) }, blue = { Color3.fromRGB(56, 116, 228), Color3.fromRGB(44, 98, 208) } }

local function clamp01(x) return math.clamp(x, 0, 1) end
local function smooth(x) x = clamp01(x) return x * x * (3 - 2 * x) end
local function quartOut(x) x = clamp01(x) return 1 - (1 - x) ^ 4 end
local function seg(t, a, b) if b <= a then return if t >= b then 1 else 0 end return clamp01((t - a) / (b - a)) end
local function hash(n) local x = math.sin(n * 127.1 + 311.7) * 43758.5453 return x - math.floor(x) end
local function noise(t, seed)
	local i = math.floor(t) local f = t - i local a, b = hash(i + seed * 17.3), hash(i + 1 + seed * 17.3)
	local u = f * f * (3 - 2 * f) return (a + (b - a) * u) * 2 - 1
end
local function flat(v) return Vector3.new(v.X, 0, v.Z) end
local function unitOr(v, d) if v.Magnitude < 1e-4 then return d end return v.Unit end

local function loadModules()
	local tmp = Instance.new("Folder")
	for _, m in RS.Shared:GetChildren() do if m:IsA("ModuleScript") then m:Clone().Parent = tmp end end
	local M = { Config = require(tmp.Config) }
	local src
	for _, s in StarterPlayer:GetDescendants() do if s:IsA("ModuleScript") and s.Name == "AnimController" then src = s break end end
	local code = src.Source:gsub('require%(ReplicatedStorage:WaitForChild%("Shared"%):WaitForChild%("Config"%)%)', "__CFG")
	local fn = assert(loadstring(code, "=ACduo"))
	setfenv(fn, setmetatable({ __CFG = M.Config }, { __index = getfenv(1) }))
	M.AC = fn()
	return M
end

local function readJoints(rig)
	local J = {}
	for _, d in rig:GetDescendants() do
		if d:IsA("Motor6D") and d.Part0 and d.Part1 then
			J[d.Name] = { p0 = d.Part0, p1 = d.Part1, c0 = d.C0, c1i = d.C1:Inverse() }
		elseif d:IsA("AnimationConstraint") and d.Attachment0 and d.Attachment1 then
			local a0, a1 = d.Attachment0, d.Attachment1
			J[d.Name] = { p0 = a0.Parent, p1 = a1.Parent, c0 = a0.CFrame, c1i = a1.CFrame:Inverse() }
		end
	end
	return J
end
local function readAccessories(rig)
	local acc = {}
	for _, a in rig:GetChildren() do
		if a:IsA("Accessory") then
			local h = a:FindFirstChild("Handle")
			if h then
				for _, w in h:GetDescendants() do
					if w:IsA("Weld") and w.Part0 and w.Part1 then
						if w.Part0 == h then table.insert(acc, { h = h, body = w.Part1, rel = w.C1 * w.C0:Inverse() })
						else table.insert(acc, { h = h, body = w.Part0, rel = w.C0 * w.C1:Inverse() }) end
						break
					elseif w:IsA("RigidConstraint") and w.Attachment0 and w.Attachment1 then
						local a0, a1 = w.Attachment0, w.Attachment1
						local hA = if a0.Parent == h then a0 else a1
						local bA = if a0.Parent == h then a1 else a0
						table.insert(acc, { h = h, body = bA.Parent, rel = bA.CFrame * hA.CFrame:Inverse() })
						break
					end
				end
			end
		end
	end
	return acc
end
local function buildRig(descName, name, parent)
	local desc = SS.FootbombAssets.BotAvatars[descName]:Clone()
	local rig = Players:CreateHumanoidModelFromDescription(desc, Enum.HumanoidRigType.R15)
	rig.Name = name
	local hum = rig:FindFirstChildOfClass("Humanoid")
	hum.DisplayDistanceType = Enum.HumanoidDisplayDistanceType.None
	hum.HealthDisplayType = Enum.HumanoidHealthDisplayType.AlwaysOff
	hum.NameDisplayDistance = 0
	local R = { model = rig, hum = hum, name = name, root = rig:FindFirstChild("HumanoidRootPart") }
	for _, a in rig:GetChildren() do
		if a:IsA("Accessory") then
			local t = a.AccessoryType
			if t == Enum.AccessoryType.Back or t == Enum.AccessoryType.Waist or t == Enum.AccessoryType.Front or t == Enum.AccessoryType.Shoulder or a:FindFirstChildWhichIsA("WrapLayer", true) then
				a:Destroy()
			end
		end
	end
	R.J = readJoints(rig)
	R.acc = readAccessories(rig)
	R.standY = hum.HipHeight + R.root.Size.Y / 2
	for _, d in rig:GetDescendants() do
		if d:IsA("BasePart") then
			d.Anchored = true d.CanCollide = false d.CanQuery = false d.CanTouch = false
		elseif d:IsA("JointInstance") or d:IsA("Constraint") or d:IsA("NoCollisionConstraint") or d:IsA("WrapTarget") or d:IsA("Attachment") or d:IsA("Bone") or d:IsA("LuaSourceContainer") then
			d:Destroy()
		end
	end
	R.root.Transparency = 1
	rig.Parent = parent
	task.wait()
	for _, d in rig:GetDescendants() do
		if d:IsA("JointInstance") or d:IsA("Constraint") or d:IsA("NoCollisionConstraint") or d:IsA("Attachment") then d:Destroy() end
	end
	return R
end
local function applyPose(R, pose, rootCF)
	R.root.CFrame = rootCF
	for _, name in ORDER do
		local j = R.J[name]
		if j then j.p1.CFrame = j.p0.CFrame * j.c0 * (pose[name] or CFrame.identity) * j.c1i end
	end
	for _, a in R.acc do a.h.CFrame = a.body.CFrame * a.rel end
end
local function blend(a, b, w)
	local o = {}
	for _, n in ORDER do o[n] = (a[n] or CFrame.identity):Lerp(b[n] or CFrame.identity, w) end
	return o
end

local function part(name, parent, size, props)
	local p = Instance.new("Part")
	p.Name = name p.Anchored = true p.CanCollide = false p.CanQuery = false p.CanTouch = false p.CastShadow = false
	p.Size = size p.Material = Enum.Material.Neon p.Transparency = 1
	p.TopSurface = Enum.SurfaceType.Smooth p.BottomSurface = Enum.SurfaceType.Smooth
	for k, v in props or {} do p[k] = v end
	p.Parent = parent
	return p
end

local function buildHUD(S)
	local old = CoreGui:FindFirstChild("FB_DuoHUD") if old then old:Destroy() end
	local g = Instance.new("ScreenGui")
	g.Name = "FB_DuoHUD" g.IgnoreGuiInset = true g.DisplayOrder = 9999 g.Archivable = false g.ResetOnSpawn = false
	local calib = Instance.new("Frame")
	calib.Size = UDim2.fromScale(1, 1) calib.BackgroundColor3 = Color3.fromRGB(255, 0, 255) calib.BorderSizePixel = 0 calib.Visible = false calib.Parent = g
	local cells = {}
	for i = 0, 14 do
		local c = Instance.new("Frame")
		c.BorderSizePixel = 0 c.AnchorPoint = Vector2.new(0, 1)
		c.Position = UDim2.new(0.004 + i * 0.0075, 0, 1, 0) c.Size = UDim2.new(0.0065, 0, 0.0095, 0)
		c.BackgroundColor3 = Color3.new(0, 0, 0) c.Parent = g
		cells[i] = c
	end
	g.Parent = CoreGui
	S.hud = { gui = g, calib = calib, cells = cells }
end
function D.SetCounter(n)
	local S = _G.FB_DUO
	local cells = S.hud.cells
	cells[0].BackgroundColor3 = Color3.new(1, 1, 1)
	cells[1].BackgroundColor3 = Color3.new(0, 0, 0)
	local parity = 0
	for b = 0, 11 do
		local bit = bit32.band(bit32.rshift(n, b), 1)
		parity += bit
		cells[2 + b].BackgroundColor3 = if bit == 1 then Color3.new(1, 1, 1) else Color3.new(0, 0, 0)
	end
	cells[14].BackgroundColor3 = if parity % 2 == 1 then Color3.new(1, 1, 1) else Color3.new(0, 0, 0)
end
function D.Calib(on) _G.FB_DUO.hud.calib.Visible = on end

local SCENES = {}

local function animStart(S, e)
	if not e.kind then return e.t, 0 end
	local AC = S.M.AC
	local dur = e.dur or AC.Duration(e.kind)
	local info = AC.Info(e.kind)
	local cAt = e.contactAt or ((info and info.strike or 0) * dur)
	return e.t - cAt, dur
end
local function specialStart(S, e)
	local ta, dur = animStart(S, e)
	local dir = flat(e.slide or e.dive).Unit
	local L = e.len or (if e.slide then 5 else 3.6)
	local uc = (e.t - ta) / dur
	return e.at - dir * L * quartOut(uc * 1.3), ta, dur, dir, L
end
local function rootXZ(S, who, t)
	local list = S.ev[who]
	for _, e in list do
		if e.slide or e.dive then
			local p0, ta, dur, dir, L = specialStart(S, e)
			if t >= ta and t <= ta + dur + (e.hold or 0.6) then
				return p0 + dir * L * quartOut(math.min((t - ta) / dur, 1) * 1.3), dir, 0
			end
		end
	end
	local P = S.players[who]
	local prevPos, prevT = P.start, P.t0 or 0
	local travel = 0
	for _, e in list do
		local ta, dur = animStart(S, e)
		local arrive = if e.move then e.t else ta - (e.lead or 0.1)
		local leave = if e.move then e.t else ta + math.max(dur * 0.55, 0.2)
		local pos = e.at
		local special = e.slide or e.dive
		if special then pos = specialStart(S, e) arrive = ta end
		if e.from then prevT = math.max(prevT, e.from) end
		local segLen = flat(pos - prevPos).Magnitude
		if t < arrive then
			local x = seg(t, prevT, arrive)
			local k = if special then x ^ 1.6 else smooth(x)
			return prevPos:Lerp(pos, k), (pos - prevPos), travel + segLen * k
		end
		travel += segLen
		if special then
			local p0, ta2, dur2, dir, L = specialStart(S, e)
			prevPos = p0 + dir * L
			prevT = ta2 + dur2 + (e.hold or 0.6)
		else
			if t <= leave then return pos, Vector3.zero, travel end
			prevPos, prevT = pos, leave
		end
	end
	return prevPos, Vector3.zero, travel
end

local function ballAt(S, t)
	local segs = S.bseg
	if t <= segs[1].t0 then return segs[1].p0, segs[1].v, 1 end
	for k, sg in segs do
		if t < sg.t1 or k == #segs then
			local tau = math.min(t - sg.t0, sg.t1 - sg.t0)
			return sg.p0 + sg.v * tau + G * (0.5 * sg.gs * tau * tau), sg.v + G * (sg.gs * tau), k
		end
	end
end

local function faceOf(S, e)
	if e.slide then return flat(e.slide).Unit elseif e.dive then return flat(e.dive).Unit end
	local to = e.faceTo or (e.next and e.next.at) or S.players[e.who].look
	local d = unitOr(flat(to - e.at), Vector3.xAxis)
	return if e.back then -d else d
end

local function sinkY(S, team, t)
	local el = S.scene.elim
	if not el or el.team ~= team then return 0 end
	local t1 = el.t + (el.wait or 0.9)
	local shake = if t > el.t + 0.25 and t < t1 then 0.12 * noise(t * 40, 3) else 0
	return -30 * smooth(seg(t, t1, t1 + 0.9)) ^ 1.4 + shake
end

local function playerAt(S, who, t, ballPos)
	local AC = S.M.AC
	local P = S.players[who]
	local xz, moveVec, travel = rootXZ(S, who, t)
	local toBall = flat(ballPos - xz)
	local face = if toBall.Magnitude > 0.5 then toBall.Unit else unitOr(flat(P.look - xz), Vector3.xAxis)
	if P.faceFixed then face = unitOr(flat(P.look - xz), face) end
	local pose, lift = nil, 0
	for _, e in S.ev[who] do
		if e.kind then
			local ta, dur = animStart(S, e)
			local f = faceOf(S, e)
			local pre = e.pre or 0.25
			if t >= ta - pre and t <= ta + dur + (if e.holdPose then (e.hold or 0.6) else 0.2) then
				local w = smooth(seg(t, ta - pre, ta - 0.05)) * (1 - smooth(seg(t, ta + dur, ta + dur + 0.2)))
				face = face:Lerp(f, w)
				face = unitOr(face, f)
				local u = math.clamp((t - ta) / dur, 0, 1)
				local kp = AC.KeyPoseAt(e.kind, u, e.mirror or false)
				local hold = e.holdPose and t > ta + dur
				pose = { kp = kp, w = smooth(seg(t, ta - 0.12, ta)) * (if hold then 1 else (1 - smooth(seg(t, ta + dur, ta + dur + 0.15)))) }
				if e.jump then local x = (t - e.t) / (e.air or 0.38) lift = math.max(0, e.jump * (1 - x * x)) end
				if e.dive then
					local ud = math.clamp((t - ta) / dur, 0, 1)
					lift = math.sin(math.min(ud * 1.25, 1) * math.pi) * 1.4 - 1.2 * smooth(seg(ud, 0.55, 1))
				end
				break
			end
		end
	end
	local dt = 1 / 60
	local xz2 = rootXZ(S, who, t - dt)
	local vel = (xz - xz2) / dt
	local sp = flat(vel).Magnitude
	local idle = AC.IdlePoseAt(t, P.seed)
	local base = idle
	if sp > 0.5 then
		local v = flat(vel).Unit
		local right = face:Cross(Vector3.yAxis)
		local ph = ((travel or 0) / 7.5 * math.pi * 2) % (math.pi * 2)
		local run = AC.RunPoseAt(ph, math.max(sp, 6), v:Dot(face), v:Dot(right))
		base = blend(idle, run, smooth(seg(sp, 0.5, 4)))
	end
	local final = if pose then blend(base, pose.kp, pose.w) else base
	local y = S.groundY + P.R.standY + lift + sinkY(S, P.team, t)
	local p = Vector3.new(xz.X, y, xz.Z)
	return CFrame.lookAt(p, p + face), final
end

local function prepare(S)
	local sc = S.scene
	S.ev = {}
	for id in S.players do S.ev[id] = {} end
	table.sort(sc.events, function(a, b) return a.t < b.t end)
	local chain = {}
	for _, e in sc.events do
		if e.who then table.insert(S.ev[e.who], e) end
		if not e.pose and not e.move then table.insert(chain, e) end
	end
	for k, e in chain do e.next = chain[k + 1] end
	local pts = {}
	for k, e in chain do
		if e.endPoint or not e.who then
			pts[k] = e.pos or Vector3.new(e.at.X, S.groundY + 1.3, e.at.Z)
		else
			local P = S.players[e.who]
			local cf, pose = playerAt(S, e.who, e.t, e.at + faceOf(S, e) * 5)
			local f = faceOf(S, e)
			cf = CFrame.lookAt(cf.Position, cf.Position + f)
			applyPose(P.R, pose, cf)
			local bp = P.R.model:FindFirstChild(e.part or "RightFoot")
			local p = bp.Position + f * (e.fwd or 0.9)
			if e.part == "Head" then p += Vector3.new(0, 0.9, 0) end
			if e.lift then p += Vector3.new(0, e.lift, 0) end
			pts[k] = p
		end
	end
	S.contacts = {}
	S.bseg = {}
	for k = 1, #chain - 1 do
		local a, b = chain[k], chain[k + 1]
		local T = b.t - a.t
		local gs = a.gs or 1
		local d = pts[k + 1] - pts[k]
		local v = (d - G * (0.5 * gs * T * T)) / T
		table.insert(S.bseg, { t0 = a.t, t1 = b.t, p0 = pts[k], p1 = pts[k + 1], v = v, gs = gs, who = a.who, team = a.who and S.players[a.who].team, power = a.power })
	end
	for k, e in chain do
		table.insert(S.contacts, { t = e.t, pos = pts[k], who = e.who, team = e.who and S.players[e.who].team, big = e.big, endPoint = e.endPoint })
	end
	S.tLand = chain[#chain].t
end

function D.Setup(name, opts)
	opts = opts or {}
	if _G.FB_DUO then D.Cleanup() end
	local S = { opts = opts, name = name }
	_G.FB_DUO = S
	S.M = loadModules()
	local cam = workspace.CurrentCamera
	S.camOrig = { cf = cam.CFrame, fov = cam.FieldOfView, focus = cam.Focus }
	Selection:Set({})
	local sc = SCENES[name]()
	S.scene = sc
	local folder = Instance.new("Folder")
	folder.Name = "FB_Duo" folder.Archivable = false folder.Parent = workspace
	S.folder = folder
	local FS = sc.fieldSize or 42
	S.FS = FS
	local half = FS / 2
	local gap = 2
	S.field = {}
	for _, team in { "red", "blue" } do
		local c = Vector3.new((if team == "red" then -1 else 1) * (half + gap / 2), 6, -70)
		local f = SS.FootbombAssets.FieldTemplate:Clone()
		f.Name = "Field_" .. team
		f:ScaleTo(FS / 34)
		f:PivotTo(CFrame.new(c))
		local grassTop
		for _, d in f:GetDescendants() do
			if d:IsA("BasePart") then
				d.Anchored = true d.CanCollide = false d.CanQuery = false
				if d.Name == "Grass" then
					local light = d.Color.G > 0.64
					d.MaterialVariant = "" d.Material = Enum.Material.Grass
					d.Color = if light then GRASS[team][1] else GRASS[team][2]
					grassTop = d.Position.Y + d.Size.Y / 2
				elseif d.Name == "Line" then
					local off = d.Position - c
					if math.abs(off.X) > half - 1.5 and math.sign(off.X) == (if team == "red" then 1 else -1) and d.Size.Z > d.Size.X then d.Transparency = 1 end
				elseif d.Name == "PlayerWall" or d.Name == "Root" or d.Name == "Spot" then
					d.Transparency = 1
				end
			end
		end
		f.Parent = folder
		S.field[team] = { model = f, center = c, pivot = f:GetPivot(), grass = {} }
		for _, d in f:GetDescendants() do if d:IsA("BasePart") and d.Name == "Grass" then table.insert(S.field[team].grass, { p = d, c = d.Color }) end end
		S.groundY = grassTop
	end
	part("MidDirt", folder, Vector3.new(gap + 0.4, 14 * FS / 34, FS + 1), { Transparency = 0, Material = Enum.Material.Ground, Color = Color3.fromRGB(156, 106, 66), CFrame = CFrame.new(0, S.groundY - 7 * FS / 34 - 0.5, -70) })
	part("MidLine", folder, Vector3.new(gap + 0.2, 1.02, FS + 0.5), { Transparency = 0, Material = Enum.Material.SmoothPlastic, Color = Color3.new(1, 1, 1), CFrame = CFrame.new(0, S.groundY - 0.49, -70) })
	S.players = {}
	for i, p in sc.players do
		local R = buildRig(p.avatar, p.id, folder)
		S.players[p.id] = { R = R, team = p.team, start = p.start, t0 = p.t0, look = p.look or Vector3.new(if p.team == "red" then 30 else -30, 0, -70), seed = 1.1 + i * 0.73, faceFixed = p.faceFixed }
	end
	local ball = RS.ClientAssets.Balls:FindFirstChild(sc.ball or "Ball_RankChampion"):Clone()
	ball.Name = "DuoBall" ball.Anchored = true ball.CanCollide = false ball.CanQuery = false ball.CanTouch = false
	for _, d in ball:GetDescendants() do if d:IsA("LuaSourceContainer") or d:IsA("Attachment") or d:IsA("Trail") or d:IsA("ParticleEmitter") or d:IsA("Beam") then d:Destroy() end end
	ball.Parent = folder
	S.ball = ball
	S.ballRot = ball.CFrame - ball.CFrame.Position
	S.trail = {}
	for i = 1, 18 do S.trail[i] = part("Trail" .. i, folder, Vector3.new(1, 1, 1)) end
	S.rings = {}
	for i = 1, 6 do S.rings[i] = part("Ring" .. i, folder, Vector3.new(1, 1, 1), { Shape = Enum.PartType.Ball }) end
	S.shock = part("Shock", folder, Vector3.new(0.4, 4, 4), { Shape = Enum.PartType.Cylinder })
	S.shock2 = part("Shock2", folder, Vector3.new(0.4, 4, 4), { Shape = Enum.PartType.Cylinder })
	S.flash = part("Flash", folder, Vector3.new(4, 4, 4), { Shape = Enum.PartType.Ball })
	S.pillar = part("Pillar", folder, Vector3.new(60, 6, 6), { Shape = Enum.PartType.Cylinder })
	S.debris = {}
	for i = 1, 22 do S.debris[i] = part("Debris" .. i, folder, Vector3.new(1, 1, 1), { Material = if i % 3 == 0 then Enum.Material.Neon else Enum.Material.Grass }) end
	S.dust = {}
	for i = 1, 10 do S.dust[i] = part("Dust" .. i, folder, Vector3.new(4, 4, 4), { Shape = Enum.PartType.Ball, Material = Enum.Material.SmoothPlastic, Color = Color3.fromRGB(235, 225, 215) }) end
	S.hl = {}
	for id, P in S.players do
		local h = Instance.new("Highlight")
		h.FillTransparency = 1 h.OutlineTransparency = 1 h.OutlineColor = TEAMHOT[P.team] h.DepthMode = Enum.HighlightDepthMode.Occluded
		h.Adornee = P.R.model h.Parent = folder
		S.hl[id] = h
	end
	buildHUD(S)
	task.wait(0.5)
	for _, d in folder:GetDescendants() do if d:IsA("JointInstance") or d:IsA("Constraint") or d:IsA("NoCollisionConstraint") or d:IsA("Attachment") then d:Destroy() end end
	prepare(S)
	D.BuildTimeline()
	return #S.frames
end

function D.BuildTimeline()
	local S = _G.FB_DUO
	local frames = {}
	local T = 0
	for ci, cut in S.scene.seq do
		local jump = false
		if cut.T0 then T = cut.T0 jump = true end
		for _, sg in cut.segs do
			local n, s0, s1 = sg[1], sg[2], sg[3] or sg[2]
			for k = 0, n - 1 do
				local sp = if n > 1 then s0 + (s1 - s0) * (k / (n - 1)) else s0
				table.insert(frames, { T = T, cut = ci, cam = cut.cam, s = 0, speed = sp, jump = jump })
				jump = false
				T += sp / FPS
			end
		end
	end
	local lastCut, s = -1, 0
	for _, f in frames do
		if f.cut ~= lastCut then s = 0 lastCut = f.cut end
		f.s = s s += 1 / FPS
	end
	S.frames = frames
	return #frames
end

local function look(pos, at, roll) return CFrame.lookAt(pos, at) * CFrame.Angles(0, 0, math.rad(roll or 0)) end

local function camFor(S, c, T, s, ball)
	local g = S.groundY
	local function root(id) local cf = playerAt(S, id, T, ball) return cf.Position end
	local function ballLag(l) return (ballAt(S, T - l)) end
	if c.type == "follow" then
		local p = root(c.who)
		local P = S.players[c.who]
		local toward = if c.toward then c.toward else Vector3.new(if P.team == "red" then 1 else -1, 0, 0)
		toward = unitOr(flat(toward), Vector3.xAxis)
		local right = toward:Cross(Vector3.yAxis)
		local pos = p - toward * (c.back or 14) + Vector3.new(0, c.up or 7, 0) + right * (c.side or 0)
		local tgtB = ballLag(c.lag or 0.12)
		local at = p:Lerp(Vector3.new(tgtB.X, math.clamp(tgtB.Y, g + 1, g + (c.maxY or 22)), tgtB.Z), c.mix or 0.45) + toward * (c.ahead or 6)
		return look(pos, at, c.roll), c.fov or 62
	elseif c.type == "side" then
		local b = ballLag(c.lag or 0.15)
		local x = (c.x0 or 0) + (b.X - (c.x0 or 0)) * (c.track or 0.5)
		local pos = Vector3.new(x + (c.dx or 0) + (c.pan or 0) * s, g + (c.h or 18), -70 + (c.zs or 1) * (c.dist or 48))
		local at = Vector3.new(x * (c.trackLook or 1), g + (c.lookY or 4) + math.clamp(b.Y - g, 0, 20) * (c.yTrack or 0.25), -70 + (c.zLook or 0))
		return look(pos, at, c.roll), c.fov or 50
	elseif c.type == "hero" then
		local p = root(c.who)
		local P = S.players[c.who]
		local toward = unitOr(flat(c.toward or Vector3.new(if P.team == "red" then 1 else -1, 0, 0)), Vector3.xAxis)
		local right = toward:Cross(Vector3.yAxis)
		local a = math.rad((c.angle or 70) + (c.orbit or 0) * s)
		local dir = (toward * math.cos(a) + right * math.sin(a))
		local pos = p + dir * (c.dist or 9) + Vector3.new(0, (c.h or 1.2), 0)
		if c.abs then pos = Vector3.new(pos.X, g + (c.h or 1.2), pos.Z) end
		local at = p + Vector3.new(0, c.lookY or 2.5, 0)
		if c.ballMix then at = at:Lerp(ballLag(0), c.ballMix) end
		return look(pos, at, c.roll), c.fov or 55
	elseif c.type == "ball" then
		local b = ballAt(S, T)
		local bp = ballLag(c.lag or 0.25)
		local dir = unitOr(b - bp, Vector3.xAxis)
		local pos = b - dir * (c.back or 10) + Vector3.new(0, c.up or 3, 0) + dir:Cross(Vector3.yAxis) * (c.side or 0)
		local at = b + dir * (c.ahead or 6)
		return look(pos, at, c.roll), c.fov or 65
	elseif c.type == "orbit" then
		local ctr = if c.who then root(c.who) else (c.center or Vector3.new(0, g, -70))
		local a = math.rad((c.a0 or 0) + (c.speed or 20) * s)
		local pos = ctr + Vector3.new(math.cos(a) * (c.r or 30), c.h or 14, math.sin(a) * (c.r or 30))
		return look(pos, ctr + Vector3.new(0, c.lookY or 3, 0), c.roll), c.fov or 50
	elseif c.type == "fixed" then
		local at = c.at
		if c.ballMix then at = at:Lerp(ballLag(c.lag or 0.1), c.ballMix) end
		local pos = c.pos + (c.dolly or Vector3.zero) * s
		return look(pos, at, c.roll), c.fov or 50
	end
end

function D.Frame(i)
	local S = _G.FB_DUO
	local f = S.frames[i + 1]
	if not f then return false end
	local T = f.T
	local ball, vel, k = ballAt(S, T)
	local landed = T >= S.tLand
	for id, P in S.players do
		local cf, pose = playerAt(S, id, T, ball)
		applyPose(P.R, pose, cf)
	end
	local el = S.scene.elim
	for team, F in S.field do
		local dy = sinkY(S, team, T)
		F.model:PivotTo(F.pivot + Vector3.new(0, dy, 0))
		local glow = 0
		if el and el.team == team and T >= el.t then glow = math.exp(-(T - el.t) / 0.18) end
		for _, gp in F.grass do gp.p.Color = gp.c:Lerp(Color3.new(1, 1, 1), 0.4 * glow) end
	end
	local spin = T * 14
	local axis = unitOr(vel:Cross(Vector3.yAxis), Vector3.zAxis)
	S.ball.CFrame = CFrame.new(ball) * CFrame.fromAxisAngle(axis, -spin) * S.ballRot
	S.ball.Transparency = if landed then 1 else 0
	for _, d in S.ball:GetDescendants() do if d:IsA("BasePart") or d:IsA("Decal") then d.Transparency = if landed then 1 else 0 end end
	local sgm = S.bseg[k]
	local col = TEAMCOL[(sgm and sgm.team) or "red"]
	local spd = vel.Magnitude
	local strong = clamp01((spd - 30) / 40) * (if sgm and sgm.power then 1.4 else 1)
	for j, tp in S.trail do
		local ta, tb = T - (j - 1) * 0.016, T - j * 0.016
		local a = (ballAt(S, ta))
		local b = (ballAt(S, tb))
		local L = (a - b).Magnitude
		if landed or f.cam.noTrail or strong <= 0.02 or L < 0.05 or (sgm and tb < sgm.t0 + 0.03) then
			tp.Transparency = 1
		else
			local w = (1.15 - 0.95 * (j / #S.trail)) * (0.75 + 0.3 * strong)
			tp.Shape = Enum.PartType.Ball
			tp.Size = Vector3.new(w, w, w)
			tp.CFrame = CFrame.new(b)
			tp.Color = col:Lerp(Color3.new(1, 1, 1), 0.35 * (1 - j / #S.trail))
			tp.Transparency = math.clamp(0.3 + 0.7 * (j / #S.trail) + (1 - strong) * 0.4, 0, 1)
		end
	end
	local ri = 1
	for _, c in S.contacts do
		local dtc = T - c.t
		if dtc >= 0 and dtc < 0.35 and not c.endPoint and ri <= #S.rings then
			local r = S.rings[ri] ri += 1
			local x = dtc / 0.35
			local sz = (c.big and 7 or 4.5) * (0.3 + quartOut(x))
			r.Size = Vector3.new(sz, sz, sz)
			r.CFrame = CFrame.new(c.pos)
			r.Color = TEAMHOT[c.team or "red"]
			r.Material = Enum.Material.ForceField
			r.Transparency = 0.1 + 0.9 * x
		end
	end
	for j = ri, #S.rings do S.rings[j].Transparency = 1 end
	local endC = S.contacts[#S.contacts]
	local tI = S.tLand
	local di = T - tI
	local ip = endC.pos
	local icol = TEAMCOL[(S.bseg[#S.bseg].team) or "red"]
	if di >= 0 and di < 1.6 then
		local x = di / 0.55
		local sz = 6 + 46 * quartOut(x)
		S.shock.Size = Vector3.new(0.3, sz, sz)
		S.shock.CFrame = CFrame.new(ip.X, S.groundY + 0.25 + sinkY(S, el and el.team or "blue", T), ip.Z) * CFrame.Angles(0, 0, math.rad(90))
		S.shock.Color = icol:Lerp(Color3.new(1, 1, 1), 0.3)
		S.shock.Material = Enum.Material.ForceField
		S.shock.Transparency = clamp01(x * 0.95)
		local x2 = (di - 0.08) / 0.7
		local sz2 = 4 + 30 * quartOut(clamp01(x2))
		S.shock2.Size = Vector3.new(0.15, sz2, sz2)
		S.shock2.CFrame = S.shock.CFrame
		S.shock2.Color = Color3.new(1, 1, 1)
		S.shock2.Transparency = if x2 < 0 then 1 else clamp01(0.75 + 0.25 * x2)
		local xf = di / 0.14
		local fs = 2.5 + 6.5 * quartOut(xf)
		S.flash.Size = Vector3.new(fs, fs, fs)
		S.flash.CFrame = CFrame.new(ip)
		S.flash.Color = icol:Lerp(Color3.new(1, 1, 1), 0.55)
		S.flash.Transparency = clamp01(0.45 + 0.55 * xf)
		local xp = di / 0.6
		S.pillar.Size = Vector3.new(70 * (0.4 + 0.6 * quartOut(xp)), 5 * (1 - xp) + 0.5, 5 * (1 - xp) + 0.5)
		S.pillar.CFrame = CFrame.new(ip + Vector3.new(0, 35 * (0.4 + 0.6 * quartOut(xp)), 0)) * CFrame.Angles(0, 0, math.rad(90))
		S.pillar.Color = icol:Lerp(Color3.new(1, 1, 1), 0.6)
		S.pillar.Transparency = 1
		for j, dp in S.debris do
			local a = hash(j) * math.pi * 2
			local sp = 14 + 22 * hash(j + 40)
			local up = 16 + 18 * hash(j + 80)
			local tt = math.min(di, 1.5)
			local p = ip + Vector3.new(math.cos(a) * sp * tt, up * tt - 45 * tt * tt, math.sin(a) * sp * tt)
			local s0 = 0.5 + 1.3 * hash(j + 7)
			dp.Size = Vector3.new(s0, s0, s0)
			dp.CFrame = CFrame.new(p) * CFrame.Angles(di * 9 * hash(j + 1), di * 7 * hash(j + 2), 0)
			dp.Color = if j % 3 == 0 then icol else GRASS[el and el.team or "blue"][1 + j % 2]
			dp.Transparency = if p.Y < S.groundY - 2 then 1 else clamp01((di - 0.8) / 0.3)
		end
		for j, dd in S.dust do
			local a = hash(j + 200) * math.pi * 2
			local r = 3 + 12 * quartOut(di / 1.2) * (0.6 + 0.5 * hash(j + 210))
			local p = Vector3.new(ip.X + math.cos(a) * r, S.groundY + 1 + 3 * quartOut(di / 1.2) * hash(j + 220), ip.Z + math.sin(a) * r)
			local s0 = (2.5 + 3 * hash(j + 230)) * (0.5 + 0.8 * quartOut(di / 1.0))
			dd.Size = Vector3.new(s0, s0, s0)
			dd.CFrame = CFrame.new(p)
			dd.Transparency = clamp01(0.72 + 0.28 * (di / 1.2))
		end
	else
		for _, p in { S.shock, S.shock2, S.flash, S.pillar } do p.Transparency = 1 end
		for _, p in S.debris do p.Transparency = 1 end
		for _, p in S.dust do p.Transparency = 1 end
	end
	for id, h in S.hl do
		local a = 1
		for _, c in S.contacts do
			if c.who == id and c.big and T >= c.t - 0.25 and T < c.t + 0.6 then a = math.min(a, 0.15 + 0.85 * seg(T, c.t + 0.1, c.t + 0.6)) end
		end
		h.OutlineTransparency = a
	end
	local cf, fov = camFor(S, f.cam, T, f.s, ball)
	local amp = 0
	if di >= 0 then amp += 1.1 * math.exp(-di / 0.22) end
	for _, c in S.contacts do if c.big and T >= c.t then amp += 0.35 * math.exp(-(T - c.t) / 0.15) end end
	amp *= (f.cam.shake or 1)
	if amp > 0.01 then
		cf = cf * CFrame.new(noise(T * 30, 1) * amp * 0.5, noise(T * 30, 2) * amp * 0.5, 0) * CFrame.Angles(0, 0, math.rad(noise(T * 25, 3) * amp * 1.5))
	end
	local camera = workspace.CurrentCamera
	camera.CameraType = Enum.CameraType.Scriptable
	camera.FieldOfView = fov
	camera.CFrame = cf
	camera.Focus = cf * CFrame.new(0, 0, -20)
	D.SetCounter(i)
	return true
end

function D.Count() return #_G.FB_DUO.frames end
function D.Info()
	local S = _G.FB_DUO
	local o = { n = #S.frames, cuts = {}, land = S.tLand }
	local last = -1
	for i, f in S.frames do if f.cut ~= last then table.insert(o.cuts, { i - 1, f.T }) last = f.cut end end
	return o
end

function D.Play(opts)
	opts = opts or {}
	local S = _G.FB_DUO
	S.playing = true
	local from, to = opts.from or 0, opts.to or (#S.frames - 1)
	task.spawn(function()
		if opts.delay then task.wait(opts.delay) end
		for i = from, to do
			if not S.playing then break end
			D.Frame(i)
			task.wait(opts.hold or 0.1)
		end
		D.SetCounter(4095)
		S.playing = false
	end)
	return to - from + 1
end
function D.Stop() if _G.FB_DUO then _G.FB_DUO.playing = false end end

function D.Cleanup()
	local S = _G.FB_DUO
	if not S then return end
	S.playing = false
	if S.folder then S.folder:Destroy() end
	if S.hud then S.hud.gui:Destroy() end
	local cam = workspace.CurrentCamera
	cam.CameraType = Enum.CameraType.Fixed
	if S.camOrig then cam.FieldOfView = S.camOrig.fov cam.CFrame = S.camOrig.cf cam.Focus = S.camOrig.focus end
	_G.FB_DUO = nil
end

D.SCENES = SCENES
D._ballAt = function(T) return ballAt(_G.FB_DUO, T) end
D._playerAt = function(id, T) local S = _G.FB_DUO return playerAt(S, id, T, (ballAt(S, T))) end
return D
