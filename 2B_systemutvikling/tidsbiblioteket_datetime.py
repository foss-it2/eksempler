import datetime as dt

naa = dt.datetime.now() # Lager et datetime-objekt ved hjelp av datetime-biblioteket.
print(f"Lokal tid: {naa.time()}")
print(f"Typen til naa-objektet: {type(naa)}") # datetime-objekt

england_tid = dt.datetime.utcnow()
print(f"England-tid: {england_tid.time()}")

# Utskrifter med string-format-time metoden. 
# Se her for alle koder: https://www.w3schools.com/python/gloss_python_date_format_codes.asp
print(f"Ukedag nummer: {naa.isoweekday()}")
print(f"Dato: {naa.strftime('%d %m %Y %H : %M : %S')}")
print(f"Dato: {naa.strftime('%d.%m.%Y, Tid: %H:%M:%S')}")

# Manuelt tidsobjekt
fremtidig_dag = dt.datetime(2024,2,17,10,0,0)
print(f"Fremtidig dag: {fremtidig_dag.strftime('%d.%m.%Y, Tid: %H:%M:%S')}")
print(f"Fremtidig dag i antall sekunder siden 1. jan 1970: {fremtidig_dag.timestamp()}")
en_annen_dag = dt.datetime.fromtimestamp(1649329200) # Må gi antall sekunder siden 1. jan 1970.
print(f"En annen dag: {en_annen_dag}")

# Tidsdifferanse
differanse = fremtidig_dag - naa
print(f"Typen til differanse: {type(differanse)}")  # timedelta-objekt
print(f"Differanse automatisk utskrift: {differanse}")
total_tid = differanse.days*24*3600 + differanse.seconds
print(f"Differanse i antall sekunder: {total_tid}")


