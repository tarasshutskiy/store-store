from django.contrib import admin
from .models import Platform, GameLine, Company, Genre, GameShots, Game, Comment

admin.site.register(Platform)
admin.site.register(GameLine)
admin.site.register(Company)
admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(GameShots)
admin.site.register(Comment)