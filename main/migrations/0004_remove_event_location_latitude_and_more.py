# Generated by Django 4.2.1 on 2023-06-01 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_event_catagorey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location_latitude',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location_longitude',
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ]
