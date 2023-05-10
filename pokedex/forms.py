from django import forms

class PokemonFileForm(forms.ModelForm):
    pokemon_json_file = forms.FileField(required=False)

    class Meta:
        model = PokemonFile
        fields = ('name', )
