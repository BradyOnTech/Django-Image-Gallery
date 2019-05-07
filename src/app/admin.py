from django.contrib import admin
from django.db import models
from .models import Album

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'published_date')
    list_filter = ('published_date')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'

    def save_model(self, request, obj, form, change):
        

admin.site.register(Album,AlbumAdmin)