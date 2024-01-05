"""
Menysystem for teminalapp
"""


def vis_hovedmeny():
    print("1. Utfør handling 1")
    print("2. Utfør handling 2")
    print("3. Utfør handling 3")
    print("4. Avslutt")


def utfør_handling_1():
    print("Du har valgt handling 1. Gjør noe her.")


def utfør_handling_2():
    print("Du har valgt handling 2. Gjør noe annet her.")


def utfør_handling_3():
    print("Du har valgt handling 3. Gjør noe helt annet her.")


while True:
    vis_hovedmeny()

    valg = input("Velg et menyvalg (1-4): ")

    if valg == "1":
        utfør_handling_1()
    elif valg == "2":
        utfør_handling_2()
    elif valg == "3":
        utfør_handling_3()
    elif valg == "4":
        print("Programmet avsluttes.")
        break
    else:
        print("Ugyldig valg. Prøv igjen.")
