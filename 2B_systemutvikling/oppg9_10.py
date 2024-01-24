import datetime as dt


class Tidspunkt:
    """
    Klasse for å lage tidspunkt-objekter.

    Parametre:
        tidsstempel = dt.datetime.now().timestamp() (int): tidspunktets tidsstempel
    """

    def __init__(self, tidsstempel=dt.datetime.now().timestamp()):
        """Konstruktør"""
        self.datotid = dt.datetime.fromtimestamp(tidsstempel)

    def tidsstempel(self):
        """Gir hele tidsstemplet"""
        return self.datotid

    def dato(self):
        """Gir dato på formen dd.mm.yyyy"""
        return self.datotid.strftime("%d.%m.%Y")

    def dag(self):
        """Gir datoens dag (01-31)"""
        return self.datotid.strftime("%d")

    def maaned(self):
        """Gir månedens fulle navn (på norsk)"""
        maaneder = ["Januar","Februar","Mars","April","Mai","Juni","Juli","August","September","Oktober","November","Desember"]
        maaned = self.datotid.month
        return maaneder[maaned - 1]

    def aar(self):
        """Gir årstall med fire siffer"""
        return self.datotid.strftime("%Y")
    
    def tid(self):
        """Gir tiden som HH:MM:SS"""
        return self.datotid.strftime("%H:%M:%S")


def main():
    naa = Tidspunkt()


    print(naa.dato())
    print(naa.maaned())
    print(naa.tid())
    print(f"{naa.dato()} er i måned {naa.maaned()} = {naa.tidsstempel()}")

    tidligere = Tidspunkt(1649329200)
    print(tidligere.dato())
    print(f"{tidligere.dato()} er i måned {tidligere.maaned()} = {tidligere.tidsstempel()}")

if __name__ == "__main__":
    main()
