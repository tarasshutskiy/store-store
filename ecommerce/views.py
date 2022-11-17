from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Game, Genre


class GameView(ListView):
    ''''''
    model = Game
    paginate_by = 3
    queryset = Game.objects.filter(draft=False)
    template_name = "post/game_list.html"
    context_object_name = 'game_list'



class GameDetailView(DetailView):
    ''''''
    model = Game
    slug_field = 'url'
    template_name = "post/game_detail.html"


class GenreView(ListView):
    ''''''
    model = Genre
    template_name = "genres/genres.html"
    context_object_name = 'genres'

    def get_queryset(self):
        return Game.objects.filter(genres__url=self.kwargs['genre_slug'])