#djangoo REST framework
from rest_framework import serializers

#models
from PokemonEC.command.models import Pokemon

class PokemonModelSerializer(serializers.ModelSerializer):
    class Meta: 
        
        model = Pokemon
        fields = [
            "name",
            "height",
            "weight",
            "pokemon_id",
        ]
    
    def create(self, validated_data):
    
        pokemon = Pokemon.objects.create(**validated_data)
        return pokemon
    
