from pylab import *


k = 28.8

def a(v): # A
  L = k*v**2  # B
  F = 9.81*70 - L
  aks = F/70
  return aks

s = 0
v = 3
t = 0
dt = 0.01

while s <= 6000:
  v = v + a(v)*dt   # C
  s = s + v*dt
  t = t + dt 


