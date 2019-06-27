from django.shortcuts import render,get_object_or_404
from localcommercial.models import Localcommercial
from django.views.generic import ListView
from . import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import Sousse_Choices,price_choices,Nabeul_Choices,surfacemin_choices,surfacemax_choices,pricemin_choices,localcommercial_choices

# Create your views here.



def index(request):
    localcommercials = Localcommercial.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(localcommercials, 6)
    page = request.GET.get('page')
    paged_localcommercials = paginator.get_page(page)
    context = {
        'localcommercials' : paged_localcommercials
    }
    return render(request, 'localcommercials/localcommercials.html', context)


def localcommercial(request, localcommercial_id):
    localcommercial = get_object_or_404(Localcommercial, pk=localcommercial_id)
    context = {
        'localcommercial' : localcommercial
    }
    return render (request, 'localcommercials/localcommercial.html', context)



def search(request):
    queryset_list = Localcommercial.objects.order_by('-list_date').filter(is_published=True)
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
    # Surface
    if 'surfacemax' in request.GET:
        surface = request.GET['surfacemax']
        if surface:
            queryset_list = queryset_list.filter(surface__lte=surface)
    if 'surfacemin' in request.GET:
        surface = request.GET['surfacemin']
        if surface:
            queryset_list = queryset_list.filter(surface__gte=surface)
    # Price
    if 'pricemax' in request.GET:
        price = request.GET['pricemax']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    if 'pricemin' in request.GET:
        price = request.GET['pricemin']
        if price:
            queryset_list = queryset_list.filter(price__gte=price)
    # Type
    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            queryset_list = queryset_list.filter(type__iexact=type)


    context = {
        'surfacemin_choices' : surfacemin_choices,
        'surfacemax_choices' : surfacemax_choices,
        'Nabeul_Choices' : Nabeul_Choices,
        'price_choices' : price_choices,
        'pricemin_choices' : pricemin_choices,
        'localcommercials' : queryset_list,
        'localcommercial_choices' : localcommercial_choices,
        'Sousse_Choices' : Sousse_Choices,
        'values' : request.GET,
    }
    return render (request, 'localcommercials/search.html', context)
