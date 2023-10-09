"""
14)
Lag en liste med 1000 tilfeldige heltall mellom 1 og 100. Sorter lista, og bruk den sorterte 
lista for å finne det minste og det største tallet. Kontroller svaret ved å bruke metodene min() og max() .

"""
from random import randint
tall = [randint(1,100) for i in range(1000)]
print(tall)

tall.sort()
minst = tall[0]
maks = tall[-1]
print(f"Minst = {minst}, maks = {maks}")

print(f"Max/min metoder: Minst = {min(tall)}, maks = {max(tall)}")

