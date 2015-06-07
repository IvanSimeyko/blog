# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20150603_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_short_description',
            field=models.CharField(max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
