from django.contrib import admin
from Apteki.models import Lekarstv

#admin.site.register(Lekarstv)

@admin.register(Lekarstv)
class AdminLekarstv(admin.ModelAdmin):
    list_display=["name", "price"]

