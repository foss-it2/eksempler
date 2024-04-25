import matplotlib.pyplot as plt
import numpy as np


def f(x):
    # f(x) = 4x3 – x5
    return 4*x**3 - x**5

xverdier = np.linspace(-2, 2, 5)   # Lager matematisk array (vektor)
yverdier = f(xverdier)             # Utfører matematisk operasjon på hele arrayet på én gang.

# Skriver ut en oversikt over tilgjengelige stiler
print(plt.style.available)

# Angir at vi vil bruke stilen "dark_background"
plt.style.use("dark_background")

plt.plot(xverdier, yverdier, color="salmon")

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Femtegradsfunksjon")
plt.xlim(-3, 3)
plt.ylim(-7,7)

plt.show()
