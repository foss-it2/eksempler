"""
Caesar-kryptering.
Flytt bokstaver noen hakk lenger bort i alfabetet.
"""

def caesar_cipher_encrypt(text, key):
    norwegian_alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'
    shifted_alphabet = norwegian_alphabet[key:] + norwegian_alphabet[:key]
    str1 = "hijklmnopqrstuvwxyzæøå" + "abcdefg"
    print(norwegian_alphabet[-7:])
    print(norwegian_alphabet[:-7])

    encrypted_text = ''
    for char in text:
        c = char.lower()
        if c in norwegian_alphabet:
            index = norwegian_alphabet.index(c) # Plukker ut indeksen til bokstaven
            encrypted_text += shifted_alphabet[index]
        else:
            encrypted_text += c
    return encrypted_text


def caesar_cipher_decrypt(text, key):
    return caesar_cipher_encrypt(text, -key)    # Dekryptering gjøres ved å kryptere med negativ nøkkel.


# Testing
original_text = "hei, verden! æøå"
key = 7

encrypted_text = caesar_cipher_encrypt(original_text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_cipher_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
