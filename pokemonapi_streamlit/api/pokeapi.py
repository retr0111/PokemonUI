import requests

def fetch_pokemon_data():
    response = requests.get("https://pokeapi.co/api/v2/")
    data = response.json()
    return data
