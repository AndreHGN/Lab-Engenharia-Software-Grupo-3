# Generated by Django 3.2.8 on 2021-11-12 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lote', '0009_alter_pagamento_taxadecomissao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagamento',
            name='taxaDeComissao',
        ),
    ]
