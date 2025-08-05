#!/usr/bin/env python3
import argparse

# ArgumentParser für Objekte
parser = argparse.ArgumentParser(description='Hilfe für den Taschenrechner.')

# Argumente hinzufügen
parser.add_argument("pflicht_int", help="Es wird ein erster Integer benötigt", type=int)
parser.add_argument("pflicht_int2", help="Es wird ein zweiter Integer benötigt", type=int)
parser.add_argument("--operation", choices=["add", "sub", "mul", "div"], default="add", help="Die gewünschte Operation: add, sub, mul oder div")

# Argumente parsen
args = parser.parse_args()

if args.operation == "add":
    ergebnis = args.pflicht_int + args.pflicht_int2
elif args.operation == "sub":
    ergebnis = args.pflicht_int - args.pflicht_int2
elif args.operation == "mul":
    ergebnis = args.pflicht_int * args.pflicht_int2
elif args.operation == "div":
    if args.pflicht_int2 != 0:
        ergebnis = args.pflicht_int / args.pflicht_int2
    else:
        ergebnis = "Division durch Null ist nicht erlaubt!"

print("Das Ergebnis ist:", ergebnis)
print("Ende des Programms")   