# -*- coding: utf-8 -*-
"""
Created on 170221
Tegner planck-kurven til Sola og bølgelengden for maks intensitet.
Sammenlikner med Wiens forskyvningslov.

hmauroy@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt


# Konstanter
h = 6.63e-34
c = 3.00e8
k = 1.38e-23
pi = np.pi

T = 5780   # temperatur i kelvin


# Definerer x-aksen
x = np.linspace(100e-9, 3000e-9, 200)
sol = []
rigel = []
betelgeuse = []

for i in range(0, len(x)):
    # print(x[i])
    # Regner ut et nytt punkt for kurven
    p_sol = (2*h*np.power(c, 2)) / \
        (np.power(x[i], 5)) * 1/(np.exp(h*c/(x[i]*k*T))-1)
    # print(p)
    sol.append(p_sol)
    # Rigel
    # p_rigel = (2*pi*h*np.power(c,2))/(np.power(x[i],5)) * 1/(np.exp(h*c/(x[i]*k*11000))-1)
    # rigel.append(p_rigel)
    # Betelgeuse
    # p_betelgeuse = (2*pi*h*np.power(c,2))/(np.power(x[i],5)) * 1/(np.exp(h*c/(x[i]*k*3500))-1)
    # betelgeuse.append(p_betelgeuse)


# Finner toppunktet
maxIndex = np.argmax(sol)
print(x[maxIndex])

# Lager et nytt x-array som er zoomet inn
x2 = np.linspace(200e-9, 1500e-9, 200)
sol2 = []
# Regner ut nye y-verdier
for i in range(0, len(x2)):
    # Regner ut et nytt punkt for kurven
    p_sol2 = (2*h*np.power(c, 2)) / \
        (np.power(x2[i], 5)) * 1/(np.exp(h*c/(x2[i]*k*T))-1)
    sol2.append(p_sol2)

# Plotte kurver og punkter
plt.plot(x, sol, "-b", label="Sol, 5780K")
#plt.plot(x2,sol2, "-r", label="Sol zoom, 5780K") # Plotte zoomet inn
plt.plot(x[maxIndex], sol[maxIndex], 'ro',label="$T_{topp}$=" + f"{1e9*x[maxIndex]:.1f} nm")
plt.plot(x_wien, y_wien, "-k", label="Wiens forsk.lov")
plt.legend(loc="upper right")
plt.xlabel("Bølgelengde (m)")
plt.ylabel("U (W/m2\u2022m)")
# plt.xscale("log") # Plotte logaritmisk x-akse
plt.show()
