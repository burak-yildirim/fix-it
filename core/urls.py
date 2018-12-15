from django.urls import path
from .views import DeviceView

urlpatterns = [
    path('device/<int:pk>/', DeviceView.as_view(), name='detail'),
]
