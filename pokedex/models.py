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


class Team(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    trainer = models.CharField(max_length=255)
    pokemon_1 = models.ForeignKey("Pokemon", on_delete=models.CASCADE, related_name='pokemon1')
    pokemon_2 = models.ForeignKey("Pokemon", on_delete=models.CASCADE, related_name='pokemon2', null=True)
    pokemon_3 = models.ForeignKey("Pokemon", on_delete=models.CASCADE, related_name='pokemon3', null=True)
    pokemon_4 = models.ForeignKey("Pokemon", on_delete=models.CASCADE, related_name='pokemon4', null=True)
    pokemon_5 = models.ForeignKey("Pokemon", on_delete=models.CASCADE, related_name='pokemon5', null=True)
    pokemon_6 = models.ForeignKey("Pokemon", on_delete=models.CASCADE, related_name='pokemon6', null=True)
