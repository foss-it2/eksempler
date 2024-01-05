class Konto:
    def __init__(self, konto_nr, eier, saldo=0):
        self.konto_nr = konto_nr
        self.eier = eier
        self.saldo = saldo
        self.transaksjoner = []

    def vis_saldo(self):
        print(f"Saldo på konto {self.konto_nr}: {self.saldo} kr")

    def gjennomfør_transaksjon(self, beløp, transaksjonstype):
        self.saldo += beløp if transaksjonstype == "innskudd" else -beløp
        transaksjon = f"{transaksjonstype.capitalize()}: {beløp} kr"
        self.transaksjoner.append(transaksjon)
        print(f"Transaksjon gjennomført: {transaksjon}")
        self.vis_saldo()


class Sparekonto(Konto):
    def __init__(self, konto_nr, eier, saldo=0, rente=0.02):
        super().__init__(konto_nr, eier, saldo)
        self.rente = rente

    def beregn_renter(self):
        rente_beløp = self.saldo * self.rente
        self.gjennomfør_transaksjon(rente_beløp, "rente")


class Brukskonto(Konto):
    def __init__(self, konto_nr, eier, saldo=0, kredittgrense=1000):
        super().__init__(konto_nr, eier, saldo)
        self.kredittgrense = kredittgrense

    def vis_kredittgrense(self):
        print(
            f"Kredittgrense på konto {self.konto_nr}: {self.kredittgrense} kr")

    def gjennomfør_transaksjon(self, beløp, transaksjonstype):
        if transaksjonstype == "uttak" and beløp > self.saldo + self.kredittgrense:
            print(
                "Transaksjon avvist: Ikke nok penger og overskridelse av kredittgrense.")
        else:
            super().gjennomfør_transaksjon(beløp, transaksjonstype)


def hovedmeny():
    print("1. Opprett konto")
    print("2. Overfør penger")
    print("3. Vis transaksjonshistorikk")
    print("4. Vis saldo")
    print("5. Beregn renter (for sparekonto)")
    print("6. Vis kredittgrense (for brukskonto)")
    print("0. Avslutt")


bankkontoer = {}


while True:
    hovedmeny()
    valg = input("Velg menyvalg (0-6): ")

    if valg == "0":
        print("Programmet avsluttes.")
        break

    elif valg == "1":
        navn = input("Skriv inn navnet ditt: ")
        konto_type = input(
            "Velg konto-type (S for sparekonto, B for brukskonto): ").upper()

        if konto_type == "S":
            rente = float(input(
                "Skriv inn rentesatsen for sparekontoen (for eksempel 0.02 for 2% rente): "))
            ny_konto = Sparekonto(len(bankkontoer) + 1, navn, rente=rente)
        elif konto_type == "B":
            kredittgrense = float(
                input("Skriv inn kredittgrensen for brukskontoen: "))
            ny_konto = Brukskonto(len(bankkontoer) + 1,
                                  navn, kredittgrense=kredittgrense)
        else:
            print("Ugyldig konto-type. Konto ikke opprettet.")
            continue

        bankkontoer[ny_konto.konto_nr] = ny_konto
        print(f"Konto {ny_konto.konto_nr} opprettet for {ny_konto.eier}.")

    elif valg == "2":
        fra_konto = int(
            input("Skriv inn konto-nummeret du vil overføre fra: "))
        til_konto = int(
            input("Skriv inn konto-nummeret du vil overføre til: "))
        beløp = float(input("Skriv inn beløpet du vil overføre: "))

        if fra_konto in bankkontoer and til_konto in bankkontoer:
            bankkontoer[fra_konto].gjennomfør_transaksjon(beløp, "uttak")
            bankkontoer[til_konto].gjennomfør_transaksjon(beløp, "innskudd")
        else:
            print("Ugyldige konto-numre. Transaksjon ikke gjennomført.")

    elif valg == "3":
        konto_nr = int(
            input("Skriv inn konto-nummeret du vil se transaksjonshistorikk for: "))
        if konto_nr in bankkontoer:
            print(f"Transaksjonshistorikk for konto {konto_nr}:")
            for transaksjon in bankkontoer[konto_nr].transaksjoner:
                print(transaksjon)
        else:
            print("Ugyldig konto-nummer.")

    elif valg == "4":
        konto_nr = int(input("Skriv inn konto-nummeret du vil se saldo for: "))
        if konto_nr in bankkontoer:
            bankkontoer[konto_nr].vis_saldo()
        else:
            print("Ugyldig konto-nummer.")

    elif valg == "5":
        konto_nr = int(
            input("Skriv inn konto-nummeret du vil beregne renter for: "))
        if konto_nr in bankkontoer and isinstance(bankkontoer[konto_nr], Sparekonto):
            bankkontoer[konto_nr].beregn_renter()
        else:
            print("Ugyldig konto-nummer eller konto er ikke en sparekonto.")

    elif valg == "6":
        konto_nr = int(
            input("Skriv inn konto-nummeret du vil se kredittgrense for: "))
        if konto_nr in bankkontoer and isinstance(bankkontoer[konto_nr], Brukskonto):
            bankkontoer[konto_nr].vis_kredittgrense()
        else:
            print("Ugyldig konto-nummer eller konto er ikke en brukskonto.")
