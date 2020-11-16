from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length=25, blank=True)
    nazwisko = models.CharField(max_length=30, blank=True)
    pesel = models.CharField( blank=True, max_length=11)
    nr_tel = PhoneNumberField(blank=True, help_text="Numer kontaktowy lub do rodzica")

    def __str__(self):
        return f'{self.user.username} Profile'

class Lekarz(models.Model):
    "Lekarz należący do przychodni"
    SPECJALIZACJE = {
        (0, 'Pediatra'),
        (1, 'Alergolog'),
        (2, 'Dermatolog'),
        (3, 'Laryngolog'),
        (4, 'Ginekolog'),
    }

    imie = models.CharField(max_length=25, blank=False)
    nazwisko = models.CharField(max_length=30, blank=False)
    nr_gabinetu = models.PositiveSmallIntegerField(blank=False, unique=True,validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    specjalizacja = models.PositiveSmallIntegerField(default=0, choices=SPECJALIZACJE)

    class Meta:
        verbose_name = 'Lekarz'
        verbose_name_plural = 'Lekarze'

    def __str__(self):
        return self.dane_lekarz()

    def dane_lekarz(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pacjent(models.Model):
    """Pacjent, który rejestruje się"""
    imie = models.CharField(max_length=25, blank=False)
    nazwisko = models.CharField(max_length=30, blank=False)
    pesel = models.CharField(primary_key=True, blank=False, max_length=11, unique=True)
    nr_tel = PhoneNumberField(blank=True, help_text="Numer kontaktowy lub do rodzica")
    email = models.EmailField(blank=False)

    class Meta:
        verbose_name = 'Pacjent'
        verbose_name_plural = 'Pacjenci'

    def __str__(self):
        return self.dane_pacjent()

    def dane_pacjent(self):
        return "{} {} ({})".format(self.imie, self.nazwisko, self.pesel)


class Wizyta(models.Model):
    """Konkretna wizyta, łącząca ze sobą pacjenta i lekarza"""
    WIZYTA = {
        (0, 'Teleporada'),
        (1, 'Normalna wizyta'),
    }

    data_wizyty = models.DateField(default=timezone.now, blank=False)
    godzina_wizyty = models.TimeField(blank=False)
    id_pacjent = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_lekarz = models.ForeignKey(Lekarz, on_delete=models.CASCADE)
    dodatkowe_inf = models.TextField(max_length=300, blank=True, null=True)
    rodzaj_wizyty = models.SmallIntegerField(blank=True, choices=WIZYTA)

    class Meta:
        verbose_name = 'Wizyta'
        verbose_name_plural = 'Wizyty'