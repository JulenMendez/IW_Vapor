from django.shortcuts import render
from django.http import HttpRequest, QueryDict, HttpResponse

# Create your views here.


def index(request:HttpRequest):
    return render(request, 'shop/shop_main.html')



def category(request:HttpRequest, category_name:str):
    return render(request, 'category.html')


def dev(request:HttpRequest, dev_name:str):
    return render(request, 'developer.html')


def search(request:HttpRequest):
    query_string:str = request.META.get('QUERY_STRING', '')
    query_dict:QueryDict = QueryDict(query_string, encoding="UTF-8")
    name:str = query_dict.get('name', '')

    return HttpResponse(f"Has buscado:{name}.")



