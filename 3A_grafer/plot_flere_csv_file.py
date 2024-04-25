from matplotlib import pyplot as plt
import csv

filnavn = "pendel-med-demping.csv"

def les_csv(filnavn,n_overskrifter):
    xverdier = []
    yverdier = []
    with open(filnavn, encoding="utf-8") as fil:
        filinnhold = csv.reader(fil, delimiter=";")

        for i in range(n_overskrifter):
            overskrifter = next(filinnhold)
        for rad in filinnhold:
            # 1) Lese ut x-verdi
            xverdier.append(float(rad[0]))
            # 2) Lese ut y-verdi
            yverdier.append(float(rad[1]))

    return overskrifter,xverdier,yverdier

# Datasett 1
overskrift1, xverdier1, yverdier1 = les_csv("pendel-med-demping.csv",8)
overskrift2, xverdier2, yverdier2 = les_csv("pendel-uten-demping.csv",8)

# 3) Plotte scatter og linje med fancy farger etc.
plt.scatter(xverdier1, yverdier1, marker="o", color="hotpink",
            facecolors="goldenrod", s=500, zorder=1,edgecolors="black")
plt.plot(xverdier1, yverdier1, zorder=1, color="goldenrod")
plt.scatter(xverdier2, yverdier2, marker="o", color="hotpink",
            facecolors="hotpink", s=500, zorder=2, edgecolors="darkslategray")
plt.plot(xverdier2, yverdier2, zorder=2, color="darkslategray")
plt.show()