from django.shortcuts import render
from django.http import HttpRequest, QueryDict, HttpResponse
from . import services

# Create your views here.



def index(request:HttpRequest):
    context:dict = {}
    context["big_sales"] = services.get_big_sale()
    context["title_list"], context["games_list"] = services.get_shop_games()
    
    return render(request, 'shop/shop_main.html', context)



def category(request:HttpRequest, category_name:str):
    return render(request, 'category.html')


def dev(request:HttpRequest, dev_name:str):
    return render(request, 'developer.html')


def search(request:HttpRequest):
    query_string:str = request.META.get('QUERY_STRING', '')
    query_dict:QueryDict = QueryDict(query_string, encoding="UTF-8")
    name:str = query_dict.get('name', '')

    return HttpResponse(f"Has buscado:{name}.")



