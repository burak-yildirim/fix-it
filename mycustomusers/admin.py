from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils import timezone
from .models import Employee


class EmployeeCreationForm(forms.ModelForm):
    """
    Form for creating new Employee account
    """

    password1 = forms.CharField(
        label="Parola", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Tekrar Parola", widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = (
            "fullname",
            "email",
            "employee_type",
            "is_active",
        )

    def clean_password2(self):
        # To check if two password fields values' match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parolalar eşleşmiyor!")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.handle_activation()
        user.is_admin = True if user.employee_type == Employee.ADMIN else False
        user.set_password(self.clean_password2())
        if commit:
            user.save()
        return user


class EmployeeChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Employee
        fields = (
            "fullname",
            "email",
            "password",
            "is_active",
            "employee_type",
            "is_admin",
            "date_joined",
            "last_activated",
            "last_deactivated",
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class EmployeeAdmin(UserAdmin):
    # Forms to update and add employee instances
    form = EmployeeChangeForm
    add_form = EmployeeCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("email", "fullname", "is_active", "employee_type",)
    list_filter = ("is_admin",)
    fieldsets = (
        # Account Info
        ("Hesap", {"fields": (
            "email",
            "password",
            "is_active",
            "date_joined",
            "last_activated",
            "last_deactivated",
        )}),
        # Personal Info
        ("Kişisel Bilgiler", {"fields": ("fullname",)}),
        # Permissions
        ("İzinler", {"fields": ("is_admin",)}),
        # Department
        ("Departman", {"fields": ("employee_type",)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "fullname",
                "email",
                "password1",
                "password2",
                "employee_type",
                "is_active",
            )
        }),
    )
    search_fields = ("email", "fullname",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(Employee, EmployeeAdmin)
# We are not using Django's built-in permissions,
# so ->
admin.site.unregister(Group)
