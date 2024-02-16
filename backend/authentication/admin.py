from django.contrib import admin
from .models import Token
# Register your models here.


admin.site.register(Token)
class TokenAdmin(admin.ModelAdmin):
  list_display = ('token', 'user')
  fields = ('token', 'user')
  readonly_fields = ('token', 'user')
