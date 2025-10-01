from django.urls import path
from .views import ProductListView,ProductDetailView, search_list, playstation_list, xbox_list, nintendo_list, gaming_pc_list, contact_view, contact_success, about_view, email_list_signup, newsletter_success, terms, privacy, dmca_policy, affiliate_disclosure

app_name = 'core'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
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
    path('product/<slug>/', ProductDetailView.as_view(), name='product_detail'),
]
