from django.urls import path

from . import views

app_name = 'pokedex'
urlpatterns = [
    path('teams/create/', views.TeamCreateView.as_view()),
    path('teams/update/', views.TeamUpdateView.as_view()),
    path('teams/delete/<str:team>/', views.TeamDeleteView.as_view()),
    path('teams/<str:team>/', views.TeamDetailView.as_view()),
    path('teams/', views.TeamListView.as_view()),

    path('pokemons/<str:pokemon_name>/', views.PokemonDetailView.as_view()),
    path('pokemons/create/', views.PokemonCreateView.as_view()),
    path('pokemons/', views.PokemonListView.as_view()),
]
