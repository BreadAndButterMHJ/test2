import numpy as np
from matplotlib import pyplot as plt

plt.figure(1)
t = np.arange(1, 10, 0.1)
plt.plot(t, t, 'r', alpha=0.7)

plt.figure(2)
plt.plot(t, t)
plt.show()
