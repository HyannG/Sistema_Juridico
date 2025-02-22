# Generated by Django 5.1.6 on 2025-02-22 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advogado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='advogado', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, unique=True, verbose_name='Número do Processo')),
                ('cliente', models.CharField(max_length=255, verbose_name='Cliente')),
                ('status', models.CharField(choices=[('Aberto', 'Aberto'), ('Em Andamento', 'Em Andamento'), ('Finalizado', 'Finalizado')], default='Aberto', max_length=50, verbose_name='Status')),
                ('tipo', models.CharField(choices=[('Cível', 'Cível'), ('Criminal', 'Criminal'), ('Trabalhista', 'Trabalhista'), ('Tributário', 'Tributário'), ('Família', 'Família')], max_length=50, verbose_name='Tipo de Processo')),
                ('parte_contraria', models.CharField(max_length=255, verbose_name='Parte Contrária')),
                ('juiz', models.CharField(max_length=255, verbose_name='Juiz Responsável')),
                ('ultima_atualizacao', models.DateField(auto_now=True, verbose_name='Última Atualização')),
                ('advogado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processos', to='advogado.advogado')),
            ],
        ),
    ]
