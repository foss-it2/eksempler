# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:40:40 2023

@author: hemaa062

Beregner fall for en gjenstand med a=9.81
"""

# Konstanter
m = 0.2 # kg
g = 9.81  # m/s**2
dt = 0.001

# Krefter som virker
G = m * g

# Variabler
v = -3      # m/s
s = 0 # m
a = G / m
t = 0

# Simuleringsteknisk
# Ønsker å stoppe når 
v_slutt = 0

# Simuleringsløkke
while s < 5:
    s = s + v * dt # hvor langt kommer vi på dt sekunder med farten v? 
    v = v + a * dt # justerer farten
    t = t + dt

print(f"tiden det tar å komme til 5 er {t}, da er fart lik {v}")

    
    













