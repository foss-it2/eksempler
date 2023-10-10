"""
Ordbok-testing
"""

bok = {}
bok["fornavn"] = "Henrik"
bok["etternavn"] = "Mauroy"
print(bok)
bok[1] = "En"
print(bok)
bok["En hel setning"] = "kan være nøkkel"
print(bok)
print(bok["etternavn"])
if "En hel setning" in bok:
    bok.pop("En hel setning")
print(bok)
if "Henrik" in bok.values():
    print("Ja")
for key, val in bok.items():
    print(key, ",", val)

# Henriks for loop
for key in bok:
    print("nøkkel:", key, ", verdi er:",bok[key])

print(len(bok))
