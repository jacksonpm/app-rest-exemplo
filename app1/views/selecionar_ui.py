from django.shortcuts import render


def selecionar_ui(request):
    return render(request, 'selecionar_ui.html')
