from django.shortcuts import render, redirect, get_object_or_404
from .models import Lekarz, Pacjent, Wizyta
from .forms import PacjentForm, LekarzForm, WizytaForm, PeselForm, CreateUserForm, UserUpdateForm, ProfileUpdateForm, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    lekarze = Lekarz.objects.all()
    context = {'lekarze': lekarze}
    return render(request, 'home.html', context)


def weryfikacja_view(request, id):
    context = {
        'id': id
    }
    return render(request, 'weryfikacja.html', context)


def rejestracja_view(request, id):
    form = PacjentForm()

    if request.method == 'POST':
        form = PacjentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(wizyta_view, id=id, pesel=form.cleaned_data['pesel'])

    context = {
        'id': id,
        'form': form
    }
    return render(request, 'rejestracja.html', context)


@login_required
def wizyta_view(request, id):
    form = WizytaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')

    form = WizytaForm(initial={'id_lekarz': id, 'id_pacjent': Profile.objects.get(pesel=request.user.profile.pesel)})

    context = {'form': form}
    return render(request, 'wizyta.html', context)


def pesel_view(request, id):

    form = PeselForm(request.POST or None)
    a = False
    b = ""
    c = PacjentForm()
    if form.is_valid():
        a = True
        b = form.cleaned_data['pesel']
        c = Pacjent.objects.get(pesel=b)
        return redirect(wizyta_view, id=id, pesel=b)

#    if form.is_valid():
#        pacjent = get_object_or_404(Pacjent, form.pesel)
#        return redirect(wizyta_view, id=id, pesel=form.pesel)

    context = {'id': id,
               'form': form,
               'a': a,
               'b': b,
               'c': c}
    return render(request, 'pesel.html', context)


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

