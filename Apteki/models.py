# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Lekarstv(models.Model):
    name = models.CharField("Наименование", max_length=150)
    price = models.IntegerField("цена")
    address = models.TextField("Адрес аптеки")
    photo = models.ImageField("изображение", upload_to="Lekarstv/images", default="", blank=True)

    class Meta:
        verbose_name = "Лекарство"
        verbose_name_plural = "Лекарства"

    def __str__(self):
        return self.name