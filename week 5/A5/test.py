import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import dftModel as DFT
import utilFunctions as UF

(fs, x) = UF.wavread('../../sounds/sine-440.wav')
M = 501 # window size
N = 2048 # FFT size
t = -20 # threshold using for the peak detection
w = get_window('hamming', M)
x1 = x[.8*fs:.8*fs+M] # M samples in the middle of the sound 
mX, pX = DFT.dftAnal(x1, w, N)
ploc = UF.peakDetection(mX, t)
iploc, ipmag, ipphase = UF.peakInterp(mX, pX, ploc)
# pmag = mX[ploc]

freqaxis = fs*np.arange(N/2+1)/float(N)
plt.plot(freqaxis, mX)
plt.plot(fs * iploc/ float(N), ipmag, marker='x', linestyle='')

plt.show()

