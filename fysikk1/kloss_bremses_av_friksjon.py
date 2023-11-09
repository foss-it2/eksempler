# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:40:40 2023

@author: hemaa062

Beregner bremsing av kloss på friksjonsunderlag.
"""

from matplotlib import pyplot as plt

# Konstanter
m = 0.2 # kg
g = 9.81  # m/s**2
dt = 0.001
u = 0.4

# Krefter som virker
G = m * g
N = G
R = u * N
F = 0.25 * R
sum_krefter = F - R

# Variabler
v = 5      # m/s
s = 0 # m
a = (F-R)/m
print(f"Akselerasjon a = {a}")
t = 0
xverdier = []
yverdier = []

# Simuleringsteknisk
# Ønsker å stoppe når 
s_slutt = 1.5
sikkerhetsteller = 0
# Simuleringsløkke
while v >= 4.2:
    sikkerhetsteller += 1   # Legger til 1 til telleren
    if sikkerhetsteller >= 1000000:
        print("Simuleringen stopper ikke, sjekk kriterier for while loop!")
        break
    xverdier.append(t)
    yverdier.append(v)
    s = s + v * dt # hvor langt kommer vi på dt sekunder med farten v? 
    v = v + a * dt # justerer farten
    t = t + dt
    

print(f"tiden det tar å komme frem er {t}, da er fart lik {v}")

plt.plot(xverdier,yverdier, label="Posisjon (s)")
plt.title("Fart som funksjon av tid")  # tittel på grafen
plt.xlabel("$t$ / s")                       # x-akse-tittel
plt.ylabel("$v$ / m/s")                       # y-akse-tittel
plt.grid()                                  # viser rutenett
plt.show()   



    
    













