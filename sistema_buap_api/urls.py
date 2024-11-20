"""point_experts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistema_buap_api.views import bootstrap
from sistema_buap_api.views import admin
from sistema_buap_api.views import maestro
from sistema_buap_api.views import alumno
from sistema_buap_api.views import materia
from sistema_buap_api.views import graficas
from sistema_buap_api.views import auth

urlpatterns = [
    #Version
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    #Create Admin
        path('admin/', admin.AdminView.as_view()),
    #Create Alumno
        path('alumno/', alumno.AlumnoView.as_view()),
    #Create Maestro
        path('maestro/', maestro.MaestroView.as_view()),
    #Create Materia
        path('materia/', materia.MateriaView.as_view()),
    #Admin Data
        path('lista-admins/', admin.AdminAll.as_view()),
    #Maestro Data
        path('lista-maestros/', maestro.MaestrosAll.as_view()),
    #Maestro Data
        path('lista-alumnos/', alumno.AlumnosAll.as_view()),
    # Materia Data
        path('lista-materias/', materia.MateriasAll.as_view()),
    #Edit Admin
        path('admins-edit/', admin.AdminsViewEdit.as_view()),
    #Edit Maestro
        path('maestros-edit/', maestro.MaestrosViewEdit.as_view()),
    #Edit Maestro
        path('alumnos-edit/', alumno.AlumnosViewEdit.as_view()),
    # Edit Materia
        path('materias-edit/', materia.MateriasViewEdit.as_view()),
    # Graficas
        path('graficas-allUsersByType/', graficas.GraficaAllUsersbyType.as_view()),
        path('graficas-materiasByDay/', graficas.MateriasByDay.as_view()),
        path('graficas-materiasByPrograma/', graficas.MateriasByPrograma.as_view()),
    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view())
]
