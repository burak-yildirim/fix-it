from django.shortcuts import render
from django.db.models import Q
from django.views.generic import edit
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import classonlymethod
from core.models import Device, Customer
from .decorators import authorization_required


@authorization_required
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

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return authorization_required(view)


class DeviceDetail(generic.DetailView):
    model = Device
    template_name = "representative/device_detail.html"

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return authorization_required(view)


class DeviceUpdate(edit.UpdateView):
    model = Device
    template_name = "representative/device_form.html"
    fields = ["name", "customer", "customer_compliant", ]
    success_url = reverse_lazy("repr:operation_panel")

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return authorization_required(view)


class CustomerCreate(edit.CreateView):
    model = Customer
    template_name = "representative/customer_form.html"
    fields = ["civil_id", "fullname", "email", "phone", "address"]
    success_url = reverse_lazy("repr:create_broken_device")

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return authorization_required(view)


class CustomerDetail(generic.DetailView):
    model = Customer
    template_name = "representative/customer_detail.html"

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return authorization_required(view)


class CustomerUpdate(edit.UpdateView):
    model = Customer
    template_name = "representative/customer_form.html"
    fields = ["civil_id", "fullname", "email", "phone", "address"]
    success_url = reverse_lazy("repr:create_broken_device")

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return authorization_required(view)
