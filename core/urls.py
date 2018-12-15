from django.urls import path
from .views import DeviceView

app_name = "core"

urlpatterns = [
    path('device/<int:pk>/', DeviceView.as_view(), name='detail'),
]
