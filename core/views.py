from django.shortcuts import render, redirect
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

        if form.is_valid():
            id = form.cleaned_data['id']
            device = Device.objects.get(id=id)
            if device is not None:
                return redirect('core:detail', pk=device.id)
        return render(request, self.template_name, {'form': form})


class DeviceView(generic.DetailView):
    model = Device
    template_name = "core/deviceDetail.html"
