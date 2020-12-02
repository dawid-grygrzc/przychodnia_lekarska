from .models import Account, Doctor, Visit
from .forms import CreateUserForm, VisitForm, UpdateAccountForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from Rejestracja.settings import EMAIL_HOST_USER

# View for Register Account
def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


# View for Home Page (list of doctors)
def home_view(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'home.html', context)


def delete_visit_view(request, id):
    form = VisitForm(request.POST)
    visit = Visit.objects.get(id=id)
    (Visit.objects.get(id=id)).delete()
    if form.is_valid():
        form.save()

        patient = request.user

        subject = 'Twoja wizyta została odwołana!'
        header = 'Twoja wizyta została zarejestrowana pomyślnie!\n\nDane wizyty:\n'

        patient_first_name = patient.first_name
        patient_last_name = patient.last_name
        patient_phone = patient.phone

        visit_date_time = str(form.cleaned_data['visit_date_time'])[0:-6]
        visit_type = Visit.get_type_field(form.Meta.model)
        visit_add_inf = form.cleaned_data['add_inf']
        visit_doctor = form.cleaned_data['doctor']
        visit_doctor_office = visit_doctor.office_nr

        email_name = 'Imie: ' + patient_first_name
        email_last_name = '\nNaziwsko: ' + patient_last_name
        email_phone = '\nNumer telefonu: ' + str(patient_phone)

        email_visit_date_time = '\nData i godzina wizyty: ' + str(visit_date_time)
        email_visit_type = '\nTyp wizyty: ' + str(visit_type)
        email_visit_add_inf = '\nDodatkowe informacje: ' + visit_add_inf
        email_visit_doctor = '\nImię i nazwisko doktora: ' + str(visit_doctor)
        email_visit_doctor_office = '\nNumer gabinetu: ' + str(visit_doctor_office)

        message = header + email_name + email_last_name + email_phone + email_visit_date_time + \
                  email_visit_type + email_visit_add_inf + email_visit_doctor + email_visit_doctor_office

        to_email = [EMAIL_HOST_USER, patient.email]
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            to_email,
            fail_silently=False,
        )
        return redirect('home')

    form = VisitForm(initial={'visit': id, 'patient': request.user})

    context = {
        'form': form,
        'visit': visit,

    }
    return render(request, 'visits.html', context)


# View for your visits
@login_required
def visits_view(request):
    visits = Visit.objects.filter(patient=request.user)

    context = {'visits': visits}
    return render(request, 'visits.html', context)


# View for Visit
@login_required
def visit_view(request, id):
    form = VisitForm(request.POST)
    doc = Doctor.objects.get(id=id)
    doc_spec = doc.get_specialization()
    if form.is_valid():
        form.save()

        patient = request.user

        subject = 'Dziękujemy za rejestrację wizyty!'
        header = 'Twoja wizyta została zarejestrowana pomyślnie!\n\nDane wizyty:\n'

        patient_first_name = patient.first_name
        patient_last_name = patient.last_name
        patient_phone = patient.phone

        visit_date_time = str(form.cleaned_data['visit_date_time'])[0:-6]
        visit_type = Visit.get_type_field(form.Meta.model)
        visit_add_inf = form.cleaned_data['add_inf']
        visit_doctor = form.cleaned_data['doctor']
        visit_doctor_office = visit_doctor.office_nr

        email_name = 'Imie: ' + patient_first_name
        email_last_name = '\nNaziwsko: ' + patient_last_name
        email_phone = '\nNumer telefonu: ' + str(patient_phone)

        email_visit_date_time = '\nData i godzina wizyty: ' + str(visit_date_time)
        email_visit_type = '\nTyp wizyty: ' + str(visit_type)
        email_visit_add_inf = '\nDodatkowe informacje: ' + visit_add_inf
        email_visit_doctor = '\nImię i nazwisko doktora: ' + str(visit_doctor)
        email_visit_doctor_office = '\nNumer gabinetu: ' + str(visit_doctor_office)

        message = header + email_name + email_last_name + email_phone + email_visit_date_time + \
                  email_visit_type + email_visit_add_inf + email_visit_doctor + email_visit_doctor_office

        to_email = [EMAIL_HOST_USER, patient.email]
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            to_email,
            fail_silently=False,
        )
        return redirect('home')

    form = VisitForm(initial={'doctor': id, 'patient': request.user})

    context = {
        'form': form,
        'doc': doc,
        'doc_spec': doc_spec
    }
    return render(request, 'visit.html', context)


# View for profile of user
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = UpdateAccountForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'profile.html', context)

def contact_view(request):
    context = {}
    return render(request, 'kontakt.html', context)

def oNas_view(request):
    context = {}
    return render(request, 'o_nas.html', context)
