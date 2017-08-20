# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Lekarstvo(models.Model):
    name_lek = models.CharField("Наименование", max_length=150)
    price_lek = models.IntegerField("цена")
    apteka_adress = models.TextField("Адрес аптеки")

    class Meta:
        verbose_name = "Лекарство"
        verbose_name_plural = "Лекарства"

    def __str__(self):
        return self.name_lek