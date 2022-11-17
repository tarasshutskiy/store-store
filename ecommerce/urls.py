from django.contrib import admin
from django.urls import path
from .views import GameView, GameDetailView, GenreView

urlpatterns = [
    path('', GameView.as_view(), name='game_list'),
    path('genres/<slug:genre_slug>/', GenreView.as_view(), name='genres'),
    path('<slug:slug>/', GameDetailView.as_view(), name='game_detail'),
]
