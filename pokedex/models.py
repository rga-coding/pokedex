from django.db import models
class PokemonFile(models.Model):

    name = models.CharField(max_length=100, primary_key=True, help_text='Pokemons to load')

