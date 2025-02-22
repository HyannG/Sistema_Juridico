from rest_framework import serializers
from .models import Advogado

class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = ['nome', 'email', 'telefone', 'senha']
