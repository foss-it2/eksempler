"""
Skriv et program som beregner summen og gjennomsnittet av tallene i lista 
tall = [2, 3, 4, 5, -5, 8, 4, -7, 2, 9, 7, -9, 5, 3, 8, 5, -3, 3, 3, 2, 0, 1, 9, 1] . 
Du skal ikke bruke innebygde funksjoner.
"""

tall = [2, 3, 4, 5, -5, 8, 4, -7, 2, 9, 7, -9, 5, 3, 8, 5, -3, 3, 3, 2, 0, 1, 9, 1]
summen = 0
for x in tall:
    summen += x

print(f"sum er {summen}")

gjsnitt = summen / len(tall)
print(f"Gjennomsnitt: {gjsnitt}")