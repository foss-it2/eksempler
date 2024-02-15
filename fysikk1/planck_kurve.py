"""
Created on 170221
Tegne planck-kurver

hmauroy@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

# Konstanter
h = 6.63e-34
c = 3.00e8
k = 1.38e-23
pi = np.pi

A = 3000   # temperatur i kelvin
B = 4000
C = 5000
D = 6000


x = np.linspace(100e-9, 3000e-9, 100)
arr_a = []
arr_b = []
arr_c = []
arr_d = []

for i in range(0, len(x)):
    # print(x[i])
    # Regner ut et nytt punkt for kurven
    p_a = (2*pi*h*np.power(c, 2)) / \
        (np.power(x[i], 5)) * 1/(np.exp(h*c/(x[i]*k*A))-1)
    # print(p)
    arr_a.append(p_a)
    # Rigel
    p_b = (2*pi*h*np.power(c, 2)) / \
        (np.power(x[i], 5)) * 1/(np.exp(h*c/(x[i]*k*B))-1)
    arr_b.append(p_b)
    # Betelgeuse
    p_c = (2*pi*h*np.power(c, 2)) / \
        (np.power(x[i], 5)) * 1/(np.exp(h*c/(x[i]*k*C))-1)
    arr_c.append(p_c)
    p_d = (2*pi*h*np.power(c, 2)) / \
        (np.power(x[i], 5)) * 1/(np.exp(h*c/(x[i]*k*D))-1)
    arr_d.append(p_d)


# Plotte punktene
plt.plot(x, arr_a, "-r", label="3000")
plt.plot(x, arr_b, "-y", label="4000")
plt.plot(x, arr_c, "-g", label="5000")
plt.plot(x, arr_d, "-b", label="6000")
plt.legend(loc="upper right")
plt.xlabel("Bølgelengde (m)")
plt.ylabel("U (W/m2)")
plt.show()
