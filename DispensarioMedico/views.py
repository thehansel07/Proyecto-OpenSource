from django.shortcuts import render, redirect
from .models import Marcas, Tipofarmacos, Ubicacioness, Medicamentos, Pacientes, Tipopacientes,Medicos, Especialidadesmedicos, Visitas
import sweetify
from datetime import datetime 



# Create your views here Client to server.

def index(request):
    return render(request, 'index.html')

def principalMarcas(request):
    listadoMarcas = Marcas.objects.all()
    return render(request, 'principalMarcas.html', {'marcas': listadoMarcas})

def principalTipoFarmaco(request):
    listadoTipoFarmacos = Tipofarmacos.objects.all()
    return render(request, 'principalTipoFarmaco.html', {'tipoFarmacos': listadoTipoFarmacos})

def principalUbicaciones(request):
    ubicaciones = Ubicacioness.objects.all()
    return render(request, 'principalUbicaciones.html', {'ubicaciones': ubicaciones})

def principalMedicamentos(request):
    marcas = Marcas.objects.all()
    tipoFarmacos = Tipofarmacos.objects.all()
    ubicaciones = Ubicacioness.objects.all()
    medicamentos = Medicamentos.objects.all()
    return render(request, 'principalMedicamentos.html', {'medicamentos': medicamentos,
                                                                               'marcas': marcas,
                                                                               'tipoFarmacos': tipoFarmacos,
                                                                               'ubicaciones': ubicaciones})
def principalPaciente(request):
    pacientes = Pacientes.objects.all()
    tipoPaciente = Tipopacientes.objects.all()

    return render(request, 'principalPaciente.html', {'pacientes': pacientes,
                                                      'tipoPaciente':tipoPaciente})


def principalMedico(request):
    medicos = Medicos.objects.all()
    especialidades = Especialidadesmedicos.objects.all()
    return render(request, 'principalMedico.html', {'medicos': medicos,
                                                      'especialidades':especialidades})


def principalVisitas(request):
    
    visitas = Visitas.objects.all()
    medicos = Medicos.objects.all()
    medicamentos = Medicamentos.objects.all()
    pacientes = Pacientes.objects.all()
    return render(request, 'principalVisitas.html', {'medicos': medicos,
                                                    'visitas':visitas, 
                                                    'medicamentos':medicamentos, 
                                                    'pacientes':pacientes})


def registrarVisita(request):
    idmedico   = request.POST['txtidMedico']
    idPaciente = request.POST['txtidPaciente']
    fechavisita = request.POST['txtfechavisita']
    horavisita = request.POST['txthoravisita']
    descripcionMedicamento = request.POST['txtdescripcionMedicamento']
    recomendacionVisita = request.POST['txtRecomendacionVisita']
    estado = request.POST['txtEstadoVisita']

    medico_instance = Medicos.objects.get(idmedico=idmedico)
    paciente_instance = Pacientes.objects.get(idPaciente =idPaciente)

    print(medico_instance)
    print(paciente_instance)



    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Visitas.objects.create( idmedico  = medico_instance,
                            idPaciente = paciente_instance,
                            fechavisita = fechavisita,
                            horavisita = horavisita,
                            medicamentossuministrado  = descripcionMedicamento,
                            recomendaciones  = recomendacionVisita,
                            estado=estado )
    
    sweetify.success(request, 'Visita Agregada Correctamente!!!')

    return redirect('/principalVisitas')


def registrarMedico(request):
    nombre = request.POST['txtNombreMedico']
    cedula = request.POST['txtCedulaMedico']
    tandaLabor = request.POST['txttandaLaborMedico']
    idespecialidades = request.POST['txtidEspecialidades']
    estado = request.POST['txtEstadoMedico']

    especialidades_instance = Especialidadesmedicos.objects.get(idespecialidades=idespecialidades)


    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Medicos.objects.create( nombre = nombre,
                            cedula = cedula,
                            tandalabor = tandaLabor,
                            idespecialidades = especialidades_instance,
                            estado=estado )
    
    sweetify.success(request, 'Medico Agregado Correctamente!!!')

    return redirect('/principalMedico')

def registrarPaciente(request):
    nombre = request.POST['txtNombrePaciente']
    cedula = request.POST['txtCedulaPaciente']
    noCarnet = request.POST['txtNoCarnetPaciente']
    idTipoPaciente = request.POST['txtidTipoPaciente']
    estado = request.POST['txtEstadoPaciente']

    tipoPaciente_instance = Tipopacientes.objects.get(idTipoPaciente=idTipoPaciente)


    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Pacientes.objects.create(nombre=nombre,
                            cedula=cedula,
                            nocarnet=noCarnet,
                            idTipoPaciente=tipoPaciente_instance,
                            estado=estado )
    
    sweetify.success(request, 'Paciente Agregado Correctamente!!!')

    return redirect('/principalPaciente')



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

