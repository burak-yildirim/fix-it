from django.db import models
from django.contrib.auth.models import User
from string import Template


class Customer(models.Model):
    civil_id = models.IntegerField(unique=True)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)

    def __str__(self):
        mystr = Template("$n - $e - $p - $c")
        words = {
            "n": self.fullname,
            "e": self.email,
            "p": self.phone,
            "c": str(self.civil_id),
        }
        return mystr.substitute(words)


class Device(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_compliant = models.CharField(max_length=500)
    recieved_at = models.DateTimeField('Ürün kayıt tarihi', auto_now_add=True)
    repaired_at = models.DateTimeField(
        'Onarılma tarihi', null=True, blank=True)
    delivered_at = models.DateTimeField('Teslim tarihi', null=True, blank=True)

    def __str__(self):
        mystr = Template("$n - $c")
        words = {
            "n": self.name,
            "c": str(self.customer),
        }
        return mystr.substitute(words)


class Employee(User):
    REPR = 0  # Stands for customer representative
    TECH = 1  # Stands for technical service employee
    EMPLOYEE_TYPE_CHOICES = (
        (REPR, "Müşteri Temsilcisi"),
        (TECH, "Teknik Servis Görevlisi")
    )

    username = models.CharField(
        "Kullanıcı Adı", blank=True, null=True, unique=True)
    fullname = models.CharField("Ad Soyad", blank=False, unique=False)
    email = models.EmailField("Email Adresi", blank=False, unique=True)
    is_active = models.BooleanField("Aktiflik Durumu", default=False)
    last_activated = models.DateTimeField(
        "Son Aktif Edilme Tarihi", blank=True)
    last_deactivated = models.DateTimeField(
        "Son Pasif Edilme Tarihi", blank=True)
    employee_type = models.PositiveSmallIntegerField(
        choices=EMPLOYEE_TYPE_CHOICES)
