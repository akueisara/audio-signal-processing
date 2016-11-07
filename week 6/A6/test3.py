import numpy as np
import matplotlib.pyplot as plt
import sys, os
from scipy.signal import get_window
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as UF
import sineModel as SM
import harmonicModel as HM

inputFile = '../../sounds/vignesh.wav'
window = 'blackman'
M = 1201
N = 2048
t = -90
minSineDur = 0.1
nH = 50
minf0 = 130
maxf0 = 300
f0et = 5
harmDevSlope = 0.1

Ns = 512
H = 128 # one-fourth of Ns

(fs, x) = UF.wavread(inputFile)
w = get_window(window, M)

hfreq, hmag, hpahse = HM.harmonicModelAnal(x, fs, w, N, H, t, nH, minf0, maxf0, f0et, harmDevSlope, minSineDur)

numFrames = int(hfreq[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
hfreq[hfreq<=0] = np.nan
plt.plot(frmTime, hfreq)

plt.show()

