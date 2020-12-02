# Generated by Django 3.1.3 on 2020-11-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rej', '0018_auto_20201128_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Laryngolog'), (4, 'Ginekolog'), (1, 'Alergolog'), (2, 'Dermatolog'), (0, 'Pediatra')], default=0),
        ),
    ]