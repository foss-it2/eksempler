import matplotlib.pyplot as plt
import numpy as np

utdanningsprogram = [
    "Bygg- og anleggsteknikk",
    "Elektro og datateknologi",
    "Helse- og oppvekstfag",
    "Naturbruk",
    "Restaurant- og matfag",
    "Teknologi- og industrifag",
    "Håndverk, design og produktutvikling",
    "Frisør, blomster, interiør og eksponeringsdesign",
    "Informasjonsteknologi og medieproduksjon",
    "Salg, service og reiseliv"
]

antallGutter = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]
antallJenter = [352, 268, 7286, 1028, 709, 851, 243, 826, 200, 895]

# Angir dimensjoner for figure-objektet
fig, ax = plt.subplots(figsize=(10, 5))

y = np.arange(10) * 2   # Justerer mellomrom med faktoren etter array-konstrueringen.

# Lager stolpediagram jenter
ax.barh(y+0.2, antallJenter, height=0.4, label="Jenter")
# Lager stolpediagram gutter
ax.barh(y-0.2, antallGutter, height=0.4, label="Gutter")
# Legger til akseverdier
ax.set_yticks(y, utdanningsprogram)
ax.legend()                                               # Legger til beskrivelse

fig.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet

ax.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
plt.show()         # Viser diagrammet
