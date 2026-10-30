from django.shortcuts import render
from django.http import HttpRequest, QueryDict, HttpResponse
from . import services, models

# Create your views here.



def index(request:HttpRequest):
    context:dict = {}
    context["big_sales"] = services.get_big_sale()
    context["title_list"], context["games_list"] = services.get_shop_games()
    
    return render(request, 'shop/shop_main.html', context)


def category(request:HttpRequest, category_name:str):
    context:dict = {}

    context["tag"] = services.get_tag_by_name(category_name)

    if not isinstance(context["tag"], models.Tag):
        return HttpResponse(context["tag"])

    context["games_list"] = services.get_games_by_tag(context["tag"], 3)
    
    return render(request, 'shop/category.html', context)


def dev(request:HttpRequest, dev_name:str):
    context:dict = {}

    context["developer"] = services.get_dev_by_name(dev_name)

    if not isinstance(context["developer"], models.Dev):
        return HttpResponse(context["developer"])

    context["games_list"] = services.get_games_by_dev(context["developer"], 3)
    
    return render(request, 'shop/developer.html', context)


def search(request:HttpRequest):
    query_string:str = request.META.get('QUERY_STRING', '')
    query_dict:QueryDict = QueryDict(query_string, encoding="UTF-8")
    name:str = query_dict.get('name', '')

    context:dict = {}
    context["games_list"] = services.search_games_by_title(name)

    return render(request, 'shop/search.html', context)



def game(request:HttpRequest, game_name:str):
    context:dict = {}

    context["game"] = services.get_game_by_title(game_name)

    if not isinstance(context["game"], models.Game):
        return HttpResponse(context["game"])
    
    return render(request, 'shop/store.html', context)
