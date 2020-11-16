from django import forms
from django.forms import ModelForm
from .models import Pacjent, Wizyta, Lekarz, Profile
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['imie', 'nazwisko', 'pesel', 'nr_tel']


class PacjentForm(ModelForm):
    class Meta:
        model = Pacjent
        fields = ['imie', 'nazwisko', 'pesel', 'email', 'nr_tel']


class LekarzForm(ModelForm):
    class Meta:
        model = Lekarz
        fields = ['imie', 'nazwisko', 'nr_gabinetu', 'specjalizacja']


class WizytaForm(ModelForm):
    class Meta:
        model = Wizyta
        fields = ['id_pacjent', 'id_lekarz', 'dodatkowe_inf', 'data_wizyty', 'godzina_wizyty', 'rodzaj_wizyty']
        widgets = {
            'data_wizyty': widgets.AdminDateWidget,
            'godzina_wizyty': widgets.AdminTimeWidget
        }


class PeselForm(forms.Form):
    pesel = forms.CharField(max_length=11)