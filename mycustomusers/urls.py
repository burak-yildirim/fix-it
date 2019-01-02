from django.urls import path
from .views import LoginView, LogoutView, redirect_user_view, not_logged_in

app_name = "mycustomusers"

# /users/
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("redirect/", redirect_user_view, name="redirect"),
    path("not-logged-in", not_logged_in, name="not_logged_in"),
]
