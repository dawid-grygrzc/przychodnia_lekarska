# Generated by Django 3.1.3 on 2020-11-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rej', '0011_auto_20201128_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Ginekolog'), (0, 'Pediatra'), (2, 'Dermatolog'), (1, 'Alergolog'), (3, 'Laryngolog')], default=0),
        ),
    ]
