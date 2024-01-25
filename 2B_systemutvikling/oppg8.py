"""
Hvilken dato og hvilket tidspunkt er 2 milliarder sekunder etter 01.01.1970?
"""
import datetime as dt

en_mrd_sek_etter_unixstart = dt.datetime.fromtimestamp(2e9)

print(en_mrd_sek_etter_unixstart) # 18. mai 2033 :)


