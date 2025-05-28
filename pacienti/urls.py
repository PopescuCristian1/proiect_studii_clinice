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
    path('pacienti/editeaza/<int:pacient_id>/', views.editeaza_pacient, name='editeaza_pacient'),
    path('studii/editeaza/<int:studiu_id>/', views.editeaza_studiu, name='editeaza_studiu'),
    path('inregistrari/editeaza/<int:inregistrare_id>/', views.editeaza_inregistrare, name='editeaza_inregistrare'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pacienti/exporta_pdf/', views.exporta_pacienti_pdf, name='exporta_pacienti_pdf'),
    path('studii/exporta_pdf/', views.exporta_studii_pdf, name='exporta_studii_pdf'),
    path('inregistrari/exporta_pdf/', views.exporta_inregistrari_pdf, name='exporta_inregistrari_pdf'),
]
