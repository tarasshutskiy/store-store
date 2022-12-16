
from django.db import models
from django.urls import reverse


class Platform(models.Model):
    '''Платформа'''
    title = models.CharField('Назва', max_length=120)
    description = models.TextField('Описання')
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформи'

    def get_absolute_url(self):
        return reverse('platform', kwargs={'platform_slug': self.url})

class GameLine(models.Model):
    '''Лінійка Гри'''
    title = models.CharField('Назва', max_length=120)
    descriptions = models.TextField('Описання')
    image = models.ImageField('Зображення', upload_to='game_line/')

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Лінійка гри'
        verbose_name_plural = 'Лінійка ігор'


class Company(models.Model):
    ''''''
    title = models.CharField('Назва', max_length=140)
    descriptions = models.TextField('Описання')
    image = models.ImageField('Зображення', upload_to='company/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компанія'
        verbose_name_plural = 'Компанії'


class Genre(models.Model):
    '''Жанр'''
    title = models.CharField('Назва', max_length=140)
    descriptions = models.TextField('Описання')
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genres', kwargs={'genres_slug': self.url})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'


class Game(models.Model):
    '''Гра'''
    title = models.CharField('Назва', max_length=140)
    games_line = models.ForeignKey(
        GameLine, verbose_name='Лінійка гри', on_delete=models.SET_NULL, null=True
    )
    descriptions = models.TextField('Описання')
    poster = models.ImageField('Постер', upload_to='games/')
    year = models.PositiveSmallIntegerField('Рік', default=2022)
    country = models.CharField('Країна', max_length=40)
    platform = models.ManyToManyField(Platform, verbose_name='Платформа', related_name='game_platform')
    genres = models.ManyToManyField(Genre, verbose_name='Жанри', related_name='game_genres')
    company = models.ForeignKey(
        Company, verbose_name='Компанія', on_delete=models.SET_NULL, null=True
    )
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    url = models.SlugField(max_length=120)
    draft = models.BooleanField('Чорновик', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Гра'
        verbose_name_plural = 'Ігри'


class GameShots(models.Model):
    '''Зображення з гри'''
    title = models.CharField('Назва', max_length=140)
    descriptions = models.TextField('Описання')
    game = models.ForeignKey(
        Game, verbose_name='Гра', on_delete=models.CASCADE
    )
    image = models.ImageField('Зображення', upload_to='gamesshots/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Зображення з гри'
        verbose_name_plural = 'Зображення з ігор'


