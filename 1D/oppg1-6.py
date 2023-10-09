"""
1 Lag lista verdensdeler som inneholder verdensdelenes navn. Skriv ut den første, midterste og siste verdensdelen i lista. Bruk både positive og negative indekser for å skrive ut verdiene.
2 Lag en liste med heltallene fra og med 1 til og med 50. Skriv ut lista for å sjekke at du har fått med de riktige tallene.
3 Lag en liste med de første 100 positive oddetallene. Skriv ut lista for å sjekke at du har fått med de riktige tallene.
4 Lag en liste som inneholder de første 20 kvadrattallene. Kvadrattall er tall opphøyd i annen, for eksempel 22, 32, osv.
5 Lag en liste som inneholder de første 15 kubikktallene. Kubikktall er tall opphøyd i tredje, for eksempel 23, 33, osv.
6 Finn ut hva funksjonene min() , max() og sum() gjør. Bruk dem på lister som du har laget i oppgavene ovenfor (lister med tall).
"""
import math
# Oppg 1
verdensdeler = ["Afrika", "Amerika", "Asia", "Australia", "Europa"]
print(verdensdeler[0])
midt = math.floor(len(verdensdeler)/2)
midt = len(verdensdeler)//2 # Alternativt med heltallsdivisjon som skreller vekk desimalene.
print(verdensdeler[midt])
print(verdensdeler[-1])
print( verdensdeler[ len(verdensdeler)//2 ] )

# Oppg 2
heltall = [i for i in range(1,51)]
print(heltall)

# Oppg 3
oddetall = []
for i in range(1,101):
    if i % 2 != 0:
        oddetall.append(i)
print(oddetall)

# Oppg 4
kvadrattall = [i**2 for i in range(1,21)]
print(kvadrattall)

# Oppg 5
kubikktall = [i**3 for i in range(1,15)]
print(kubikktall)

# Oppg 6
print(min(oddetall))
print(max(oddetall))
print(sum(oddetall))
