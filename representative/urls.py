from django.urls import path
from .views import ReprControlPanelView

app_name = "repr"

# "/repr/"
urlpatterns = [
    path("operation-panel/", ReprControlPanelView, name="operation_panel"),
]
