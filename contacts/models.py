# -*- coding: utf-8 -*-
from django.db import models
import datetime


class Contact(models.Model):
    contact_name = models.CharField(max_length=25)
    contact_subject = models.CharField(max_length=100)
    contact_text = models.TextField(null=True, blank=True)
    contact_email = models.EmailField()
    contact_date = models.DateTimeField(blank=False, default=datetime.datetime.now)

    def __unicode__(self):
        return self.contact_name