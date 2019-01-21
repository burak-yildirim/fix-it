from django.shortcuts import render
from django.db.models import Q
from django.views.generic import edit
from django.views import generic
from django.urls import reverse_lazy
from core.models import Device, Customer


def repr_operation_panel_view(request):
    devices = Device.objects.filter(Q(repaired_at=None) or Q(repaired_at=""))
    mydict = {
        "devices": enumerate(devices),
    }
    return render(request, "representative/operation-panel.html", mydict)


class DeviceCreate(edit.CreateView):
    model = Device
    template_name = "representative/device_form.html"
    fields = ["name", "customer", "customer_compliant", ]
    success_url = reverse_lazy("repr:operation_panel")


class DeviceDetail(generic.DetailView):
    model = Device
    template_name = "representative/device_detail.html"


class CustomerCreate(edit.CreateView):
    model = Customer
    template_name = "representative/customer_form.html"
    fields = ["civil_id", "fullname", "email", "phone", "address"]
    success_url = reverse_lazy("repr:create_broken_device")
