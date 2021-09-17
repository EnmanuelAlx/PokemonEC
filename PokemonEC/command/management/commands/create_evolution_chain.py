
from django.core.management import BaseCommand
from PokemonEC.command.views import pokemons
from PokemonEC.command.serializers.pokemons import PokemonModelSerializer
from PokemonEC.command.models.pokemons import Pokemon

class Command(BaseCommand):
    help = 'Create Pokemon Evolution Chain'
    def add_arguments(self, parser):
        parser.add_argument('ec_id',
            nargs=1,
            type=int
        )
        
    def handle(self, *args, **options):
        ec_id = options.get('ec_id', None)
        
        if ec_id:
            ec_id = ec_id[0]
        
        ec = pokemons.pokemon_evolution_chain(ec_id)

        self.stdout.write("Evolution Chain created")
        return 
        
