from django.shortcuts import render


def TechControlPanelView(request):
    return render(request, "deviceservice/operation-panel.html")
