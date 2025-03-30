from django.db import models
from django.shortcuts import reverse

     
class FeautureProduct(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    slug = models.SlugField()
    description = models.TextField()
    aff_link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:feature_product_detail", kwargs={
            'slug': self.slug
        })

class FeautureProductImage(models.Model):
    feauture_product = models.ForeignKey(FeautureProduct, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.feauture_product.title

    
class RecentProduct(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    slug = models.SlugField()
    description = models.TextField()
    aff_link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:recent_product_detail", kwargs={
            'slug': self.slug
        })

class RecentProductImage(models.Model):
    recent_product = models.ForeignKey(RecentProduct, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.recent_product.title
    


class BestSeller(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    slug = models.SlugField()
    description = models.TextField()
    aff_link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:best_seller_product_detail", kwargs={
            'slug': self.slug
        })

class BestSellerImage(models.Model):
    best_product = models.ForeignKey(BestSeller, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.best_product.title
    
    
class SpecialOffer(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    slug = models.SlugField()
    description = models.TextField()
    aff_link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:special_offer_product_detail", kwargs={
            'slug': self.slug
        })

class SpecialOfferImage(models.Model):
    special_product = models.ForeignKey(SpecialOffer, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.special_product.title
    
    
class Sign_up(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.email