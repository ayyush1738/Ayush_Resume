from django.urls import path
from . import views

urlpatterns = [
    path('htop', views.htop, name='htop'),  # Maps /htop to the htop view
]
