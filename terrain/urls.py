from django.urls import path
from terrain import views


urlpatterns = [
    path('<int:terrain_id>/', views.terrain, name='terrain'),
    path('search/', views.search, name='searchterrain'),
]
