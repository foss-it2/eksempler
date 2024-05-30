"""
Innlesing av datafil er utarbeidet i samarbeid med lærer
på forberedelsesdagen.
Logikk for innlesing kan ha innhold fra eksempler fra lærer.
"""
import json
import matplotlib.pyplot as plt
import numpy as np


filnavn = "05994_20240126-145813-json.json"

# Les hele filen linje for linje
with open(filnavn, 'r', encoding="utf-8") as file:
    lines = file.readlines()

# Slå sammen linjene fra og med linje 3.
json_data = ''.join(lines[2:])
data = json.loads(json_data)
    

# Hva slags datatype er data?
print(type(data))
# 1) Legge sammen total tid for kvinner for Nattesøvn, Måltider, Sosialt samvær
totaltid_noen_behov_k = {"timer": 0, "minutter": 0}
aktiviteter_alle = []
aktiviteter_kvinner = []
aktiviteter_menn = []
for objekt in data:
    if objekt["alle aktiviteter"] == "� Nattesøvn":
        if objekt["kjønn"] == "Kvinner":
            tid = str(objekt["Tidsbruk 2000 I alt"])
            timer = int(tid[0])
            minutter = int(tid[2:]) # minutter parses til minutter
            print(timer,minutter)
            totaltid_noen_behov_k["timer"] += timer
            totaltid_noen_behov_k["minutter"] += minutter
    if objekt["alle aktiviteter"] == "� Måltider":
        if objekt["kjønn"] == "Kvinner":
            tid = str(objekt["Tidsbruk 2000 I alt"])
            timer = int(tid[0])
            minutter = int(tid[2:]) # minutter parses til minutter
            print(timer,minutter)
            totaltid_noen_behov_k["timer"] += timer
            totaltid_noen_behov_k["minutter"] += minutter
    if objekt["alle aktiviteter"] == "� Sosialt samvær":
        if objekt["kjønn"] == "Kvinner":
            tid = str(objekt["Tidsbruk 2000 I alt"])
            timer = int(tid[0])
            minutter = int(tid[2:]) # minutter parses til minutter
            print(timer,minutter)
            totaltid_noen_behov_k["timer"] += timer
            totaltid_noen_behov_k["minutter"] += minutter

    # Lager statistikk over total tid per aktivitet
    akt = objekt["alle aktiviteter"]
    tid = str(objekt["Tidsbruk 2000 I alt"])
    if "." in tid:
        tid_liste = tid.split(".")
        timer_sek = int(tid_liste[0])*3600
        minutter_sek = int(tid_liste[1])*60
    else:
        timer_sek = int(tid)
        minutter_sek = 0
       
    totaltid = timer_sek + minutter_sek
    if objekt["kjønn"] == "Alle":
        aktiviteter_alle.append([totaltid,akt]) # liste der tid forekommer først så enkelt å sortere.
    if objekt["kjønn"] == "Kvinner":
        aktiviteter_kvinner.append([totaltid,akt]) # liste der tid forekommer først så enkelt å sortere.
    if objekt["kjønn"] == "Menn":
        aktiviteter_menn.append([totaltid,akt]) # liste der tid forekommer først så enkelt å sortere.

aktiviteter_alle.sort()
aktiviteter_kvinner.sort()
aktiviteter_menn.sort()
print("alle",aktiviteter_alle[-3:]) 
print("kvinner",aktiviteter_kvinner[-3:]) 
print("menn",aktiviteter_menn[-3:])


print(f"Total tid for søvn, måltider og sosialt samvær: {totaltid_noen_behov_k}")

# Konstruerer dataformat for plotting
aktivetet_labels = []
antall_kvinner = []
antall_menn = []
# Kvinner:
for aktivitet in aktiviteter_kvinner:
    aktivetet_labels.append(aktivitet[1])
    antall_kvinner.append(aktivitet[0])
# Menn:
for aktivitet in aktiviteter_menn:
    antall_menn.append(aktivitet[0])

# Plottingen er hentet fra læreboka Aunivers

# Create a figure object with specified dimensions
fig, ax = plt.subplots(figsize=(10, 8))  # Adjust figure size as needed

# Custom spacing factor
spacing = 2.2
y = np.arange(len(aktivetet_labels)) * spacing  # Justerer spacing ytterligere

# Plotting bars for girls
ax.barh(y + 0.4, antall_kvinner, height=0.8, label="Kvinner")
# Plotting bars for boys
ax.barh(y - 0.4, antall_menn, height=0.8, label="Menn")
# Setting y-axis values
ax.set_yticks(y, aktivetet_labels)
ax.legend()

fig.subplots_adjust(left=0.4)  # Adjust left margin for labels

ax.grid(axis="x")  # Adding grid lines (vertical only)
plt.show()
