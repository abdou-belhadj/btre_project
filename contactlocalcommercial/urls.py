from django.urls import path
from . import views

urlpatterns = [
    path('contactlocalcommercial/', views.contact, name='contactlocalcommercial'),
]
