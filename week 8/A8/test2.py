import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/transformations/'))
import sineModel as SM
import sineTransformations as ST
import utilFunctions as UF

inputFile = '../../sounds/piano.wav'
window = 'hamming'
M = 1001
N = 2048
t = -100
minSineDur = 0.01
maxSines = 150
freqDevOffset = 30
freqDevSlope = 0.02

Ns = 512
H = 218

(fs, x) = UF.wavread(inputFile)

w = get_window(window, M)

tfreq, tmag, tphase = SM.sineModelAnal(x, fs, w, N, H, t, maxSines, minSineDur, freqDevOffset, freqDevSlope)

# y = SM.sineModelSynth(tfreq, tmag, tphase, Ns, H, fs)
y = SM.sineModelSynth(tfreq, tmag, np.array([]), Ns, H, fs)

UF.wavwrite(y, fs, 'test2.wav')

plt.plot(x)
plt.plot(y)
plt.show()
