# Generated by Django 3.2.16 on 2022-11-14 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(max_length=140, verbose_name='Назва')),
                ('descriptions', models.TextField(verbose_name='Описання')),
                ('image', models.ImageField(upload_to='company/', verbose_name='Зображення')),
            ],
            options={
                'verbose_name': 'Компанія',
                'verbose_name_plural': 'Компанії',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(max_length=140, verbose_name='Назва')),
                ('descriptions', models.TextField(verbose_name='Описання')),
                ('poster', models.ImageField(upload_to='games/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2022, verbose_name='Рік')),
                ('country', models.CharField(max_length=40, verbose_name='Країна')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('url', models.SlugField(max_length=120)),
                ('draft', models.BooleanField(default=False, verbose_name='Чорновик')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.company', verbose_name='Компанія')),
            ],
            options={
                'verbose_name': 'Гра',
                'verbose_name_plural': 'Ігри',
            },
        ),
        migrations.CreateModel(
            name='GameLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(max_length=120, verbose_name='Назва')),
                ('descriptions', models.TextField(verbose_name='Описання')),
                ('image', models.ImageField(upload_to='game_line/', verbose_name='Зображення')),
            ],
            options={
                'verbose_name': 'Лінійка гри',
                'verbose_name_plural': 'Лінійка ігор',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(max_length=140, verbose_name='Назва')),
                ('descriptions', models.TextField(verbose_name='Описання')),
                ('url', models.SlugField(max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанри',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Описання')),
                ('url', models.SlugField(max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Платформа',
                'verbose_name_plural': 'Платформи',
            },
        ),
        migrations.CreateModel(
            name='GameShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(max_length=140, verbose_name='Назва')),
                ('descriptions', models.TextField(verbose_name='Описання')),
                ('image', models.ImageField(upload_to='company/', verbose_name='Зображення')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.game', verbose_name='Гра')),
            ],
            options={
                'verbose_name': 'Зображення з гри',
                'verbose_name_plural': 'Зображення з ігор',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='games_line',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.gameline', verbose_name='Лінійка гри'),
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(related_name='game_genres', to='ecommerce.Genre', verbose_name='Жанри'),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(related_name='game_platform', to='ecommerce.Platform', verbose_name='Платформа'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150, verbose_name='Коментарій')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час створення')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.game', verbose_name='Гра')),
            ],
            options={
                'verbose_name': 'Коментарій',
                'verbose_name_plural': 'Коментарії',
            },
        ),
    ]
