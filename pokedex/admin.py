from django.contrib import admin
from pokedex.forms import PokemonFileForm, PokemonForm
class PokemonFileAdmin(admin.ModelAdmin):
    form = PokemonFileForm
    list_display = ('name',)
    list_per_page = 50

