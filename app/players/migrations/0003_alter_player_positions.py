# Generated by Django 3.2 on 2021-04-15 18:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_rename_players_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='positions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None),
        ),
    ]
