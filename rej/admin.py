from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Pacjent)
admin.site.register(Wizyta)
admin.site.register(Lekarz)
admin.site.register(Profile)
