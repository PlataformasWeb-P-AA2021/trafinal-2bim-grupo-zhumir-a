
"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # casas
    path('crear/casa', views.crear_casa,
        name='crear_casa'),
    path('editar_casa/<int:id>', views.editar_casa,
        name='editar_casa'),
    path('eliminar/casa/<int:id>', views.eliminar_casa,
        name='eliminar_casa'),
    # Departamentos
    path('dept', views.dept,
        name='dept'),
    path('crear/departamento', views.crear_departamento,
        name='crear_departamento'),
    path('editar_departamento/<int:id>', views.editar_departamento,
        name='editar_departamento'),
    path('eliminar/departamento/<int:id>', views.eliminar_departamento,
        name='eliminar_departamento'),
    



    path('saliendo/logout/', views.logout_view, name="logout_view"),
    path('entrando/login/', views.ingreso, name="login"),
 ]
