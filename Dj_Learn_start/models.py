# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from Apteki.models import Lekarstv


class Post(models.Model):

    title = models.CharField(u"Заголовок", max_length=150)
    text = models.TextField(u"Текст")
    date_create = models.DateTimeField(u"Дата создания", auto_now_add=True)

    class Meta:
        ordering = ['-date_create']

    def __str__(self):
        """Возвращает строковое представление модели."""
        return u'{} {}'.format(self.title, self.date_create)



class Order(models.Model):
    lekarstvo = models.ForeignKey(Lekarstv, verbose_name='Лекарство')
    name = models.CharField("name", max_length=50)
    #price = models.CharField("price", max_length=50)
    #address = models.CharField("adress", max_length=50)