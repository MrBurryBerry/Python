# Schleifen in Python
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for zahl in zahlen:
    print("Aktuelle Zahl:", zahl)

#for schleife mit range
for i in range(1, 6):
    print("Aktueller Wert:", i)


# while Schleife
count = 0
while count < 5:
    print("Count ist:", count)
    count = count+1  # Erhöht den Wert von count um 1


# while schleife mit einer bedinugng

n = 10
while n > 0:
    print("Countdown:", n)
    n -= 1  # Verringert den Wert von n um 1