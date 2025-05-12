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
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from .forms import StudiuClinicForm

def adauga_studiu(request):
    if request.method == 'POST':
        form = StudiuClinicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_studii')
    else:
        form = StudiuClinicForm()
    return render(request, 'Studii/adauga_studiu.html', {'form': form})

from .models import StudiuClinic

def lista_studii(request):
    studii = StudiuClinic.objects.all()
    return render(request, 'Studii/lista_studii.html', {'studii': studii})



