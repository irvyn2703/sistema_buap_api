from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


class Administradores(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave_admin = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    ocupacion = models.CharField(max_length=255, null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update =  models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del admin "+self.first_name+" "+self.last_name

class Alumnos(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255, null=True, blank=True)
    curp = models.CharField(max_length=255, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    ocupacion = models.CharField(max_length=255, null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Perfil del alumno {self.user.first_name} {self.user.last_name}"

class Maestros(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave = models.CharField(max_length=255, null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255, null=True, blank=True)
    cubiculo = models.CharField(max_length=255, null=True, blank=True)
    area_investigacion = models.CharField(max_length=255, null=True, blank=True)
    materias_json = models.JSONField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Perfil del maestro {self.user.first_name} {self.user.last_name}"

class Materias(models.Model):
    nrc = models.CharField(max_length=6, primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    seccion = models.CharField(max_length=3, null=True, blank=True)  
    dias_json = models.JSONField(null=False, blank=False)  
    hora_inicio = models.CharField(max_length=255, null=False, blank=False)
    hora_fin = models.CharField(max_length=255, null=False, blank=False)  
    salon = models.CharField(max_length=255, null=True, blank=True)
    programa = models.CharField(max_length=255, null=False, blank=False)
    creditos = models.CharField(max_length=2, null=False, blank=False) 
    maestro = models.ForeignKey(Maestros, on_delete=models.CASCADE, null=False, blank=False)
    creation = models.DateTimeField(auto_now_add=True)  
    update = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Materia {self.nombre} (NRC: {self.nrc})"
