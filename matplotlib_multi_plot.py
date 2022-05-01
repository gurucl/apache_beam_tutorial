from matplotlib import pyplot as plt
import numpy as np

def getValue(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)

x = np.arange(0, 5, 0.1)
y = np.arange(0, 5, 0.02)

plt.subplot(211)
plt.legend()
plt.title("Graph-1")
plt.xlabel("X-axix")
plt.ylabel("Y-axis")
plt.plot( x, getValue(x), 'b    o', y, getValue(y), color = 'b')

plt.subplot(212)
plt.legend()
plt.title("Graph-2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(y, np.cos(2*np.pi*y), color = 'g', label='lineTwo')

plt.show()
