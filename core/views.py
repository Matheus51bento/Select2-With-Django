from django.shortcuts import render
from .models import Comida


def inicio(request):
    data = Comida.objects.all()
    return render(request, 'index.html', {'data': data})
