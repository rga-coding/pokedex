from rest_framework import serializers

from .models import Pokemon, Team


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
