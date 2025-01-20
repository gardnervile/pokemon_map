from django.db import migrations

def replace_null_with_empty_string(apps, schema_editor):
    Pokemon = apps.get_model('pokemon_entities', 'Pokemon')
    Pokemon.objects.filter(title_en__isnull=True).update(title_en='')
    Pokemon.objects.filter(title_jp__isnull=True).update(title_jp='')

class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20250120_1541'),
    ]

    operations = [
        migrations.RunPython(replace_null_with_empty_string),
    ]
