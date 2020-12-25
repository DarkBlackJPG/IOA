import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

plt.figure()
vals = np.arange(0, 20, 0.01)
y = []
x1 = []
x2 = []

for i in range(0, vals.size):
    y.append(i/100)
    x1.append(sp.spherical_jn(1, vals[i]))
    x2.append(sp.spherical_jn(2, vals[i]))
plt.plot(y, x1, label='Bessel first order')
plt.plot(y, x2, label='Bessel second order')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.grid(color='lightgray', linestyle='-', linewidth=1)
plt.xticks(np.arange(min(vals), max(vals)+1, 1.0))
plt.legend()
plt.show()
