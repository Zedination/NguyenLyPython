import matplotlib.pyplot as plt
import numpy as np

# legend la chu thich, label la ten chu thich

x = np.linspace(-np.pi, np.pi, 200)
fsin = np.sin(x)
fcos = np.cos(x)
fig, axs = plt.subplot(1, 2)
axs[0].plot(x, fsin, 'r-', label='Sin')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
axs[0].legend()

axs[1].plot(x, fcos, 'g-', label='Cos')
axs[1].set_xlim(-5, 5)
axs[1].legend()
fig.tight_layout()
plt.show()
