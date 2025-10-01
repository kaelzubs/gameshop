from django.contrib.sitemaps import Sitemap
from core.models import Product
from itertools import chain



class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        p = Product.objects.all()
        p = chain(p)
        return list(p)