from django.urls import path
from .views import FeautureProductListView, FeautureProductDetailView, RecentProductListView, RecentProductDetailView, BestSellerListView, BestSellerDetailView, SpecialOfferListView, SpecialOfferDetailView, search_list, playstation_list, xbox_list, nintendo_list, gaming_pc_list, contact_view, contact_success, about_view, email_list_signup, newsletter_success, terms, privacy, dmca_policy, affiliate_disclosure

app_name = 'core'

urlpatterns = [
    path('', FeautureProductListView.as_view(), name='feauture_product_list'),
    path('', RecentProductListView.as_view(), name='recent_product_list'),
    path('', BestSellerListView.as_view(), name='best_seller_list'),
    path('', SpecialOfferListView.as_view(), name='special_offer_list'),
    path('search_list/', search_list, name='search_list'),
    path('playstation/', playstation_list, name='playstation_list'),
    path('xbox/', xbox_list, name='xbox_list'),
    path('nintendo/', nintendo_list, name='nintendo_list'),
    path('gaming-pc/', gaming_pc_list, name='gaming_pc_list'),
    path('contact-us/', contact_view, name='contact'),
    path('contact-success/', contact_success, name='contact_success'),
    path('about-us/', about_view, name='about'),
    path('newsletter/', email_list_signup, name='email_list'),
    path('newsletter-subscription-successful/', newsletter_success, name='success'),
    path('terms-of-use/', terms, name='terms'),
    path('privacy-policy/', privacy, name='privacy'),
    path('dmca-policy/', dmca_policy, name='dmca_privacy'),
    path('affiliate-disclosure/', affiliate_disclosure, name='affiliate_disclosure'),
    path('feature_product/<slug>/', FeautureProductDetailView.as_view(), name='feature_product_detail'),
    path('recent_product/<slug>/', RecentProductDetailView.as_view(), name='recent_product_detail'),
    path('best_seller/<slug>/', BestSellerDetailView.as_view(), name='best_seller_product_detail'),
    path('special_offer/<slug>/', SpecialOfferDetailView.as_view(), name='special_offer_product_detail'),
]
