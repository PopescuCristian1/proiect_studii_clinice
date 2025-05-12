from django import forms
from .models import Pacient

class PacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = ['nume', 'prenume', 'data_nasterii', 'sex', 'email', 'telefon']

from django import forms
from .models import StudiuClinic

class StudiuClinicForm(forms.ModelForm):
    class Meta:
        model = StudiuClinic
        fields = ['titlu', 'descriere', 'data_inceput', 'data_sfarsit', 'pacienti']

from django import forms
from .models import InregistrareMedicala

class InregistrareMedicalaForm(forms.ModelForm):
    class Meta:
        model = InregistrareMedicala
        fields = ['pacient', 'studiu', 'observatii']

