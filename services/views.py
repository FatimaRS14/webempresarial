from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    #se creara una lista para poder vincular los servicio que se crean desde el admin 
    services = Service.objects.all()

    return render(request, 'services/services.html', {'services': services})