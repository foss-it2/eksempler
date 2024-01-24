import datetime as dt

naa = dt.datetime.now()
print(naa)
print(naa.timestamp())
print(naa.strftime('%d.%m.%Y, Tid: %H:%M:%S.%f'))
