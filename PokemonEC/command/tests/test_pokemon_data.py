from django.test import TestCase
from PokemonEC.command.models.pokemons import Pokemon, Stat

from PokemonEC.command.views import pokemons

class TestModelData(TestCase):
    
    
    def test_make_charmander_evolution_chain(self):
        ec_charmander = 2
        ec_charmander = pokemons.pokemon_evolution_chain(ec_charmander)

        self.assertIsInstance(ec_charmander[0], Pokemon)
        self.assertEqual(ec_charmander[1].prevolution.first().name, 'charmander')
        self.assertIsInstance(ec_charmander[0].stat_set.first(), Stat)
        
    def test_make_eevee_evolution_chain(self):
        ec_eevee = 67
        ec_eevee = pokemons.pokemon_evolution_chain(ec_eevee)
        self.assertIsInstance(ec_eevee[0], Pokemon)
        self.assertEqual(ec_eevee[1].prevolution.first().name, 'eevee')
        self.assertIsInstance(ec_eevee[0].stat_set.first(), Stat)
        
    def test_make_squirtle_evolution_chain(self):
        ec_squirtle = 3
        ec_squirtle = pokemons.pokemon_evolution_chain(ec_squirtle)
        self.assertIsInstance(ec_squirtle[0], Pokemon)
        self.assertEqual(ec_squirtle[1].prevolution.first().name, 'squirtle')
        self.assertIsInstance(ec_squirtle[0].stat_set.first(), Stat)
    
    
    