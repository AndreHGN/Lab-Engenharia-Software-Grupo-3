# Generated by Django 3.2.8 on 2021-11-18 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lote', '0013_alter_leilao_vencedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='leilao',
            field=models.IntegerField(default=None),
        ),
    ]
