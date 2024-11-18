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

class MateriasAll(generics.CreateAPIView):
    """
    Obtener todas las materias activas ordenadas por NRC.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        materias = Materias.objects.all().order_by("nrc")
        materias = MateriaSerializer(materias, many=True).data

        if not materias:
            return Response({}, status=400)

        return Response(materias, status=200)


class MateriaView(generics.CreateAPIView):
    """
    Vista para obtener y crear materias.
    """
    # Obtener una materia por NRC
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        materia = get_object_or_404(Materias, nrc=request.GET.get("nrc"))
        materia = MateriaSerializer(materia, many=False).data

        return Response(materia, status=200)

    # Registrar nueva materia
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = MateriaSerializer(data=request.data)
        if serializer.is_valid():
            nrc = serializer.validated_data.get("nrc")

            # Verificar si el NRC ya existe
            existing_materia = Materias.objects.filter(nrc=nrc).first()
            if existing_materia:
                return Response({"message": f"El NRC {nrc} ya está en uso"}, status=400)

            # Crear la nueva materia
            materia = serializer.save()
            return Response({"materia_created_nrc": materia.nrc}, status=201)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MateriasViewEdit(generics.CreateAPIView):
    """
    Vista para editar y eliminar materias.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        # Buscar la materia por NRC
        materia = get_object_or_404(Materias, nrc=request.data["nrc"])

        # Actualizar los datos de la materia
        materia.nombre = request.data.get("nombre", materia.nombre)
        materia.seccion = request.data.get("seccion", materia.seccion)
        materia.dias_json = request.data.get("dias_json", materia.dias_json)
        materia.hora_inicio = request.data.get("hora_inicio", materia.hora_inicio)
        materia.hora_fin = request.data.get("hora_fin", materia.hora_fin)
        materia.salon = request.data.get("salon", materia.salon)
        materia.programa = request.data.get("programa", materia.programa)
        materia.creditos = request.data.get("creditos", materia.creditos)

        # Actualizar la relación con el maestro si está presente
        if "maestro" in request.data:
            maestro = get_object_or_404(Maestros, id=request.data["maestro"])
            materia.maestro = maestro

        # Guardar los cambios en la materia
        materia.save()

        # Serializar y devolver la materia actualizada
        updated_materia = MateriaSerializer(materia, many=False).data
        return Response(updated_materia, status=200)



    def delete(self, request, *args, **kwargs):
        # Buscar la materia por NRC y eliminarla
        materia = get_object_or_404(Materias, nrc=request.GET.get("nrc"))
        try:
            materia.delete()
            return Response({"details": "Materia eliminada"}, status=200)
        except Exception as e:
            return Response({"details": "Error al eliminar la materia"}, status=400)
