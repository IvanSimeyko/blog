# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_comment_comment_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
