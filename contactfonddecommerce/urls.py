from django.urls import path
from . import views

urlpatterns = [
    path('contactfonddecommerce/', views.contact, name='contactfonddecommerce'),
]
