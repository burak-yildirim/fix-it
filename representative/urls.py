from django.urls import path, include
from .views import (
    repr_operation_panel_view,
    DeviceCreate,
    DeviceUpdate,
    DeviceDetail,
    CustomerCreate,
    CustomerDetail,
    CustomerUpdate
)

app_name = "repr"

# "/repr/"
urlpatterns = [
    path("operation-panel/", repr_operation_panel_view, name="operation_panel"),
    path("device/create/", DeviceCreate.as_view(), name="device_create"),
    path("device/<int:pk>/", DeviceDetail.as_view(), name="device_detail"),
    path("device/<int:pk>/update/", DeviceUpdate.as_view(), name="device_update"),
    path("customer/create/", CustomerCreate.as_view(), name="customer_create"),
    path("customer/<int:pk>/", CustomerDetail.as_view(), name="customer_detail"),
    path("customer/<int:pk>/update/",
         CustomerUpdate.as_view(), name="customer_update")
]
