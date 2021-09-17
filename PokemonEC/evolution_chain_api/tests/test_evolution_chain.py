from django.test import TestCase

# Create your tests here.
from PokemonEC.pokeapi.services import pokeapi
from PokemonEC.evolution_chain_api.views.pokemons import evolution_chain_from_name 
from PokemonEC.command.models import Pokemon, Stat
from rest_framework.response import Response

class TestEvolutioNChainCharmander(TestCase):
    
    def setUp(self):
        self.charmander = Pokemon.objects.create(
            name='charmander',
            height = 9,
            weight = 4,
            pokemon_id = 4,
        )
        self.charmeleon = Pokemon.objects.create(
            name='charmeleon',
            height = 9,
            weight = 4,
            pokemon_id = 5,
        )
        self.charizard = Pokemon.objects.create(
            name='charizard',
            height = 50,
            weight = 50,
            pokemon_id = 6,
        )
        self.charmeleon.prevolution.through.objects.create(
            from_pokemon_id = self.charmeleon.id,
            to_pokemon_id = self.charmander.id
        )
        self.charizard.prevolution.through.objects.create(
            from_pokemon_id = self.charizard.id,
            to_pokemon_id = self.charmeleon.id
        )  
        self.stats = Stat.objects.create(
            name = 'hp',
            base_stat=55,
            pokemon= self.charmander
        )
        self.stats = Stat.objects.create(
            name = 'attack',
            base_stat=55,
            pokemon= self.charmander
        )
        self.stats = Stat.objects.create(
            name = 'def',
            base_stat=55,
            pokemon= self.charmander
        )
        self.stats = Stat.objects.create(
            name = 'hp',
            base_stat=55,
            pokemon= self.charmeleon
        )
        self.stats = Stat.objects.create(
            name = 'attack',
            base_stat=55,
            pokemon= self.charmeleon
        )
        self.stats = Stat.objects.create(
            name = 'def',
            base_stat=55,
            pokemon= self.charmeleon
        )
        self.stats = Stat.objects.create(
            name = 'hp',
            base_stat=55,
            pokemon= self.charizard
        )
        self.stats = Stat.objects.create(
            name = 'attack',
            base_stat=55,
            pokemon= self.charizard
        )
        self.stats = Stat.objects.create(
            name = 'def',
            base_stat=55,
            pokemon= self.charizard
        )
        
    
    def test_get_charmander_from_db(self):
        pokemon_name = 'charmander'
        pokemon = Pokemon.objects.filter(name__contains=pokemon_name).first()
        self.assertEqual(pokemon.name, pokemon_name)
          
        
    def test_get_charmander_evolution_chain(self):
        pokemon_name = 'charmander'
        evolution_chain_charmander = evolution_chain_from_name(pokemon_name)
        self.assertIsInstance(evolution_chain_charmander,Response)
        
        
    def test_get_any_pokemon_evolution_chain(self):
        pokemon_name = 'eevee'
        evolution_chain_any = evolution_chain_from_name(pokemon_name)
        self.assertIsInstance(evolution_chain_any, Response)
        
    def test_evolution_jolteon_pokemon_evolution_chain(self):
        pokemon_name = 'jolteon'
        evolution_chain_any = evolution_chain_from_name(pokemon_name)
        self.assertIsInstance(evolution_chain_any, Response)