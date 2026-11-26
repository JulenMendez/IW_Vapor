from django.urls import path
from . import views

urlpatterns =  [
    path('', views.index , name='index'),
    path('category/<str:category_name>', views.category, name='category'),
    path('dev/<str:dev_name>', views.dev, name='dev'),
    path('search', views.search, name='search'),
    path('games/<str:game_name>', views.game, name='game'),
    path('ajax/search-preview', views.ajax_search_preview, name='ajax_search_preview'),
    path('qtip/game-desc/<str:game_name>', views.qtip_game_desc, name='qtip_game_desc')
]

