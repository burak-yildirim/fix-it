from django.shortcuts import render
from django.views import generic
from .forms import CheckDeviceForm
from .models import Device


class Index(generic.View):
    form_class = CheckDeviceForm
    template_name = "core/index.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        pass


class DeviceView(generic.DetailView):
    model = Device
    template_name = "core/deviceDetail.html"
