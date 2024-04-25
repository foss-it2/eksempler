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

# Create a figure object with specified dimensions
fig, ax = plt.subplots(figsize=(10, 8))  # Adjust figure size as needed

# Custom spacing factor
spacing = 2.2
y = np.arange(len(utdanningsprogram)) * spacing # Justerer spacing ytterligere

# Plotting bars for girls
ax.barh(y + 0.4, antallJenter, height=0.8, label="Jenter")
# Plotting bars for boys
ax.barh(y - 0.4, antallGutter, height=0.8, label="Gutter")
# Setting y-axis values
ax.set_yticks(y, utdanningsprogram)
ax.legend()

fig.subplots_adjust(left=0.4)  # Adjust left margin for labels

ax.grid(axis="x")  # Adding grid lines (vertical only)
plt.show()
