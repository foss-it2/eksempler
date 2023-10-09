"""
Lag en tom liste. Fyll opp lista med heltallene fra 1 til 20. 
Deretter fjerner du alle partallene fra lista, slik at du sitter igjen med oddetallene.
"""

tall = [i for i in range(1,21)]
print(tall)

# chatGPT som lager en ny filtrert liste
filtered_list = [x for x in tall if x % 2 != 0]
print(filtered_list)

# Henriks løsning som redigerer original liste
for i in range(len(tall)-1,0,-2):   # Går baklengs pga pop() ødelegger indekseringen etter hvert. Bedre å fjerne bakfra.
    if tall[i] % 2 == 0:
        tall.pop(i)
print(tall)


