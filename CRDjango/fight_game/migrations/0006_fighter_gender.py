# Generated by Django 2.0.4 on 2018-04-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fight_game', '0005_auto_20180424_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='gender',
            field=models.CharField(choices=[('male', 'Masculino'), ('female', 'Femenino')], default='female', max_length=6, verbose_name='Sexo'),
        ),
    ]