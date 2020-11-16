# Generated by Django 3.1.3 on 2020-11-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rej', '0002_auto_20201116_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lekarz',
            name='specjalizacja',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Ginekolog'), (0, 'Pediatra'), (3, 'Laryngolog'), (1, 'Alergolog'), (2, 'Dermatolog')], default=0),
        ),
        migrations.AlterField(
            model_name='wizyta',
            name='godzina_wizyty',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='wizyta',
            name='rodzaj_wizyty',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'Teleporada'), (1, 'Normalna wizyta')]),
        ),
    ]