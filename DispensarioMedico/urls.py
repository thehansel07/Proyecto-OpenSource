# Gestionar la rutas solamente del proyecto MTV

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrarMarcas/', views.registrarMarcas, name='registrarMarcas' ),
    path('edicionMarcas/<idmarca>', views.edicionMarcas, name='edicionMarcas' ),
    path('editarMarcas/', views.editarMarcas, name='editarMarcas'),
    path('eliminarMarcas/<idmarca>',views.eliminarMarcas,name='eliminarMarcas' )
]