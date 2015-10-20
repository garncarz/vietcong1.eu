# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20151009_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(upload_to=game.models.MapImage.upload_to)),
                ('map', models.ForeignKey(to='game.Map', related_name='images')),
            ],
        ),
    ]
