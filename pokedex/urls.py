from django.urls import path

from . import views

app_name = 'pokedex'
urlpatterns = [
    path('teams/<str:team>/', views.TeamDetailView.as_view()),
    path('teams/', views.TeamListView.as_view()),

    path('pokemons/<str:pokemon_name>/', views.PokemonDetailView.as_view()),
    path('pokemons/create/', views.PokemonCreateView.as_view()),
    path('pokemons/', views.PokemonListView.as_view()),
]
