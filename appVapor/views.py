from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'shop/shop_main.html')



def category(request, category_name:str):
    return render(request, 'category.html')


def dev(request, dev_name:str):
    return render(request, 'developer.html')
