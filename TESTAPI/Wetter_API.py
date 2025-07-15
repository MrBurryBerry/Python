import requests

def wetter_abfragen_ohne_api_key(stadt="Karlsruhe"):
    url = f"https://wttr.in/{stadt}?format=j1"  # JSON-Format

    try:
        response = requests.get(url)
        if response.status_code == 200:
            daten = response.json()

            aktuelles_wetter = daten["current_condition"][0]
            temperatur = aktuelles_wetter["temp_C"]
            beschreibung = aktuelles_wetter["weatherDesc"][0]["value"]
            luftfeuchtigkeit = aktuelles_wetter["humidity"]
            wind = aktuelles_wetter["windspeedKmph"]

            print(f"Wetter in {stadt}:")
            print(f"- Temperatur: {temperatur}°C")
            print(f"- Beschreibung: {beschreibung}")
            print(f"- Luftfeuchtigkeit: {luftfeuchtigkeit}%")
            print(f"- Windgeschwindigkeit: {wind} km/h")
        else:
            print("Fehler beim Abrufen der Wetterdaten.")
    except Exception as e:
        print("Ein Fehler ist aufgetreten:", e)

if __name__ == "__main__":
    wetter_abfragen_ohne_api_key()
