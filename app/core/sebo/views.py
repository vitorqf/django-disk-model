from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Disk
from .forms import DiskForm

# Create your views here.
def index(request):
    context = Disk.objects.all()
    return render(request, 'index.html', {'disks': context})


def disk(request, pk):
    context = Disk.objects.get(pk=pk)
    return render(request, 'disk.html', {'disk': context})

def disk_create(request):
    if request.method == 'POST':
        form = DiskForm(request.POST)
        if form.is_valid():
            disk = Disk()
            disk.name = form.cleaned_data['name']
            disk.description = form.cleaned_data['description']
            disk.seal = form.cleaned_data['seal']
            disk.year = form.cleaned_data['year']
            disk.gender = form.cleaned_data['gender']
            disk.country = form.cleaned_data['country']
            disk.quantity = form.cleaned_data['quantity']
            
            disk.save()
            return HttpResponseRedirect(reverse(index))
        
        else:
            return render(request, 'create.html', {'form': form})
        
    else:
        form = DiskForm()
        return render(request, 'create.html', {'form': form})
    
def disk_edit(request, pk):
    disk = Disk.objects.get(pk=pk)
    if request.method == 'POST':
        form = DiskForm(request.POST, instance=disk)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, 'edit.html', {'form': form})
        
    else:
        form = DiskForm(instance=disk)
        return render(request, 'edit.html', {'form': form})
    
def disk_delete(request, pk):
    disk = Disk.objects.get(pk=pk)
    disk.delete()
    return HttpResponseRedirect(reverse(index))