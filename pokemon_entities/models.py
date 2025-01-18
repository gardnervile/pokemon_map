from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя покемона')
    image = models.ImageField(upload_to='pokemons/', null=True, blank=True, verbose_name='Изображение покемона')
    description = models.TextField(blank=True, verbose_name='Описание')
    title_en = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя покемона на английском')
    title_jp = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя покемона на японском')
    evolved_from = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='evolutions', verbose_name='Эволюционирует из')
    evolves_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='evolves_from', verbose_name='Эволюционирует в')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)