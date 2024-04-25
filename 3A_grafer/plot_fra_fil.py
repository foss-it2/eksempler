from matplotlib import pyplot as plt
import csv

filnavn = "data.csv"
data = []
with open(filnavn, encoding="utf-8") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    print(overskrifter)
    for rad in filinnhold:
        data.append(rad)

xverdier = []
yverdier = []

for linje in data:
    xverdier.append( float(linje[0]) )
    yverdier.append( float(linje[1]) )

print(xverdier)
print(yverdier)
plt.scatter(xverdier, yverdier, marker="p", color="hotpink", s=10000)
plt.plot(xverdier, yverdier,color="darkslateblue")
plt.show()