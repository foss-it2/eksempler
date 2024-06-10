import requests
import json
from datetime import datetime


def tidsObjektFraString(tidsstreng):
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    return datetime.strptime(tidsstreng, date_format)


# result = requests.get('http://mauroy.no/temperatur/getData_json.php', timeout=5)
url = 'http://api.met.no/weatherapi/locationforecast/2.0/compact.json?lat=-37.866069&lon=144.973337'
# Må lure APIet til å tro det er en nettleser som kontakter den.
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers, timeout=5)
print(f"status code: {result.status_code}")
#print(result.text)


data = json.loads(result.text)

pretty_data = json.dumps(data,ensure_ascii=False,indent=4)



# Lagrer data for å ikke kalle på API hele tiden mens man utvikler. Da kan man bli sperret.
#with open("vaerdata.json","w") as fil:
 #   fil.write(pretty_data)

print(pretty_data[:2000])



"""
# Åpner filen vi har lastet ned data til.
with open("vaerdata.json", "r") as fil:
    data_json = fil.read()

print(data_json[:1000])

data = json.loads(data_json)
"""

# Henter ut tiden på dette formatet: 2024-06-10T09:25:25Z
last_update = data["properties"]["meta"]["updated_at"]
print(last_update)
# Må fortelle datetime hva slags format tiden ligger på
date_format = '%Y-%m-%dT%H:%M:%SZ'
last_update = tidsObjektFraString(last_update)
print(f"{last_update.day}/{last_update.month}-{last_update.year}")

data_varsel = data["properties"]["timeseries"]

print(type(data_varsel))

time_now = datetime.now()
# Leter i værvarselet for tiden som er nærmest tiden akkurat nå. Ser på antall dager og sekunder i tidsdifferanse.
# Plukker deretter ut det værvarselet.

neste_time = {}
neste_tid = None

for linje in data_varsel:
    #print(linje)
    tid_str = linje["time"]
    tid = tidsObjektFraString(tid_str)
    tidsdiff = tid - time_now
    if tidsdiff.days == 0 and tidsdiff.seconds < 3600:
        print(tid)
        neste_time = linje
        neste_tid = tid
varsel = neste_time["data"]["instant"]["details"]
trykk = varsel["air_pressure_at_sea_level"]
temperatur = varsel["air_temperature"]
skydekke = varsel["cloud_area_fraction"]
luftfuktighet = varsel["relative_humidity"]
vindretning = varsel["wind_from_direction"]
vind = varsel["wind_speed"]

print(f"Værvarsel kl. {neste_tid.strftime('%H:%M')} (oppdatert kl. {last_update.strftime('%H:%M')}):")
print(f"{temperatur}C, {trykk}hPa, {vind}m/s fra {vindretning}grader. Relativ luftfuktighet {luftfuktighet}%")






