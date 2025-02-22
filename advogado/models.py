from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Advogado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="advogado")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")

    def __str__(self):
        return self.user.username


class Processo(models.Model):
    advogado = models.ForeignKey(Advogado, related_name="processos", on_delete=models.CASCADE)
    numero = models.IntegerField(unique=True, verbose_name="Número do Processo")
    cliente = models.CharField(max_length=255, verbose_name="Cliente")
    
    STATUS_CHOICES = (
        ('Aberto', 'Aberto'),
        ('Protocolado', 'Protocolado'),
        ('Finalizado', 'Finalizado'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Aberto', verbose_name="Status")
    
    TIPO_CHOICES = (
        ('Cível', 'Cível'),
        ('Criminal', 'Criminal'),
        ('Trabalhista', 'Trabalhista'),
        ('Tributário', 'Tributário'),
        ('Família', 'Família'),
        ('Previdenciário', 'Previdenciário'),
        ('administração', 'Administração'),
        ('Sucessão', 'Sucessão'),
        ('Consumidor', 'Consumidor'),
    )
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name="Tipo de Processo")
    
    parte_contraria = models.CharField(max_length=255, verbose_name="Parte Contrária")
    juiz = models.CharField(max_length=255, verbose_name="Juiz Responsável")
    ultima_atualizacao = models.DateField(auto_now=True, verbose_name="Última Atualização")
    
    def __str__(self):
        return f"{self.numero} - {self.cliente}"
