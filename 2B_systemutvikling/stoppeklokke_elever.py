"""
Stoppeklokke laget foran elever.
"""

import datetime as dt
import time

class Stoppeklokke:
    def __init__(self) -> None:
        # Lager starttid som datetime-objekt senere ved start av klokken
        self.starttid = None
        self.splittider = [] # lagring av tidspunktene
        self.isrunning = False
    
    def utskrift(self):
        for tid in self.splittider:
            print(tid)
    
    def startKlokke(self):
        self.isrunning = True
        # Sett starttid!
        self.starttid = dt.datetime.now()

    def splitTid(self):
        # Lage tidsobjekt
        split = dt.datetime.now() - self.starttid
        # Legg timedelta-objektet til listen.
        self.splittider.append(split)

klokke = Stoppeklokke()

temp = input("Trykk ENTER for å starte >>> ")
klokke.isrunning = True
# starte klokke
klokke.startKlokke()

while klokke.isrunning:
    # Input bruker
    temp = input("Trykk ENTER for ny tid (Stopp med Ctrl-C) >>> ")
    # lage splittid
    klokke.splitTid()
    # skrive ut
    klokke.utskrift()
    time.sleep(0.250) # Pause på 250 ms for at ikke ENTER-tast skal lage mange tider av gangen.
