# Generated by Django 3.0.2 on 2021-04-23 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='emballag',
        ),
    ]
