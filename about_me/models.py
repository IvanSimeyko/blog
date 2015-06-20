from django.db import models


class About_me(models.Model):
    info = models.TextField()

    class Meta():
        db_table = 'about_me'
