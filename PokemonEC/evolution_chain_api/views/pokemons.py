from PokemonEC.pokeapi.services import pokeapi
from PokemonEC.command.serializers.pokemons import PokemonModelSerializer
from PokemonEC.command.serializers.stats import StatModelSerializer
from PokemonEC.command.models import Pokemon

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.management import call_command

import json

@api_view()
def evolution_chain_from_name(request, pokemon_name):
    print(pokemon_name)
    pokemon = Pokemon.objects.filter(name__contains=pokemon_name)
    if not pokemon:
        try:
            res = pokeapi.pokemon_species(pokemon_name)
            data = res.json()
            evolution_chain_url = data['evolution_chain']['url']
            ec_id = evolution_chain_url.split('/')[-2]
            call_command('create_evolution_chain', ec_id)
            pokemon = Pokemon.objects.filter(name__contains=pokemon_name)
        except Exception as e:
            message = e.args
            return Response({'message' : e.args}, status=status.HTTP_404_NOT_FOUND)
    
    pokemon = pokemon.first()
    pre_chain = _prevolution_chain(pokemon)
    post_chain = _evolution_chain(pokemon)
    pokemon_serializer = PokemonModelSerializer(pokemon).data
    stat_serializer = StatModelSerializer(pokemon.stats, many=True).data
    pokemon_serializer['prevolutions'] = pre_chain['prevolution']
    pokemon_serializer['evolution'] = post_chain['evolution']
    pokemon_serializer['stats'] = stat_serializer
    
    return Response(pokemon_serializer, status=status.HTTP_200_OK)

def _prevolution_chain(pokemon, chain= []):
    
    prevolutions = pokemon.prevolution.all()
    serializer = PokemonModelSerializer(pokemon)
    pokemon_serializer = serializer.data
    pokemon_serializer['prevolution'] = []
    stat_serializer = StatModelSerializer(pokemon.stats, many=True)
    pokemon_serializer['stats'] = stat_serializer.data
    if prevolutions.count() == 0:
        return pokemon_serializer

    
    for prevolution in prevolutions.all():
        pokemon_serializer['prevolution'].append(_prevolution_chain(prevolution, []))
        

    return pokemon_serializer

def _evolution_chain(pokemon, chain = []):
    
    evolutions = Pokemon.objects.filter(prevolution=pokemon)
    
    serializer = PokemonModelSerializer(pokemon)
    pokemon_serializer = serializer.data
    pokemon_serializer['evolution'] = []
    stat_serializer = StatModelSerializer(pokemon.stats.all(), many=True)
    pokemon_serializer['stats'] = stat_serializer.data
    
    if evolutions.count() == 0:
        return pokemon_serializer
        
    
    for evolution in evolutions:
        pokemon_serializer['evolution'].append(_evolution_chain(evolution, []))
        
        
    return pokemon_serializer

    