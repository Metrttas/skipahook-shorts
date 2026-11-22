import cv2, numpy as np, subprocess, sys, os
R='/home/claude/sah/docs/ref/'
OUT=sys.argv[1]
W,H,FPS,D=1916,902,60,6.0
def panel(f, cols, rows, c, r, inset=0):
    im=cv2.imread(R+f); h,w=im.shape[:2]; pw,ph=w//cols,h//rows
    return im[r*ph+inset:(r+1)*ph-inset, c*pw+inset:(c+1)*pw-inset]
P={
 's_ships_bl': lambda: panel('sea2_ships_blender.jpg',2,1,0,0,4),
 's_ship_sail': lambda: panel('sea2_phaseD_ships.jpg',2,2,0,0,2),
 's_ship_far': lambda: panel('sea2_phaseD_ships.jpg',2,2,1,0,2),
 's_ship_ghost': lambda: panel('sea2_phaseD_ships.jpg',2,2,0,1,2),
 's_ship_giant': lambda: panel('sea2_phaseD_ships.jpg',2,2,1,1,2),
 's_isle_light': lambda: panel('sea2_isles_blender.jpg',2,4,0,0,2),
 's_isle_skull': lambda: panel('sea2_isles_blender.jpg',2,4,1,1,2),
 's_isle_volcano': lambda: panel('sea2_isles_blender.jpg',2,4,0,2,2),
 's_isle_ice': lambda: panel('sea2_isles_blender.jpg',2,4,1,2,2),
 's_isle_storm': lambda: panel('sea2_isles_blender.jpg',2,4,0,3,2),
 's_game_skull': lambda: panel('sea2_phaseC_islands.jpg',2,2,0,0,2),
 's_game_volcano': lambda: panel('sea2_phaseC_islands.jpg',2,2,1,0,2),
 's_game_ice': lambda: panel('sea2_phaseC_islands.jpg',2,2,0,1,2),
 's_game_tower': lambda: panel('sea2_phaseC_islands.jpg',2,2,1,1,2),
 's_storm_rain': lambda: panel('sea2_phaseB_weather.jpg',1,3,0,0,2),
 's_storm_bolt': lambda: panel('sea2_phaseB_weather.jpg',1,3,0,1,2),
 's_storm_whirl': lambda: panel('sea2_phaseB_weather.jpg',1,3,0,2,2),
 's_whirlpool': lambda: cv2.imread(R+'sea2_whirlpool.jpg'),
 's_boss_1': lambda: panel('sea2_bosses_blender.jpg',2,2,0,0,2),
 's_boss_2': lambda: panel('sea2_bosses_blender.jpg',2,2,1,0,2),
 's_boss_3': lambda: panel('sea2_bosses_blender.jpg',2,2,0,1,2),
 's_boss_4': lambda: panel('sea2_bosses_blender.jpg',2,2,1,1,2),
 's_finds_isle': lambda: panel('sea2_c2_finds.jpg',2,2,0,0,2),
 's_finds_ship': lambda: panel('sea2_c2_finds.jpg',2,2,1,0,2),
 's_finds_chest': lambda: panel('sea2_c2_finds.jpg',2,2,0,1,2),
 's_finds_bottle': lambda: panel('sea2_c2_finds.jpg',2,2,1,1,2),
 's_waves': lambda: cv2.imread(R+'sea2_waves_preview.jpg'),
 's_studio_isles': lambda: panel('sea2_isles_studio.jpg',2,1,0,0,2),
 's_studio_lava': lambda: panel('sea2_isles_studio.jpg',2,1,1,0,2),
}

def crop(f,x0,y0,x1,y1):
    im=cv2.imread(R+f); return im[y0:y1,x0:x1]
