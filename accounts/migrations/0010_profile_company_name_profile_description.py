# Generated by Django 4.2.1 on 2023-06-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_profile_followers_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
    ]
