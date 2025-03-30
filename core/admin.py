from django.contrib import admin
from .models import FeautureProduct, FeautureProductImage, RecentProduct, RecentProductImage, BestSeller, BestSellerImage, SpecialOffer, SpecialOfferImage

class FeautureProductImageAdmin(admin.StackedInline):
    model=FeautureProductImage

@admin.register(FeautureProduct)
class FeautureProductAdmin(admin.ModelAdmin):
    inlines=[FeautureProductImageAdmin]
    prepopulated_fields = {'slug': ('title',),}

    class Meta:
        model=FeautureProduct

# @admin.register(FeautureProductImage)
# class FeautureProductImageAdmin(admin.ModelAdmin):
#     pass

######################################################
class RecentProductImageAdmin(admin.StackedInline):
    model=RecentProductImage

@admin.register(RecentProduct)
class RecentProductAdmin(admin.ModelAdmin):
    inlines=[RecentProductImageAdmin]
    prepopulated_fields = {'slug': ('title',),}

    class Meta:
        model=RecentProduct

# @admin.register(RecentProductImage)
# class RecentProductImageAdmin(admin.ModelAdmin):
#     pass

###################################################

class BestSellerImageAdmin(admin.StackedInline):
    model=BestSellerImage

@admin.register(BestSeller)
class BestSellerAdmin(admin.ModelAdmin):
    inlines=[BestSellerImageAdmin]
    prepopulated_fields = {'slug': ('title',),}

    class Meta:
        model=BestSeller

# @admin.register(BestSellerImage)
# class BestSellerImageAdmin(admin.ModelAdmin):
#     pass

###################################################

class SpecialOfferImageAdmin(admin.StackedInline):
    model=SpecialOfferImage

@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    inlines=[SpecialOfferImageAdmin]
    prepopulated_fields = {'slug': ('title',),}

    class Meta:
        model=SpecialOffer

# @admin.register(SpecialOfferImage)
# class SpecialOfferImageAdmin(admin.ModelAdmin):
#     pass

#######################################################
