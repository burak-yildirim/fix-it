from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Device


class BaseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control"


class CheckDeviceForm(BaseModelForm):
    id = forms.IntegerField(label="Arıza Kayıt Numarası",
                            help_text="Cihaz kaydı sırasında verilen numaradır.")

    class Meta:
        model = Device
        fields = ["id"]
