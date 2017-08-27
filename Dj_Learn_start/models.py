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
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Записи в блоге"

    def __str__(self):
        """Возвращает строковое представление модели."""
        return u'{} {}'.format(self.title, self.date_create)



class Order(models.Model):
    lekarstvo = models.ForeignKey(Lekarstv, verbose_name='Лекарство')
    name = models.CharField("Введите наименование лекарства ", max_length=50)
    #price = models.CharField("price", max_length=50)
    #address = models.CharField("adress", max_length=50)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, verbose_name="Комментарии")
    text = models.CharField("Текст комментария", max_length=200)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text