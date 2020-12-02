# Generated by Django 3.1.3 on 2020-11-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rej', '0021_auto_20201128_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Ginekolog'), (2, 'Dermatolog'), (0, 'Pediatra'), (3, 'Laryngolog'), (1, 'Alergolog')], default=0),
        ),
        migrations.AlterField(
            model_name='visit',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'Teleporada'), (1, 'Normalna_wizyta')], default=0),
        ),
    ]
