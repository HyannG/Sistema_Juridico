from django.shortcuts import render, redirect
from .forms import AdvogadoRegistrationForm, ProcessoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Processo
@login_required
def dashboard(request):
    processos = Processo.objects.filter(advogado=request.user.advogado)
    processos_abertos = processos.filter(status='Aberto').count()
    processos_andamento = processos.filter(status='Em Andamento').count()
    processos_finalizados = processos.filter(status='Finalizado').count()

    context = {
        'processos': processos,  
        'processos_abertos': processos_abertos,
        'processos_andamento': processos_andamento,
        'processos_finalizados': processos_finalizados,
    }
    return render(request, 'dashboard.html', context)

def register(request):
    if request.method == 'POST':
        form = AdvogadoRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = AdvogadoRegistrationForm()
    return render(request, 'cadastro.html', {'form': form})  

@login_required
def cadastrar_processo(request):
    if request.method == 'POST':
        form = ProcessoForm(request.POST)
        if form.is_valid():
            processo = form.save(commit=False)
            processo.advogado = request.user.advogado  
            processo.save()
            return redirect('dashboard')  
    else:
        form = ProcessoForm()
    
    return render(request, 'cadastrar_processo.html', {'form': form})

@login_required
def excluir_processo(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id, advogado=request.user.advogado)
    processo.delete()
    return redirect('dashboard')

@login_required
def editar_processo(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id, advogado=request.user.advogado)  
    if request.method == 'POST':
        form = ProcessoForm(request.POST, instance=processo)
        if form.is_valid():
            form.save()
            return redirect('dashboard') 
    else:
        form = ProcessoForm(instance=processo)   
    return render(request, 'editar_processo.html', {'form': form})

@login_required
def detalhes(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id, advogado=request.user.advogado)
    return render(request, 'detalhes.html', {'processo': processo})