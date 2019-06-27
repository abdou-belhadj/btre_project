from django.urls import path
from localcommercial import views


urlpatterns = [
    path('<int:localcommercial_id>/', views.localcommercial, name='localcommercial'),
    path('search/', views.search, name='searchlocalcommercial'),


]
