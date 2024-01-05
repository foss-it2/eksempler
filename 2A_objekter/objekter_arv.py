"""
Noen klasser.
"""

class Form:
    def __init__(self, farge="#ff0000") -> None:
        self.farge = farge

    def __str__(self):
        return f"Jeg er et geometrisk objekt:)"


class Firkant(Form):
    def __init__(self,lengde, hoyde, farge) -> None:
        super().__init__(farge)
        self.lengde = lengde
        self.hoyde = hoyde

    def __str__(self):
        return f"Jeg er en firkant :)"
    
    def areal(self):
        return self.lengde * self.hoyde

class Kvadrat(Firkant):
    def __init__(self, lengde, farge) -> None:
        super().__init__(lengde, lengde, farge)
    
    def __str__(self):
        return f"Jeg er et perfekt kvadrat :)"
    

# Bruker klassene
per = Form("#00ffff")
pål = Firkant(3,7)  # Fargen settes automatisk av klassen Form.
espen = Kvadrat(5,"#ffff00")

print(per)
print(pål)
print(espen)