from django.test import TestCase
from PokemonEC.command.views import pokemons
from PokemonEC.pokeapi.services import pokeapi

class TestModels(TestCase):
    
    def test_api_failure(self):
        ec_errror = -1
        ec_error = pokemons.pokemon_evolution_chain(ec_errror)
        self.assertEqual(ec_error, [])
        
    
    