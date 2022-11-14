from django.shortcuts import render
from django.views.generic.base import View

from .models import Game


class GameView(View):
    ''''''
    def get(self, request):
        games = Game.objects.all()
        return render(request, 'game.html', {'game_list': games})