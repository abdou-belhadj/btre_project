from django.shortcuts import render,get_object_or_404
from listings.models import Listing
from django.views.generic import ListView
from . import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import Sousse_Choices,price_choices,pricemin_choices,bedroom_choices,rent_choices,rentmin_choices,garage_choices,Nabeul_Choices,rentstyle_choices,buy_choices

# Create your views here.




def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing' : listing
    }
    return render (request, 'listings/listing.html', context)



def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True, type='Vendre')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    # State
    # if 'state' in request.GET:
    #     state = request.GET['state']
    #     if state:
    #         queryset_list = queryset_list.filter(state__iexact=state)
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

    if 'garage' in request.GET:
        garage = request.GET['garage']
        if garage:
            queryset_list = queryset_list.filter(garage__iexact=garage)
    # Price
    if 'pricemax' in request.GET:
        price = request.GET['pricemax']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    if 'pricemin' in request.GET:
        price = request.GET['pricemin']
        if price:
            queryset_list = queryset_list.filter(price__gte=price)
    # biens
    if 'biens' in request.GET:
        biens = request.GET['biens']
        if biens:
            queryset_list = queryset_list.filter(biens__iexact=biens)


    context = {
        'Nabeul_Choices' : Nabeul_Choices,
        'pricemin_choices' : pricemin_choices,
        'garage_choices' : garage_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'buy_choices' : buy_choices,
        'listings' : queryset_list,
        'Sousse_Choices' : Sousse_Choices,
        'values' : request.GET,
    }
    return render (request, 'listings/search.html', context)

def searchforrent(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True, type='Louer')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    # State
    # if 'state' in request.GET:
    #     state = request.GET['state']
    #     if state:
    #         queryset_list = queryset_list.filter(state__iexact=state)
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)
    if 'garage' in request.GET:
        garage = request.GET['garage']
        if garage:
            queryset_list = queryset_list.filter(garage__iexact=garage)
    # Price
    if 'pricemax' in request.GET:
        price = request.GET['pricemax']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    if 'pricemin' in request.GET:
        price = request.GET['pricemin']
        if price:
            queryset_list = queryset_list.filter(price__gte=price)
    # biens
    if 'biens' in request.GET:
        biens = request.GET['biens']
        if biens:
            queryset_list = queryset_list.filter(biens__iexact=biens)

    context = {
        'Nabeul_Choices' : Nabeul_Choices,
        'bedroom_choices' : bedroom_choices,
        'rent_choices' : rent_choices,
        'rentmin_choices' : rentmin_choices,
        'garage_choices' : garage_choices,
        'rentstyle_choices' : rentstyle_choices,
        'listings' : queryset_list,
        'Sousse_Choices' : Sousse_Choices,
        'values' : request.GET,
    }
    return render (request, 'listings/search_for_rent.html', context)
