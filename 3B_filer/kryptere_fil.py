"""
Krypterer en fil med Caesar-kryptering.
"""

from caesar_cipher import caesar_cipher_encrypt

filnavn = "MikkelRev.txt"
kryptert_filnavn = filnavn + "_kryptert.txt"

# Kan lese inn hele filen og håndtere den som tekst.
with open(filnavn, encoding="utf-8") as fil:
  innhold = fil.read()

kryptert = caesar_cipher_encrypt(innhold,7)

with open(kryptert_filnavn, "w") as fil:
  fil.write(kryptert)
