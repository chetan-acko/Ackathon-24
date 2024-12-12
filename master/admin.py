from django.contrib import admin

from master import models


# Register your models here.
@admin.register(models.Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "slug")

@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "make")

@admin.register(models.Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "model")

@admin.register(models.VariantColor)
class VariantColorAdmin(admin.ModelAdmin):
    list_display = ("Variant", "name")

@admin.register(models.BasicFeature)
class BasicFeatureAdmin(admin.ModelAdmin):
    list_display = ("variantcolor", "body_type", "fuel_type", "transmission_type")
