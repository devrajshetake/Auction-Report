# Generated by Django 4.0.5 on 2022-08-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_player_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.FloatField(default=0),
        ),
    ]