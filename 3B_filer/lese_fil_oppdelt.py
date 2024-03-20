filnavn = "MikkelRev.txt"

with open(filnavn, encoding="utf-8") as fil:
  innhold = fil.read()

# Deler opp innhold i ord
ord = innhold.split(" ")
for oppdelt in ord:
  print(oppdelt)


# Deler opp som en liste
bokstaver = list(innhold)
print(bokstaver)