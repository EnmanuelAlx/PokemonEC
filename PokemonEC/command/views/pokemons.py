from PokemonEC.pokeapi.services import pokeapi
from PokemonEC.command.serializers.pokemons import PokemonModelSerializer
from PokemonEC.command.serializers.stats import StatModelSerializer
from PokemonEC.command.models import Pokemon

def pokemon_evolution_chain(ec_id):
    try:
        res = pokeapi.pokemon_evolution_chain(ec_id)
        data = res.json()
        first_chain = data['chain']
        
        pokemons = _create_chain(first_chain, None, [])
        return pokemons
    except Exception as e:
        message = e.args
        print(message)
        return []
    

def _create_chain(chain, prevolution, pokemons):
    name = chain['species']['name']
    pokemon = None
    if prevolution:
        pokemon = _create_pokemon(name, prevolution)
        pokemons.append(pokemon)
    else:
        pokemon = _create_pokemon(name)
        pokemons.append(pokemon)
    

    for ch in chain['evolves_to']:
        # pokemon = make_pokemon(name, prevolution)
        _create_chain(ch, pokemon, pokemons)
    
    return pokemons

def _create_pokemon(pokemon, prevolution=None):
    res = pokeapi.pokemon_stats(pokemon)
    data = res.json()
    num_stats = 6
    stats = data['stats'][:num_stats]
    data['pokemon_id'] = data['id']
    serializer = PokemonModelSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    
    pokemon = serializer.save()
    
    if prevolution:
        pokemon.prevolution.through.objects.create(
            from_pokemon_id = pokemon.id,
            to_pokemon_id = prevolution.id
        )
        
    
    
    _make_stats(stats, pokemon.id)
    
    return pokemon
    
def _make_stats(stats, pokemon_id):
    
    for stat in stats: 
        stat['name'] = stat['stat']['name']
        stat['pokemon'] = pokemon_id
        serializer = StatModelSerializer(data = stat)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
    
    