def registrarMedicamentos(request):
    descripcion = request.POST['txtDescripcionMedicamentos']
    idubicaciones = request.POST['txtIdUbicaciones']
    idtipofarmaco = request.POST['txtidTipoFarmaco']
    idmarca = request.POST['txtIdMarca']
    estado = request.POST['txtEstadoMedicamentos']
    dosis = request.POST['txtDosisMedicamentos']

    tipofarmacos_instance = Tipofarmacos.objects.get(idtipofarmaco=idtipofarmaco)
    marca_instance = Marcas.objects.get( idmarca= idmarca)
    ubicaciones_instance = Ubicacioness.objects.get(idubicaciones =idubicaciones)


    #Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    Medicamentos.objects.create(descripcion=descripcion,
                                idtipofarmaco=tipofarmacos_instance,
                                idmarca=marca_instance,
                                idubicaciones =ubicaciones_instance,
                                dosis =dosis,
                                estado=estado)

    sweetify.success(request, 'Medicamentos Agregado Correctamente!!!')

    return redirect('/principalMedicamentos')






def edicionVisita(request, idvisitas):
    visitas = Visitas.objects.get(idvisitas=idvisitas)
    medicos = Medicos.objects.all()
    medicamentos = Medicamentos.objects.all()
    pacientes = Pacientes.objects.all()
    return render(request, 'edicionVisita.html', {'medicos': medicos,
                                                    'visitas':visitas, 
                                                    'medicamentos':medicamentos, 
                                                    'pacientes':pacientes})

def edicionMedico(request, idmedico):
    medico = Medicos.objects.get(idmedico=idmedico)
    especialidad = Especialidadesmedicos.objects.all()
    return render(request, 'edicionMedico.html', {'medico': medico, 
                                                   'especialidad':especialidad})
def edicionPaciente(request, idpaciente):
    paciente = Pacientes.objects.get(idPaciente=idpaciente)
    tipoPaciente = Tipopacientes.objects.all()
    return render(request, 'edicionPaciente.html', {'paciente': paciente, 
                                                   'tipoPaciente':tipoPaciente})
def edicionMarcas(request, idmarca):
    marca = Marcas.objects.get(idmarca=idmarca)
    return render(request, 'edicionMarcas.html', {'marca': marca})


def edicionTipoFarmaco(request, idtipofarmaco):
    tipoFarmaco = Tipofarmacos.objects.get(idtipofarmaco=idtipofarmaco)
    return render(request, 'edicionTipoFarmaco.html', {'tipoFarmaco': tipoFarmaco})

def edicionUbicaciones(request, idubicaciones):
    ubicaciones = Ubicacioness.objects.get(idubicaciones=idubicaciones)
    return render(request, 'edicionUbicaciones.html', {'ubicaciones': ubicaciones})

def edicionMedicamentos(request, idmedicamentos):
    medicamentos = Medicamentos.objects.get(idmedicamentos=idmedicamentos)
    marcas = Marcas.objects.all()
    tipoFarmacos = Tipofarmacos.objects.all()
    ubicaciones = Ubicacioness.objects.all()
    return render(request, 'edicionMedicamentos.html', {'medicamentos': medicamentos,
                                                                            'marcas': marcas,
                                                                             'tipoFarmacos': tipoFarmacos,
                                                                            'ubicaciones': ubicaciones})










def editarVisita(request):
    id_visitas = request.POST['txtidvisitas']
    id_medico   = request.POST['txtidMedico']
    id_Paciente = request.POST['txtidPaciente']
    fecha_visita = request.POST['txtfechavisita']
    hora_visita = request.POST['txthoravisita']
    medicamentos_suministrado = request.POST['txtdescripcionMedicamento']
    recomendaciones_ = request.POST['txtRecomendacionVisita']
    estado_ = request.POST['txtEstadoVisita']


    medico_instance = Medicos.objects.get(idmedico=id_medico)
    paciente_instance = Pacientes.objects.get(idPaciente =id_Paciente)

    print(medicamentos_suministrado)

    if 'txtEstadoVisita' in request.POST:
        estado_ = request.POST['txtEstadoVisita']
    else:
        estado_ = '0'

    # Valid if estado is on or off#
    if estado_ == 'on':
        estado_ = 1
    else:
        estado_ = 0

    visit = Visitas.objects.get(idvisitas=id_visitas)
    visit.idmedico = medico_instance
    visit.idPaciente = paciente_instance
    visit.fechavisita = fecha_visita
    visit.horavisita = hora_visita
    visit.medicamentossuministrado = medicamentos_suministrado
    visit.recomendaciones = recomendaciones_
    visit.estado = estado_
    visit.save()
    
    sweetify.success(request, 'Visita Actualizada Correctamente!!!')

    return redirect('/principalVisitas')



