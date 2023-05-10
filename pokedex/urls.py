from django.urls import path

from . import views

app_name = 'pokedex'
urlpatterns = [

    path('pokemons/<str:pokemon_name>/', views.PokemonDetailView.as_view()),
    path('pokemons/create/', views.PokemonCreateView.as_view()),
    path('pokemons/', views.PokemonListView.as_view()),
