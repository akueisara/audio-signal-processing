import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.signal import get_window
sys.path.append('../../software/models/')
import dftModel as DFT

fs = 44100 # sampling rate
f = 5000.0 # frequency
M = 101 # window size
x = np.cos(2*np.pi*f*np.arange(M)/float(fs))
N = 512
w = get_window('blackmanharris', M)
mX, pX = DFT.dftAnal(x, w, N)

# only display the positive part and it's shown in hertz
plt.plot(np.arange(0, fs/2 + 1, fs/float(N)), mX-max(mX))
plt.show()
