from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from enum import Enum


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        choices = list()
        # Loop thru defined enums
        for item in cls:
            choices.append((item.value, item.name))
        # return as tuple
        return tuple(choices)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.value


class VisitType(ChoiceEnum):
    Teleporada = 0
    Normalna_wizyta = 1


class Specialization(ChoiceEnum):
    Pediatra = 0
    Alergolog = 1
    Dermatolog = 2
    Laryngolog = 3
    Ginekolog = 4


class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, psl, phone, password=None):
        if not email:
            raise ValueError("Podaj email")
        if not first_name:
            raise ValueError("Podaj imię")
        if not last_name:
            raise ValueError("Podaj nazwisko")
        if not psl:
            raise ValueError("Podaj pesel")
        if not phone:
            raise ValueError("Podaj numer telefonu")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            psl=psl,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, first_name, last_name, psl, phone, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            psl=psl,
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.TextField(max_length=40, blank=False)
    last_name = models.TextField(max_length=40, blank=False)
    psl = models.CharField(max_length=11, unique=True, blank=False)
    phone = PhoneNumberField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',
                       'last_name',
                       'psl',
                       'phone']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Doctor(models.Model):
    "Lekarz należący do przychodni"

    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    office_nr = models.PositiveSmallIntegerField(blank=False, unique=True,validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    specialization = models.PositiveSmallIntegerField(default=0, choices=Specialization.choices())

    class Meta:
        verbose_name = 'Lekarz'
        verbose_name_plural = 'Lekarze'

    def __str__(self):
        return self.doctor_data()

    def doctor_data(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_specialization(self):
        if self.specialization == 1:
            return 'Alergolog'
        elif self.specialization == 2:
            return 'Dermatolog'
        elif self.specialization == 0:
            return 'Pediatra'
        elif self.specialization == 4:
            return 'Ginekolog'
        elif self.specialization == 3:
            return 'Laryngolog'


class Visit(models.Model):
    """Konkretna wizyta, łącząca ze sobą pacjenta i lekarza"""

    visit_date_time = models.DateTimeField(default=timezone.now, blank=False)
    patient = models.ForeignKey(Account, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    add_inf = models.TextField(max_length=300, blank=True, null=True)
    type = models.SmallIntegerField(default=0, blank=False, choices=VisitType.choices())

    class Meta:
        verbose_name = 'Wizyta'
        verbose_name_plural = 'Wizyty'


    def visit_display(self):
        return self.get_date() + "\n" + self.add_inf + "\n" + self.doctor.doctor_data() + "\n" + self.get_type_field()


    def get_add_inf(self):
        return self.add_inf

    def get_doctor_data(self):
        return self.doctor.doctor_data()

    def get_date(self):
        return str(self.visit_date_time)[0:-6]

    def get_type_field(self):
        if self.type == VisitType.Teleporada:
            return 'Teleporada'
        else:
            return 'Normalna wizyta'


