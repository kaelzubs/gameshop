from .models import Product, ProductImage, Sign_up
from django.views.generic import ListView, DetailView
from django.db.models import Q
from itertools import chain
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailSignupForm, ContactForms
from django.conf import settings
import requests
import json
from django.core.mail import send_mail, get_connection


class ProductListView(ListView):
    model = Product
    paginate_by = 40
    template_name = "gameshopa/index.html"
    forms = EmailSignupForm()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_image"] = Product.objects.all()
        context['forms'] = EmailSignupForm()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "gameshopa/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = EmailSignupForm()
        product = Product.objects.get(slug=self.kwargs['slug'])
        context['product_images'] = ProductImage.objects.filter(product=product)
        return context


def search_list(request):
    query = request.GET.get('q')
    if query:
        product_list = Product.objects.filter(Q(name__icontains=query) |
                                                Q(price__icontains=query) |
                                                Q(description__icontains=query))
    else:
        product_list = Product.objects.all()

    results = product_list
    results = list(results)
    p = Paginator(results, 16) 
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    forms = EmailSignupForm()

    return render(request, 'gameshopa/search.html', {
        'search_list': page_obj,
        'forms': forms
    })

#################################################################
def playstation_list(request):
    plist = Product.objects.filter(Q(name__icontains="playstation")
                                           | Q(description__icontains="playstation")
                                           | Q(price__icontains="playstation"))

    results = chain(plist)
    results = list(results)
    p = Paginator(results, 16) 
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    forms = EmailSignupForm()

    return render(request, 'gameshopa/playstation.html', {
        "playstation": page_obj,
        'forms': forms
    })

#################################################################
def xbox_list(request):
    xlist = Product.objects.filter(Q(name__icontains="xbox")
                                    | Q(description__icontains="xbox")
                                    | Q(price__icontains="xbox"))

    results = chain(xlist)
    results = list(results)
    p = Paginator(results, 16) 
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    forms = EmailSignupForm()

    return render(request, 'gameshopa/xbox.html', {
        "xbox": page_obj,
        'forms': forms
    })

def nintendo_list(request):
    nlist = Product.objects.filter(Q(name__icontains="nintendo")
                                           | Q(description__icontains="nintendo")
                                           | Q(price__icontains="nintendo"))

    results = chain(nlist)
    results = list(results)
    p = Paginator(results, 16) 
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    forms = EmailSignupForm()

    return render(request, 'gameshopa/nintendo.html', {
        "nintendo": page_obj,
        'forms': forms
    })

def gaming_pc_list(request):
    glist = Product.objects.filter(Q(name__icontains="gaming pc")
                                           | Q(description__icontains="gaming pc")
                                           | Q(price__icontains="gaming pc"))

    results = chain(glist)
    results = list(results)
    p = Paginator(results, 16) 
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    forms = EmailSignupForm()

    return render(request, 'gameshopa/gamingpc.html', {
        "gaming_pc": page_obj,
        'forms': forms
    })


def contact_view(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForms(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd['email'],
                ['kaelzubs@gmail.com', 'info@gameshopa.com'],
                fail_silently=False,
                connection=con
            )
            return redirect('core:contact_success')
    else:
        form = ContactForms()
        if 'submitted' in request.GET:
            submitted = True

    forms = EmailSignupForm()

    return render(request, 'gameshopa/contact.html', {
        'form': form,
        'forms': forms
    })

def contact_success(request):
    forms = EmailSignupForm()
    return render(request, 'gameshopa/contact_success.html', {
        'forms': forms
    })

def about_view(request):
    forms = EmailSignupForm()
    return render(request, 'gameshopa/about.html', {
        'forms': forms
    })


MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'

def subscribe(email):
    data = {
        'email_address': email,
        'status': 'subscribed'
    }
    r = requests.post(
        members_endpoint,
        auth=('', MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()


def email_list_signup(request):
    forms = EmailSignupForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            email_signup_qs = Sign_up.objects.filter(email=forms.instance.email)
            if email_signup_qs.exists():
                return render(request, 'gameshopa/subscribed.html', {
                    'forms': forms
                })
            else:
                subscribe(forms.instance.email)
                forms.save()
                
            return redirect('core:success')
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def newsletter_success(request):
    forms = EmailSignupForm()
    return render(request, 'gameshopa/sub_success.html', {
        'forms': forms
    })

def handler404(request, exception):
    forms = EmailSignupForm()
    response = render(request, "gameshopa/error_404.html", {
        'forms': forms
    })
    response.status_code = 404
    return response

def handler500(request):
    forms = EmailSignupForm()
    response = render(request, "gameshopa/error_500.html", {
        'forms': forms
    })
    response.status_code = 500
    return response

def terms(request):
    forms = EmailSignupForm()
    return render(request, 'gameshopa/terms.html', {
        'forms': forms
    })

def privacy(request):
    forms = EmailSignupForm()
    return render(request, 'gameshopa/privacy_policy.html', {
        'forms': forms
    })

def dmca_policy(request):
    forms = EmailSignupForm()
    return render(request, 'gameshopa/dmca_policy.html', {
        'forms': forms
    })

def affiliate_disclosure(request):
    forms = EmailSignupForm()
    return render(request, 'gameshopa/affiliate_disclosure.html', {
        'forms': forms
    })