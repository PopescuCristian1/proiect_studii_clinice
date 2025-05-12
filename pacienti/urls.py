from django.urls import path
from . import views

urlpatterns = [
    path('adauga/', views.adauga_pacient, name='adauga_pacient'),
    path('lista/', views.lista_pacienti, name='lista_pacienti'),
    path('', views.home, name='home'),

]
