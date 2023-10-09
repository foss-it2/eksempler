"""
Basert på oppgavene 10-15 kan vi nå bruke biblioteket math som har flere fine funksjoner for matematikk. 
  
Lag et program som kombinerer Pythagoras læresetning og areal av en sirkel: Hensikt er å finne ut av om en rettvinklet trekant får plass inni en sirkel med gitt areal. 
  
1. Input skal være arealet til sirkelen og de to korteste sidene (katetene) i trekanten. 
  
2. Programmet må utføre beregninger som innebærer en if test (kanskje vanskelig?)
  
3. Printe ut et svar om trekanten får plass eller ikke.
"""

from math import sqrt, pi

areal = float(input("Areal: "))
kat1 = float(input("Korteste katet: "))
kat2 = float(input("Lengste katet: "))

# Finner hypotenus
hyp = sqrt(kat1**2 + kat2**2)

# Finner radius i sirkel A = pi * r^2 -> r = sqrt(A/pi)
r = sqrt(areal/pi)

# Får trekanten plass i sirkel må hypotenus være mindre enn diameteren.
print(f"Hypotenus lengde: {hyp:.1f}, diameter i sirkel: {2*r:.1f}")
if hyp <= 2*r:
    print("Hurra! Trekanten får plass!")
else:
    print("Det er ikke plass til trekanten :(")