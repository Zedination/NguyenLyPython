import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2*np.pi,2*np.pi,200)
ysin = np.sin(x)
ycos = np.cos(x)

plt.subplot("221")
plt.plot(x,ysin,"r-",label ="Sin")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.subplot("222")
plt.plot(x,ycos,"b-",label ="Cos")
plt.legend()

plt.subplot("223")
plt.plot(x,ycos,"b-",label ="Cos")
plt.legend()

plt.show()