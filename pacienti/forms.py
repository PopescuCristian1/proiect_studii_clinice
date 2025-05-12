from django import forms
from .models import Pacient

class PacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = ['nume', 'prenume', 'data_nasterii', 'sex', 'email', 'telefon']
