"""
Eksperiment med måling av smeltevarme.
"""
from matplotlib import pyplot as plt

# Laster inn datasettet
filnavn = "smeltekurve_isvann.txt"
with open(filnavn, "r") as f:
    datafil = f.readlines()

x = []
y = []
header_lest = False
for p in datafil:
    if header_lest:
        line = p.split("\t")    # Splitter på tabulator
        x_buf = float(line[0])  # x-data er i sekunder...
        if x_buf >= 10000:
            break
        y_buf = float(line[1])
        x.append(x_buf)
        y.append(y_buf)
    else:
        header_lest = True

# plt.plot(x[:4400],y[:4400])
plt.plot(x, y, label="Temperatur")
plt.xlabel("x, tid (s)")
plt.ylabel("y, Temperatur (C)")
plt.grid()
plt.show()
