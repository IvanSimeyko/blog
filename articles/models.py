# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
#import PIL


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(article_publish=True)


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_short_description = models.TextField()
    #article_image = models.ImageField(null=True, blank=True)
    article_text = models.TextField()
    article_date = models.DateTimeField(auto_now_add=True)
    article_modified_date = models.DateTimeField(auto_now=True)
    article_publish = models.BooleanField(default=True)
    article_likes = models.IntegerField(default=0)
    article_tags = models.ManyToManyField(Tag)
    #article_slug = models.SlugField(max_length=25, default='ivan')

    objects = ArticleQuerySet.as_manager()

    class Meta():
        db_table = 'article'
        ordering = ['-article_date']
        verbose_name = 'Article'
        verbose_name_plural = "Articles"


class Comment(models.Model):

    class Meta():
        db_table = 'comment'

    comment_name = models.ForeignKey(User)
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_article = models.ForeignKey(Article)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_likes = models.IntegerField(default=0)
