"""Admin configuration of navigation."""

from django.contrib import admin
from navigation.models import Navigation, NavigationDropDown, NavigationLogo
from modeltranslation.admin import TranslationAdmin


@admin.register(Navigation)
class NavigationAdmin(TranslationAdmin):
    """Admin of the navigation item."""

    list_display = ("name", "url", "type", "order")
    ordering = ["order"]


@admin.register(NavigationDropDown)
class NavigationDropDownAdmin(admin.ModelAdmin):
    """Admin of the drop down item."""

    list_display = ("name", "url", "type", "order", "parent")
    ordering = ["order"]


@admin.register(NavigationLogo)
class NavigationLogoAdmin(admin.ModelAdmin):
    """Admin of the navigation logo."""

    list_display = ["name", "url", "image", "alt_text"]
