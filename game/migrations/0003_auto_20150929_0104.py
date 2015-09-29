# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20150929_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='map',
            field=models.ForeignKey(to='game.Map', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='mode',
            field=models.ForeignKey(to='game.Mode', null=True, blank=True),
        ),
    ]
