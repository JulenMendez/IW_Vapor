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
        
