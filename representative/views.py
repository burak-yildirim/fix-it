from django.shortcuts import render


def ReprControlPanelView(request):
    return render(request, "representative/operation-panel.html")
