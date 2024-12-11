from django.db import models
from django.db.models import JSONField
from master.utils import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Make(BaseModel):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(
        default=False,
        blank=True,
        null=True,
        db_index=True)
    slug = models.SlugField(
        blank=True,
        null=True,
        max_length=100,
        unique=True,
        db_index=True)
    dump_data = JSONField(null=True, blank=True, default=dict)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Model(BaseModel):

    make = models.ForeignKey(Make, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, default=None)
    slug = models.SlugField(blank=True, null=True, max_length=100)
    dump_data = JSONField(null=True, blank=True, default=dict)

    def save(self, *args, **kwargs):
        self.slug = slugify(
            "{make} {model}".format(
                make=self.make.name,
                model=self.name))
        super().save(*args, **kwargs)

class Variant(BaseModel):

    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, default=None)
    slug = models.SlugField(blank=True, null=True, max_length=100)
    dump_data = JSONField(null=True, blank=True, default=dict)

    def save(self, *args, **kwargs):
        self.slug = slugify(
            "{make} {model} {variant}".format(
                make=self.model.make.name,
                model=self.model.name,
            variant=self.name))
        super().save(*args, **kwargs)


class VariantColor(BaseModel):

    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, default=None)
    slug = models.SlugField(blank=True, null=True, max_length=100)
    dump_data = JSONField(null=True, blank=True, default=dict)

    def save(self, *args, **kwargs):
        self.slug = slugify(
            "{make} {model} {variant}".format(
                make=self.model.make.name,
                model=self.model.name,
            variant=self.name))
        super().save(*args, **kwargs)
