from django.urls import path
from .views import repr_operation_panel_view, DeviceCreate, CustomerCreate

app_name = "repr"

# "/repr/"
urlpatterns = [
    path("operation-panel/", repr_operation_panel_view, name="operation_panel"),
    path("create-device/", DeviceCreate.as_view(),
         name="device_create"),
    path("create-customer/", CustomerCreate.as_view(), name="customer_create"),
]
