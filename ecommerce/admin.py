from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Platform, GameLine, Company, Genre, GameShots, Game, Comment


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
    list_display_links = ('title',)


@admin.register(GameLine)
class GameLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image')
    list_display_links = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')

    get_image.short_description = 'Image'

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image')
    list_display_links = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')

    get_image.short_description = 'Image'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
    list_display_links = ('title',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_poster', 'url', 'year', 'draft')
    list_filter = ('platform', 'company', 'genres', 'year')
    search_fields = ('title', 'platform__title')
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    fieldsets = (
        ("Game", {
            "fields": (('title', 'games_line', 'company'),)
        }),
        ("Info", {
            "fields": (('descriptions', 'get_poster', 'poster'),)
        }),
        ("Platform and Genre", {
            'classes': ('collapse',),
            "fields": (('platform', 'genres'),)
        }),
        ("Other", {
            "fields": (('year', 'country', 'price', 'url'),)
        }),
        ("Publish", {
            "fields": (('draft',),)
        }),
    )
    readonly_fields = ('get_poster',)

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="50"')

    get_poster.short_description = 'Image'



@admin.register(GameShots)
class GameShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'game')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('game', 'author', 'time_create')
