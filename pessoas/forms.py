from django import forms
from pessoas.models import Pessoa

class PessoaForm(forms.ModelForm):
	senha = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Pessoa

class testeForm(forms.Form):
	campo1 = forms.CharField(max_length='30', required=True)
	campo2 = forms.CharField(widget=forms.PasswordInput, required=True)