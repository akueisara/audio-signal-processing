import numpy as np
import matplotlib.pyplot as plt

N = 64
k0 = 7
x = np.cos(2 * np.pi * k0 / N * np.arange(N))

X = np.array([])
nv = np.arange(-N/2, N/2)
kv = np.arange(-N/2, N/2)

for k in kv:
    s = np.exp(1j * 2 * np.pi * k / N * nv)
    X = np.append(X, sum(x*np.conjugate(s)))

y = np.array([])
for n in nv:
    s = np.exp(1j * 2 * np.pi * n / N * kv)
    y = np.append(y, 1.0/N * sum(X*s))
    
plt.plot(kv, y)
plt.axis([-N/2, N/2-1, -1, 1])

plt.show()
