# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Apteki', '0001_initial'),
        ('Dj_Learn_start', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('lekarstvo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apteki.Lekarstv', verbose_name='Лекарство')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_create']},
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dj_Learn_start.Post', verbose_name='Комментарии'),
        ),
    ]