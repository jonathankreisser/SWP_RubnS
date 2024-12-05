
class Fahrzeug:
    def __init__(self, marke: str, modell: str):
        self.marke = marke
        self.modell = modell

    def beschreibung(self):
        return f"Das Fahrzeug ist ein {self.marke} {self.modell}."

class Auto(Fahrzeug):
    def __init__(self, marke: str, modell: str, tueren: int):
        super().__init__(marke, modell)
        self.tueren = tueren

    def beschreibung(self):
        
        return f"Das Auto ist ein {self.marke} {self.modell} mit {self.tueren} Türen."

class Motorrad(Fahrzeug):
    def __init__(self, marke: str, modell: str, typ: str):
        super().__init__(marke, modell)
        self.typ = typ

    def beschreibung(self):
        return f"Das Motorrad ist ein {self.marke} {self.modell} vom Typ {self.typ}."


auto = Auto("Volkswagen", "Golf", 4)
motorrad = Motorrad("Yamaha", "MT-07", "Sport")

print(auto.beschreibung())
print(motorrad.beschreibung())
