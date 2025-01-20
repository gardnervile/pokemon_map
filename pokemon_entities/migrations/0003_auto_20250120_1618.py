# Generated by Django 3.1.14 on 2025-01-20 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_remove_pokemon_evolves_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='evolved_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evolves_to', to='pokemon_entities.pokemon', verbose_name='Эволюционирует из'),
        ),
    ]
