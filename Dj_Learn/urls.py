"""Dj_Learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Apteki.views import list, detail
from Dj_Learn_start.views import post_detail, test, post_list, addcomment
from django.conf.urls.static import static
from django.conf import settings


lekpatterns = [
    url(r'^list/', list, name='list'),
    url(r'^detail/(?P<lekarstv_id>\d+)/$', detail, name='detail'),
]

urlpatterns = [
    url(r'^test/', test, name='test'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/addcomment/$', addcomment, name='addcomment'),
    url(r'^admin/', admin.site.urls),
    url(r'^lekarstv/', include(lekpatterns)),
    url(r'^auth/', include("loginsys.urls")),
    url(r'^$', post_list, name='post_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

