from django.db import models
from django.shortcuts import reverse

     
class Product(models.Model):
    name = models.CharField()
    price = models.FloatField()
    slug = models.SlugField()
    description = models.TextField()
    aff_link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:product_detail", kwargs={
            'slug': self.slug
        })

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.product.name


class Sign_up(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.email