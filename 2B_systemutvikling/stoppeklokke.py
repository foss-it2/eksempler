"""
Terminalprogram for en stoppeklokke ved bruk av datetime-biblioteket.
"""
import datetime as dt
import time

class Stoppeklokke:
    def __init__(self) -> None:
        self.tstart = dt.datetime.now()
        self.tider = []
    
    def haandterEnter(self):
        nyTid = dt.datetime.now()
        self.tider.append(nyTid)

    def skrivUtAlleTider(self):
        for tid in self.tider:
            print(tid)

klokke = Stoppeklokke()

isRunning = True

while isRunning:
    time.sleep(0.1)
    klokke.skrivUtAlleTider()
    temp = input("Trykk ENTER for ny split-tid (0 for å stoppe) ")
    if temp == "0":
        isRunning = False
        print("Stopper!")
    else:
        klokke.haandterEnter()