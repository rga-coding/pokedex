import json

from django import forms

from pokedex.models import Pokemon, PokemonFile
from pokedex.utils import add_pokeapi_pokemon


class PokemonFileForm(forms.ModelForm):
    pokemon_json_file = forms.FileField(required=False)

    class Meta:
        model = PokemonFile
        fields = ('name', )

    def save(self, commit=True):
        add_pokeapi_pokemon(json.load(self.cleaned_data['pokemon_json_file']))
        return super().save(commit=commit)


class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = ('name', 'types', 'hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed', )
