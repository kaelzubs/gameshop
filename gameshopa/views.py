from django.contrib.sitemaps import Sitemap
from core.models import FeautureProduct, RecentProduct, BestSeller, SpecialOffer
from itertools import chain



class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        f = FeautureProduct.objects.all()
        r = RecentProduct.objects.all()
        b = BestSeller.objects.all()
        s = SpecialOffer.objects.all()
        frbs = chain(f,r,b,s)
        return list(frbs)