from django.urls import path
from .views import repr_operation_panel_view

app_name = "repr"

# "/repr/"
urlpatterns = [
    path("operation-panel/", repr_operation_panel_view, name="operation_panel"),
]
