# Generated by Django 4.2.10 on 2024-02-12 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_alter_vendas_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itensvendas',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='vendas.vendas'),
        ),
    ]
