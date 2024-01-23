"""Core admin config, shared across all apps"""
from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    """Adds created/updated_at filtering and ordering"""

    readonly_fields = ("created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)
