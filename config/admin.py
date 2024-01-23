"""Custom configuration for the admin."""
from admin_site_search.views import AdminSiteSearchView
from django.contrib import admin
from django.contrib.admin.apps import AdminConfig


class CustomAdminSite(AdminSiteSearchView, admin.AdminSite):
    """Extends the admin site with site search, and custom headers/titles"""

    site_header = "DJ-Template Administration"
    site_title = "dj-template"
    index_title = "Admin"


class CustomAdminConfig(AdminConfig):
    """Extends the admin config to change the default site"""

    default_site = "config.admin.CustomAdminSite"
