import requests

# CoinGecko API-Endpunkt
url = 'https://api.coingecko.com/api/v3/simple/price'

# Parameter: Wir wollen den Preis von Bitcoin in USD
params = {
    'ids': 'bitcoin',
    'vs_currencies': 'eur'
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Fehlermeldung, wenn der Statuscode nicht 200 ist
    data = response.json()
    
    price = data['bitcoin']['eur']
    print(f"Aktueller Bitcoin-Preis: €{price}")

except requests.exceptions.RequestException as e:
    print(f"Fehler bei der API-Anfrage: {e}")