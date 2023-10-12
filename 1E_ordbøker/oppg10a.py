"""
Lag en datastruktur som samler dataene som i tabellen ovenfor.
a: Skriv ut vinnertiden på 400 m for hvert av årstallene.
b: Skriv ut vinnertidene fra OL i 2020.
c: Skriv ut den dårligste og den beste vinnertiden på 200 m.
d: Hvilke av de to datastrukturene vil du foretrekke for å løse oppgavene a og b ovenfor?

"""

sommer_ol = [
    {"øvelse": 100, "vinnertider": {"2004": 10.93, "2008": 10.87, "2012": 10.75, "2016": 10.71, "2020": 10.61}}, 
    {"øvelse": 200, "vinnertider": {"2004": 22.06, "2008": 21.74, "2012": 21.88, "2016": 21.78, "2020": 21.53}}, 
    {"øvelse": 400, "vinnertider": {"2004": 49.41, "2008": 49.62, "2012": 49.55, "2016": 49.44, "2020": 48.36}}, 
]


ovelse = sommer_ol[-1]["øvelse"]
print(f"Vinnertiden på {ovelse} var:")
data = sommer_ol[-1]["vinnertider"]
for ol in data:
    resultat = data[ol]
    print(f"{ol}: {resultat} sekunder")
    

    