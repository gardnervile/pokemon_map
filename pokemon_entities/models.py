from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя покемона')
    image = models.ImageField(upload_to='pokemons/', null=True, blank=True, verbose_name='Изображение покемона')
    description = models.TextField(blank=True, verbose_name='Описание')
    title_en = models.CharField(max_length=255, blank=True, verbose_name='Имя покемона на английском')
    title_jp = models.CharField(max_length=255, blank=True, verbose_name='Имя покемона на японском')
    evolved_from = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_forms', verbose_name='Эволюционирует из')
   

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities', verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время исчезновения')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')