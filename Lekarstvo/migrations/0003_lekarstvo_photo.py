# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lekarstvo', '0002_auto_20170820_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='lekarstvo',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='Lekarstvo/images', verbose_name='изображение'),
        ),
    ]
