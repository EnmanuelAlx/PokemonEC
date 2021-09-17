
from django.http import HttpResponse
import requests


BASE_URL = "https://pokeapi.co/api/v2"

def pokemon_evolution_chain(id):
    url = f"{BASE_URL}/evolution-chain/{id}"
    res = requests.get(url)
    if res.status_code == 200:
        return res
    raise Exception('Error when obtaining PokeAPI data')

def pokemon_stats(pokemon_name):
    url = f"{BASE_URL}/pokemon/{pokemon_name}"
    res = requests.get(url)
    if res.status_code == 200:
        return res
    raise Exception('Error when obtaining PokeAPI data')

def pokemon_species(pokemon_name):
    url = f"{BASE_URL}/pokemon-species/{pokemon_name}"
    res = requests.get(url)
    if res.status_code == 200:
        return res
    raise Exception('Error when obtaining PokeAPI data')