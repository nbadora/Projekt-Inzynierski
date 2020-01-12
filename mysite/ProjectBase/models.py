from django.db import models
from django import forms

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name="Product Name")
    producent_name = models.CharField(max_length=200, verbose_name="Producent Name")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price")
    availability = models.BooleanField(verbose_name='Avaliable')
    count = models.PositiveSmallIntegerField(verbose_name='In Stock')
    image = models.ImageField(verbose_name='Picture', blank=True, upload_to="gallery")
    desc = models.CharField(max_length=1000, verbose_name="Product Description", default='')

    def __str__(self):
        return self.product_name

class Service(models.Model):
    service_name = models.CharField(max_length=200, verbose_name='Service Name')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price")
    desc = models.CharField(max_length=1000, verbose_name="Product Description", default='')

    def __str__(self):
        return self.service_name

class New(models.Model):
    news_title = models.CharField(max_length=200, verbose_name="Title")
    details = models.CharField(max_length=1000, verbose_name="News details", default='0000000')
    created_on = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    # updated_on = models.DateTimeField(auto_now= True, blank = True, null = True)

    def __str__(self):
        return self.news_title


        