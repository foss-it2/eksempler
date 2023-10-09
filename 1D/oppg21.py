"""
Lag et program som bruker input() og en while -løkke. Brukeren skal angi tall som skal 
legges til i en liste. Det er brukeren som bestemmer hvor mange tall som skal lagres. 
Når brukeren er ferdig, kan hun skrive «x» i stedet for et tall, og løkka skal avsluttes. 
Deretter skal du skrive ut en oversikt over de registrerte tallene 
sammen med det minste tallet, det største tallet og summen av tallene.
"""

# Legger til tall
inn = ""
liste = []
minst = 0
maks = 0
summen = 0
while inn != "x":
    inn = input("Skriv inn et heltall ('x' for å avslutte): ")
    tall = 0
    if inn == "x":
        break
    else:
        tall = int(inn)
    liste.append(tall)
    summen += tall
    if tall < minst:
        minst = tall
    elif tall > maks:
        maks = tall

print("Tallene lagt inn:")
for tall in liste:
    print(tall, end = " ")
print("")
print(f"sum er {summen}")

gjsnitt = summen / len(liste)
print(f"Gjennomsnitt: {gjsnitt}")

print(f"Min: {minst}, maks: {maks}")
