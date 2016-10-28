import numpy as np
import matplotlib.pyplot as plt
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as UF

fs = 44100
Ns = 512
ipfreq = np.array([4000.0])
ipmag = np.array([0.0])
ipphase = np.array([0.0])
Y = UF.genSpecSines_p(ipfreq, ipmag, ipphase, Ns, fs)
absY = abs(Y[:Ns/2])
absY[absY<np.finfo(float).eps] = np.finfo(float).eps

freqaxis = fs*np.arange(Ns/2)/float(Ns)
plt.plot(freqaxis, 20*np.log10(absY))
plt.show()
