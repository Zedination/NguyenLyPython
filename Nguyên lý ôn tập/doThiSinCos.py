import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3 * np.pi, 3 * np.pi, 60)
ySin = np.sin(x)
yCos = np.cos(x)

plt.subplot(221)
plt.plot(x, ySin, "r-", label='Sin')
plt.legend()

plt.subplot(224)
plt.plot(x, yCos, "ro", label='Cos')
plt.legend()

plt.tight_layout()
plt.show()
