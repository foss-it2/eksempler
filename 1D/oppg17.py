"""
Lag et program som finner den korteste og den lengste teksten i en liste, altså teksten med færrest tegn og teksten med flest tegn.
"""
tekst = "Lag et program som finner den korteste og den lengste teksten i en liste, altså teksten med færrest tegn og teksten med flest tegn."

liste = tekst.split(" ")
for ord in liste:
    print(ord)

print("*"*100)
lengst = liste[0]
kortest = liste[0]

for ord in liste:
    if len(ord) > len(lengst):
        lengst = ord
    elif len(ord) < len(kortest):
        kortest = ord

print(lengst)
print(kortest)