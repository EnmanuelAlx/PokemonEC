from django.test import TestCase
from PokemonEC.command.models import pokemons
from PokemonEC.pokeapi.services import pokeapi

class TestModels(TestCase):
    def test_create_pokemon(self):
        data = {
            "name" : 'charmander',
            "height" : 6,
            "weight" : 85,
            "pokemon_id" : 4,    
        }
        
        charmander = pokemons.Pokemon.objects.create(**data)
        self.assertIsInstance(charmander, pokemons.Pokemon)
    
    def test_create_pokemon_with_stats(self):
        data = {
            "name" : 'charmander',
            "height" : 6,
            "weight" : 85,
            "pokemon_id" : 4,    
        }
        charmander = pokemons.Pokemon.objects.create(**data)
        stats = {
            "name" : 'hp',
            'base_stat': 50,
            'pokemon' : charmander
        }
        stats = pokemons.Stat.objects.create(**stats)
        self.assertIsInstance(stats.pokemon, pokemons.Pokemon)
        self.assertIsInstance(stats, pokemons.Stat)
    
    
    