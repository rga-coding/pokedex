from django.db import models
class PokemonFile(models.Model):

    name = models.CharField(max_length=100, primary_key=True, help_text='Pokemons to load')


class Pokemon(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    types = models.CharField(max_length=255, null=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return self.name


