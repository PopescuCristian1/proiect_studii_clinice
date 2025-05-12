from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db import models

from .models import Pacient, StudiuClinic, InregistrareMedicala
from .forms import PacientForm, StudiuClinicForm, InregistrareMedicalaForm

# Afiseaza homepage-ul
def home(request):
    return render(request, 'home.html')

# Adauga un pacient nou
def adauga_pacient(request):
    if request.method == 'POST':
        form = PacientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacienti')
    else:
        form = PacientForm()
    
    return render(request, 'pacienti/adauga_pacient.html', {'form': form})

# Listeaza toti pacientii sau filtreaza dupa nume/prenume
def lista_pacienti(request):
    query = request.GET.get('q')
    if query:
        pacienti = Pacient.objects.filter(
            models.Q(nume__icontains=query) | models.Q(prenume__icontains=query)
        )
    else:
        pacienti = Pacient.objects.all()
    return render(request, 'pacienti/lista_pacienti.html', {'pacienti': pacienti, 'query': query})

# Adauga un nou studiu clinic
def adauga_studiu(request):
    if request.method == 'POST':
        form = StudiuClinicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_studii')
    else:
        form = StudiuClinicForm()
    return render(request, 'Studii/adauga_studiu.html', {'form': form})

# Listeaza toate studiile clinice
def lista_studii(request):
    studii = StudiuClinic.objects.all()
    return render(request, 'Studii/lista_studii.html', {'studii': studii})

# Adauga o inregistrare medicala (pacient + studiu + observatii)
def adauga_inregistrare(request):
    if request.method == 'POST':
        form = InregistrareMedicalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inregistrari')
    else:
        form = InregistrareMedicalaForm()
    
    return render(request, 'pacienti/adauga_inregistrare.html', {'form': form})

# Listeaza toate inregistrarile medicale
def lista_inregistrari(request):
    inregistrari = InregistrareMedicala.objects.select_related('pacient', 'studiu').all()
    return render(request, 'pacienti/lista_inregistrari.html', {'inregistrari': inregistrari})

# Returneaza studiile asociate unui pacient
def studii_pentru_pacient(request):
    pacient_id = request.GET.get('pacient_id')
    if pacient_id:
        studii = StudiuClinic.objects.filter(pacienti__id=pacient_id).values('id', 'titlu')
        return JsonResponse(list(studii), safe=False)
    return JsonResponse([], safe=False)

from django.shortcuts import render, redirect, get_object_or_404

def editeaza_pacient(request, pacient_id):
    pacient = get_object_or_404(Pacient, id=pacient_id)
    if request.method == 'POST':
        form = PacientForm(request.POST, instance=pacient)
        if form.is_valid():
            form.save()
            return redirect('lista_pacienti')
    else:
        form = PacientForm(instance=pacient)
    return render(request, 'pacienti/editeaza_pacient.html', {'form': form})


from django.shortcuts import get_object_or_404
from .models import StudiuClinic
from .forms import StudiuClinicForm

# Lista studiilor + cautare
def lista_studii(request):
    query = request.GET.get("q")
    if query:
        studii = StudiuClinic.objects.filter(titlu__icontains=query)
    else:
        studii = StudiuClinic.objects.all()
    return render(request, 'Studii/lista_studii.html', {'studii': studii, 'query': query})

# Editarea unui studiu
def editeaza_studiu(request, studiu_id):
    studiu = get_object_or_404(StudiuClinic, id=studiu_id)
    if request.method == 'POST':
        form = StudiuClinicForm(request.POST, instance=studiu)
        if form.is_valid():
            form.save()
            return redirect('lista_studii')
    else:
        form = StudiuClinicForm(instance=studiu)
    return render(request, 'Studii/editeaza_studiu.html', {'form': form})


# Lista inregistrarilor medicale + cautare
def lista_inregistrari(request):
    query = request.GET.get('q')
    if query:
        inregistrari = InregistrareMedicala.objects.select_related('pacient', 'studiu').filter(
            models.Q(pacient__nume__icontains=query) | models.Q(pacient__prenume__icontains=query)
        )
    else:
        inregistrari = InregistrareMedicala.objects.select_related('pacient', 'studiu').all()
    
    return render(request, 'pacienti/lista_inregistrari.html', {'inregistrari': inregistrari, 'query': query})

# Editare inregistrare medicala
def editeaza_inregistrare(request, inregistrare_id):
    inregistrare = get_object_or_404(InregistrareMedicala, id=inregistrare_id)
    if request.method == 'POST':
        form = InregistrareMedicalaForm(request.POST, instance=inregistrare)
        if form.is_valid():
            form.save()
            return redirect('lista_inregistrari')
    else:
        form = InregistrareMedicalaForm(instance=inregistrare)
    return render(request, 'pacienti/editeaza_inregistrare.html', {'form': form})
