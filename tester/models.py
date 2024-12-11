from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
from django.core.validators import MaxValueValidator, MinValueValidator


def default_product_image():
    return "product_images/default.jpg"


class ConfigurableDataTable(models.Model):
    provider_name = models.CharField(max_length=100, blank=True, null=True)
    intrest_rate = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=False,
        null=False
    )
    image = models.ImageField(default=None)
    is_active = models.BooleanField(default=True)
