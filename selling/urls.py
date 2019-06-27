from django.urls import path
from selling import views


urlpatterns = [
    path('Sell/', views.index, name='selling'),
]
