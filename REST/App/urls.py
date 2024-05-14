from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # Add more URL patterns as needed
]
