# Generated by Django 3.2 on 2021-04-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20210415_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
