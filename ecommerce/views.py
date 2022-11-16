from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View


from .models import Game


class GameView(ListView):
    ''''''
    model = Game
    queryset = Game.objects.filter(draft=False)
    template_name = "game_list.html"


class GameDetailView(DetailView):
    ''''''
    model = Game
    slug_field = 'url'
    template_name = "game_detail.html"


