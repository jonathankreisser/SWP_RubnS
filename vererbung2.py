from typing import List
from collections import Counter

class Person:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender

class Mitarbeiter(Person):
    def __init__(self, name: str, gender: str, abteilung: 'Abteilung'):
        super().__init__(name, gender)
        abteilung.add_mitarbeiter(self)

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name: str, gender: str, abteilung: 'Abteilung'):
        super().__init__(name, gender, abteilung)
        abteilung.set_leiter(self)

class Abteilung:
    def __init__(self, name: str):
        self.name = name
        self.mitarbeiter: List[Mitarbeiter] = []
        self.leiter: Abteilungsleiter = None

    def add_mitarbeiter(self, mitarbeiter: Mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def set_leiter(self, leiter: Abteilungsleiter):
        self.leiter = leiter

class Firma:
    def __init__(self, name: str):
        self.name = name
        self.abteilungen: List[Abteilung] = []

    def add_abteilung(self, abteilung: Abteilung):
        self.abteilungen.append(abteilung)

    def get_total_mitarbeiter(self) -> int:
        return sum(len(abt.mitarbeiter) for abt in self.abteilungen)

    def get_total_abteilungsleiter(self) -> int:
        return sum(1 for abt in self.abteilungen if abt.leiter)

    def get_total_abteilungen(self) -> int:
        return len(self.abteilungen)

    def get_groesste_abteilung(self) -> str:
        if not self.abteilungen:
            return "Keine Abteilungen vorhanden"
        return max(self.abteilungen, key=lambda abt: len(abt.mitarbeiter)).name

    def get_gender_ratio(self) -> dict:
        genders = [m.gender for abt in self.abteilungen for m in abt.mitarbeiter]
        total = len(genders)
        if total == 0:
            return {"Male": 0, "Female": 0}
        counter = Counter(genders)
        return {g: (counter[g] / total) * 100 for g in ["Male", "Female"]}

# Instanziierung
firma = Firma("TechCorp")

# Abteilungen erstellen
entwicklung = Abteilung("Entwicklung")
marketing = Abteilung("Marketing")

firma.add_abteilung(entwicklung)
firma.add_abteilung(marketing)

# Mitarbeiter und Abteilungsleiter erstellen
Abteilungsleiter("Alice", "Female", entwicklung)
Mitarbeiter("Bob", "Male", entwicklung)
Mitarbeiter("Charlie", "Male", entwicklung)

Abteilungsleiter("Diana", "Female", marketing)
Mitarbeiter("Eve", "Female", marketing)

# Statistiken anzeigen
print("Anzahl Mitarbeiter:", firma.get_total_mitarbeiter())
print("Anzahl Abteilungsleiter:", firma.get_total_abteilungsleiter())
print("Anzahl Abteilungen:", firma.get_total_abteilungen())
print("Größte Abteilung:", firma.get_groesste_abteilung())
print("Geschlechterverteilung:", firma.get_gender_ratio())