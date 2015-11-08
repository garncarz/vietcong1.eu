# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_mapimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='online_since',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='server',
            name='online_since',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
