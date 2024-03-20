filnavn = "MikkelRev.txt"

linjer = []

with open(filnavn, encoding="utf-8") as fil:
  for linje in fil:
    #linjer.append(linje)
    #linjer.append(linje.rstrip())  # Fjerner linjeskift fra filens tekstkoding.
    linjer.append(linje.rstrip().split(" "))  # Fjern linjeskift og del opp i ord

for l in linjer:
  print(l)

print("*******")
print(linjer[0])
print("*******")