# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20150929_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='frags',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='ping',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
