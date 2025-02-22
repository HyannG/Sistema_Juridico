from django.urls import path
from . import views
from .views import cadastrar_processo, detalhes, editar_processo, excluir_processo



urlpatterns = [
    path('', views.register, name='cadastro'),  
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastrar-processo/', cadastrar_processo, name='cadastrar_processo'),
    path('processo/excluir/<int:processo_id>/', excluir_processo, name='excluir_processo'),
    path('processo/editar/<int:processo_id>/', editar_processo, name='editar_processo'),
    path('processo/<int:processo_id>/', detalhes, name='detalhes'),
]
