# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='country',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='country_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='hradba',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='infoport',
            field=models.PositiveSmallIntegerField(default=15425),
        ),
        migrations.AlterField(
            model_name='server',
            name='maxplayers',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='server',
            name='numplayers',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='server',
            name='offline_since',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='port',
            field=models.PositiveSmallIntegerField(default=5425),
        ),
    ]
