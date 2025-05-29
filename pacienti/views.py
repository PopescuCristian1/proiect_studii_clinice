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
    sex = request.GET.get('sex')
    are_studii = request.GET.get('studii')

    pacienti = Pacient.objects.all()

    if query:
        pacienti = pacienti.filter(
            models.Q(nume__icontains=query) | models.Q(prenume__icontains=query)
        )

    if sex in ['M', 'F']:
        pacienti = pacienti.filter(sex=sex)

    if are_studii == 'cu':
        pacienti = pacienti.filter(studii__isnull=False).distinct()
    elif are_studii == 'fara':
        pacienti = pacienti.filter(studii__isnull=True)

    return render(request, 'pacienti/lista_pacienti.html', {
        'pacienti': pacienti,
        'query': query,
        'selected_sex': sex,
        'studii_filter': are_studii
    })



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
from datetime import date
from django.db.models import Count, Q

def lista_studii(request):
    query = request.GET.get("q")
    min_pacienti = request.GET.get("min")
    status = request.GET.get("status")

    studii = StudiuClinic.objects.annotate(num_pacienti=Count('pacienti'))

    if query:
        studii = studii.filter(titlu__icontains=query)

    if min_pacienti and min_pacienti.isdigit():
        studii = studii.filter(num_pacienti__gte=int(min_pacienti))

    if status == "active":
        studii = studii.filter(Q(data_sfarsit__isnull=True) | Q(data_sfarsit__gte=date.today()))
    elif status == "finalizate":
        studii = studii.filter(data_sfarsit__lt=date.today())

    return render(request, 'Studii/lista_studii.html', {
        'studii': studii,
        'query': query,
        'min_pacienti': min_pacienti,
        'status_filter': status
    })


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
    studiu_id = request.GET.get('studiu')

    inregistrari = InregistrareMedicala.objects.select_related('pacient', 'studiu').all()

    if query:
        inregistrari = inregistrari.filter(
            models.Q(pacient__nume__icontains=query) |
            models.Q(pacient__prenume__icontains=query)
        )

    if studiu_id and studiu_id.isdigit():
        inregistrari = inregistrari.filter(studiu__id=studiu_id)

    studii = StudiuClinic.objects.all()

    return render(request, 'pacienti/lista_inregistrari.html', {
        'inregistrari': inregistrari,
        'query': query,
        'studii': studii,
        'selected_studiu': studiu_id
    })


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

from django.db.models import Count, Avg
from datetime import date

def dashboard(request):
    total_pacienti = Pacient.objects.count()
    total_studii = StudiuClinic.objects.count()
    total_inregistrari = InregistrareMedicala.objects.count()

    studii_active = StudiuClinic.objects.filter(data_sfarsit__isnull=True).count()
    studii_finalizate = StudiuClinic.objects.filter(data_sfarsit__lt=date.today()).count()

    medie_pacienti = StudiuClinic.objects.annotate(num=Count('pacienti')).aggregate(avg=Avg('num'))['avg'] or 0

    context = {
        'total_pacienti': total_pacienti,
        'total_studii': total_studii,
        'total_inregistrari': total_inregistrari,
        'studii_active': studii_active,
        'studii_finalizate': studii_finalizate,
        'medie_pacienti': round(medie_pacienti, 2),
    }

    return render(request, 'dashboard.html', context)

from django.shortcuts import render
from .models import Pacient, StudiuClinic, InregistrareMedicala
from django.db.models import Avg
from datetime import date

def dashboard(request):
    pacienti = Pacient.objects.count()
    studii = StudiuClinic.objects.count()
    inregistrari = InregistrareMedicala.objects.count()
    active = StudiuClinic.objects.filter(
    Q(data_sfarsit__isnull=True) | Q(data_sfarsit__gte=date.today())).count()
    finalizate = StudiuClinic.objects.filter(data_sfarsit__lt=date.today()).count()
    
    media = StudiuClinic.objects.annotate(nr=models.Count('pacienti')).aggregate(avg=Avg('nr'))['avg']

    context = {
        'pacienti': pacienti,
        'studii': studii,
        'inregistrari': inregistrari,
        'active': active,
        'finalizate': finalizate,
        'media': media or 0,
    }

    return render(request, 'dashboard.html', context)

#pdf lista pacienti
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from .models import Pacient

def exporta_pacienti_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="lista_pacienti.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("Lista pacienților", styles['Title']))
    elements.append(Spacer(1, 12))

    data = [['Nume complet', 'Email']]
    pacienti = Pacient.objects.all()
    for p in pacienti:
        data.append([f"{p.nume} {p.prenume}", p.email])

    table = Table(data, colWidths=[250, 250])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0d6efd')),  # albastru Bootstrap
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey]),
    ]))

    elements.append(table)
    doc.build(elements)

    return response

#pdf lista studii
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import StudiuClinic

def exporta_studii_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="lista_studii.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    elements.append(Paragraph("Lista studiilor clinice", styles['Title']))
    elements.append(Spacer(1, 12))

    # Antete
    data = [["Titlu", "Descriere", "Început", "Sfârșit", "Nr. pacienți"]]

    studii = StudiuClinic.objects.all()
    for studiu in studii:
        data.append([
            studiu.titlu,
            studiu.descriere,
            studiu.data_inceput.strftime('%Y-%m-%d'),
            studiu.data_sfarsit.strftime('%Y-%m-%d') if studiu.data_sfarsit else "—",
            studiu.pacienti.count()
        ])

    table = Table(data, colWidths=[90, 160, 70, 70, 60])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0d6efd')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))

    elements.append(table)
    doc.build(elements)

    return response

#pdf inregistrari medicale
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from django.http import HttpResponse
from .models import InregistrareMedicala

def exporta_inregistrari_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="inregistrari_medicale.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 16)
    p.drawCentredString(width / 2, height - 50, "Lista înregistrărilor medicale")

    data = [["Pacient", "Studiu", "Observații"]]
    for inregistrare in InregistrareMedicala.objects.select_related("pacient", "studiu"):
        data.append([
            str(inregistrare.pacient),
            str(inregistrare.studiu),
            inregistrare.observatii or ""
        ])

    table = Table(data, colWidths=[170, 170, 170])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0d6efd")),  
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))

    table.wrapOn(p, width, height)
    table.drawOn(p, 50, height - 100 - (30 * len(data)))

    p.showPage()
    p.save()

    return response





