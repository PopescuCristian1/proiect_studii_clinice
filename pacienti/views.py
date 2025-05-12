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


from .forms import InregistrareMedicalaForm
from .models import InregistrareMedicala

def adauga_inregistrare(request):
    if request.method == 'POST':
        form = InregistrareMedicalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inregistrari')
    else:
        form = InregistrareMedicalaForm()
    
    return render(request, 'pacienti/adauga_inregistrare.html', {'form': form})

def lista_inregistrari(request):
    inregistrari = InregistrareMedicala.objects.select_related('pacient', 'studiu').all()
    return render(request, 'pacienti/lista_inregistrari.html', {'inregistrari': inregistrari})


from django.http import JsonResponse
from .models import StudiuClinic

def studii_pentru_pacient(request):
    pacient_id = request.GET.get('pacient_id')
    if pacient_id:
        studii = StudiuClinic.objects.filter(pacienti__id=pacient_id).values('id', 'titlu')
        return JsonResponse(list(studii), safe=False)
    return JsonResponse([], safe=False)
