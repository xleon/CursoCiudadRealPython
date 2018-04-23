# Generated by Django 2.0.4 on 2018-04-23 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Fecha/hora de inicio')),
            ],
            options={
                'verbose_name': 'Luchador',
                'verbose_name_plural': 'Luchadores',
            },
        ),
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=10, verbose_name='Alias')),
                ('skills', models.IntegerField(default=0)),
                ('force', models.IntegerField(default=0)),
                ('resistance', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Luchador',
                'verbose_name_plural': 'Luchadores',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Nombre')),
                ('start_date', models.DateTimeField(verbose_name='Fecha/hora de inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha/hora final')),
                ('category', models.IntegerField(choices=[(0, 'Pluma'), (1, 'Medio'), (2, 'Pesado')], default=0, verbose_name='Categoría')),
                ('fighters', models.ManyToManyField(to='fight_game.Fighter', verbose_name='Luchadores')),
            ],
            options={
                'verbose_name': 'Torneo',
            },
        ),
        migrations.AddField(
            model_name='combat',
            name='fighter1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cf1', to='fight_game.Fighter', verbose_name='Luchador 1'),
        ),
        migrations.AddField(
            model_name='combat',
            name='fighter2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cf2', to='fight_game.Fighter', verbose_name='Luchador 2'),
        ),
        migrations.AddField(
            model_name='combat',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fight_game.Tournament', verbose_name='Torneo'),
        ),
    ]
