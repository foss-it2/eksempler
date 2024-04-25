import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(-2, 2, 20)
yverdier = xverdier**5

plt.axhline(0, color="black", zorder=0)
plt.axvline(0, color="black", zorder=0)
plt.plot(xverdier, yverdier, color="coral", linestyle="dashed", zorder=1)
plt.scatter(xverdier, yverdier, color="skyblue", marker="D", zorder=2)
plt.grid()

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()
