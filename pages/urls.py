from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('aracsec', views.aracsec, name='aracsec'),
    path('araclarim', views.araclarim, name='araclarim'),
    path('sonKonumlar', views.sonKonumlar, name='sonKonumlar'),
]
