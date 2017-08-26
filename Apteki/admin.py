from django.contrib import admin
from .models import Lekarstv

#admin.site.register(Lekarstv)

@admin.register(Lekarstv)
class AdminLekarstv(admin.ModelAdmin):
    list_display=["name", "price"]

