# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_remove_article_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_tags',
            field=models.ManyToManyField(to='articles.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
