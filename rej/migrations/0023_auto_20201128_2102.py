# Generated by Django 3.1.3 on 2020-11-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rej', '0022_auto_20201128_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Laryngolog'), (1, 'Alergolog'), (2, 'Dermatolog'), (4, 'Ginekolog'), (0, 'Pediatra')], default=0),
        ),
        migrations.AlterField(
            model_name='visit',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'Teleporada'), (1, 'Normalna_wizyta'), (2, 'xd')], default=0),
        ),
    ]
