"""
Skriv en kode som bytter plass på verdiene i lista tall = [3, 4, 1, 2, 5] 
slik at den blir sortert. Du skal altså sortere lista manuelt.
"""

tall = [3, 4, 1, 2, 5] 

# Butter 3 og 1
buffer = tall[0]
tall[0] = tall[2]
tall[2] = buffer

# bytter 4 og 2
buffer = tall[1]
tall[1] = tall[3]
tall[3] = buffer

print(tall)