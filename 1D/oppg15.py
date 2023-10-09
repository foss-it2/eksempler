"""
15)
Ta utgangspunkt i lista du laget i forrige oppgave. Legg til verdiene 17, 42 og 81 på riktige 
posisjoner slik at lista forblir sortert.
"""
from random import randint
tall = [randint(1,100) for i in range(20)]
tall.sort()
print("utgangspunktet:")
print(tall)

# Enkleste mulighet: Legger til verdiene 17, 42 og 81 og sorterer
print("Enkleste mulighet: Legger til verdiene 17, 42 og 81 og sorterer.")
tall.append(17)
tall.append(42)
tall.append(81)

tall.sort()
print("Med innsatte verdier.")
print(tall)



# Programmert med algoritme der vi setter inn tallet på rett plass
tall = [randint(1,100) for i in range(20)]
tall.sort()
print(("Lager en ny liste med tall og bruker algoritme 2:"))
print(tall)


liste = [17, 42, 81]
for mittTall in liste:
    for i in range(0,len(tall)-1): # Går frem til 1 mindre enn siste indeks pga. sammenlikning med neste indeks inni for-loop.
        current = tall[i]
        neste = tall[i+1]
        if current <= mittTall <= neste:
            tall.insert(i+1,mittTall)
            break # hopper ut av loopen.
        
print("Med innsatte verdier.")
print(tall)

