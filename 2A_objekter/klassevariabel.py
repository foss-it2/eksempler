class Person:
    personnummer = 1

    def __init__(self, navn) -> None:
        self.navn = navn
        self.personnummer = Person.personnummer # Henter ut øyeblikksverdien til global variabel.
        Person.personnummer += 1 # Øker vi global variabel.

personA = Person("AAA")
personB = Person("BBB")

print(f"PersonA: {personA.navn}, personnummer: {personA.personnummer}")
print(f"PersonB: {personB.navn}, personnummer: {personB.personnummer}")

"""Initier hacking!!! Hahaha!"""
Person.personnummer=1   # Nå får de neste objektene samme verdier som de første.

personC = Person("CCC")
personD = Person("DDD")
print(f"PersonC: {personC.navn}, personnummer: {personC.personnummer}") # Aiaiai! Her har personnummeret blitt det samme som AAA.
print(f"PersonD: {personD.navn}, personnummer: {personD.personnummer}")
    
