import json
from django.test import TestCase
import pytest
from config import APP_ROOT_DIR
from pokedex.utils import add_pokeapi_pokemon

class TestAddPokeApiPokemon(TestCase):

    def test_add_pokeapi_pokemon(self, mocker):
        with open(f"{APP_ROOT_DIR}/config/bulbasaur.json") as file:
            bulbasaur = json.load(file)

        pokemon_model = mocker.patch('pokedex.models.Pokemon')
        pokemon_add_bool = add_pokeapi_pokemon(pokemons=bulbasaur)
        assert pokemon_add_bool is True
        assert pokemon_model.is_called is True
        assert pokemon_model.save.is_called is True
