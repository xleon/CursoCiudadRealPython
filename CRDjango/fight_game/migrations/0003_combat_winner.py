# Generated by Django 2.0.4 on 2018-04-23 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fight_game', '0002_auto_20180423_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='combat',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='combat_winner', to='fight_game.Fighter', verbose_name='Ganador'),
        ),
    ]
