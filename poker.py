import random
from collections import Counter


#F Strings an 2 stellen und unittest klassen erstellen

# Deck erstellen
def erstelle_deck():
    # Farben und Symbole für das Deck
    FARBEN = ['Herz', 'Karo', 'Pik', 'Kreuz']
    SYMBOLEN = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    return [(symbol, farbe) for farbe in FARBEN for symbol in SYMBOLEN]

# 5 karten zufällig
def ziehe_fuenf_karten(deck):
    return random.sample(deck, 5)


# kombinationen prüfen
def ist_paar(hand):
    werte = [karte[0] for karte in hand]
    counter = Counter(werte)
    return 2 in counter.values()

def ist_drilling(hand):
    werte = [karte[0] for karte in hand]
    counter = Counter(werte)
    return 3 in counter.values()

def ist_vierling(hand):
    werte = [karte[0] for karte in hand]
    counter = Counter(werte)
    return 4 in counter.values()

def ist_full_house(hand):
    werte = [karte[0] for karte in hand]
    counter = Counter(werte)
    return sorted(counter.values()) == [2, 3]

def ist_flush(hand):
    farben = [karte[1] for karte in hand]
    return len(set(farben)) == 1

def ist_strasse(hand):
    werte = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    indices = sorted([werte.index(karte[0]) for karte in hand])
    return indices == list(range(indices[0], indices[0] + 5))

# kombinationen zählen
def spiele_poker_simulation(spiele_anzahl):
    deck = erstelle_deck()
    ergebnisse = Counter()

    for _ in range(spiele_anzahl):
        hand = ziehe_fuenf_karten(deck)

        if ist_flush(hand) and ist_strasse(hand):
            ergebnisse['Straße Flush'] += 1
        elif ist_vierling(hand):
            ergebnisse['Vierling'] += 1
        elif ist_full_house(hand):
            ergebnisse['Full House'] += 1
        elif ist_flush(hand):
            ergebnisse['Flush'] += 1
        elif ist_strasse(hand):
            ergebnisse['Straße'] += 1
        elif ist_drilling(hand):
            ergebnisse['Drilling'] += 1
        elif ist_paar(hand):
            ergebnisse['Paar'] += 1
        else:
            ergebnisse['Keine Kombination'] += 1

    return ergebnisse

#prozente berechnen
def berechne_prozentuale_anteile(ergebnisse, spiele_anzahl):
    anteile = {}
    for kombination, anzahl in ergebnisse.items():
        anteile[kombination] = (anzahl / spiele_anzahl) * 100
    return anteile


def main():
    spiele_anzahl = 100_000
    starten = input("Etwas Tippen zum Starten:")
    ziehe_fuenf_karten(erstelle_deck())
    ist_paar(ziehe_fuenf_karten(erstelle_deck()))
    ist_drilling(ziehe_fuenf_karten(erstelle_deck()))
    ist_vierling(ziehe_fuenf_karten(erstelle_deck()))
    ist_full_house(ziehe_fuenf_karten(erstelle_deck()))
    ist_flush(ziehe_fuenf_karten(erstelle_deck()))
    ist_strasse(ziehe_fuenf_karten(erstelle_deck()))
    spiele_poker_simulation(spiele_anzahl)

    ergebnisse = spiele_poker_simulation(spiele_anzahl)
    berechne_prozentuale_anteile(ergebnisse, spiele_anzahl)



    anteile = berechne_prozentuale_anteile(ergebnisse, spiele_anzahl)

    print("Ergebnisse der Simulation:")
    for kombination, anzahl in ergebnisse.items():
        print(f"{kombination}: {anzahl}")

    print("\nProzentuale Anteile:")
    for kombination, anteil in anteile.items():
        print(f"{kombination}: {anteil:.2f}%")


if __name__ == "__main__":
    main()
