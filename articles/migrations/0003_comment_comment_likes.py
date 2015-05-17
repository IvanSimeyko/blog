# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20150517_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_likes',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
