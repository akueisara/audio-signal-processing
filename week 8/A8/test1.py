import numpy as np
from scipy.signal import get_window, resample
import math
import sys, os, time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as UF
import dftModel as DFT
import matplotlib.pyplot as plt

(fs, x1) = UF.wavread('../../sounds/rain.wav')
(fs, x2) = UF.wavread('../../sounds/soprano-E4.wav')

M = N = 512
w = get_window('hanning', M)
x1w = x1[10000:10000+M]*w
x2w = x2[10000:10000+M]*w

mX1, pX1 = DFT.dftAnal(x1w, w, N)
mX2, pX2 = DFT.dftAnal(x2w, w, N)

smoothf = .2
mX2smooth1 = resample(np.maximum(-200, mX2), mX2.size*smoothf)
mX2smooth2 = resample(mX2smooth1, N/2+1)

balancef = .7
mY = balancef * mX2smooth2 + (1-balancef) * mX1

y = DFT.dftSynth(mY, pX1, N)

# plt.plot(mX1)
# plt.plot(mX2)
# plt.plot(mX2smooth2)
# plt.plot(mY)
plt.plot(y)
plt.show()
