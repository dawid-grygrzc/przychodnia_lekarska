from django import forms
from django.forms import ModelForm
from .models import Account, Doctor, Visit
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets
from django.utils.translation import ngettext


# Form for Create User
class CreateUserForm(UserCreationForm):
    password_help_texts = ["Twoje hasło nie powinno być podobne do Twoich informacji personalnych.",
                           "Twoje hasło powinno zawierać co najmniej 8 znaków.",
                           "Twoje hasło nie powinno składać się z samych cyfr."]

    class Meta:
        model = Account
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'psl', 'phone']
        widgets = {
            'first_name': forms.Textarea(
                attrs={
                    "rows": 1
                }
            ),
            'last_name': forms.Textarea(
                attrs={
                    "rows": 1
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Hasło'
        self.fields['password2'].label = 'Powtórz hasło'
        self.fields['first_name'].label = 'Imię'
        self.fields['last_name'].label = 'Nazwisko'
        self.fields['psl'].label = 'PESEL'
        self.fields['phone'].label = 'Numer telefonu'


# Form for Visit
class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['patient', 'doctor', 'add_inf', 'visit_date_time', 'type']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['add_inf'].label = 'Dodatkowe informacje'
        self.fields['type'].label = 'Typ wizyty'
        self.fields['visit_date_time'].label = 'Data i godzina wizyty'


# Form for Update Account
class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'psl', 'phone']
        widgets = {
            'first_name': forms.Textarea(
                attrs={
                    "rows": 1
                }
            ),
            'last_name': forms.Textarea(
                attrs={
                    "rows": 1
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['first_name'].label = 'Imię'
        self.fields['last_name'].label = 'Nazwisko'
        self.fields['psl'].label = 'PESEL'
        self.fields['phone'].label = 'Numer telefonu'
