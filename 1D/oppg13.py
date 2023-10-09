"""
navn = ["Anne", "Per", "Ole", "Anne", "Lise", "Ole", "Anne", "Per", "Anne", "Tor", "Ole"] . 
Her forekommer noen av navnene flere ganger. Rydd opp i lista 
slik at hvert navn bare forekommer én gang i lista.
"""

navn = ["Anne", "Per", "Ole", "Anne", "Lise", "Ole", "Anne", "Per", "Anne", "Tor", "Ole"]

# Går  gjennom lista og markerer duplikater.
# Lagrer navnet underveis så vi kan lete etter neste navn ved neste gjennomkjøring
navn_for_sletting = []
for i in range(0,len(navn)):
    if i > len(navn)-1:
        print("Har gått til slutten av listen, avbryter loop.")
        break
    current =  navn[i]
    print(f"Søker etter {current}")
    for j in range(i+1,len(navn)):
        if navn[j] == current:
            navn_for_sletting.append(j)
    # Utfør sletting før vi går til neste navn
    print(f"Sletter indekser {navn_for_sletting}.")
    # Må sortere listen for sletting i synkende rekkefølge for å kunne bruke pop().
    navn_for_sletting.sort()
    navn_for_sletting.reverse()
    for indeks in navn_for_sletting:
        navn.pop(indeks)
    navn_for_sletting = []
    print(f"navn er nå: {navn}")
    



