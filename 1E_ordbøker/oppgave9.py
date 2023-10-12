"""
Skriv ut den dårligste og den beste vinnertiden på 200 m.
"""

sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]

# Lagrer min og maks tider samt korresponderende år.
maks = 0 
min = 1e30
maksaar = 0
minaar = 0

for ol in sommer_ol:
    aar = ol["årstall"]
    if ol["vinnertider"]["200 m"] < min:
        min = ol["vinnertider"]["200 m"]
        minaar = ol["årstall"]
    if ol["vinnertider"]["200 m"] > maks:
        maks = ol["vinnertider"]["200 m"]
        maksaar = ol["årstall"]
  
print(f"Den dårligste vinnertiden i 200 m var på {maks} i år {maksaar}. Den beste tiden var på {min} i år {minaar}.")