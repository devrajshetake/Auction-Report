# Generated by Django 4.0.5 on 2022-08-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_alter_player_base_price_alter_player_selling_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
    ]