import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as UF

bins = np.array([-4, -3, -2, -1, 0, 1, 2, 3])+.5
X = UF.genBhLobe(bins)
