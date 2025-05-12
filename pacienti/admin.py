from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pacient, StudiuClinic, InregistrareMedicala

admin.site.register(Pacient)
admin.site.register(StudiuClinic)
admin.site.register(InregistrareMedicala)
