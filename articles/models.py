from django.db import models
import datetime


class Article(models.Model):

    class Meta():
        db_table = 'article'

    article_title = models.CharField(max_length=100)
    article_image = models.ImageField(null=True, blank=True)
    article_text = models.TextField()
    article_date = models.DateTimeField(auto_now_add=True)
    article_likes = models.IntegerField()
