# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(u"Заголовок", max_length=150)
    text = models.TextField(u"Текст")
    date_create = models.DateTimeField(u"Дата создания", auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return u'{} {}'.format(self.title, self.date_create)