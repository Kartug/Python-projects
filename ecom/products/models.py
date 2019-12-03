from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(default="")
    primaryCategory = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:product", kwargs={
            'slug': self.slug
        })


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    mainimage = models.ImageField(
        upload_to='products/', blank=True, null=True)
    # image_url = models.CharField(max_length=2083)
    slug = models.SlugField(default="")
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    # category = models.ForeignKey(
    #     Category, on_delete=models.CASCADE, default="0", editable=False, null=True)
    preview_text = models.TextField(
        max_length=200, verbose_name='Preview Text', default="")
    detail_text = models.TextField(
        max_length=1000, verbose_name='Detail Text', default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:product", kwargs={
            'slug': self.slug
        })


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
