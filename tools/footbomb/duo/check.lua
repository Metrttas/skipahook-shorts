-- Szenen-Prüfer: nach D.Setup(scene) ausführen, return _G.FB_CHECK()
-- Meldet OVERLAP (Spieler < 3.2 auseinander), BALLHIT (Ball fliegt durch einen Spieler, der ihn nicht spielt),
-- LOWBALL (Ball unter Bodenhöhe vor der Landung), OOB (Spieler außerhalb seines Feldes). LOWBALL bei t=0 (Ball am Fuß) und
-- BALLHIT direkt nach Annahme (Ball am Körper des Annehmenden) sind normal.
_G.FB_CHECK = function()
	local D = _G.FB_DD local S = _G.FB_DUO local g = S.groundY
	local out = {} local apex = 0 local seen = {}
	local function note(k, s) if not seen[k] then seen[k] = true table.insert(out, s) end end
	local cts = {} for _, c in S.contacts do if c.who then cts[c.who] = cts[c.who] or {} table.insert(cts[c.who], c.t) end end
	for t = 0, S.tLand + 0.6, 1 / 30 do
		local b = D._ballAt(t) apex = math.max(apex, b.Y - g)
		local pos = {}
		for id in S.players do local cf = D._playerAt(id, t) pos[id] = cf.Position end
		for a, pa in pos do for c, pc in pos do if a < c then
			local d = (Vector3.new(pa.X, 0, pa.Z) - Vector3.new(pc.X, 0, pc.Z)).Magnitude
			if d < 3.2 then note("ov" .. a .. c, string.format("OVERLAP %s-%s t=%.2f d=%.1f", a, c, t, d)) end
		end end end
		if t < S.tLand - 0.03 then
			for id, p in pos do
				local near = false for _, ct in (cts[id] or {}) do if math.abs(t - ct) < 0.22 then near = true end end
				local d = (b - (p + Vector3.new(0, 0.3, 0))).Magnitude
				if not near and d < 2.8 and b.Y < p.Y + 3.2 then note("bh" .. id .. math.floor(t * 4), string.format("BALLHIT %s t=%.2f d=%.1f", id, t, d)) end
			end
			if b.Y < g + 0.7 then note("low" .. math.floor(t * 4), string.format("LOWBALL t=%.2f y=%.1f", t, b.Y - g)) end
		end
		if t < S.tLand then for id, p in pos do local P = S.players[id]
			local bad = (P.team == "red" and p.X > -1.2) or (P.team == "blue" and p.X < 1.2) or math.abs(p.Z + 70) > 21 or math.abs(p.X) > 43
			if bad then note("oob" .. id, string.format("OOB %s t=%.2f (%.1f,%.1f)", id, t, p.X, p.Z)) end end end
	end
	local cs = {} for _, c in S.contacts do table.insert(cs, string.format("%s@%.2f y=%.1f", tostring(c.who), c.t, c.pos.Y - g)) end
	return string.format("apex=%.1f land=%.2f n=%d | %s\n%s", apex, S.tLand, #S.frames, table.concat(cs, " "), table.concat(out, "\n"))
end
return true
