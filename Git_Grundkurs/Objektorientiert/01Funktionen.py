#!/usr/bin/env python3

#Einführung in Funktionen mit Typehints
def addiere(zahl1: int, zahl2: int) -> int:
    return zahl1 + zahl2
    """
    Funktion zum Addieren zweier Zahlen
    """


def begruessung(name: str) -> str:
    return f"Hallo {name}, willkommen!"
    """
    Funktion zur Begrüßung von einer Person
    """


#Berechnung der Fläche eines Rechteckts

def berechne_flaeche(länge: float, breite: float) -> float:
    """
    Funktion zur Berechnung der Fläche eines Rechtecks
    Parameter:
    länge (float): Länge des Rechtecks
    breite (float): Breite des Rechtecks
    Rückgabe:
    float: Fläche des Rechtecks
    """
    return länge * breite

#Aufruf der Funktionen
ergebnis = addiere(111, 12132)
print("Die Summe ist:", ergebnis)

gruß = begruessung("Max")
print(gruß)