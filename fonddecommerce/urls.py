from django.urls import path
from fonddecommerce import views


urlpatterns = [
    path('<int:fonddecommerce_id>/', views.fonddecommerce, name='fonddecommerce'),
    path('search/', views.search, name='searchfonddecommerce'),
]
