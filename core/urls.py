from django.urls import path
from .views import DeviceView, not_authorized

app_name = "core"

# "/core/"
urlpatterns = [
    path('device/<int:pk>/', DeviceView.as_view(), name='detail'),
    path('not-authorized/', not_authorized, name='not_authorized')
]
