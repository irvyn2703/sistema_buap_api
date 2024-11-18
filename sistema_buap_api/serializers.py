from rest_framework import serializers
from sistema_buap_api.models import User, Administradores, Alumnos, Maestros, Materias

# Serializer para User
class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

# Serializer para Administradores
class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Administradores
        fields = '__all__'

# Serializer para Alumnos
class AlumnoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Alumnos
        fields = '__all__'

# Serializer para Maestros
class MaestroSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Maestros
        fields = '__all__'

# Serializer para Materias
class MateriaSerializer(serializers.ModelSerializer):
    maestro = serializers.PrimaryKeyRelatedField(
        queryset=Maestros.objects.all(), write_only=True
    )
    maestro_details = MaestroSerializer(read_only=True, source="maestro")

    class Meta:
        model = Materias
        fields = [
            "nrc",
            "nombre",
            "seccion",
            "dias_json",
            "hora_inicio",
            "hora_fin",
            "salon",
            "programa",
            "creditos",
            "creation",
            "update",
            "maestro",
            "maestro_details",
        ]
