"""
Ordbok
nøkkel: verdi
"""
bok = {}
bok["fornavn"] = "Henrik"
bok["fornavn"] = "AAA"
bok["etternavn"] = "Mauroy"
bok["postnr"] = 1450
bok[42] = "førtito"
if "postnr" in bok:
    bok.pop("postnr")
print(bok)
bok["testverdi"] = 1450

til_sletting = []
for x in bok:
    print(x, bok[x])
    if bok[x] == 1450:
        til_sletting.append(x)

for key in til_sletting:
    bok.pop(key)

print(bok)
    
# Gå gjennom ordbok med løkke, 
# slett nøkkel/verdi hvis verdi er tallet 1450.

ordbok ={
    "nøkkel1": "verdi",
    "nøkkel2": "verdi",
    "nøkkel3": "verdi",
    "nøkkel4": "verdi",
    "nøkkel5": "osv",
}
