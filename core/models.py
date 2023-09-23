from django.db import models
from django.shortcuts import reverse

     
class FeautureProduct(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    aff_link = models.CharField(max_length=100)
    image = models.ImageField()
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:feature_product_detail", kwargs={
            'slug': self.slug
        })
    
class RecentProduct(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    aff_link = models.CharField(max_length=100)
    image = models.ImageField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:recent_product_detail", kwargs={
            'slug': self.slug
        })


class BestSeller(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    aff_link = models.CharField(max_length=100)
    image = models.ImageField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:best_seller_product_detail", kwargs={
            'slug': self.slug
        })
    
    
class SpecialOffer(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    aff_link = models.CharField(max_length=100)
    image = models.ImageField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:special_offer_product_detail", kwargs={
            'slug': self.slug
        })
    
class Sign_up(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.email