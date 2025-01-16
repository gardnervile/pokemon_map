from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pokemons/', null=True, blank=True)

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    
# your models here
