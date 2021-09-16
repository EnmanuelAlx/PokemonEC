
from django.http import HttpResponse
import requests


BASE_URL = "https://pokeapi.co/api/v2"

def pokemon_evolution_chain(id):
    url = f"{BASE_URL}/evolution-chain/{id}"
    res = requests.get(url)
    return res

def pokemon_stats(pokemon_name):
    url = f"{BASE_URL}/pokemon/{pokemon_name}"
    res = requests.get(url)
    return res