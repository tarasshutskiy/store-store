from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Game, Genre, Platform


class PlatformGenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Game.objects.filter(draft=False).distinct('year')

    def get_platforms(self):
        return Platform.objects.all()


class GameView(PlatformGenreYear, ListView):
    ''''''
    model = Game
    paginate_by = 6
    queryset = Game.objects.filter(draft=False)
    template_name = "game_list.html"
    context_object_name = 'game_list'


class GameDetailView(PlatformGenreYear, DetailView):
    ''''''
    model = Game
    slug_field = 'url'
    template_name = "game_detail.html"


class FilterGameView(PlatformGenreYear, ListView):
    template_name = "game_list.html"

    def get_queryset(self):
        queryset = Game.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre')) |
            Q(platform__in=self.request.GET.getlist('platform'))
        ).distinct()
        return queryset


