import requests
from rest_framework.response import Response
from rest_framework.views import APIView

from pokedex.models import Pokemon, Team
from pokedex.utils import add_pokeapi_pokemon

from .serializer import PokemonSerializer, TeamSerializer


class PokemonListView(APIView):
    def get(self, request) -> object:
        """
        Get a pokemons
        """
        pokemon = Pokemon.objects.all()
        # base_url/pokemon?search
        query = self.request.GET.get('search')
        if query is not None:
            pokemon = pokemon.filter(name__contains=query) | pokemon.filter(type__contains=query)
        serializer = PokemonSerializer(pokemon, many=True)
        return Response(serializer.data)


class PokemonDetailView(APIView):
    def get(self, request, pokemon_name: str) -> object:
        """
        Get requested pokemon
        """

        pokemon = Pokemon.objects.filter(name=pokemon_name.lower())
        if not pokemon:
            return Response(
                data={"errors": f"Pokemon '{pokemon_name}' not found!"},
                status=404,
            )
        serializer = PokemonSerializer(pokemon, many=True)
        return Response(serializer.data)


class PokemonCreateView(APIView):
    def post(self, request) -> object:
        pokemon_identifier = request.data.get('pokemon')
        if not pokemon_identifier:
            return Response(
                data={"errors": "Expected key 'pokemon' not found"},
                status=400,
            )
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{request.data.get('pokemon')}/")
        if req.status_code != 404:
            return Response(
                data={"errors": f"Requested pokemon not found!"},
                status=req.status_code,
            )
        elif req.status_code != 200:
            return Response(
                data={"errors": f"Unexpected error: {req.reason}!"},
                status=req.status_code,
            )

        add_pokeapi_pokemon([req.json()])
        newly_added_pokemon = Pokemon.objects.filter(name=req['name'])
        return Response(newly_added_pokemon, status=201)


class TeamListView(APIView):
    def get(self, request) -> object:
        """
        Get all teams
        """

        team = Team.objects.all()
        # base_url/team?search
        query = self.request.GET.get('search')
        if query is not None:
            team = team.filter(name__contains=query) | team.filter(trainer__contains=query)
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)


class TeamDetailView(APIView):

    def get(self, request, team: str) -> object:
        """
        Get requested team
        """
        my_team = Team.objects.filter(name=team.lower())
        if not my_team:
            return Response(
                data={"errors": f"Team '{team}' not found!"},
                status=404,
            )
        serializer = TeamSerializer(my_team, many=True)
        return Response(serializer.data)


class TeamCreateView(APIView):
    def post(self, request) -> object:
        """
        Create team with a trainer and at least 1 and at most 6 pokemon.
        """

        team_data = {k: v.lower() for k, v in request.data.items()}
        serializer = TeamSerializer(data=team_data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(
                data={
                    "errors": f"{', '.join(serializer.errors.keys())}",
                    "team": "Name must be unique",
                    "pokemon": "Pokemon names must a known pokemon.",
                },
                status=400,
            )

        return Response(serializer.data, status=201)


class TeamUpdateView(APIView):
    def put(self, request) -> object:
        """
        Update existing team.
        """
        team_data = {k: v.lower() for k, v in request.data.items()}
        to_update_team = Team.objects.filter(name=team_data.get('name'))
        if not to_update_team:
            return Response(
                data={"errors": "Team not found!"},
                status=404,
            )
        to_update_team.update(
            name=team_data.get('name'),
            trainer=team_data.get('trainer'),
            pokemon_1=team_data.get('pokemon_1'),
            pokemon_2=team_data.get('pokemon_2'),
            pokemon_3=team_data.get('pokemon_3'),
            pokemon_4=team_data.get('pokemon_4'),
            pokemon_5=team_data.get('pokemon_5'),
            pokemon_6=team_data.get('pokemon_6'),
        )
        return Response(team_data)

