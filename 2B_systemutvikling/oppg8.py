"""
Hvilken dato og hvilket tidspunkt er 1 milliard sekunder etter 01.01.1970?
"""
import datetime as dt

en_mrd_sek_etter_unixstart = dt.datetime.fromtimestamp(1e9)

print(en_mrd_sek_etter_unixstart)
