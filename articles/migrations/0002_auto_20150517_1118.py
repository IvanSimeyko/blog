# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_article', models.ForeignKey(to='articles.Article')),
            ],
            options={
                'db_table': 'comment',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