P.update({
 's_ship_sloop': lambda: panel('sea2_ships_blender.jpg',3,1,0,0,4),
 's_ship_brig': lambda: panel('sea2_ships_blender.jpg',3,1,1,0,4),
 's_ship_galleon': lambda: panel('sea2_ships_blender.jpg',3,1,2,0,4),
 's_ship_harbor': lambda: crop('sea2_phaseD_ships.jpg',4,536,636,882),
 's_ship_storm': lambda: crop('sea2_phaseD_ships.jpg',644,536,1276,882),
 's_ship_sail': lambda: crop('sea2_phaseD_ships.jpg',1284,536,1916,882),
 's_rest_galleon': lambda: panel('sea2_phaseD_rest.jpg',2,3,0,0,2),
 's_rest_deep': lambda: panel('sea2_phaseD_rest.jpg',2,3,1,0,2),
 's_ship_ghost': lambda: panel('sea2_phaseD_rest.jpg',2,3,0,1,2),
 's_sea_giant': lambda: panel('sea2_phaseD_rest.jpg',2,3,1,1,2),
 's_bossg_1': lambda: panel('sea2_boss_ingame.jpg',2,2,0,0,2),
 's_bossg_2': lambda: panel('sea2_boss_ingame.jpg',2,2,1,0,2),
 's_bossg_3': lambda: panel('sea2_boss_ingame.jpg',2,2,0,1,2),
 's_bossg_4': lambda: panel('sea2_boss_ingame.jpg',2,2,1,1,2),
 's_spyglass': lambda: panel('sea2_phaseD_rest.jpg',2,3,0,2,2),
})
P['s_waves_game']=lambda: crop('sea2_storm_ingame.jpg',0,205,1200,480)
P['s_waves_night']=lambda: crop('sea2_storm_ingame.jpg',0,700,1050,960)
# 18.11.: Release-Bilder (Open Sea live 17.11., Zonen 16-19). FIT = ganzes Bild im 9:16-Band zeigen (Rand = unscharfes Bild)
P['s_poster']=lambda: crop('u234_update_log.jpg',1035,0,1651,620)
P['s_ulog']=lambda: crop('u234_update_log.jpg',0,0,1000,620)
P['s_z_candy']=lambda: panel('u230_studio.jpg',2,3,0,0,2)
P['s_z_crystal']=lambda: panel('u230_studio.jpg',2,3,1,0,2)
P['s_z_mush']=lambda: panel('u230_studio.jpg',2,3,0,1,2)
P['s_z_rainbow']=lambda: panel('u230_studio.jpg',2,3,1,1,2)
P['s_z_rainbow2']=lambda: panel('u230_studio.jpg',2,3,0,2,2)
P['s_z_roof']=lambda: crop('u231_cave_v2.jpg',4,4,1148,500)
P['s_z_lagoonview']=lambda: crop('u231_cave_v2.jpg',1156,4,2300,500)
P['s_z_cave']=lambda: crop('u231_cave_v2.jpg',4,548,1148,1044)
P['s_z_bench']=lambda: crop('u233_rainbow_bench.jpg',0,48,1050,799)
# 19.11.: neue Fische Zonen 16-19 (u230b_new_fish 1270x1858, je Zone 2x4 Karten), Bänke 16-19 (u232), neue Ruten (u230_gear)
P['s_nf_candy']=lambda: crop('u230b_new_fish.jpg',0,62,1270,650)
P['s_nf_crystal']=lambda: crop('u230b_new_fish.jpg',0,660,1270,1252)
P['s_nf_rainbow']=lambda: crop('u230b_new_fish.jpg',0,1252,1270,1858)
def card(c, r, zone):  # eine Fisch-Karte (Bild + Name + Seltenheit), zone 0/1/2
    y0=[[105,380],[704,976],[1298,1571]][zone][r]; x0=12+c*314
    return crop("u230b_new_fish.jpg",x0,y0,x0+302,y0+286)
P['s_f_sugarplum']=lambda: card(3,1,0)
P['s_f_lollipop']=lambda: card(1,0,0)
P['s_f_colossus']=lambda: card(3,1,1)
P['s_f_angler']=lambda: card(1,1,1)
P['s_f_leviathan']=lambda: card(3,1,2)
P['s_f_unicorn']=lambda: card(0,1,2)
P['s_benches']=lambda: cv2.imread(R+'u232_benches.jpg')
P['s_bench_candy']=lambda: panel('u232_benches.jpg',2,2,0,0,2)
P['s_bench_crystal']=lambda: panel('u232_benches.jpg',2,2,1,0,2)
P['s_bench_jungle']=lambda: panel('u232_benches.jpg',2,2,0,1,2)
P['s_bench_rainbow']=lambda: panel('u232_benches.jpg',2,2,1,1,2)
P['s_gear_rods']=lambda: crop('u230_gear.jpg',0,0,1800,445)
P['s_gear_hooks']=lambda: crop('u230_gear.jpg',0,450,1800,1346)
P['s_teaser']=lambda: cv2.imread(R+'u234_event_teaser.jpg')
FIT={'s_poster','s_ulog','s_z_bench','s_nf_candy','s_nf_crystal','s_nf_rainbow','s_f_sugarplum','s_f_lollipop','s_f_colossus','s_f_angler',
     's_f_leviathan','s_f_unicorn','s_benches','s_gear_rods','s_gear_hooks','s_teaser'}
