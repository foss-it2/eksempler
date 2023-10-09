"""
Vi har lista tall = [0, 1, 2, 0, 0, 3, 4, 5, 0, 0, 6, 0, 7, 0, 8, 0, 0, 0, 9, 10] . 
Her har der sneket seg inn flere 0-er som vi ikke ønsker i lista. Skriv et program som 
rydder i lista ved å fjerne alle forekomster av 0.
"""
tall = [0, 1, 2, 0, 0, 3, 4, 5, 0, 0, 6, 0, 7, 0, 8, 0, 0, 0, 9, 10]

buffer = tall[0]    # Lagrer tallet
while 0 in tall:    # Så lenge 0 er i listen "tall"
    tall.remove(0)
tall.insert(0,buffer) # setter inn lagret tall
print(tall)
