# zum Lernen von Variablen in Python

#Variablen speichern Werte
name = "Lars"
alter = 25

#Variablen können verändert werden
alter = 26

#Typumwandlung (Casting)
alter_string = str(alter) # von int zu str

print("Name:", name)
print("Alter:", alter_string)

# Gleitkommazahl zu Ganzzahl casten
hoehe = 178.3 # Float
hoehe_int = int(hoehe) # float zu Integer

# Ausgabe des Ergebnisses
print("Höhe als Ganzzahl:", hoehe_int)

#Listen sind eine Art Container, in dem mehrere Werte gespeichert werden können
zahlen_liste = [1, 2, 3, 4, 5]
meine_buchstaben_liste = ['a', 'b', 'c', 'd', 'e']
meine_gemischte_liste = [1, 'a', 2, 'b', 3, 'c']

#hinzufügen eines Wertes zu einer Liste
meine_gemischte_liste.append('f')

#Werte ausgeben
print("Liste:", meine_gemischte_liste)
print("Liste 1 Wert:", meine_gemischte_liste[2])  # Erster Wert

# Werte in der Liste ändern
meine_gemischte_liste[0] = 'x'
print("Geänderte Liste:", meine_gemischte_liste)

#Werte aus der Liste entfernen
meine_gemischte_liste.remove('b')
print("Liste nach Entfernen eines Wertes:", meine_gemischte_liste)

# länge der Liste
print("Länge der Liste:", len(meine_gemischte_liste))

# Dictonaries sind eine Art Container, in dem Schlüssel-Wert-Paare gespeichert werden
mein_dict = {
    'name': 'Lars',
    'alter': 25,
    'stadt': 'Karlsruhe'
}
print("Dictionary:", mein_dict) #ähnlich wie bei der Liste kann auch nur ein bestimmter wert ausgegeben werden
print("Name aus Dictionary:", mein_dict['name'])

# Werte im Dictionary ändern
mein_dict['alter'] = 26
print("Geändertes Dictionary:", mein_dict)

# Werte im Dictionary hinzufügen
mein_dict['beruf'] = 'Softwareentwickler'
print("Dictionary nach Hinzufügen eines Wertes:", mein_dict)    

# Werte im Dictionary entfernen
del mein_dict['stadt']
print("Dictionary nach Entfernen eines Wertes:", mein_dict)

