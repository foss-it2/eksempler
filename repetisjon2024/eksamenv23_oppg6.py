"""
Implementerer en pseudokode
"""

#poeng = int(input("Skriv inn poengsummen din: "))
p = -1
if p < 50:
    print("Ikkje bestått")
elif p > 50 and p < 69:
    print("Bestått")
elif p > 70 and p < 89:
    print("Godt bestått")
elif p > 90 and p < 100:
    print("Mykje godt bestått")
else:
    print("Ikkje gyldig poengsum")

# Rettet kode
p = 70
if p > 0 and p < 50:
    print("Ikkje bestått")
elif p >= 50 and p <= 69:
    print("Bestått")
elif p >= 70 and p <= 89:
    print("Godt bestått")
elif p >= 90 and p <= 100:
    print("Mykje godt bestått")
else:
    print("Ikkje gyldig poengsum")
