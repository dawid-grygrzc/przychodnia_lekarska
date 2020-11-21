from django import forms
from django.forms import ModelForm
from .models import Account, Doctor, Visit
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets


# Form for Create User
class CreateUserForm(UserCreationForm):
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


# Form for Visit
class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['patient', 'doctor', 'add_inf', 'visit_date_time', 'type']


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
