from .models import Tag, Dev, Game
from django.shortcuts import get_object_or_404, get_list_or_404
import random



def get_big_sale() -> Game:
    game = Game.objects.order_by("-discount")[0]

    return game



def get_shop_games() -> tuple[list[str], list[list[Game]]]:
    pull:list[str] = ["Ofertas", "Gratis", "Acción", "FPS", "Menos de 20€", "Mas recientes"]
    queries:list = [
        Game.objects.exclude(discount=0).order_by("?")[:3],
        Game.objects.filter(price=0).order_by("?")[:3],
        Game.objects.filter(tags__name="Acción").order_by("?")[:3],
        Game.objects.filter(tags__name="FPS").order_by("?")[:3],
        Game.objects.filter(price__lt=2000)[:3],
        Game.objects.order_by("-realese_date")[:3]
    ]

    title_list:list[str] = []
    games_list:list[list[Game]] = []

    while len(title_list) != 4:
        i:int = random.randint(0, len(pull)-1)
        title = pull[i]

        if title in title_list:
            continue

        query = queries[i]

        games = []
        for n in range(3):
            games.append(query[n])

        title_list.append(title)
        games_list.append(games)
        
    return title_list, games_list





def get_tag_by_name(tag_url_name:str) -> Tag:
    tag_name = Tag.name_from_url(tag_url_name)
    return get_object_or_404(Tag, name__iexact=tag_name)


def get_games_by_tag(tag:Tag, limit:int):
    games = Game.objects.filter(tags__in=tag).order_by("?")

    if limit == -1:
        return games
    else:
        return games[:limit]



def get_dev_by_name(dev_url_name:str) -> Dev:
    dev_name = Dev.name_from_url(dev_url_name)
    return get_object_or_404(Dev, name__iexact=dev_name)


def get_games_by_dev(dev:Dev, limit:int):
    games = Game.objects.filter(dev=dev).order_by("?")

    if limit == -1:
        return games
    else:
        return games[:limit]



def search_games_by_title(title:str):
    games = Game.objects.filter(title__icontains=title).order_by("title")
    return games


def get_game_by_title(game_title_ulr:str):
    game_title = Game.name_from_url(game_title_ulr)
    return get_object_or_404(Game, title__iexact=game_title)