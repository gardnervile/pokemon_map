from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pokemons/', null=True, blank=True)
    description = models.TextField(blank=True)
    title_en  = models.CharField(max_length=255, null=True)
    title_jp = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank = True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)
# your models here
