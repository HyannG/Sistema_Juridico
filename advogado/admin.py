from django.contrib import admin
from .models import Advogado, Processo

@admin.register(Advogado)
class AdvogadoAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefone', 'username', 'email')  
    search_fields = ('user__username', 'user__email', 'telefone')  

    def username(self, obj):
        return obj.user.username 

    def email(self, obj):
        return obj.user.email  
    
@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cliente', 'status', 'tipo', 'advogado', 'ultima_atualizacao')
    list_filter = ('status', 'tipo', 'advogado') 
    search_fields = ('numero', 'cliente', 'parte_contraria', 'juiz')  
    readonly_fields = ('ultima_atualizacao',) 

    def advogado(self, obj):
        return obj.advogado.user.username  