# 22.11.: WINTER-UPDATE (live seit Sa 21.11. 18:00 Berlin, Updates 235-241). Nur Bilder aus dem gebackenen Live-Stand (u237/u238) bzw.
#   ohne Palmen-Ausschnitt (u235 zeigt noch Palmen -> nur die Nacht-Insel links), HUD weggeschnitten, alles FIT.
P['s_w_overview']=lambda: crop('u238_baked_overview.jpg',0,110,1580,880)
P['s_w_base']=lambda: crop('u238_baked_base.jpg',0,110,1580,880)
P['s_w_snowman']=lambda: crop('u237_base_winter.jpg',0,110,1580,880)
P['s_w_night']=lambda: crop('u235_winter_night.jpg',150,110,840,800)
P['s_w_poster']=lambda: cv2.imread(R+'u239_winter_poster.jpg')
P['s_w_log']=lambda: crop('u239_update_log.jpg',400,190,1540,890)
P['s_w_pass']=lambda: crop('u236_season2_pass.jpg',420,225,1500,855)
P['s_w_fish']=lambda: cv2.imread(R+'u240_winter_fish.jpg')
P['s_w_f_puffer']=lambda: panel('u240_winter_fish.jpg',3,2,0,0,2)
P['s_w_f_koi']=lambda: panel('u240_winter_fish.jpg',3,2,1,0,2)
P['s_w_f_betta']=lambda: panel('u240_winter_fish.jpg',3,2,0,1,2)
P['s_w_f_narwhal']=lambda: panel('u240_winter_fish.jpg',3,2,2,1,2)
FIT|={'s_w_overview','s_w_base','s_w_snowman','s_w_night','s_w_poster','s_w_log','s_w_pass','s_w_fish','s_w_f_puffer','s_w_f_koi','s_w_f_betta','s_w_f_narwhal'}
names=sys.argv[2:] or list(P)
sheet=[]
for n in names:
    im=P[n]()
    if n=='s_waves':  # 3 Panels nebeneinander -> auf Breite einpassen (contain) statt cover
        pass
    if n in ('s_ship_sloop','s_ship_brig','s_ship_galleon'):
        im=im[28:]; h,w=im.shape[:2]; tw=int(h*2.12); px=(tw-w)//2; py=0
        im=cv2.copyMakeBorder(im,py,py,px,px,cv2.BORDER_REPLICATE)
    if n in FIT:  # Inhalt passt in die Bandmitte (Seitenverh. 1.54), Rest = unscharfer Hintergrund
        h,w=im.shape[:2]; tw,th=1916,902; fg_h=th; fg_w=int(w*th/h)
        if fg_w>1300: fg_w=1300; fg_h=int(h*1300/w)
        bg=cv2.GaussianBlur(cv2.resize(im,(tw,int(h*tw/w)))[:th] if h*tw/w>=th else cv2.resize(im,(tw,th)),(0,0),25)
        bg=(bg*0.55).astype(np.uint8); fg=cv2.resize(im,(fg_w,fg_h),interpolation=cv2.INTER_AREA)
        y0=(th-fg_h)//2; x0=(tw-fg_w)//2; bg[y0:y0+fg_h,x0:x0+fg_w]=fg; im=bg
    h,w=im.shape[:2]
    big=cv2.resize(im,None,fx=2.4*W/w if w<W else 1.15*W/w,fy=2.4*W/w if w<W else 1.15*W/w,interpolation=cv2.INTER_LANCZOS4)
    big=cv2.addWeighted(big,1.4,cv2.GaussianBlur(big,(0,0),2),-0.4,0)
    bh,bw=big.shape[:2]
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
        '-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p',f'{OUT}/{n}.mp4'],stdin=subprocess.PIPE)
    N=int(D*FPS)
    for i in range(N):
        t=i/(N-1); e=t*t*(3-2*t)
        # cover: Skala so, dass das Panel das Bild fuellt, langsam 1.00->1.10, leichter Schwenk
        s0=max(W/bw,H/bh)
        if n=='s_waves': s0=W/bw*1.0
        s=s0*(1.0+0.10*e)
        cx=bw/2+(0.04*bw)*(e-0.5); cy=bh/2
        M=np.array([[s,0,W/2-cx*s],[0,s,H/2-cy*s]],np.float32)
        fr=cv2.warpAffine(big,M,(W,H),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT)
        p.stdin.write(fr.tobytes())
        if i==N//2: sheet.append(cv2.resize(fr,(480,226)))
    p.stdin.close(); p.wait()
cols=4; rows=(len(sheet)+cols-1)//cols
S=np.zeros((rows*226,cols*480,3),np.uint8)
for i,f in enumerate(sheet): S[(i//cols)*226:(i//cols+1)*226,(i%cols)*480:(i%cols+1)*480]=f; cv2.putText(S,names[i],((i%cols)*480+6,(i//cols)*226+22),0,0.6,(0,255,255),2)
cv2.imwrite(OUT+'/_sheet.jpg',S)
