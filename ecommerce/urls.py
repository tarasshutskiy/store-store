from django.contrib import admin
from django.urls import path
from .views import GameView, GameDetailView, FilterGameView, PlatformView, GenreView

urlpatterns = [
    path('', GameView.as_view(), name='game_list'),
    path('filter/', FilterGameView.as_view(), name='filter'),
    path('<slug:slug>/', GameDetailView.as_view(), name='game_detail'),
    path('platform/<slug:platform_slug>/', PlatformView.as_view(), name='platform'),
    path('genres/<slug:genres_slug>/', GenreView.as_view(), name='genres'),
]
