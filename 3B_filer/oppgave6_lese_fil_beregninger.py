"""
Last ned fila  tall.txt . Den inneholder fem tall i hver linje. 
Lag et program som leser inn fila. 
For hver rad skal sum og gjennomsnitt beregnes. 
Skriv resultatene til en ny fil der både tallene, 
summen av dem og gjennomsnittet lagres. 
Skriv linjer som gjør teksten lett å lese, for eksempel:
Tall: 2 4 8 4 12,    sum: 30,    gjennomsnitt: 6
"""

linjer = []

filnavn = "tall.txt"

utliste = []

with open(filnavn, encoding="utf-8") as fil:
  for linje in fil:
    #linjer.append(linje)
    #linjer.append(linje.rstrip())  # Fjerner linjeskift fra filens tekstkoding.
    # Fjern linjeskift og del opp i ord
    miniliste = linje.rstrip().split("-") # resultat av split() gir liste
    sum = 0
    tall_streng = ""
    for tall in miniliste:
      sum += int(tall)
      tall_streng += tall + " "
    snitt = sum / len(miniliste)
    #print(f"Tall {tall_streng} sum: {sum},    gjennomsnitt: {snitt}")
    utliste.append(f"Tall {tall_streng} sum: {sum},    gjennomsnitt: {snitt}")

print(utliste)