"""
Krypterer en fil med Caesar-kryptering.
"""

from caesar_cipher import caesar_cipher_decrypt

filnavn = "MikkelRev.txt_kryptert.txt"
dekryptert_filnavn = filnavn + "_dekryptert.txt"

# Kan lese inn hele filen og håndtere den som tekst.
with open(filnavn, encoding="utf-8") as fil:
  innhold = fil.read()

kryptert = caesar_cipher_decrypt(innhold,7)

with open(dekryptert_filnavn, "w") as fil:
  fil.write(kryptert)
