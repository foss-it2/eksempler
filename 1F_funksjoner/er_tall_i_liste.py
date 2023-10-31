"""
Returnerer indeks for tall hvis det er i en liste.
"""

def er_tall_i_liste(mittTall,liste):
    for tall in liste:
        if tall == mittTall:
            return True
    return False

liste = [1,4,5,6,5]
print(er_tall_i_liste(1,liste))

def minIndexOf(mittTall,liste):
    for i in range(len(liste)):
        if liste[i] == mittTall:
            return i
    return False

indeks = minIndexOf(1,liste)
if  indeks is not False:
    print("Tallet finnes på indeks",indeks)
else:
    print("Tallet er ikke i listen")

