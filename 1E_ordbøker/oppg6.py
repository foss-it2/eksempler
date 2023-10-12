"""
"""

sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]

for ol in sommer_ol:
  aar = ol["årstall"]
  vinnertid_100m = ol["vinnertider"]["100 m"]
  vinnertid_200m = ol["vinnertider"]["200 m"]
  print(f"I {aar} var vinnertiden på 200 m: {vinnertid_200m}.")