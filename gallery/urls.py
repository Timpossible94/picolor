from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('Galerie/', views.gallery, name = "gallery"),
    path('Kontakt/', views.contact, name = "contact")
]
