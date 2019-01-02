from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import (
    views as auth_views,
    login as auth_login,
    logout as auth_logout,
)
from django.views import generic
from .forms import CustomAuthenticationForm


def redirect_employee(user):
    """
    Redirects employees to their operation page.
    This is NOT A VIEW. Notice that it takes 'user(employee)' 
    as a paremeter but not 'request'.
    For view, see 'redirect_user_view'.
    """
    if not user.is_authenticated:
        return redirect("mycustomusers:not_logged_in")
    elif user.is_repr():
        return redirect("repr:operation_panel")
    elif user.is_tech():
        return redirect("tech:operation_panel")
    elif user.is_admin:
        return redirect("admin:index")
    return redirect("mycustomusers:not_logged_in")


class LoginView(auth_views.LoginView):
    """
    LoginView class which uses custom login form html and
    dynamically redirects users(employees) according to their
    departments.
    """
    template_name = "mycustomusers/login.html"
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        """Logs users(employees) in and redirects dynamically"""
        employee = form.get_user()
        print(employee)
        auth_login(self.request, employee)

        return redirect_employee(employee)

    def dispatch(self, request, *args, **kwargs):
        """
        If an authenticated user tries to reach login page,
        redirects them automatically.
        """
        employee = request.user
        if employee.is_authenticated:
            return redirect_employee(employee)
        return super().dispatch(request, *args, **kwargs)


class LogoutView(generic.View):

    def get(self, request):
        if request.user.is_authenticated:
            auth_logout(request)

        return redirect("index")

    def post(self, request):
        """ Can logout with post method too. """
        self.get(request)


def redirect_user_view(request):
    """
    View that redirects users to their operation page.
    """
    return redirect_employee(request.user)


def not_logged_in(request):
    return render(request, "mycustomusers/not-logged-in.html")
