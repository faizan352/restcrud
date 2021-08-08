from django.contrib import admin
from .models import StreamPlatform, WatchList


# Register your models here.

@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'about', 'website']


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'storyline', 'active']
