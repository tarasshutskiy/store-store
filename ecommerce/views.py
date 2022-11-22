from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Game, Genre, Platform


class PlatformGenreYear:
    """Фільтр відображення на сторінці"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Game.objects.filter(draft=False).distinct('year')

    def get_countries(self):
        return Game.objects.filter(draft=False).distinct('country')

    def get_platforms(self):
        return Platform.objects.all()


class GameView(PlatformGenreYear, ListView):
    '''Список Ігр'''
    model = Game
    paginate_by = 6
    queryset = Game.objects.filter(draft=False)
    template_name = "game_list.html"
    context_object_name = 'game_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            game_list = Game.objects.filter(
                title__icontains=query,
                draft=False).select_related('games_line',)
            return game_list
        else:
            game_list = Game.objects.filter(draft=False).select_related('games_line',)
            return game_list


class PlatformView(PlatformGenreYear, ListView):
    '''Список ігор по платформі'''
    model = Game
    queryset = Game.objects.filter(draft=False)
    template_name = "platform_list.html"
    context_object_name = 'platform'

    def get_queryset(self):
        return Game.objects.filter(platform__url=self.kwargs['platform_slug'])


class GenreView(PlatformGenreYear, ListView):
    '''Список ігор по жанрам'''
    model = Game
    queryset = Game.objects.filter(draft=False)
    template_name = "genres_list.html"
    context_object_name = 'genres'

    def get_queryset(self):
        return Game.objects.filter(genres__url=self.kwargs['genres_slug'])


class GameDetailView(PlatformGenreYear, DetailView):
    '''Деталізація ігри'''
    model = Game
    slug_field = 'url'
    template_name = "game_detail.html"


class FilterGameView(PlatformGenreYear, ListView):
    """Робота фільтру"""
    template_name = "game_list.html"

    def get_queryset(self):
        queryset = Game.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(country__in=self.request.GET.getlist('country')) |
            Q(genres__in=self.request.GET.getlist('genre')) |
            Q(platform__in=self.request.GET.getlist('platform'))
        ).distinct()
        return queryset


