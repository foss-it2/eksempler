"""
Interaktiv kalkulator for å beregne varighet av tidsrom.
"""
import datetime as dt

def tidsdifferanse(tidstreng1, tidstreng2):
    """
    Beregner differansen i tid mellom to ulike tidspunkt.
    Tidsformat: ÅÅÅÅ-MM-DD TT:MM:SS
    returnerer differanse som tuple (dager, timer, minutter, sekunder, aar, aar_int)
    """
    tid1 = dt.datetime.fromisoformat(tidstreng1)
    tid2 = dt.datetime.fromisoformat(tidstreng2)
    differanse = tid2 - tid1
    dager = differanse.days
    uker = dager / 7
    aar = dager/365
    aar_int = dager//365
    sekunder = differanse.seconds
    timer = sekunder // 3600
    sekunder -= timer * 3600
    minutter = sekunder // 60
    sekunder -= minutter * 60
    return dager, timer, minutter, sekunder, aar, aar_int, uker

def main():
    tid_fra_bruker = input("Skriv inn et tidspunkt med formatet: ÅÅÅÅ-MM-DD TT:MM \n")

    tid2_fra_bruker = input("Skriv inn et fremtidig tidspunkt med formatet: ÅÅÅÅ-MM-DD TT:MM \n")

    #tid1 = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # tid1 = dt.datetime.fromtimestamp(1e9)
    # tid2 = dt.datetime.fromtimestamp(100e9 + 33333)

    # dager, timer, minutter, sekunder, aar, aar_int = tidsdifferanse(tid1, "2024-05-17")
    dager, timer, minutter, sekunder, aar, aar_int , uker= tidsdifferanse(tid_fra_bruker, tid2_fra_bruker)

    print(f"{aar} år, {aar_int} hele år, {int(uker)} hele uker, {dager} dager, {timer} timer, {minutter} minutter, {sekunder} sekunder.")

if __name__ == "__main__":
    main()