# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20150929_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='map',
            field=models.ForeignKey(blank=True, related_name='servers', null=True, to='game.Map'),
        ),
    ]
