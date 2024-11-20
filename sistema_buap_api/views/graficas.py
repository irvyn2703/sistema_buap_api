from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from sistema_buap_api.serializers import *
from sistema_buap_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json


class GraficaAllUsersbyType(generics.CreateAPIView):
    #Esta función es esencial para todo donde se requiera autorización de inicio de sesión (token)
    permission_classes = (permissions.IsAuthenticated,)
    #Contar el total de cada tipo de usuarios
    def get(self, request, *args, **kwargs):
        #Obtener total de admins
        admin = Administradores.objects.filter(user__is_active = 1).order_by("id")
        lista_admins = AdminSerializer(admin, many=True).data
        # Obtienes la cantidad de elementos en la lista
        total_admins = len(lista_admins)

        #Obtener total de maestros
        maestros = Maestros.objects.filter(user__is_active = 1).order_by("id")
        lista_maestros = MaestroSerializer(maestros, many=True).data
        
        total_maestros = len(lista_maestros)

        #Obtener total de alumnos
        alumnos = Alumnos.objects.filter(user__is_active = 1).order_by("id")
        lista_alumnos = AlumnoSerializer(alumnos, many=True).data
        total_alumnos = len(lista_alumnos)

        return Response({'admins': total_admins, 'maestros': total_maestros, 'alumnos':total_alumnos }, 200)

class MateriasByDay(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # Inicializar el contador de días
        dias_totales = {
            "lunes": 0,
            "martes": 0,
            "miércoles": 0,
            "jueves": 0,
            "viernes": 0,
            "sábado": 0,
            "domingo": 0,
        }

        # Obtener todas las materias activas
        materias = Materias.objects.all()

        for materia in materias:
            dias_json = materia.dias_json
            if isinstance(dias_json, list):
                for dia in dias_json:
                    dia = dia.lower()
                    if dia in dias_totales:
                        dias_totales[dia] += 1

        return Response(dias_totales, status=200)

class MateriasByPrograma(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # Inicializar el contador por programa
        programas_totales = {
            "Ingeniería en Ciencias de la Computación": 0,
            "Licenciatura en Ciencias de la Computación": 0,
            "Ingeniería en Tecnologías de la Información": 0,
        }

        # Obtener todas las materias activas
        materias = Materias.objects.all()

        for materia in materias:
            programa = materia.programa
            if programa in programas_totales:
                programas_totales[programa] += 1

        return Response(programas_totales, status=200)



