"""
Lag en funksjon som teller antall forekomster av et tegn i en tekst. 
(Altså én parameter for tegnet og én for teksten.) 
"""

def antall_forekomster(tegn, tekst):
    teller = 0
    for bokstav in tekst:
        if bokstav == tegn:
            teller += 1
    return teller

antall = antall_forekomster("e", "To be or not to be.")
print(f"Antall forekomster: {antall}")
