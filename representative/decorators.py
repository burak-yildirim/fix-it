from django.shortcuts import render


def authorization_required(func):
    def wrapper(request, *args, **kwargs):
        if not (request.user.is_repr or request.user.is_admin):
            return render(request, "core/not_authorized.html")
        return func(request, *args, **kwargs)
    return wrapper
