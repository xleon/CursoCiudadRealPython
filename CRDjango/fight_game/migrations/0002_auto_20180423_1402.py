# Generated by Django 2.0.4 on 2018-04-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fight_game', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='combat',
            options={'verbose_name': 'Combate'},
        ),
        migrations.AlterField(
            model_name='fighter',
            name='alias',
            field=models.CharField(max_length=20, verbose_name='Alias'),
        ),
    ]