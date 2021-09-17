#djangoo REST framework
from rest_framework import serializers

#models
from PokemonEC.command.models import Stat

class StatModelSerializer(serializers.ModelSerializer):
    
    class Meta: 
        
        model = Stat
        fields = '__all__'
    
    def create(self, validated_data):
        pokemon = Stat.objects.create(**validated_data)
        return pokemon
    
