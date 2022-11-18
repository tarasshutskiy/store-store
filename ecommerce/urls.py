from django.contrib import admin
from django.urls import path
from .views import GameView, GameDetailView, FilterGameView

urlpatterns = [
    path('', GameView.as_view(), name='game_list'),
    path('filter/', FilterGameView.as_view(), name='filter'),
    path('<slug:slug>/', GameDetailView.as_view(), name='game_detail'),
]
