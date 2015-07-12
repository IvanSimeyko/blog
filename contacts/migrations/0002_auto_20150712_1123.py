# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_email',
            field=models.EmailField(max_length=75, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x88 email \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_name',
            field=models.CharField(max_length=25, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x88\xd0\xb5 \xd0\xb8\xd0\xbc\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_subject',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_text',
            field=models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
    ]
