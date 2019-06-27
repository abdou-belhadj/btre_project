from django.shortcuts import render,get_object_or_404
from terrain.models import Terrain
from django.views.generic import ListView
from . import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices,Nabeul_Choices,surfacemin_choices,surfacemax_choices,pricemin_choices,Sousse_Choices

# Create your views here.


# 
# def index(request):
#     terrains = Terrain.objects.order_by('-list_date').filter(is_published=True)
#     paginator = Paginator(terrains, 6)
#     page = request.GET.get('page')
#     paged_terrains = paginator.get_page(page)
#     context = {
#         'terrains' : paged_terrains
#     }
#     return render(request, 'terrains/terrains.html', context)


def terrain(request, terrain_id):
    terrain = get_object_or_404(Terrain, pk=terrain_id)
    context = {
        'terrain' : terrain
    }
    return render (request, 'terrains/terrain.html', context)



def search(request):
    queryset_list = Terrain.objects.order_by('-list_date').filter(is_published=True)
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


    context = {
        'surfacemin_choices' : surfacemin_choices,
        'surfacemax_choices' : surfacemax_choices,
        'Nabeul_Choices' : Nabeul_Choices,
        'price_choices' : price_choices,
        'pricemin_choices' : pricemin_choices,
        'Sousse_Choices' : Sousse_Choices,
        'terrains' : queryset_list,
        'values' : request.GET,
    }
    return render (request, 'terrains/search.html', context)
