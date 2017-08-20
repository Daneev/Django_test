from django.contrib import admin
from Lekarstvo.models import Lekarstvo

#admin.site.register(Lekarstvo)

@admin.register(Lekarstvo)
class AdminLekarstvo(admin.ModelAdmin):
    list_display=["name_lek", "price_lek"]

