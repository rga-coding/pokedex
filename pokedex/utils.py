
from pokedex.models import Pokemon


def add_pokeapi_pokemon(pokemons: list) -> bool:
    # ToDo add try except/error handling
    for pokemon in pokemons:
        new_pokemon = Pokemon(
            name=pokemon['name'].lower(),
            types=', '.join([p['type']['name'] for p in pokemon['types']]),
            hp=int(pokemon['stats'][0]['base_stat']),
            attack=int(pokemon['stats'][1]['base_stat']),
            defense=int(pokemon['stats'][2]['base_stat']),
            special_attack=int(pokemon['stats'][3]['base_stat']),
            special_defense=int(pokemon['stats'][4]['base_stat']),
            speed=int(pokemon['stats'][5]['base_stat']),
        )
        new_pokemon.save()
    return True
