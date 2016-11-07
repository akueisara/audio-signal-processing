import numpy as np
from scipy.signal import get_window
import sys, os, time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as UF
import harmonicModel as HM

(fs, x) = UF.wavread('../../sounds/oboe-A4.wav')
w = get_window('hamming', 1001)
N = 2048
t = -50
minf0 = 300
maxf0 = 500
f0et = 1
H = 1000

f0 = HM.f0Detection(x, fs, w, N, H, t, minf0, maxf0, f0et)
