# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('ping', models.PositiveSmallIntegerField()),
                ('frags', models.PositiveSmallIntegerField()),
                ('online', models.BooleanField(default=True)),
                ('online_since', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('infoport', models.PositiveSmallIntegerField()),
                ('port', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=256)),
                ('country', models.CharField(null=True, max_length=2)),
                ('country_name', models.CharField(null=True, max_length=50)),
                ('version', models.CharField(max_length=4)),
                ('hradba', models.CharField(null=True, max_length=4)),
                ('numplayers', models.PositiveSmallIntegerField()),
                ('maxplayers', models.PositiveSmallIntegerField()),
                ('password', models.BooleanField(default=False)),
                ('dedic', models.BooleanField(default=False)),
                ('vietnam', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=True)),
                ('online_since', models.DateTimeField(auto_now_add=True)),
                ('offline_since', models.DateTimeField(null=True)),
                ('map', models.ForeignKey(to='game.Map')),
                ('mode', models.ForeignKey(to='game.Mode')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='server',
            field=models.ForeignKey(to='game.Server'),
        ),
        migrations.AddField(
            model_name='map',
            name='modes',
            field=models.ManyToManyField(to='game.Mode'),
        ),
    ]
