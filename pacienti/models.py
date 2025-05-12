from django.db import models


class Pacient(models.Model):
    SEX_OPTIUNI = [('M', 'Masculin'), ('F', 'Feminin')]
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    data_nasterii = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_OPTIUNI)
    email = models.EmailField(blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nume} {self.prenume}"

    class Meta:
        verbose_name = "Pacient"
        verbose_name_plural = "Pacienți"

class StudiuClinic(models.Model):
    titlu = models.CharField(max_length=100)
    descriere = models.TextField(blank=True)
    data_inceput = models.DateField()
    data_sfarsit = models.DateField(null=True, blank=True)
    pacienti = models.ManyToManyField('Pacient', related_name='studii')

    def __str__(self):
        return self.titlu
    class Meta:
        verbose_name = "Studiu clinic"
        verbose_name_plural = "Studii clinice"

    
class InregistrareMedicala(models.Model):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    studiu = models.ForeignKey(StudiuClinic, on_delete=models.CASCADE)
    data_inregistrarii = models.DateField(auto_now_add=True)
    observatii = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pacient} – {self.studiu}"

    class Meta:
        verbose_name = "Înregistrare medicală"
        verbose_name_plural = "Înregistrări medicale"

