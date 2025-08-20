#!/usr/bin/env python3

#Aufgaben Textanalyse
# 1. Ein Pflichtargument (positional argument), das einen Text entgegennimmt.
# 2. Ein optionals Argument --details, das zustzäliche Informationen liefer: Anzahl der Wörter
# 3. Wenn das Argument --details nicht angegeben ist, soll das Programm die Anzahl der Zeichen im Text ausgeben.

import argparse


#ArgumentParser für Textanalyse
parser = argparse.ArgumentParser(description='Textanalyse-Tool.')

#Argumente hinzufügen
parser.add_argument("text", nargs='+', help="Eingabe Text (mehrere Wörter erlaubt)")
parser.add_argument("--details", action='store_true', help="Anzahl der Wörter im Text anzeigen")

args=parser.parse_args()

text = ' '.join(args.text)
characters = len(text)
words = len(text.split())

print(f"Anzahl der Zeichen: {characters}")
if args.details:
    print(f"Anzahl der Wörter: {words}")

    vowels = "aeiou"
    sum_vowels = sum(1 for char in text.lower() if char in vowels)
    print(f"Anzahl der Vokale: {sum_vowels}")

    consonants = "bcdfghjklmnpqrstvwxyz"
    sum_consonants = sum(1 for char in text.lower() if char in consonants)
    print(f"Anzahl der Konsonanten: {sum_consonants}")
    
