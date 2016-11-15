import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft
import sys, os, math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import dftModel as DFT
import utilFunctions as UF
import harmonicModel as HM
import matplotlib.pyplot as plt

## hprModel Demo
(fs, x) = UF.wavread('../../sounds/oboe-A4.wav')
pin = 40000
M = 801
N = 2048
t = -80
minf0 = 300
maxf0 = 500
f0et = 5
nH = 60
harmDevSlope = .001

w = get_window('blackman', M)
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))

x1 = x[pin-hM1:pin+hM2]
mX, pX = DFT.dftAnal(x1, w, N)
ploc = UF.peakDetection(mX, t)
iploc, ipmag, ipphase = UF.peakInterp(mX, pX, ploc)
ipfreq = fs*iploc/N
f0 = UF.f0Twm(ipfreq, ipmag, f0et, minf0, maxf0, 0)
hfreq, hmag, hphase = HM.harmonicDetection(ipfreq, ipmag, ipphase, f0, nH, [], fs, harmDevSlope)

Ns = 512
hNs = 256
Yh = UF.genSpecSines(hfreq, hmag, hphase, Ns, fs)

wr = get_window('blackmanharris', Ns)
xw2 = x[pin-hNs-1:pin+hNs-1] * wr / sum(wr)
fftbuffer = np.zeros(Ns)
fftbuffer[:hNs] = xw2[hNs:]
fftbuffer[hNs:] = xw2[:hNs]
X2 = fft(fftbuffer)
Xr = X2 - Yh

# plt.plot(x1)
# plt.plot(mX)
# plt.plot(abs(Yh))
plt.plot(20*np.log10(abs(Yh[:70])))
plt.plot(20*np.log10(abs(X2[:70])))
plt.plot(20*np.log10(abs(Xr[:70])))
plt.show()
