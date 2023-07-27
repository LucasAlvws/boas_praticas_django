from django.contrib import admin
from .models import Fotografia

# Register your models here.

class FotografiaList(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "categoria", "foto", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Fotografia, FotografiaList)
