import matplotlib.pyplot as plt
import numpy as np


def f(t):
    return t ** 3 + 3 * t + 1


x = np.arange(-50, 50, 3)
y = f(x)
plt.plot(x, y, 'ro', label='Ham bac 3')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-60, 60)
plt.tight_layout()
plt.savefig('doThiBac3.png')
plt.show()