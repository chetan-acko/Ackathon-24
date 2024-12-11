from django import forms
from django.utils.html import format_html
from django.contrib import admin

from .forms import ProviderForm
from .models import ConfigurableDataTable

class ConfigurableDataTableAdmin(admin.ModelAdmin):
    form = ProviderForm
    list_display = ('id','provider_name','intrest_rate', 'preview_image','is_active')  # Add 'id' for identification

    def preview_image(self, obj):
        if obj.image:
            image_url = obj.image.url
            # image_url  = 'https://ackodrive-uat-assets.s3.amazonaws.com/media/test.png'
            return format_html(f'<img src="{image_url}" width="30" />')
        else:
            return "No image"

    preview_image.short_description = 'Image Preview'

admin.site.register(ConfigurableDataTable, ConfigurableDataTableAdmin)
