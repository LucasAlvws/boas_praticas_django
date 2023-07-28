from django import forms

from .models import Fotografia


class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia

        exclude = ['publicada', 'data_foto', 'usuario']
        labels = {
            'descricao' : "Descrição",
            'usuario' : "Usuário"
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }
        
