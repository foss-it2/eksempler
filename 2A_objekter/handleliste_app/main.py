class Vare:
    def __init__(self, navn, antall=1, kategori=0) -> None:
        self.navn = navn
        self.antall = antall
        self.plukket = False
        self.kategori = kategori
        self.id = 1
    
    def __str__(self):
        if self.plukket:
            return f"  X  {self.navn}: {self.antall} stk."
        else:
            return f"     {self.navn}: {self.antall} stk."

class FruktOgGrønt(Vare):
    def __init__(self, navn, antall=1, kategori=0, økologisk=False) -> None:
        super().__init__(navn, antall, kategori)
        self.økologisk = økologisk
    
    def __str__(self):
        if self.økologisk:
            return super().__str__() + " Økologisk"
        else:
            return super().__str__()


class Brødvarer(Vare):
    def __init__(self, navn, antall=1, kategori=0, oppskaaret=False) -> None:
        super().__init__(navn, antall, kategori)
        self.oppskaaret = oppskaaret

    def __str__(self):
        if self.oppskaaret:
            return super().__str__() + " Oppskåret"
        else:
            return super().__str__()

"""
2.	vise handlelisten sortert på kategori
3.  markere varer som plukket
"""

class App:
    def __init__(self, navn) -> None:
        self.navn = navn
        self.varer = []
        self.kategorier = {0:"Ingen kategori", 1:"Frukt og grønt", 2: "Brødvarer"}
        self.running = True
    
    def visKategori(self):
        teller = 0
        print("Kategorier")
        print("------------")
        for key in self.kategorier:
            print(f"{teller}. {self.kategorier[key]}")
            teller += 1
    
    def leggTilKategori(self):
        """Fungerer ikke når man bruker klasser. Man kan ikke lage nye klasser mens programmet kjører."""
        kategori = input("Ny kategori: ")
        lengde = len(self.kategorier)
        print(lengde)
        self.kategorier[lengde+1] = kategori  # Legger inn ny kategori med et tall som er neste "indeks" for ordboken
    
    def velgKategori(self):
        return int(input(f"Velg kategori: "))
    
    def leggTilVare(self):
        self.visKategori()
        kategori = self.velgKategori()
        #kategori = 1
        if kategori == 1:
            navn = input("Navn: ")
            antall = int(input("Antall: "))
            øko = int(input("Økologisk (0(nei) eller 1(ja)) "))
            if øko == 1:
                øko = True
            else:
                øko = False
            self.varer.append(FruktOgGrønt(navn, antall, 1, øko))
        elif kategori == 2:
            navn = input("Navn: ")
            antall = int(input("Antall: "))
            valg = input("Oppskåret (0(nei) eller 1(ja)) ")
            if valg == "1":
                oppskaaret = True
            else:
                oppskaaret = False
            self.varer.append(Brødvarer(navn, antall, 2, oppskaaret))
        else:
            navn = input("Navn: ")
            antall = int(input("Antall: "))
            self.varer.append(Vare(navn, antall))
    
    def visHandleliste(self):
        # 1) Går gjennom alle varer og legger dem inn etter kategori i en liste.
            # Med while loop kjører man gjennom og sjekker på kategori inntil teller har blitt like lang som antall varer i handlelisten.
        # 2) Gå gjennom ordboken sortert på kategori og print informasjon.
        # 3) Vi må kunne henvise til et objekt unikt ved hjelp av en ID. Da lager vi en variabel for Vare-klassen.
        teller = 1
        sortert = {}
        for kategori in self.kategorier:    # Looper gjennom nøklene, dvs. 0, 1, 2...
            print(f"Kategori:  {self.kategorier[kategori]}")
            sortert[kategori] = []  # Legger sorterte varer inn i en liste.
            for vare in self.varer:
                if vare.kategori == kategori:
                    sortert[kategori].append(vare)
        for kategori in sortert:
            print(f"{self.kategorier[kategori]}")
            print("---------------------------------")
            liste = sortert[kategori]
            if len(liste) == 0:
                print("Ingen varer")
            for vareobjekt in liste:
                # Setter teller som ID til objektet. Så kan vi henvise til objektet senere ved valg av plukket.
                # ID til hver vare blir oppdatert for hver gang listen vises. Ikke noe som skjer i virkeligheten, men en mulighet i dette programmet.
                # Ved nye varer vil ID for flere objekter bli forskjøvet.
                vareobjekt.id = teller
                print(f"{teller}. {vareobjekt}")
                teller += 1
            print("---------------------------------")



        self.markerPlukket() # Viser alltid mulighet for å marker plukket
    
    def markerPlukket(self):
        valg = int(input("Hvilken vare er plukket (0 for å gå til hovedmeny)? "))
        if 0 < valg <= len(self.varer):
            # Henviser til varens ID for å sette plukket-flagget.
            # Må søke for å finne varen
            for vare in self.varer:
                if vare.id == valg:
                    vare.plukket = True


    def hovedMeny(self):
        print()
        print("--------------------------")
        print("1: Legg til vare")
        print("2: Vis handleliste")
        print("3: Marker plukket")
        print("4: Vis kategorier")
        print("0: Avslutt")
        print("--------------------------")

                


def main():
    navn = input("Navn på handleliste: ")
    app = App(navn)
    app.varer.append(FruktOgGrønt("bananer", 5, 1, 1))
    app.varer.append(FruktOgGrønt("appelsiner", 2, 1, 0))

    while app.running:
        app.hovedMeny()
        valg = int(input("Valg: 0-3 "))
        if valg == 0:
            app.running = False
        elif valg == 1:
            app.leggTilVare()
        elif valg == 2:
            app.visHandleliste()
        elif valg == 3:
            app.markerPlukket()
        elif valg == 4:
            app.visKategori()

# Kjører main hvis dette scriptet kjøres som hovedprogram.
if __name__ == "__main__":
    main()
