from rest_framework import serializers
from .models import Advogado, Processo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AdvogadoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  

    class Meta:
        model = Advogado
        fields = ['id', 'user', 'telefone']

class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = ['id', 'advogado', 'numero', 'cliente', 'status', 'tipo', 'parte_contraria', 'juiz', 'ultima_atualizacao']