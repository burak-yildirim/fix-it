from django.shortcuts import render
from django.db.models import Q
from core.models import Device


def repr_operation_panel_view(request):
    devices = Device.objects.filter(Q(repaired_at=None) or Q(repaired_at=""))
    mydict = {
        "devices": enumerate(devices),
    }
    return render(request, "representative/operation-panel.html", mydict)
