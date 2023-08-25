from django.contrib import admin

from estore_app1 import models


# Register your models here.
class RegisterCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


admin.site.register(models.Category, RegisterCategory)


class RegisterProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'offer', 'category', 'stock', 'available', 'created', 'modified']
    list_editable = ['price', 'offer', 'category', 'stock', 'available']
    prepopulated_fields = {'slug': ['name', 'category']}
    list_per_page = 20


admin.site.register(models.Product, RegisterProduct)
