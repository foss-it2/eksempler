""""
Klasser som omhandler akvarium og fisker.
"""
class Akvarium:
    def __init__(self, l, b, h) -> None: # -> None betyr at metoden ikke returnerer noe.
        self.l = l
        self.b = b
        self.h = h
    
    def beregnVolum(self) -> float:
        return self.l * self.b * self.h

def main():
    """Hovedprogram"""
    akvarium1 = Akvarium(15, 40, 25)
    print(f"Volum av tomt akvarium: {akvarium1.beregnVolum():.1f} cm^3")

# Kjører main-funksjon hvis filen er selve hovedprogrammet.
if __name__ == "__main__":
    main()
    
