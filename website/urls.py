from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tabelaPrecosComida/', views.tabelaPrecosComida, name='tabelaPrecosComida'),
]