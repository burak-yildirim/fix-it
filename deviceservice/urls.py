from django.urls import path
from .views import TechControlPanelView

app_name = "tech"

# "/tech/"
urlpatterns = [
    path("operation-panel/", TechControlPanelView, name="operation_panel"),
]
