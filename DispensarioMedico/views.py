from django.shortcuts import render, redirect
from .models import Marcas, Tipofarmacos, Ubicacioness, Medicamentos
import sweetify


# Create your views here Client to server.

def index(request):
    return render(request, 'index.html')
def principalMarcas(request):
    listadoMarcas = Marcas.objects.all()
    return render(request, 'principalMarcas.html', {'marcas': listadoMarcas})
def principalTipoFarmaco(request):
    listadoTipoFarmacos = Tipofarmacos.objects.all()
    print(listadoTipoFarmacos)
    return render(request, 'principalTipoFarmaco.html', {'tipoFarmacos': listadoTipoFarmacos})

def principalUbicaciones(request):
    ubicaciones = Ubicacioness.objects.all()
    return render(request, 'principalUbicaciones.html', {'ubicaciones': ubicaciones})

def principalMedicamentos(request):
    marcas = Marcas.objects.all()
    tipoFarmacos = Tipofarmacos.objects.all()
    ubicaciones = Ubicacioness.objects.all()
    medicamentos = Medicamentos.objects.all()
    print(medicamentos)
    return render(request, 'principalMedicamentos.html', {'medicamentos': medicamentos,
                                                                               'marcas': marcas,
                                                                               'tipoFarmacos': tipoFarmacos,
                                                                               'ubicaciones': ubicaciones})


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

    return redirect('/principalMarcas')


def registrarTipoFarmaco(request):
    descripcion = request.POST['txtDescripcionTipoFarmaco']
    estado = request.POST['txtEstadoTipoFarmaco']

    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Tipofarmacos.objects.create(descripcion=descripcion, estado=estado)
    sweetify.success(request, 'Marca Agregada Correctamente!!!')

    return redirect('/principalTipoFarmaco')



def registrarUbicaciones(request):
    descripcion = request.POST['txtDescripcionUbicaciones']
    estante = request.POST['txtEstanteUbicaciones']
    tramo = request.POST['txtTramoUbicaciones']
    celda = request.POST['txtCeldaUbicaciones']
    estado = request.POST['txtEstadoUbicaciones']

    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Ubicacioness.objects.create(descripcion=descripcion,
                                tramo=tramo,
                                celda=celda,
                                estante=estante,
                                estado=estado)

    sweetify.success(request, 'Ubicacion Agregada Correctamente!!!')

    return redirect('/principalUbicaciones')




def edicionMarcas(request, idmarca):
    marca = Marcas.objects.get(idmarca=idmarca)
    print(marca.estado)
    return render(request, 'edicionMarcas.html', {'marca': marca})


def edicionTipoFarmaco(request, idtipofarmaco):
    tipoFarmaco = Tipofarmacos.objects.get(idtipofarmaco=idtipofarmaco)
    return render(request, 'edicionTipoFarmaco.html', {'tipoFarmaco': tipoFarmaco})

def edicionUbicaciones(request, idubicaciones):
    ubicaciones = Ubicacioness.objects.get(idubicaciones=idubicaciones)
    return render(request, 'edicionUbicaciones.html', {'ubicaciones': ubicaciones})




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

    return redirect('/principalMarcas')


def editarTipoFarmaco(request):
    idtipofarmaco = request.POST['txtIdTipoFarmaco']
    descripcion = request.POST['txtDescripcionTipoFarmaco']

    if 'txtEstadoTipoFarmaco' in request.POST:
        estado = request.POST['txtEstadoTipoFarmaco']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    tipoFarmaco = Tipofarmacos.objects.get(idtipofarmaco=idtipofarmaco)
    tipoFarmaco.descripcion = descripcion
    tipoFarmaco.estado =estado
    tipoFarmaco.save()

    sweetify.success(request, 'Tipo Farmaco Modificado Correctamente!!!')

    return redirect('/principalTipoFarmaco')
def editarUbicaciones(request):
    idubicaciones = request.POST['txtIdUbicaciones']
    descripcion = request.POST['txtDescripcionUbicaciones']
    estante = request.POST['txtEstanteUbicaciones']
    tramo = request.POST['txtTramoUbicaciones']
    celda = request.POST['txtCeldaUbicaciones']

    if 'txtEstadoUbicaciones' in request.POST:
        estado = request.POST['txtEstadoUbicaciones']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    ubicaciones = Ubicacioness.objects.get(idubicaciones = idubicaciones)
    ubicaciones.descripcion = descripcion
    ubicaciones.estante = estante
    ubicaciones.tramo = tramo
    ubicaciones.celda = celda
    ubicaciones.estado =estado
    ubicaciones.save()

    sweetify.success(request, 'Ubicaciones Modificado Correctamente!!!')

    return redirect('/principalUbicaciones')

def eliminarMarcas(request,idmarca):
    marca = Marcas.objects.get(idmarca=idmarca)
    marca.delete()
    sweetify.success(request, 'Marca Eliminada Correctamente!!!')
    return redirect('/principalMarcas')

def eliminarTipoFarmaco(request,idtipofarmaco):
    tipoFarmaco = Tipofarmacos.objects.get(idtipofarmaco=idtipofarmaco)
    tipoFarmaco.delete()
    sweetify.success(request, 'Tipo de Farmaco Eliminado Correctamente!!!')
    return redirect('/principalTipoFarmaco')


def eliminarUbicaciones(request,idubicaciones):
    ubicaciones = Ubicacioness.objects.get(idubicaciones=idubicaciones)
    ubicaciones.delete()
    sweetify.success(request, 'Ubicacion Eliminado Correctamente!!!')
    return redirect('/principalUbicaciones')






