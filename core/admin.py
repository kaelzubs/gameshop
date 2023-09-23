from django.contrib import admin
from .models import FeautureProduct, RecentProduct, BestSeller, SpecialOffer

class GameShopaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}

admin.site.register(FeautureProduct, GameShopaAdmin)
admin.site.register(RecentProduct, GameShopaAdmin)
admin.site.register(BestSeller, GameShopaAdmin)
admin.site.register(SpecialOffer, GameShopaAdmin)
