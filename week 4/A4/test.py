import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft
import math
import matplotlib.pyplot as plt

M = 63 # Odd Window size
# window = get_window('hanning', M)
# window = get_window('hamming', M)
# window = get_window('blackman', M)
window = get_window('blackmanharris', M)
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))

N = 512 # FFT size
hN = N/2
# zero padding
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = window[hM2:]
fftbuffer[N-hM2:] = window[:hM2]

X = fft(fftbuffer)
absX = abs(X)
absX[absX<np.finfo(float).eps] = np.finfo(float).eps # make sure there's no zeros
mX = 20*np.log10(absX) # magnitude spectrum
pX = np.angle(X) # phase spectrum

# place back the data in the middle of arrays
mX1 = np.zeros(N)
pX1 = np.zeros(N)
mX1[:hN] = mX[hN:]
mX1[N-hN:] = mX[:hN]
pX1[:hN] = pX[hN:]
pX1[N-hN:] = pX[:hN]

plt.plot(np.arange(-hN, hN)/float(N)*M, mX1-max(mX1))
plt.axis([-20, 20, -100, 0])
plt.show()
