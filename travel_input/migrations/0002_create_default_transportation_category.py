from django.db import migrations

def create_default_category(apps, schema_editor):
    TransportationCategory = apps.get_model('travel_input', 'TransportationCategory')
    TransportationCategory.objects.get_or_create(
        id=1,
        defaults={'name': '기타'}
    )

def reverse_default_category(apps, schema_editor):
    TransportationCategory = apps.get_model('travel_input', 'TransportationCategory')
    TransportationCategory.objects.filter(id=1).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('travel_input', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_category, reverse_default_category),
    ] 