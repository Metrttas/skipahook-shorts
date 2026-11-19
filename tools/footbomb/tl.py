# Zeitachsen der Szenen nachbauen -> Clip-Zeiten von Schuss (K), Einschlag (I), Jubel-Schnitt (C), Ende (E)
SL=[(6,1),(8,1,.3),(30,.3),(10,.3,1)]
H18=[(8,1),(12,1,.18),(50,.18),(10,.18,.6)]
FIX=[(8,1),(10,1,.15),(40,.15),(20,.15,1),(50,1)]
SAVE=[(12,1),(10,1,.25),(40,.25),(10,.25,1),(20,1)]
S={
 'airwar_v2':(4.9,5.5,[(0.25,[(72,1)]),(None,SL+[(4,1)]),(None,[(50,1)]),(None,SL),(None,[(75,1)]),(4.55,H18),(None,[(30,.6)]),(5.37,FIX),(6.4,[(110,1)])]),
 'slidesave_v1':(2.85,3.45,[(0.2,[(54,1)]),(None,[(8,1),(12,1,.2),(45,.2),(10,.2,1),(6,1)]),(None,[(40,1)]),(2.5,H18),(None,[(30,.6)]),(3.32,FIX),(4.4,[(110,1)])]),
 'airsave_v1':(7.3,7.9,[(0.3,[(78,1)]),(None,SL),(None,[(60,1)]),(None,[(60,1)]),(None,[(66,1)]),(5.7,SAVE),(None,[(24,1)]),(6.95,H18),(None,[(30,.6)]),(7.77,FIX),(8.85,[(110,1)])]),
 'slidechain_v1':(5.1,5.7,[(0.25,[(48,1)]),(1.1,SAVE),(None,[(60,1)]),(3.45,SAVE),(None,[(24,1)]),(4.75,H18),(None,[(30,.6)]),(5.57,FIX),(6.65,[(110,1)])]),
 'airwar2_v1':(7.35,7.95,[(0.3,[(81,1)]),(1.65,SL),(None,[(39,1)]),(2.75,SL),(None,[(39,1)]),(3.85,SL),(None,[(60,1)]),(None,[(60,1)]),(None,[(36,1)]),(7.0,H18),(None,[(30,.6)]),(7.82,FIX),(8.9,[(110,1)])]),
 'bike_s1':(3.95,4.55,[(0.62,[(89,1)]),(None,[(96,1)]),(None,H18),(None,[(33,.6)]),(4.42,[(8,1),(10,1,.15),(40,.15),(20,.15,1),(55,1)]),(5.45,[(110,1)])]),
 'scorp_s1':(3.25,3.85,[(0.4,[(120,1)]),(None,[(30,1)]),(None,H18),(None,[(30,.6)]),(3.72,FIX),(4.75,[(110,1)])]),
 'tornado_s1':(3.55,4.15,[(1.2,[(93,1)]),(None,[(30,1)]),(None,H18),(None,[(30,.6)]),(4.02,FIX),(5.05,[(110,1)])]),
 'flyhead_s1':(3.4,3.95,[(0.3,[(132,1)]),(None,[(27,1)]),(None,[(15,1),(12,1,.2),(50,.2),(10,.2,.6)]),(None,[(25,.6)]),(3.83,[(7,1),(10,1,.15),(40,.15),(20,.15,1),(50,1)]),(4.9,[(110,1)])]),
}
def tl(seq):
    fr=[];T=0
    for ci,(t0,segs) in enumerate(seq):
        if t0 is not None: T=t0
        for sg in segs:
            n,s0=sg[0],sg[1]; s1=sg[2] if len(sg)>2 else s0
            for k in range(n):
                sp=s0+(s1-s0)*(k/(n-1)) if n>1 else s0
                fr.append((T,ci)); T+=sp/60
    return fr
out={}
for name,(tk,ti,seq) in S.items():
    fr=tl(seq); n=len(fr)
    K=next(i for i,(T,c) in enumerate(fr) if T>=tk)/60
    # Einschlag: erstes Bild im fixed-Schnitt (vorletzter Schnitt) mit T>=ti
    lastc=fr[-1][1]
    I=next(i for i,(T,c) in enumerate(fr) if T>=ti and c==lastc-1)/60
    C=next(i for i,(T,c) in enumerate(fr) if c==lastc)/60
    out[name]=dict(K=round(K,2),I=round(I,2),C=round(C,2),E=round(n/60-0.05,2),n=n)
    print(name,out[name])
import json; json.dump(out,open('/home/claude/fb/tl.json','w'))
