# Generated by Django 4.2.10 on 2024-02-11 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(db_index=True, max_length=11, unique=True),
        ),
    ]
