from django.shortcuts import render, redirect
from .models import Marcas
import sweetify


# Create your views here Client to server.

def index(request):
    listadoMarcas = Marcas.objects.all()
    return render(request, 'index.html', {'marcas': listadoMarcas})




def registrarMarcas(request):
    descripcion = request.POST['txtdescripcionMarca']
    estado = request.POST['txtEstadoMarca']

    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Marcas.objects.create(descripcion=descripcion, estado=estado)
    sweetify.success(request, 'Marca Agregada Correctamente!!!')

    return redirect('/')

def edicionMarcas(request, idmarca):
    marca = Marcas.objects.get(idmarca=idmarca)
    print(marca.estado)
    return render(request, 'edicionMarcas.html', {'marca': marca})

def editarMarcas(request):
    idmarca = request.POST['txtIdmarca']
    descripcion = request.POST['txtdescripcionMarca']

    if 'txtEstadoMarcas' in request.POST:
        estado = request.POST['txtEstadoMarcas']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    marca = Marcas.objects.get(idmarca=idmarca)
    marca.descripcion = descripcion
    marca.estado =estado
    marca.save()

    sweetify.success(request, 'Marca Modificada Correctamente!!!')

    return redirect('/')


def eliminarMarcas(request,idmarca):
    marca = Marcas.objects.get(idmarca=idmarca)
    marca.delete()
    sweetify.success(request, 'Marca Eliminada Correctamente!!!')

    return redirect('/')






