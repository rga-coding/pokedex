from django.contrib import admin
from pokedex.forms import PokemonFileForm, PokemonForm
from pokedex.models import Pokemon, PokemonFile, Team


class PokemonFileAdmin(admin.ModelAdmin):
    form = PokemonFileForm
    list_display = ('name',)
    list_per_page = 50


class PokemonAdmin(admin.ModelAdmin):
    form = PokemonForm
    search_fields = ['name', 'types']
    list_display = ('name', 'types', 'hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed', )
    list_per_page = 10


class TeamAdmin(admin.ModelAdmin):
    model = Team
    search_fields = ['name', 'trainer']
    list_display = [field.name for field in Team._meta.fields]


admin.site.register(PokemonFile, PokemonFileAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Team, TeamAdmin)
