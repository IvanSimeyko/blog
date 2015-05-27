from django.db import models
#import PIL


class Article(models.Model):

    class Meta():
        db_table = 'article'

    article_title = models.CharField(max_length=100)
    #article_image = models.ImageField(null=True, blank=True)
    article_text = models.TextField()
    article_date = models.DateTimeField(auto_now_add=True)
    article_likes = models.IntegerField(default=0)


class Comment(models.Model):

    class Meta():
        db_table = 'comment'

    comment_text = models.TextField(verbose_name='Comment text')
    comment_article = models.ForeignKey(Article)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_likes = models.IntegerField(default=0)
