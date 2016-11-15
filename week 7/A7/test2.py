import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as UF
import stochasticModel as STM
import matplotlib.pyplot as plt
import numpy as np

(fs, x) = UF.wavread('../../sounds/ocean.wav')
H = 128
stocf = .2
stocEnv = STM.stochasticModelAnal(x, H, H*2, stocf)

# stocEnv.shape = (2217, 25) 
# it has 2217 frames and each frame has 25 points

# plt.pcolormesh(stocEnv)
plt.pcolormesh(np.transpose(stocEnv))
plt.show()
