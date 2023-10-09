"""
Lag lister som inneholder verdiene nedenfor (én liste for hver deloppgave). 
Kan du lage listene på forskjellige måter og kun ved hjelp av programmering?
a) [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
b) [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
c) [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
"""

# a)
listea = [x for x in range(0,21,2)]
print(f"listea: {listea}")

# b)
listeb = [0]
for i in range(9):
    listeb.append(0)
print("listeb: ")
print(listeb)

# c)
listec = []
for i in range(10):
    if i % 2 == 0:
        listec.append(0)
    else:
        listec.append(1)
print("listec: ")
print(listec)