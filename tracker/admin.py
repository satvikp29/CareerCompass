from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("company", "role", "status", "owner", "created_at")
    list_filter = ("status", "source", "created_at")
    search_fields = ("company", "role", "notes")
