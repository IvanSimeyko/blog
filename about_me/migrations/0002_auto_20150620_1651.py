# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_me',
            name='info',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
