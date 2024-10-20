from rest_framework import serializers
from rest_framework.authtoken.models import Token
from sistema_buap_api.models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email')

class AdminSerializer(serializers.ModelSerializer):
    User=UserSerializer(read_only=True)

    class Meta:
        model = Administradores
        fields = '__all__'