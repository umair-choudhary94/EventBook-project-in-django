# Generated by Django 4.2.1 on 2023-06-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_event_event_type_alter_event_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('in_person', 'In-Person'), ('online', 'Online')], default='in_person', max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='state',
            field=models.TextField(default='', max_length=200),
        ),
    ]
