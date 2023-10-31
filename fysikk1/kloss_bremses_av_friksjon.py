# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:40:40 2023

@author: hemaa062

Beregner bremsing av kloss på friksjonsunderlag.
"""

# Konstanter
m = 0.2 # kg
g = 9.81  # m/s**2
dt = 0.001
u = 0.8

# Krefter som virker
G = m * g
N = G
R = u * N

# Variabler
v = 4.8485      # m/s
s = 0 # m
a = -R / m
t = 0

# Simuleringsteknisk
# Ønsker å stoppe når 
s_slutt = 1.5
sikkerhetsteller = 0
# Simuleringsløkke
while s < s_slutt:
    sikkerhetsteller += 1   # Legger til 1 til telleren
    if sikkerhetsteller >= 1000000:
        print("Simuleringen stopper ikke, sjekk kriterier for while loop!")
        break
    s = s + v * dt # hvor langt kommer vi på dt sekunder med farten v? 
    v = v + a * dt # justerer farten
    t = t + dt

print(f"tiden det tar å komme frem er {t}, da er fart lik {v}")

    
    













