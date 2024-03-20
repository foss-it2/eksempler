filnavn = "MikkelRev.txt"
#filnavn = "bibelen_king_james.txt"

with open(filnavn, encoding="utf-8") as fil:
  innhold = fil.read()

print(innhold)
print("********************")
print(f"lengden av innhold {len(innhold)}")
print(f"typen til innhold {type(innhold)}")
