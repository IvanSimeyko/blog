# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20150607_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_modified_date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
