rader3 = 8
kolonner3 = 8
tabell3 = []

for i in range(rader3):
    rad3 = []
    for j in range(4):
        if i % 2 == 0:
            rad3.append("S")
            rad3.append("H")
            print(i)
            print(rad3)

        else:
            rad3.append("H")
            rad3.append("S")
    tabell3.append(rad3)

for x in tabell3:
    print(x)
