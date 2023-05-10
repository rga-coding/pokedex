
from rest_framework.response import Response
from rest_framework.views import APIView


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

