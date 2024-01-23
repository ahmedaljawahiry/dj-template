"""Core models, shared across all apps"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """Adds created/updated_at fields"""

    created_at = models.DateTimeField(
        auto_now_add=True, null=True, help_text=_("When this instance was created")
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, help_text=_("When this instance was last updated")
    )

    class Meta:
        ordering = ["created_at"]
        abstract = True

    def __str__(self):
        return str(self.id)
