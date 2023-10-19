from django.shortcuts import render

from .models import Disk


# Create your views here.
def index(request):
    context = Disk.objects.all()
    return render(request, 'index.html', {'disks': context})


def disk(request, pk):
    context = Disk.objects.get(pk=pk)
    return render(request, 'disk.html', {'disk': context})