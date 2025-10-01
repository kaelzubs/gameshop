from django.contrib import admin
from .models import Product, ProductImage

# Register your models here.
class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","created_at")
    search_fields = ("name","slug","variants__sku")
    inlines = [ImageInline]
    prepopulated_fields = {'slug': ('name',),}

admin.site.register([ProductImage])
