from django.urls import include, path

from .views import pokemons 


urlpatterns = [
    path('evolution-chain/<str:pokemon_name>', pokemons.evolution_chain_from_name)
]