def editarMedico(request):
    idmedico  = request.POST['txtidMedico']
    nombre = request.POST['txtNombreMedico']
    cedula = request.POST['txtCedulaMedico']
    tandaLabor = request.POST['txttandaLaborMedico']
    idespecialidades = request.POST['txtidEspecialidades']

    especialidades_instance = Especialidadesmedicos.objects.get(idespecialidades=idespecialidades)

    if 'txtEstadoMedico' in request.POST:
        estado = request.POST['txtEstadoMedico']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    medico = Medicos.objects.get(idmedico=idmedico)
    medico.idespecialidades = especialidades_instance
    medico.nombre = nombre
    medico.cedula = cedula
    medico.tandalabor = tandaLabor
    medico.estado =estado
    medico.save()

    sweetify.success(request, 'Medico Modificado Correctamente!!!')

    return redirect('/principalMedico')

def editarPaciente(request):
    idPaciente  = request.POST['txtidPaciente']
    nombre = request.POST['txtNombrePaciente']
    cedula = request.POST['txtCedulaPaciente']
    noCarnet = request.POST['txtNoCarnetPaciente']
    idTipoPaciente = request.POST['txtidTipoPaciente']

    tipoPaciente_instance = Tipopacientes.objects.get(idTipoPaciente=idTipoPaciente)

    if 'txtEstadoPaciente' in request.POST:
        estado = request.POST['txtEstadoPaciente']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    pacientes = Pacientes.objects.get(idPaciente=idPaciente)
    pacientes.idTipoPaciente = tipoPaciente_instance
    pacientes.nombre = nombre
    pacientes.cedula = cedula
    pacientes.nocarnet = noCarnet
    pacientes.estado =estado
    pacientes.save()

    sweetify.success(request, 'Paciente Modificado Correctamente!!!')

    return redirect('/principalPaciente')



def editarMedicamentos(request):
    idmedicamentos  = request.POST['txtIdMedicamentos']
    descripcion = request.POST['txtDescripcionMedicamentos']
    idubicaciones  = request.POST['txtIdUbicaciones']
    idtipofarmaco  = request.POST['txtidTipoFarmaco']
    idmarca   = request.POST['txtIdMarca']
    dosis = request.POST['txtDosisMedicamentos']

    tipofarmacos_instance = Tipofarmacos.objects.get(idtipofarmaco=idtipofarmaco)
    marca_instance = Marcas.objects.get(idmarca=idmarca)
    ubicaciones_instance = Ubicacioness.objects.get(idubicaciones=idubicaciones)

    if 'txtEstadoMedicamentos' in request.POST:
        estado = request.POST['txtEstadoMedicamentos']
    else:
        estado = '0'

    # Valid if estado is on or off#
    if estado == 'on':
        estado = 1
    else:
        estado = 0

    medicamentos = Medicamentos.objects.get(idmedicamentos=idmedicamentos)
    medicamentos.idubicaciones = ubicaciones_instance
    medicamentos.idmarca = marca_instance
    medicamentos.idtipofarmaco = tipofarmacos_instance
    medicamentos.dosis = dosis
    medicamentos.descripcion = descripcion
    medicamentos.estado =estado
    medicamentos.save()

    sweetify.success(request, 'Medicamentos Modificado Correctamente!!!')

    return redirect('/principalMedicamentos')

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
    ubicaciones.estado = estado
    ubicaciones.save()

    sweetify.success(request, 'Ubicaciones Modificado Correctamente!!!')

    return redirect('/principalUbicaciones')






def eliminarVisita(request,idvisitas ):
    visita = Visitas.objects.get(idvisitas=idvisitas)
    visita.delete()
    sweetify.success(request, 'Visita Eliminado Correctamente!!!')
    return redirect('/principalVisitas')


def eliminarMedico(request,idmedico):
    medico = Medicos.objects.get(idmedico=idmedico)
    medico.delete()
    sweetify.success(request, 'Medico Eliminado Correctamente!!!')
    return redirect('/principalMedico')


def eliminarPaciente(request,idpaciente):
    paciente = Pacientes.objects.get(idPaciente=idpaciente)
    paciente.delete()
    sweetify.success(request, 'Paciente Eliminado Correctamente!!!')
    return redirect('/principalPaciente')



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


def eliminarMedicamentos(request,idmedicamentos):
    medicamentos = Medicamentos.objects.get(idmedicamentos=idmedicamentos)
    medicamentos.delete()
    sweetify.success(request, 'Medicamento Eliminado Correctamente!!!')
    return redirect('/principalMedicamentos')









