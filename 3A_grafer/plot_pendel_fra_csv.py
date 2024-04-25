from matplotlib import pyplot as plt
import csv

filnavn = "pendel-med-demping.csv"
xverdier = []
yverdier = []
with open(filnavn, encoding="utf-8") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    for i in range(8):
        overskrifter = next(filinnhold)
    print(overskrifter)
    for rad in filinnhold:
        # 1) Lese ut x-verdi
        xverdier.append(float(rad[0]))
        # 2) Lese ut y-verdi
        yverdier.append(float(rad[1]))

# 3) Plotte scatter og linje med fancy farger etc.
plt.scatter(xverdier, yverdier, marker="o", color="hotpink",
            facecolors="none", s=500, zorder=2,edgecolors="goldenrod")
plt.plot(xverdier, yverdier, zorder=1)
plt.show()