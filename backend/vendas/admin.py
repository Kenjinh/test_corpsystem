from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Vendas)
class VendasAdmin(admin.ModelAdmin):
  list_display = ('id', 'data', 'vendedor', 'cliente', 'is_active')
  list_display_links = ('id', 'data', 'vendedor', 'cliente')
  list_filter = ('data', 'vendedor', 'cliente')
  search_fields = ('data', 'vendedor', 'cliente')