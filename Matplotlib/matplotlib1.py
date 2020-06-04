import numpy as np
import matplotlib.pyplot as plt

# def f(t):
#     return np.exp(-t)*np.cos(2*np.pi*t)

# t1 = np.arange(0.0,5.0,0.1)
# t2 = np.arange(0.0,5.0,0.02)
# plt.subplot()

# bai tap 4: ve do thi
def HamBac3(x):
    return x**3 +3*x+1

x = np.arange(-50,50,0.2)
y = HamBac3(x)

plt.plot(x,y,"r-o", label = "Ham bac 3")
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(-60,60)
plt.tight_layout()
plt.legend()
plt.savefig("dothihambac3.png")
plt.show()