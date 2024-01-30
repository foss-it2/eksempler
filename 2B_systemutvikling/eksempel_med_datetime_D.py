"""
Lek md datetime-biblioteket
"""
import datetime

# 1) now()
naa = datetime.datetime.now() # Lager et tidsobjekt med biblioteket datetime sin klasse datetime og metoden now() som gir
# dato og tid fra pcns klokke.
print(naa)  # bruker __str__() metoden som er innegygget i datetime.datetime: Utskrift i ISO 8601 standarden.
# ÅÅÅÅ-MM-DD HH:MM:SS.mikrosekunder

# 2) fromTimeStamp()
fremtidig_tid = datetime.datetime.fromtimestamp(1.8e9) # tidspunkt i sekunder etter 1. jan 1970

# 3) utskrift formattert
print(naa.strftime("%Y %d"))    # Skriver ut ved av metoden strftime().
print(fremtidig_tid.strftime("%Y %d"))    # Skriver ut ved av metoden strftime().

# 4) tidsintervall mellom to datetime-objekter
intervall = fremtidig_tid - naa # lager et "datetime.timedelta"-objekt.
print(intervall)
print(f"datatypen til intervallet: {type(intervall)}")
print(f"datatypen til naa: {type(naa)}")
print(f"intervall: {intervall.days} dager og {intervall.seconds} sekunder.") # Henter ut attributtene days og seconds. 
# hours og minutes finnes ikke.

# 5) fromisoformat()
min_fødselsdato = datetime.datetime.fromisoformat("1983-05-17 01:37") # Lager tidsobjekt med tidsformatet ISO 8601.
print(f"Henrik ble født: {min_fødselsdato}")


