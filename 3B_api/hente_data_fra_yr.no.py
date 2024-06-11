"""
Enkelt program som henter værvarsel fra yr.no sitt API.
Vindretninger leses slik med klokka fra Nord som er "kl. 12":
0° — north wind (N)
22.5° — north-northeast wind (NNE)
45° — northeast wind (NE)
67.5° — east-northeast wind (ENE)
90°— east wind (E)
112.5° — east-southeast wind (ESE)
135° — southeast wind (SE)
157.5° — south-southeast wind (SSE)
180° — south wind (S)
202.5° — south-southwest wind (SSW)
225° — southwest wind (SW)
247.5° — west-southwest wind (WSW)
270° — west wind (W)
292.5° — west-northwest wind (WNW)
315° — northwest wind (NW)
337.5° — north-northwest wind (NNW)
360° — north wind (N)


"""


import requests
import json
from datetime import datetime, timedelta



def tidsObjektFraString(tidsstreng):
    """
    Lager et tidsobjekt med tiden formattert på ISO 8601 standarden.
    T indikerer tids-delen
    Z indikerer at tiden er på UTC-format. Dvs. tiden for tidssone 0.
    """
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    return datetime.strptime(tidsstreng, date_format)


# result = requests.get('http://mauroy.no/temperatur/getData_json.php', timeout=5)
url = 'http://api.met.no/weatherapi/locationforecast/2.0/compact.json?lat=59.942&lon=10.720'
# Må lure APIet til å tro det er en nettleser som kontakter den.
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers, timeout=5)
print(f"status code: {result.status_code}")
print(result.headers)
#for key,value in result.headers.items():
#    print(key,value)

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
last_update = last_update + timedelta(hours=1)  # Justerer én time frem pga UTC.
print(f"{last_update.day}/{last_update.month}-{last_update.year}")

data_varsel = data["properties"]["timeseries"]

#print(type(data_varsel))

time_now = datetime.now()
# Leter i værvarselet for tiden som er nærmest tiden akkurat nå + 1 time. Ser på antall dager og sekunder i tidsdifferanse.
# Plukker deretter ut det værvarselet.

neste_time = {}
neste_tid = None

for linje in data_varsel:
    #print(linje)
    tid_str = linje["time"]
    tid = tidsObjektFraString(tid_str)
    # Tiden vi leter etter ligger én time frem pga UTC-tid (Må egentlig passe på sommer/vintertid også).
    tid = tid + timedelta(hours=1)
    tidsdiff = tid - time_now
    if tidsdiff.days == 0 and tidsdiff.seconds < 3600:
        neste_time = linje
        neste_tid = tid
        break
varsel = neste_time["data"]["instant"]["details"]
trykk = varsel["air_pressure_at_sea_level"]
temperatur = varsel["air_temperature"]
skydekke = varsel["cloud_area_fraction"]
luftfuktighet = varsel["relative_humidity"]
vindretning = varsel["wind_from_direction"]
vind = varsel["wind_speed"]

print(f"Værvarsel kl. {neste_tid.strftime('%H:%M')} (oppdatert kl. {last_update.strftime('%H:%M')}):")
print(f"{temperatur}C, {trykk}hPa, {vind}m/s fra {vindretning}grader. Relativ luftfuktighet {luftfuktighet}%")






