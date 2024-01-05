"""
Menysystem for teminalapp
"""


def vis_hovedmeny():
    print("")   # Tom linje i starten
    print("------------------------------------------")
    print("1. Utfør handling 1")
    print("2. Utfør handling 2")
    print("3. Utfør handling 3")
    print("0. Avslutt")


def funksjon1():
    print("Du har valgt handling 1. Gjør noe her.")


def funksjon2():
    print("Du har valgt handling 2. Gjør noe annet her.")


def funksjon3():
    print("Du har valgt handling 3. Gjør noe helt annet her.")


while True:
    vis_hovedmeny()

    valg = input("Velg et menyvalg (1-4): ")

    if valg == "1":
        funksjon1()
    elif valg == "2":
        funksjon2()
    elif valg == "3":
        funksjon3()
    elif valg == "0":
        print("Programmet avsluttes.")
        break
    else:
        print("Ugyldig valg. Prøv igjen.")
