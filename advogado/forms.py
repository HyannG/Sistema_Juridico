from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Advogado, Processo

class AdvogadoRegistrationForm(UserCreationForm):
    telefone = forms.CharField(max_length=15, required=True, label="Telefone")

    class Meta:
        model = User
        fields = ["username", "email", "telefone", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Advogado.objects.create(
                user=user,
                telefone=self.cleaned_data['telefone']
            )
        return user
    
class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = [
            'numero', 'cliente', 'status', 'tipo', 
            'parte_contraria', 'juiz'
        ]
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'parte_contraria': forms.TextInput(attrs={'class': 'form-control'}),
            'juiz': forms.TextInput(attrs={'class': 'form-control'}),
        }


