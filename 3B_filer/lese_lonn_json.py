import json
import matplotlib.pyplot as plt
 
filnavn = "lonnstabell.json"
 
with open(filnavn, encoding="utf-8") as f:
  data = json.load(f)
 
arstall = data['dataset']['dimension']['Tid']['category']['label']
kvinnelonn = data['dataset']['value'][6:12]
mannlonn = data['dataset']['value'][0:6]
alle_arstall = [int(x) for x in arstall]
print(kvinnelonn)
print(mannlonn)
print(alle_arstall)
plt.figure(figsize=(8, 6))
 
# Linjegraf
plt.plot(alle_arstall, kvinnelonn, label="Kvinner")
plt.plot(alle_arstall, mannlonn, label="Menn")
 
plt.xlabel("Årstall")
plt.ylabel("Gjennomsnittlig månedslønn (kr)")
plt.title("Utvikling av månedslønn for kvinner og menn")
 
plt.legend()
plt.show()
 
plt.figure(figsize=(8, 6))
 
# Gruppert stolpediagram
bar_width = 0.35
index = range(len(arstall))
 
plt.bar(index, kvinnelonn, bar_width, label="Kvinner")
plt.bar([i + bar_width for i in index], mannlonn, bar_width, label="Menn")
 
plt.xlabel("Årstall")
plt.ylabel("Gjennomsnittlig månedslønn (kr)")
plt.title("Lønnsutvikling for kvinner og menn")
 
plt.xticks([i + bar_width / 2 for i in index], arstall)
plt.legend()
plt.show()