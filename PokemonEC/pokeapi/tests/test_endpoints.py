from django.test import TestCase

# Create your tests here.
from PokemonEC.pokeapi.services import pokeapi



    
def test_evolution_chain_service():
    res = pokeapi.pokemon_evolution_chain(1)
    status = res.status_code
    assert status == 200
        
        
def test_get_charmander_evolution_chain():
    ec_charmander = 2
    res = pokeapi.pokemon_evolution_chain(ec_charmander)
    data = res.json()
    assert data['chain']['species']['name'] == 'charmander'

def test_get_charmander_height_weight():
    ec_charmander = 2
    res = pokeapi.pokemon_evolution_chain(ec_charmander)
    data = res.json()
    charmander = data['chain']['species']['name']
    res = pokeapi.pokemon_stats(charmander)
    pokemon_data = res.json();
    assert pokemon_data['id'] == 5