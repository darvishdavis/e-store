from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('estore_app1:category', args=[self.slug])

    def __str__(self):  #  is a python method which is called when we use print/str to convert object into a string.
        return '{}' .format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='product', blank=True)
    description = models.TextField()
    price = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    rating = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    offer = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(blank=False)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('estore_app1:product', args=[self.category.slug, self.slug])

    def get_absolute_url(self):
        return reverse('estore_search:search_view')

    def __str__(self):
        return '{}' .format(self.name)
