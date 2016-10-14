import numpy as np
from scipy.signal import get_window
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as UF
import dftModel as DFT

(fs, x) = UF.wavread('../../sounds/piano.wav')

M = 511
w = get_window('hamming', M)

time = .2
x1 = x[int(time*fs):int(time*fs)+M]

N = 1024
mX, pX = DFT.dftAnal(x1, w, N)

y = DFT.dftSynth(mX, pX, w.size)*sum(w)
