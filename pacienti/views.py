from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import PacientForm

def adauga_pacient(request):
    if request.method == 'POST':
        form = PacientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacienti')
    else:
        form = PacientForm()
    
    return render(request, 'pacienti/adauga_pacient.html', {'form': form})

from .models import Pacient

def lista_pacienti(request):
    pacienti = Pacient.objects.all()
    return render(request, 'pacienti/lista_pacienti.html', {'pacienti': pacienti})

from django.shortcuts import render

def home(request):
    return render(request, 'pacienti/home.html')

