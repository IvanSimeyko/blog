# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_article_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_slug',
        ),
    ]
