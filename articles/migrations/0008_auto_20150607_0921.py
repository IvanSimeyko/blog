# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_article_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 7, 9, 21, 36, 602212), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='article_publish',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='article_short_description',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
