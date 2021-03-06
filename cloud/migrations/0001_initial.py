# Generated by Django 3.0.2 on 2021-05-30 20:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('fileId', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 5, 30, 20, 29, 39, 530448), max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, null=0)),
                ('password', models.CharField(max_length=50, null=0)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('folderId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 5, 30, 20, 29, 39, 530843))),
                ('files', models.ManyToManyField(blank=True, null=True, related_name='ffile', to='cloud.File')),
                ('sharedUsers', models.ManyToManyField(blank=True, null=True, related_name='users', to='cloud.User')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.User')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='userId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.User'),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('contentId', models.AutoField(null=0, primary_key=True, serialize=False)),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cfile', to='cloud.File')),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cfolder', to='cloud.Folder')),
            ],
        ),
        migrations.CreateModel(
            name='cloud',
            fields=[
                ('cloudId', models.AutoField(null=0, primary_key=True, serialize=False)),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='cloud.Content')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='cloud.User')),
            ],
        ),
    ]
