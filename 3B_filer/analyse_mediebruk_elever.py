import json

filnavn = "mediebruk_jsonified.json"

with open(filnavn, "r") as fil:
    data = json.load(fil)

# Hva slags datatype er data?
print(type(data))
for key in data:
    print(key)

"""
version
class
label
source
updated
note
role
id
size
dimension
extension
value
status

Tid brukt til ulike medier en gjennomsnittsdag (minutter), etter medietype, år og statistikkvariabel"

Radio
1991: 43
1992: 49
1993: 543
TV
1991: 87
1992: 347
1993: 176
"""
aar = data["dimension"]["Tid"]["category"]["index"]
# Legger alle årene inn i en liste for enklere navigering
aar_liste = []
for key in aar:
    aar_liste.append(int(key))
print(aar_liste)
ant_punkter_per_medietype = len(aar)
print(f"ant punkter per medie {ant_punkter_per_medietype}")
medietyper = data["dimension"]["Media"]["category"]["label"]
# Legger alle medietypene inn i en liste
medie_liste = []
for key,val in medietyper.items():
    medie_liste.append(val)
print(medie_liste)
# Lager statistikk for KUN papiravis.
papiravis_stat = {}
# Legge inn hvert år med tilhørende verdi i minutter
verdier = data["value"]
for i in range(ant_punkter_per_medietype):
    aaret = aar_liste[i]
    papiravis_stat[aaret] = int(verdier[i])
print(papiravis_stat)
max_tid = 0
max_aar = ""
for key,val in papiravis_stat.items():
    if val > max_tid:
        max_tid = val
        max_aar = key
print(max_aar,max_tid)

# Lager statistikk over alle medietyper
statistikk = {}
start = 0
slutt = start + ant_punkter_per_medietype
for medie in medie_liste:
    # Leger en ordbok med statistikk for aktuelt medie
    statistikk[medie] = {}
    # Legge inn hvert år med tilhørende verdi i minutter
    aar_indeks = 0
    for i in range(start,slutt):
        aaret = aar_liste[aar_indeks]
        statistikk[medie][aaret] = verdier[i]
        aar_indeks += 1
    start = slutt
    slutt = start + ant_punkter_per_medietype

print()
print(statistikk)