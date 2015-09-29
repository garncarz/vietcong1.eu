# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20150929_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='server',
            field=models.ForeignKey(related_name='players', to='game.Server'),
        ),
    ]
