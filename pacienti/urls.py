from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adauga/', views.adauga_pacient, name='adauga_pacient'),
    path('lista/', views.lista_pacienti, name='lista_pacienti'),
    path('studii/adauga/', views.adauga_studiu, name='adauga_studiu'),
    path('studii/', views.lista_studii, name='lista_studii'),
    path('inregistrari/adauga/', views.adauga_inregistrare, name='adauga_inregistrare'),
    path('inregistrari/', views.lista_inregistrari, name='lista_inregistrari'),
    path('ajax/studii/', views.studii_pentru_pacient, name='ajax_studii_pacient'),
]
