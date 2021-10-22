# Generated by Django 2.0.5 on 2018-05-11 15:11

from django.db import migrations, models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('vendedor', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=100)),
                ('valorMinimo', models.IntegerField()),
                ('valorReserva', models.IntegerField()),
                ('valorMinimoLance', models.IntegerField()),
                ('inicioLeilao', models.DateField()),
                ('finalLeilao', models.DateField()),
                ('tipoInicial', models.IntegerField()),
                ('tipoFinal', models.IntegerField()),
            ],
        ),
    ]
