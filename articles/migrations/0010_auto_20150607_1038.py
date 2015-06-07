# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20150607_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-article_date'], 'verbose_name': 'Blog Entry', 'verbose_name_plural': 'Blog Entries'},
        ),
        migrations.AddField(
            model_name='article',
            name='article_tags',
            field=models.ManyToManyField(to='articles.Tag'),
            preserve_default=True,
        ),
    ]
