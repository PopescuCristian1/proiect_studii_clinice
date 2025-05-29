# 🏥 Clinica – Aplicație pentru gestionarea pacienților și studiilor clinice

Acest proiect este o aplicație web dezvoltată în Django care permite administrarea eficientă a unei baze de date medicale simplificate. Scopul principal este de a oferi o interfață intuitivă prin care utilizatorii pot gestiona informații despre pacienți, studii clinice și înregistrări medicale asociate.
Platforma este gândită să fie utilizată de către personal medical sau administrativ pentru a păstra evidența participării pacienților în cadrul studiilor, a observațiilor medicale colectate, precum și pentru a avea o imagine de ansamblu prin intermediul unui dashboard centralizat.

Această aplicație este potrivită pentru instituții de cercetare clinică, cabinete medicale mici sau studenți care doresc să înțeleagă cum pot aplica concepte precum relații între entități (many-to-many, foreign key), formulare dinamice și export de date într-un mod practic și organizat.
Este un exemplu bun de arhitectură tipică Django, care îmbină funcționalități backend solide cu o interfață stilizată și prietenoasă, folosind Bootstrap.

---

## Funcționalități implementate

-  **Gestionarea pacienților**:
  - Adăugare, listare, căutare după nume/prenume.
  - Filtrare după sex sau participare la studii.
  - Editare individuală.
  
-  **Gestionarea studiilor clinice**:
  - Adăugare și listare.
  - Filtrare după status (activ/finalizat) și număr minim de pacienți.
  - Căutare după titlu.
  - Editare studiu.

-  **Înregistrări medicale**:
  - Adăugare doar dacă pacientul este asociat unui studiu.
  - Observații medicale și legătura cu pacientul/studiul.
  - Editare și listare cu filtrare după studiu.

-  **Dashboard**:
  - Afișează rapid statistici despre numărul total de pacienți, studii și înregistrări.
  - Număr de studii active vs. finalizate.
  - Medie de pacienți pe studiu.

-  **Export în PDF**:
  - Generare documente PDF pentru lista pacienților, studiilor și înregistrărilor.
  - Format tabelar, cu antet și rânduri ordonate.
  - Disponibil direct din interfața fiecărei pagini.

-  **Interfață modernă**:
  - Complet stilizată cu Bootstrap 5.
  - Confirmări vizuale după stergeri/adaugari.

-  **Controlul ștergerii**:
  - Operația de ștergere este permisă doar din interfața de admin Django.

---

## 🛠️ Tehnologii utilizate

- **Backend**: Django 5.2+
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Bază de date**: SQLite (default)
- **Export PDF**: ReportLab
- **Altele**: Django Template Language, dynamic form population (JS + AJAX)

