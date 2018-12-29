from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    """
    This class only adds bootstrap('form-control' class)
    to input fields of django's AuthenticationForm class.
    """

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control"
