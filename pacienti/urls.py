from django.urls import path
from . import views

urlpatterns = [
    path('adauga/', views.adauga_pacient, name='adauga_pacient'),
]
