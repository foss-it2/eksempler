from matplotlib import pyplot as plt
import csv

filnavn = "pendel-med-demping.csv"
fil2 = "pendel-uten-demping.csv"
data = []
with open(filnavn, encoding="utf-8") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    for i in range(8):
        overskrifter = next(filinnhold)
    print(overskrifter)
    for rad in filinnhold:
        data.append(rad)

xverdier2 = []
yverdier2 = []
with open(fil2, encoding="utf-8") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    for i in range(8):
        overskrifter = next(filinnhold)
    print(overskrifter)
    for rad in filinnhold:
        xverdier2.append( float(rad[0]) )
        yverdier2.append( float(rad[1]) )

xverdier = []
yverdier = []



for linje in data:
    xverdier.append( float(linje[0]) )
    yverdier.append( float(linje[1]) )

print(len(yverdier))

plt.scatter(xverdier, yverdier, 
            marker="o", 
            color="hotpink",
            s=100, facecolors='none')
plt.plot(xverdier, yverdier,color="darkslateblue")



plt.title(f"{overskrifter[1]} som funksjon av {overskrifter[0]}")
plt.show()