"""
Lag et program som bruker en løkke for å fjerne alle forekomster av tallet 3 fra denne lista: 
[1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
"""

tall = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]

while 3 in tall:
    indeks = tall.index(3)
    tall.pop(indeks)

print(tall)
    