from django.shortcuts import render
from pessoas.forms import PessoaForm, testeForm
from pessoas.models import Pessoa

def index(request):
	#form = testeForm()
	form = PessoaForm()
	return render(request, 'index.html', {'form':form})

def validar(request):
	if request.method == 'POST':
		#form = testeForm(request.POST)
		form = PessoaForm(request.POST)

		if form.is_valid():
			#print form.data['email']
			form.save()
			#pessoa = Pessoa(**form.cleaned_data)
			#pessoa.save()

			pessoas = Pessoa.objects.all().order_by('nome')

			return render(request,'validar.html',{'form':form,'pessoas':pessoas})
		else:
		return render(request,'index.html',{'form':form})
