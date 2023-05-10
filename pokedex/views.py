
from rest_framework.response import Response
from rest_framework.views import APIView

from pokedex.models import Pokemon

from .serializer import PokemonSerializer


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

