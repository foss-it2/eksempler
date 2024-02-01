"""
Interaktiv kalkulator for å beregne varighet av tidsrom.
"""
import datetime as dt

tid_fra_bruker = input("Skriv inn et fremtidig tidspunkt med formatet: ÅÅÅÅ-MM-DD TT:MM \n")
tid2 = dt.datetime.fromisoformat(tid_fra_bruker)
print(tid2)

tid1 = dt.datetime.now()

# tid1 = dt.datetime.fromtimestamp(1e9)
# tid2 = dt.datetime.fromtimestamp(100e9 + 33333)

differanse = tid2 - tid1
print(differanse)

dager = differanse.days
sekunder = differanse.seconds
print(sekunder)
timer = sekunder // 3600
sekunder -= timer * 3600
minutter = sekunder // 60
sekunder -= minutter * 60

print(f"{dager} dager, {timer} timer, {minutter} minutter, {sekunder} sekunder.")
