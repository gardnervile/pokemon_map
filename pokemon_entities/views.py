import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    current_time = localtime()

    pokemons = Pokemon.objects.all()
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        image_url = None
        if pokemon_entity.pokemon.image:
            image_url = request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        
        if image_url:
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                image_url
            )
        else:
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri('/static/default_icon.png')
            )

    pokemons_on_page = []
    for pokemon in pokemons:
        img_url = None
        if pokemon.image:
            img_url = request.build_absolute_uri(pokemon.image.url)

        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': img_url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    pokemon_entities = PokemonEntity.objects.filter(
        pokemon=pokemon,
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        image_url = request.build_absolute_uri(pokemon.image.url) if pokemon.image else None
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            image_url or request.build_absolute_uri('/static/default_icon.png')
        )

    pokemon_data = {
        'img_url': request.build_absolute_uri(pokemon.image.url) if pokemon.image else None,
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'pokemon_id': pokemon_id,
        'description': pokemon.description,
    }

    if pokemon.evolved_from:
        previous_evolution = pokemon.evolved_from
        pokemon_data["previous_evolution"] = {
            "pokemon_id": previous_evolution.id,
            "img_url": request.build_absolute_uri(previous_evolution.image.url) if previous_evolution.image else None,
            "title_ru": previous_evolution.title
        }
    next_evolution = pokemon.evolutions.first()
    if next_evolution:
        pokemon_data["next_evolution"] = {
            "pokemon_id": next_evolution.id,
          "img_url": request.build_absolute_uri(next_evolution.image.url) if next_evolution.image else None,
          "title_ru": next_evolution.title
        }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_data
    })
