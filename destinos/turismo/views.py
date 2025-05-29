# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import DestinosTuristicos
from .forms import DestinoForm

def listar_destinos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'turismo/listar.html', {'destinos': destinos})

def añadir_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = DestinoForm()
    return render(request, 'turismo/añadir.html', {'form': form})

def modificar_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, pk=id)
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'turismo/modificar.html', {'form': form})

def eliminar_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, pk=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('listar')
    return render(request, 'turismo/eliminar.html', {'destino': destino})
