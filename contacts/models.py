# -*- coding: utf-8 -*-
from django.db import models
import datetime


class Contact(models.Model):
    contact_name = models.CharField(verbose_name='Ваше имя', max_length=25)
    contact_subject = models.CharField(verbose_name='Тема сообщения', max_length=100)
    contact_text = models.TextField(verbose_name='Текст сообщения')
    contact_email = models.EmailField(verbose_name='Ваш email для ответа',)
    contact_date = models.DateTimeField(verbose_name='Дата сообщения', blank=False, default=datetime.datetime.now)

    def __unicode__(self):
        return self.contact_name