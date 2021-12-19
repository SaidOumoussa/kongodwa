from django.db import models
from django.utils.text import slugify
from django.utils import timezone
import datetime


def img(instance, filename):
    image_name, extension = filename.split(".")
    return 'product/%s.%s' % (instance.id, extension)


class Product(models.Model):
    product = models.CharField(max_length=89, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField(max_length=150)
    active = models.BooleanField(default=True)
    service = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to='img')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product

