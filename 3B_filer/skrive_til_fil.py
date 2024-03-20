filnavn = "hello.txt"

tekst = "Hello world!"

with open(filnavn, "w") as fil:
  fil.write(tekst)


# Legger til tekst i slutten av en tekstfil.
with open(filnavn, "a") as fil:
  fil.write("\n")   # Linjeskift settes inn før tekst legges til.
  fil.write("Ny linje med tekst settes inn.")

# Legger inn 1000,000 tall (Ikke gjør dette hjemme...)
  # Legger til tekst i slutten av en tekstfil.
with open(filnavn, "a") as fil:
  for i in range(1,1000001):
        fil.write("\n")   # Linjeskift settes inn før tekst legges til.
        fil.write(str(i))

