from django.urls import path

from . import views

app_name = 'pokedex'
urlpatterns = [
    path('pokemons/', views.PokemonListView.as_view()),
