# Generated by Django 3.2.8 on 2021-11-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lote', '0007_auto_20211112_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='taxaDeComissao',
            field=models.FloatField(default=None, null=True),
        ),
    ]