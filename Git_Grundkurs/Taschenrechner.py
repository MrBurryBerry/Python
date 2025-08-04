zahl1 = input("Bitte geben Sie die erste Zahl ein:")
zahl1 = int(zahl1)
zahl2 = int(input("Bitte geben Sie die zweite Zahl ein:"))

operation = input("Bitte geben Sie die gewünschte Operation ein (+,-,*,/):")

if operation == "+":
    ergebnis = zahl1 + zahl2
elif operation == "-":
    ergebnis = zahl1 - zahl2
elif operation == "*":
    ergebnis = zahl1 * zahl2
elif operation =="/":
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
    else:
        ergebnis = "Division durch Null ist nicht erlaubt!"
else:
    ergebnis = "Ungültige Operation!"

print("Das ERgebnis ist:", ergebnis)