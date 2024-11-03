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
from sistema_buap_api.views import users
from sistema_buap_api.views import auth

urlpatterns = [
    #Version
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    #Create Admin
        path('admin/', users.AdminView.as_view()),
    #Create Alumno
        path('alumno/', users.AlumnoView.as_view()),
    #Create Maestro
        path('maestro/', users.MaestroView.as_view()),
    #Admin Data
        path('lista-admins/', users.AdminAll.as_view()),
    #Maestro Data
        path('lista-maestros/', users.MaestrosAll.as_view()),
    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view())
]
