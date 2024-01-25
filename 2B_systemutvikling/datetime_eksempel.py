import datetime as dt

naa = dt.datetime(2024,1,25,12,22,10)

print(naa)

nytt_tidspunkt = dt.datetime.now()

print(nytt_tidspunkt)
print(f"Typen til objektet: {type(nytt_tidspunkt)}")
integer = 1
print(f"type til integer: {type(integer)}")

england_tid = dt.datetime.utcnow() # Får england tid
print(f"England tid: {england_tid}")

fremtidig_tid = dt.datetime(2050,1,1,10,0,0) # Skriver inn dato manuelt
fremtidig_tid2 = dt.datetime.fromtimestamp(100000000) # Skriver inn antall sekunder siden 1.jan 1970.
print(f"fremtidig 1: {fremtidig_tid}")
print(f"femtidig 1: Dag: {fremtidig_tid.day}, måned: {fremtidig_tid.month}, år: {fremtidig_tid.year}.")
print(f"fremtidig 2: {fremtidig_tid2}")


intervall = nytt_tidspunkt - fremtidig_tid2
print(f"Typen til intervall (differanse) {type(intervall)}") # timedelta-objekt
print(f"intervallet er: {intervall}")

intervall2 = dt.datetime.now() - dt.datetime(2023,12,24,16,30)
print(f"typen til intervall2: {type(intervall2)}") # timedelta-objekt
print(f"intervall2: {intervall2}")
print(f"Intervall2: dager: {intervall2.days}, timer: {intervall2.seconds}")
antall_timer = intervall2.seconds // (60*60)
print(f"antall timer: {antall_timer}")

# Utskrift av string-formatted-time
# All info om datetime her: https://www.w3schools.com/python/python_datetime.asp
naa2 = dt.datetime.now()
print(naa2.strftime("%d %m %Y %H %M %S"))
print(naa2.strftime("%d.%m.%Y %H:%M:%S og mange mikrosekunder"))
