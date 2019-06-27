from django.contrib import admin
from .models import Localcommercial
# Register your models here.


class LocalcommercialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date','city','type')
    list_display_links = ('id', 'title')
    list_filter = ('realtor','type')
    list_editable = ('is_published', 'price',)
    search_fields = ('title', 'description', 'adress', 'city', 'state', 'zipcode', 'price')
    list_per_page = 15



admin.site.register(Localcommercial, LocalcommercialAdmin)
