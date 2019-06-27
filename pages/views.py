from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from terrain.models import Terrain
from localcommercial.models import Localcommercial
from fonddecommerce.models import Fonddecommerce
from realtors.models import Realtor
from listings.choices import Sousse_Choices,price_choices,pricemin_choices,rent_choices,rentmin_choices,Nabeul_Choices,bedroom_choices,garage_choices,buy_choices,rentstyle_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    terrains = Terrain.objects.order_by('-list_date').filter(is_published=True)[:3]
    localcommercials = Localcommercial.objects.order_by('-list_date').filter(is_published=True)[:3]
    fonddecommerces = Fonddecommerce.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings' : listings,
        'terrains' : terrains,
        'localcommercials' : localcommercials,
        'fonddecommerces' : fonddecommerces,
    }
    return render(request, 'pages/index.html', context)

def indexbuy(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True, type='Vendre')[:6]
    context = {
        'listings' : listings,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'pricemin_choices' : pricemin_choices,
        'garage_choices' : garage_choices,
        'Nabeul_Choices' : Nabeul_Choices,
        'buy_choices' : buy_choices,
        'Sousse_Choices' : Sousse_Choices,
    }
    return render(request, 'pages/indexbuy.html', context)

def indexrent(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True, type='Louer')[:6]
    context = {
        'listings' : listings,
        'bedroom_choices' : bedroom_choices,
        'rent_choices' : rent_choices,
        'rentmin_choices' : rentmin_choices,
        'garage_choices' : garage_choices,
        'Nabeul_Choices' : Nabeul_Choices,
        'rentstyle_choices' : rentstyle_choices,
        'Sousse_Choices' : Sousse_Choices,
    }
    return render(request, 'pages/indexrent.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors,
    }
    return render(request, 'pages/about.html', context)

def sell(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'realtors' : realtors,
    }
    return render(request, 'pages/sell.html', context)
