# Generated by Django 3.0.2 on 2021-05-30 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0006_commander'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commander',
            name='dateCde',
            field=models.DateField(default=datetime.date(2021, 5, 30), null=True),
        ),
    ]
