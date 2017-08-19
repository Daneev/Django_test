"""Определяет схемы URL для learning_logs."""
from django.conf.urls import url
from Dj_Learn_start import views

urlpatterns = [
# Домашняя страница
    url(r'^$', views.post_list, name='post_list'),
]