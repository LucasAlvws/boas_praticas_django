from django import forms


class LoginForms(forms.Form):
    name_login = forms.CharField(
        label="Nome de usuário:",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex.: Lucas"
            }
        )
    )
    senha = forms.CharField(
        label="Senha:",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):


    name_cadastro = forms.CharField(
        label="Nome de usuário:",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex.: Lucas"
            }
        )
    )
    email_cadastro = forms.EmailField(
        label="E-mail:",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex.: lucas@lucas.com"
            }
        )
    )
    senha_1 = forms.CharField(
        label="Senha:",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label="Confirme a sua senha:",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite sua senha novamente"
            }
        )
    )


    def clean_name_cadastro(self):
        nome = self.cleaned_data.get('name_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos no campo de usuário.')
            else:
                return nome
            
    
    def clean_senha_2(self):
         senha_1 = self.cleaned_data.get('senha_1')
         senha_2 = self.cleaned_data.get('senha_2')

         if senha_1 and senha_2:
              if senha_1 != senha_2:
                   raise forms.ValidationError("Senhas não são iguais.")
              else:
                   return senha_2