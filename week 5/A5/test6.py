# function to call the main analysis/synthesis functions in software/models/sineModel.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as UF
import sineModel as SM

inputFile = '../../sounds/oboe-A4.wav'
window = 'hamming'
M = 501
N = 1024
t = -90
minSineDur = 0.1
maxSines = 20
freqDevOffset = 10
freqDevSlope = 0.001
H = 200

(fs, x) = UF.wavread(inputFile)
w = get_window(window, M)
tfreq, tmag, tphase = SM.sineModelAnal(x, fs, w, N, H, t, maxSines, minSineDur, freqDevOffset, freqDevSlope)

numFrames = int(tfreq[: ,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
tfreq[tfreq<=0] = np.nan
plt.plot(frmTime, tfreq)

plt.show()
