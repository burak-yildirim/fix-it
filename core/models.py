from django.db import models
from string import Template


class Customer(models.Model):
    civil_id = models.IntegerField("T.C. No", unique=True)
    fullname = models.CharField("Tam İsim", max_length=100)
    email = models.CharField("Email", max_length=100)
    phone = models.CharField("Telefon", max_length=20)
    address = models.CharField("Adres", max_length=300)

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
    name = models.CharField("Cihaz Adı", max_length=100)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="Müşteri")
    customer_compliant = models.CharField("Müşteri Şikayeti", max_length=500)
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

    @property
    def repair_status(self):
        ra = self.repaired_at
        return ra if not (ra is None or ra is "" or ra is "None") else "Tamir Ediliyor"

    @property
    def deliver_status(self):
        da = self.delivered_at
        return da if not (da is None or da is "" or da is "None") else "---"
