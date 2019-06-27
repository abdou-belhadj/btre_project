from django.urls import path
from . import views

urlpatterns = [
    path('contactterrain/', views.contact, name='contactterrain'),
]
