from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist


class EmployeeManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, fullname, email, employee_type, password=None, **extra_fields):
        """
        Creates an employee with required fields and extra fields if there is any 
        """
        if not email:
            raise ValueError("Kullanıcı için email olmak zorunda")
        email = self.normalize_email(email)
        user = self.model(fullname=fullname, email=email,
                          employee_type=employee_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, fullname, email, employee_type, password, **extra_fields):
        superuser = self.create_user(
            fullname, email, employee_type, password=password, **extra_fields)
        superuser.is_admin = True
        superuser.save(using=self._db)
        return superuser


class Employee(AbstractBaseUser):
    """
    Custom user model for this project. 'fullname', 'email', 'password' 
    and 'employee_type' fields are required. Others are optional. 

    'username' and 'is_staff' fields does not exist which is different 
    from default Django User class. Instead 'email' is used to 
    identify users. Also 'email' is required for email verification.
    Notice that 'is_active' field is 'False' by default and intended
    to be activated after email verification.

    'employee_type' is for differing personnels according to 
    their departments.

    Since Django 2.0 , 'get_full_name' and 'get_short_name' methods
    are not needed to be implemented, yet they are useful.
    """

    ADMIN = 0  # For admin accounts
    REPR = 1  # Stands for customer representative
    TECH = 2  # Stands for technical service employee
    EMPLOYEE_TYPE_CHOICES = (
        (ADMIN, "Admin"),
        (REPR, "Müşteri Temsilcisi"),
        (TECH, "Teknik Servis Görevlisi"),
    )

    fullname = models.CharField(
        "Ad Soyad", max_length=100, blank=False, unique=False)
    email = models.EmailField("Email Adresi", blank=False, unique=True)
    is_active = models.BooleanField("Aktiflik Durumu", default=False)
    date_joined = models.DateTimeField(
        "Katılma Tarihi", default=timezone.now)
    last_activated = models.DateTimeField(
        "Son Aktif Edilme Tarihi", null=True)
    last_deactivated = models.DateTimeField(
        "Son Pasif Edilme Tarihi", null=True)
    employee_type = models.PositiveSmallIntegerField("Hesap Türü",
                                                     choices=EMPLOYEE_TYPE_CHOICES, blank=False)
    is_admin = models.BooleanField("Admin Yetkilendirmesi", default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname", "employee_type", ]

    class Meta:
        verbose_name = "çalışan"
        verbose_name_plural = "çalışanlar"

    def get_full_name(self):
        return self.fullname

    def get_short_name(self):
        """
        Returns the first part of the fullname which is 
        right before the first space.
        """
        return str(self.fullname).split(' ')[0]

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        As understandable from the name, just sends the user an email.
        """
        send_mail(subject, message, from_email, self.email, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.email, self.fullname)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return True if self.is_admin == True else False

    def activate(self):
        self.is_active = True
        self.last_activated = timezone.now()

    def deactivate(self):
        self.is_active = False
        self.last_deactivated = timezone.now()

    def handle_activation(self):
        """
        This method is to be used at forms. Checks the database and if account
        exists, checks the last status of 'is_active' to set dates of 
        'last_activated' and 'last_deactivated'
        """
        try:
            # Employee's info at database
            employee_from_db = Employee.objects.get(id=self.id)

            # If an inactive account is getting activated
            if self.is_active and not employee_from_db.is_active:
                self.activate()
            # If an active account is getting deactivated
            elif not self.is_active and employee_from_db.is_active:
                self.deactivate()
        except ObjectDoesNotExist as e:
            # This is happening means the employee is getting created for
            # the first time and needs activation
            self.activate()
        except Exception as e:
            print(e)

    def is_repr(self):
        return True if self.employee_type == self.REPR else False

    def is_tech(self):
        return True if self.employee_type == self.TECH else False
