from django.urls import path
from . import views

urlpatterns =  [
    path('', views.index , name='index'),
    path('category/<str:category_name>', views.category, name='category'),
    path('dev/<str:dev_name>', views.dev, name='dev'),
    path('search', views.search, name='search'),
]

