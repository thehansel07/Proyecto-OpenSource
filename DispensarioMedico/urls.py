# Gestionar la rutas solamente del proyecto MTV

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('principalMarcas', views.principalMarcas, name='principalMarcas'),
    path('principalTipoFarmaco', views.principalTipoFarmaco, name='principalTipoFarmaco'),
    path('principalUbicaciones', views.principalUbicaciones, name='principalUbicaciones'),
    path('principalMedicamentos', views.principalMedicamentos, name='principalMedicamentos'),

    path('registrarMarcas/', views.registrarMarcas, name='registrarMarcas'),
    path('registrarTipoFarmaco/', views.registrarTipoFarmaco, name='registrarTipoFarmaco'),
    path('registrarUbicaciones/', views.registrarUbicaciones, name='registrarUbicaciones'),
    path('registrarMedicamentos/', views.registrarMedicamentos, name='registrarMedicamentos'),

    path('edicionMarcas/<idmarca>', views.edicionMarcas, name='edicionMarcas'),
    path('edicionTipoFarmaco/<idtipofarmaco>', views.edicionTipoFarmaco, name='edicionTipoFarmaco'),
    path('edicionUbicaciones/<idubicaciones>', views.edicionUbicaciones, name='edicionUbicaciones'),
    path('edicionMedicamentos/<idmedicamentos>', views.edicionMedicamentos, name='edicionMedicamentos'),

    path('editarMarcas/', views.editarMarcas, name='editarMarcas'),
    path('editarTipoFarmaco/', views.editarTipoFarmaco, name='editarTipoFarmaco'),
    path('editarUbicaciones/', views.editarUbicaciones, name='editarUbicaciones'),
    path('editarMedicamentos/', views.editarMedicamentos, name='editarMedicamentos'),

    path('eliminarMarcas/<idmarca>',views.eliminarMarcas,name='eliminarMarcas'),
    path('eliminarTipoFarmaco/<idtipofarmaco>', views.eliminarTipoFarmaco, name='eliminarTipoFarmaco'),
    path('eliminarUbicaciones/<idubicaciones>', views.eliminarUbicaciones, name='eliminarUbicaciones'),
    path('eliminarMedicamentos/<idmedicamentos>', views.eliminarMedicamentos, name='eliminarMedicamentos')

]