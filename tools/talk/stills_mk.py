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
 's_spyglass': lambda: panel('sea2_phaseD_rest.jpg',2,3,0,2,2),
})
names=sys.argv[2:] or list(P)
sheet=[]
for n in names:
    im=P[n]()
    if n=='s_waves':  # 3 Panels nebeneinander -> auf Breite einpassen (contain) statt cover
        pass
    if n in ('s_ship_sloop','s_ship_brig','s_ship_galleon'):
        im=im[28:]; h,w=im.shape[:2]; tw=int(h*2.12); px=(tw-w)//2; py=0
        im=cv2.copyMakeBorder(im,py,py,px,px,cv2.BORDER_REPLICATE)
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
