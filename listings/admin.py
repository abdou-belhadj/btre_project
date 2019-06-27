from django.contrib import admin
from .models import Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'realtor','city','type','biens','placeparking','abri','cellier','balcon','terasse','jardin','piscine')
    list_display_links = ('id', 'title')
    list_filter = ('realtor','type',)
    list_editable = ('is_published', 'price')
    search_fields = ('title', 'description', 'adress', 'city', 'state', 'zipcode', 'price')
    list_per_page = 15



admin.site.register(Listing, ListingAdmin)
