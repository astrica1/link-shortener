from tabnanny import verbose
from django.contrib import admin
from . import models

class UrlAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'user', 'long_url', 'valid_until')
    list_filter = ('created_at', 'valid_until', 'user')
    search_fields = ('short_url', 'long_url', 'user')
    ordering = ('-created_at', 'user')
    date_hierarchy = 'created_at'
    list_per_page = 25
    verbose_name = 'URL'
    
admin.site.register(models.Url, UrlAdmin)