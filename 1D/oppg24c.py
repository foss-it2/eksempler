"""
Lag følgende todimensjonale lister:
a) En 5 x 5-liste fylt med 0-er.
b) En 8 x 8-liste der annenhver verdi er "H" for hvit og "S" for svart (som i et sjakkbrett).
c) En 5 x 5-liste der alle verdier er 0, men verdiene i første og siste rad er 1.
d) En 5 x 5-liste der alle verdier er 0, men verdiene i første og siste kolonne er 1.
e) Skriv ut listene du har laget ovenfor, slik at de vises som tabeller.
"""
# c)
tabell_c = []
for i in range(5):
    rad = []
    for j in range(5):
        if i == 0 or i == 4:
            rad.append(1)
        else:
            rad.append(0)
    tabell_c.append(rad)
for rad in tabell_c:
    print(rad)

