from django.contrib import admin

# Register your models here.
from .models import Account, Doctor, Visit

admin.site.register(Account)
admin.site.register(Doctor)
admin.site.register(Visit)