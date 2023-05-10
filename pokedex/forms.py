from django import forms

from pokedex.models import Pokemon, PokemonFile
class PokemonFileForm(forms.ModelForm):
    pokemon_json_file = forms.FileField(required=False)

    class Meta:
        model = PokemonFile
        fields = ('name', )

class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = ('name', 'types', 'hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed', )
