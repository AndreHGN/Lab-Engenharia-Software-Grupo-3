# Generated by Django 3.2.8 on 2021-11-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lote', '0011_auto_20211112_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='leilao',
            name='cancelar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leilao',
            name='confirmaPagamento',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leilao',
            name='vencedor',
            field=models.CharField(default=None, max_length=200),
        ),
    ]