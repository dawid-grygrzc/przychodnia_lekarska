# Generated by Django 3.1.3 on 2020-11-21 18:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rej', '0002_doctor_visit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='visit_date',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='visit_time',
        ),
        migrations.AddField(
            model_name='visit',
            name='visit_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Pediatra'), (1, 'Alergolog'), (2, 'Dermatolog'), (4, 'Ginekolog'), (3, 'Laryngolog')], default=0),
        ),
        migrations.AlterField(
            model_name='visit',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Normalna wizyta'), (0, 'Teleporada')]),
        ),
    ]
