# einfache Beat-Analyse ohne librosa: Spektral-Fluss -> Tempo per Autokorrelation -> Beat-Raster mit bester Phase
import numpy as np, sys, json, subprocess
from scipy.io import wavfile
def onset_env(path, sr=22050, hop=256):
    raw=subprocess.run(['ffmpeg','-v','error','-i',path,'-ac','1','-ar',str(sr),'-f','f32le','-'],capture_output=True).stdout
    y=np.frombuffer(raw,np.float32)
    n=1024; w=np.hanning(n); frames=np.lib.stride_tricks.sliding_window_view(np.pad(y,(n//2,n//2)),n)[::hop]*w
    S=np.log1p(10*np.abs(np.fft.rfft(frames,axis=1)))
    flux=np.maximum(np.diff(S,axis=0),0).sum(1); flux=np.r_[0,flux]
    flux=(flux-flux.mean())/(flux.std()+1e-9)
    rms=np.sqrt((frames**2).mean(1))
    return y,sr,hop,flux,rms
def analyze(path):
    y,sr,hop,f,rms=onset_env(path); fps=sr/hop
    ac=np.correlate(f,f,'full')[len(f)-1:]
    lags=np.arange(len(ac))/fps; bpm=60/np.maximum(lags,1e-9)
    m=(bpm>=70)&(bpm<=180); best=np.argmax(ac*m*np.exp(-0.5*(np.log2(np.maximum(bpm,1)/120)/1.0)**2))
    per=best/fps
    # Phase
    ph=np.linspace(0,per,64,endpoint=False); sc=[]
    for p in ph:
        idx=((np.arange(p,len(f)/fps,per))*fps).astype(int); idx=idx[idx<len(f)]; sc.append(f[idx].mean())
    p0=ph[int(np.argmax(sc))]
    beats=np.arange(p0,len(y)/sr,per)
    # Lautheit je Beat (fuer Drop-Suche)
    loud=[float(rms[int(b*fps):int((b+per)*fps)].mean()) for b in beats]
    return dict(dur=len(y)/sr, bpm=60/per, period=per, beats=[round(float(b),3) for b in beats], loud=[round(l,4) for l in loud])
if __name__=='__main__':
    out={}
    for p in sys.argv[1:]:
        r=analyze(p); out[p]=r
        L=np.array(r['loud']); 
        jump=np.argmax(np.r_[0,np.diff(np.convolve(L,np.ones(2)/2,'same'))])
        print(p.split('/')[-1], f"{r['dur']:.2f}s bpm {r['bpm']:.1f} beats {len(r['beats'])} first {r['beats'][0]} drop~beat{jump}@{r['beats'][jump]}s")
        print('  loud', ' '.join(f'{x*100:.0f}' for x in L))
    json.dump(out,open('/home/claude/fb/snd/beats.json','w'),indent=0)
