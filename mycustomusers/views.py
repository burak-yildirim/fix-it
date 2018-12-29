from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import (
    views as auth_views,
    login as auth_login,
)
from .forms import CustomAuthenticationForm


class LoginView(auth_views.LoginView):
    """
    LoginView class which uses custom login form html and
    dynamically redirects users(employees) according to their
    departments.
    """
    template_name = "mycustomusers/login.html"
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        """Redirects users(employees) dynamically"""
        employee = form.get_user()
        print(employee)
        auth_login(self.request, employee)
        return HttpResponse("Hello " + employee.get_short_name())
